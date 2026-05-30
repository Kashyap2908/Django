# Django Learning Repository

This repository contains a collection of Django projects (`demo1`, `demo2`, and `demo3`) designed to demonstrate core Django framework concepts. It progresses from basic URL routing and simple views to dynamic template rendering and database integration using the Django ORM.

## 📁 Repository Structure

The repository is divided into three main demonstration projects:

### 1. `demo1`: Basic Routing and Views
This project serves as an introduction to the Django framework.
* **Concepts Covered:**
  * Setting up a Django project and app (`app1`).
  * Basic URL routing (`urls.py`).
  * Creating simple views returning `HttpResponse` (Home, About, Contact).
  * Rendering a static HTML template (`1.html`) containing inline CSS and JavaScript.

### 2. `demo2`: Django Template Language (DTL) and Context
This project introduces a fun Indian Premier League (IPL) theme to demonstrate how dynamic data interacts with HTML pages.
* **Concepts Covered:**
  * Serving multiple HTML pages (`home.html`, `MI.html`, `GT.html`, `CSK.html`).
  * Passing complex data structures (Dictionaries and Lists) from `views.py` to templates.
  * Utilizing the Django Template Language (DTL).
  * Using `{% for %}` loops to iterate over data and generate HTML tables dynamically (seen in the Mumbai Indians page).
  * Using `{% if %}` / `{% else %}` logic to render conditional data.

### 3. `demo3`: Database Integration, Models, and Forms
The most advanced project in the repository. It builds upon the IPL theme but introduces backend data management and template inheritance.
* **Concepts Covered:**
  * **Template Inheritance:** Using a `base.html` layout with `{% extends %}` and `{% block %}` tags to maintain a consistent UI (Navbar and styling) across all pages.
  * **Django Models & ORM:** Creating a `Student` model (Name, Email, Age) in `models.py` to define database schema.
  * **SQLite Integration:** Utilizing Django's default `db.sqlite3` database to store records.
  * **HTML Forms & Request Handling:** * Serving a data collection form (`get.html`).
    * Handling `GET` requests in `views.py` to capture user input.
    * Saving new records to the database using `Student.objects.create()`.
  * **Data Retrieval:** Fetching all records from the database using `Student.objects.all()` and displaying them on a dedicated page (`db.html`).

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Django (Version 6.0.3 used in this project)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repository-folder>
