# 🌌  Rick and Morty Web and API testing

## Project Overview

This repository contains a comprehensive suite of automated tests for both the Rick and Morty REST API and its corresponding Web front-end. The tests are written in Python, utilizing the powerful pytest framework for API testing and pytest-bdd with Playwright for robust Web-based Behavior-Driven Development (BDD) testing.

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHkyYmlva3prOXRieTd2Ym05NGZwYzN6d3dmZWxmcW5hMTVoOTN0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NLOuEditveb9ZfeP2O/giphy.gif">

## ⚙️ Setup and Installation

### Clone the Repository

```bash
git clone https://github.com/angelicab7/Rick-and-Morty-Web-and-API-testing
cd Rick-and-Morty-API-testing
```

### Create the environment

```bash
uv sync
```

### Activate the environment

```bash
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Install Playwright 

```bash
playwright install
```
## ▶️ Running Tests
All tests are designed to be run from the repository root directory.

### Running All Tests (API and Web)
```bash
pytest
```
This command will automatically discover and execute all standard pytest API tests and BDD Web tests.

### Running Specific Test Suites

Web Tests Only Runs all Web BDD scenarios using Playwright.
```bash
pytest tests/Web  
```
Specific Feature - Runs tests only for the character search feature.
 ```bash	
pytest tests/Web/features/search_character.feature
 ```
 API Tests Only Runs all validation tests against the Rick and Morty API.

 ```bash
pytest tests/API  
```
Specific API File - Runs tests from a single API test file.
 ```bash
pytest tests/API/test_characters.py	
 ```

## 📝 Reporting with Allure
This project is configured to generate detailed reports using Allure.

1. Generate Allure Results
Run pytest with the Allure flag to collect test data:

```bash
pytest --alluredir=allure-results
```
2. View the Report
You need to have the Allure Command Line tool installed (see Allure documentation for installation instructions). Once installed, run:

```bash
allure serve allure-results
```
This will automatically open an interactive report in your web browser.

## 📂 Project Structure

The project follows a modular structure to separate API logic from Web UI logic, and to adhere to BDD principles.

```bash
├── tests/
│   ├── API/                  # Standard Pytest tests for API endpoints
│   │   ├── test_characters.py
│   │   ├── test_episode.py
│   │   └── test_locations.py
│   └── Web/                  # BDD tests using pytest-bdd and Playwright
│       ├── features/
│       │   ├── search_character.feature # Gherkin feature files
│       │   ├── steps/
│       │   │   └── test_characters_steps.py # Step definition implementation
│       │   └── pages/        # Page Object Models (POM) for the Web UI
│       │       ├── characters_page.py
│       │       └── home_page.py
└── allure-results/           # Output directory for Allure data
```

### 🔗 Resources

- [Rick and Morty API Documentation](https://rickandmortyapi.com/documentation/#introduction)
- [Webpage](https://angelicab7.github.io/BOG001-data-lovers/index.html)
- [Requests Library](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
- [Postman Collection](https://www.postman.com/joyce-jetson/joycejetson/documentation/hkyhp5u/rick-and-morty-api)
- [Playwright Documentation](https://playwright.dev/python/docs/intro)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/en/latest/)