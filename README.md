# 📦 **BUYZIO – Full Python , Django E-Commerce Website**

A full-featured **E-commerce web application** built with **Django (Python)**, **MySQL**, **Bootstrap 5**, **HTML**, **CSS**, **JavaScript**, and **SweetAlert UI**.
This project includes User Authentication, Add to Cart, Add to Favourite (Wishlist), Product Management, Categories, Checkout UI, and Responsive Mobile Design.

---

## 🚀 **Features**

* User Registration & Login (Authentication System)
* Product Listing & Product Detail Page
* Add to Cart / Remove from Cart
* Add to Favourite / Wishlist
* Categories & Bestsellers Section
* Responsive UI with Bootstrap 5
* SweetAlert2 Popup Alerts
* MySQL Database Integration
* Django Admin Panel for backend management
* Fully mobile-friendly layout
* Modern premium UI design

---

## 🛠 **Tech Stack**

| Technology                  | Used For                              |
| --------------------------- | ------------------------------------- |
| **Python (Django)**         | Backend / MVC framework               |
| **MySQL**                   | Database                              |
| **HTML5, CSS3, JavaScript** | Frontend                              |
| **Bootstrap 5**             | UI Framework                          |
| **SweetAlert2**             | Stylish alerts & confirmation dialogs |
| **FontAwesome**             | Icons                                 |
| **Django ORM**              | Database operations                   |

---

## 📂 **Project Structure**

```
buyzio-ecommerce/
│── manage.py
│── requirements.txt
│
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/shop/
│   ├── static/css/style.css
│   └── static/images/
│
├── templates/
│   ├── shop/layouts/main.html
│   ├── shop/inc/navbar.html
│   └── shop/inc/footer.html
```

---

## ⚙ **Installation & Setup**

### Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/buyzio-ecommerce.git
cd buyzio-ecommerce
```

### Create virtual environment

```bash
python -m venv env
env\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Database in `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_karthi',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start the server

```bash
python manage.py runserver
```

---

## 📱 **Responsive Demo Screens (Add later)**

* Home Page
* Collections Page
* Product Detail
* Cart
* Favourite
* Login / Register

---

## 💡 **Future Enhancements**

* Online Payment Gateway (Razorpay / Stripe)
* Order tracking & email notifications
* Admin order processing system
* Coupon discount system
  

---

## 🧑‍💻 **Author**

**Karthikeyan**
📧 email: *[karthikeyan2006keyan@gmail.com](mailto:karthikeyan2006keyan@gmail.com)*

