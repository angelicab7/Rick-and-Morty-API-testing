# visual_utils.py

from pathlib import Path
from PIL import Image, ImageChops
import os
from playwright.sync_api import Page, Locator
import pytest
import allure

# --- Visual Regression Directories ---
VISUAL_DIR = Path("visuals")
BASELINE_DIR = VISUAL_DIR / "baseline"
CURRENT_DIR = VISUAL_DIR / "current"
DIFF_DIR = VISUAL_DIR / "diffs"

# Define a reasonable threshold for visual difference
PIXEL_TOLERANCE = 50

# Ensure directories exist
for d in [BASELINE_DIR, CURRENT_DIR, DIFF_DIR]:
    d.mkdir(parents=True, exist_ok=True)


class VisualRegression:
    def __init__(self, page: Page) -> None:
        self.page = page

    def check_element(self, screenshot_name: str, locator: Locator):
        # 1. Take a screenshot of the specified element (or the whole page)
        screenshot_bytes = locator.screenshot()
        
        # 2. Compare against baseline and get paths
        self.assert_screenshot(screenshot_bytes, screenshot_name)
    
    def check_full_page(self, screenshot_name: str):
        # 1. Take a screenshot of the full page
        screenshot_bytes = self.page.screenshot()

        # 2. Compare against baseline and get paths
        self.assert_screenshot(screenshot_bytes, screenshot_name)

    def assert_screenshot(self, image_bytes: bytes, screenshot_name: str):
        diff_count, diff_path, current_path = self.compare_and_generate_diff(screenshot_name, image_bytes)
        
        # 3. Handle First Run / No Baseline
        if diff_count == -1:
            pytest.fail(
                f"BASELINE CREATED: No baseline found for '{screenshot_name}'. "
                f"New baseline saved to {BASELINE_DIR}. Please re-run the test."
            )
            
        # 4. Handle Visual Failure
        if diff_count > PIXEL_TOLERANCE:
            # Attach all three images to the Allure report
            allure.attach.file(str(diff_path), name=f"{screenshot_name}_DIFF", attachment_type=allure.attachment_type.PNG)
            allure.attach.file(str(current_path), name=f"{screenshot_name}_CURRENT", attachment_type=allure.attachment_type.PNG)
            allure.attach.file(str(BASELINE_DIR / f"{screenshot_name}.png"), name=f"{screenshot_name}_BASELINE", attachment_type=allure.attachment_type.PNG)
            
            # Raise the failure
            pytest.fail(
                f"VISUAL REGRESSION: {diff_count} pixels difference found (Tolerance: {PIXEL_TOLERANCE}). "
                f"See Allure report for DIFF image."
            )

        # 5. Handle Success
        print(f"\n[VISUAL SUCCESS] {screenshot_name} passed with {diff_count} pixels difference.")

    def compare_and_generate_diff(self, test_name: str, current_image_bytes: bytes) -> tuple[int, Path | None, Path]:
        """
        Compares the current screenshot bytes against the baseline, saves a diff image,
        and returns the pixel difference count.

        :param test_name: Unique name for the visual test (e.g., 'homepage_header').
        :param current_image_bytes: Raw bytes of the screenshot captured by Playwright.
        :return: (Pixel difference count, Diff image path if difference > 0, Current image path)
        """
        baseline_path = BASELINE_DIR / f"{test_name}.png"
        current_path = CURRENT_DIR / f"{test_name}.png"
        diff_path = DIFF_DIR / f"DIFF_{test_name}.png"

        # Save the current screenshot bytes as a file
        with open(current_path, 'wb') as f:
            f.write(current_image_bytes)

        if not baseline_path.exists():
            # This is the first run: save the current image as the baseline and fail the test
            current_path.rename(baseline_path)
            return -1, None, baseline_path # -1 indicates no baseline found

        # Load images
        baseline_img = Image.open(baseline_path).convert("RGB")
        current_img = Image.open(current_path).convert("RGB")

        # Ensure images are the same size
        if baseline_img.size != current_img.size:
            # Resize current image to baseline size for comparison, or raise an error
            current_img = current_img.resize(baseline_img.size) 
            
        # Calculate the absolute pixel-by-pixel difference
        diff_img = ImageChops.difference(baseline_img, current_img)
        
        # Check for any difference using the bounding box
        bbox = diff_img.getbbox()
        
        if bbox:
            # Save the difference image (optional: highlight the diff by making it visually distinct)
            diff_img.save(diff_path)
            # Get the count of differing pixels (non-black pixels in the diff image)
            # We check the 'L' (luminance) channel for non-zero values
            diff_count = sum(Image.open(diff_path).convert('L').point(lambda x: x > 0).getdata()) # type: ignore

            return diff_count, diff_path, current_path
        else:
            # Images are visually identical
            if diff_path.exists():
                os.remove(diff_path) # Clean up old diff
            return 0, None, current_path

    # --- Helper for Manual Baseline Update ---
    def update_baseline(self, test_name: str):
        """Copies the latest current screenshot to the baseline folder."""
        current_path = CURRENT_DIR / f"{test_name}.png"
        baseline_path = BASELINE_DIR / f"{test_name}.png"
        if current_path.exists():
            current_path.rename(baseline_path)
            print(f"Updated baseline for: {test_name}")
        else:
            print(f"Current image not found for: {test_name}")