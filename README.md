# pytest-bdd ![Pytest Logo](https://img.shields.io/badge/Pytest-BDD-orange?logo=pytest&logoColor=white)

**`pytest-bdd`** is a plugin for **Pytest** that allows you to write tests in a **Behavior-Driven Development (BDD)** style using the **Gherkin** syntax. It combines the simplicity of Gherkin scenarios with the powerful features of Pytest, such as fixtures and plugins.

---

## 🚀 **Features**

🔹 **BDD with Gherkin**: Write test scenarios in a human-readable format (`.feature` files).  
🔹 **Seamless Pytest integration**: Use Pytest's features like fixtures, parameterization, and plugins.  
🔹 **Modular test steps**: Define reusable steps with `@given`, `@when`, and `@then` decorators.  
🔹 **Readable and maintainable tests**: Keep test logic and scenarios separate.  

---

## 🛠️ **Installation**

To install `pytest-bdd`, run:

```bash
pip install pytest-bdd
```

---

## ⚡ **Quick Start**

### 📄 Example Feature File (`login.feature`)

```gherkin
Feature: Login functionality

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    Then I should see the dashboard
```

### 🐍 Test Implementation in Python

```python
from pytest_bdd import scenarios, given, when, then

scenarios('login.feature')

@given("I am on the login page")
def open_login_page(login_page):
    login_page.open()

@when("I enter valid credentials")
def enter_credentials(login_page, valid_username, valid_password):
    login_page.login(valid_username, valid_password)

@then("I should see the dashboard")
def verify_dashboard(login_page):
    assert login_page.is_dashboard_displayed()
```

---

## 🌟 **Benefits**

✅ **Readable**: Makes test cases easy to understand for both technical and non-technical stakeholders.  
✅ **Reusable**: Test steps can be reused across multiple scenarios.  
✅ **Flexible**: Leverage Pytest's rich ecosystem for advanced testing needs.  

---

## 📚 **Documentation**

For detailed usage and examples, check the [official documentation](https://pytest-bdd.readthedocs.io/).

---

## 📜 **License**

This project is licensed under the [MIT License](LICENSE).
