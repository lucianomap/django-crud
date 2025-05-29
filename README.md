# 🚀 Django CRUD 

A simple web application developed with [Django](https://www.djangoproject.com/) to demonstrate CRUD (Create, Read, Update, Delete) operations.
This project simulates possible data operations for an Hotel managing its Guests.

---

## ✨ Features

* **List:** Landing page shows current guest list.
* **Add:** Add new guests to the hotel database.
* **Delete:** Remove guests from the database.

---

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/lucianomap/django-crud.git
    cd django-crud
    ```
2.  **Create and activate a virtual environment (optional)**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```
3.  **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Apply database migrations:**
    ```bash
    python3 manage.py migrate
    ```

5.  **Create a superuser (to access the Django Admin, if applicable):**
    ```bash
    python3 manage.py createsuperuser
    ```

---

## ▶️ Running the Application

1.  **Start the development server:**
    ```bash
    python3 manage.py runserver
    ```
2.  Open your browser and go to `http://127.0.0.1:8000/`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
