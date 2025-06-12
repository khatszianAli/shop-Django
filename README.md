#  Shop-Django

A minimalist Django-based web application simulating an online shop. It includes product listings, cart management, and user authentication using Django's built‑in tools.

---
![image](https://github.com/user-attachments/assets/26cd6610-c51b-4f1d-8e31-21091aa2940f)

##  Features

- **User accounts**: Sign up, log in, and log out functionality  
- **Product catalog**: Display products with names, descriptions, prices, and images  
- **Shopping cart**: Add/remove items and view cart contents  
- **Admin interface**: Manage products and users via `/admin/`

---
![image](https://github.com/user-attachments/assets/88e6eb4a-5d27-4feb-beba-09a9089444d2)
![image](https://github.com/user-attachments/assets/321ca840-2791-4eeb-a473-f77356fc932e)
![image](https://github.com/user-attachments/assets/7f052bd6-d5d7-4b1a-a66a-e3498f637337)



##  Requirements

- Python 3.8+  
- Django (see `requirements.txt`)  
- SQLite (default) or configure your own database in `settings.py`

---

##  Setup & Run

1. **Clone the repo**:
    ```bash
    git clone https://github.com/khatszianAli/shop-Django.git
    cd shop-Django
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # on Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Database setup**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the server**:
    ```bash
    python manage.py runserver
    ```
    Visit the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
    Admin dashboard at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---


