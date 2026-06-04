<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=BuyZio+E-Commerce&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=A+Dynamic+Full-Stack+E-Commerce+Platform&descAlignY=62&descSize=16"/>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
  <br/><br/>
  <a href="https://buyzio.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-buyzio.onrender.com-38BDAE?style=for-the-badge&logo=googlechrome&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/karthi2006-46/buyzio">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</div>

---

## About The Project

**BuyZio** is a dynamic full-stack e-commerce web application that allows users to browse products, add items to a cart, and manage their orders seamlessly. Built with Python and Django on the backend and Bootstrap for a clean responsive UI, BuyZio demonstrates a complete shopping experience from product listing to cart management.

---

## Features

- **Product Listings** — Browse products with names, images, descriptions, and prices
- **Shopping Cart** — Add, update, and remove items from the cart in real time
- **User Authentication** — Register, login, and manage personal accounts securely
- **Order Management** — Place and track orders through a simple checkout flow
- **Admin Panel** — Django admin dashboard to manage products, orders, and users
- **Responsive Design** — Fully mobile-friendly UI built with Bootstrap
- **Search and Filter** — Find products quickly by name or category

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, Django, Django ORM |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript |
| **Database** | MySQL |
| **Deployment** | Render |
| **Version Control** | Git, GitHub |
| **IDE** | VS Code |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- MySQL 8+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/karthi2006-46/buyzio.git
cd buyzio

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure the database
# Open buyzio/settings.py and update DATABASES:
# 'NAME': 'buyzio_db',
# 'USER': 'YOUR_USERNAME',
# 'PASSWORD': 'YOUR_PASSWORD',
# 'HOST': 'localhost',
# 'PORT': '3306',

# 5. Create the database
mysql -u root -p -e "CREATE DATABASE buyzio_db;"

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create a superuser (for admin panel)
python manage.py createsuperuser

# 8. Start the server
python manage.py runserver
```

> The app will be live at `http://localhost:8000`
> Admin panel at `http://localhost:8000/admin`

---

## Project Structure

```
buyzio/
├── buyzio/
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL config
│   └── wsgi.py
├── store/
│   ├── models.py            # Product, Cart, Order models
│   ├── views.py             # Business logic
│   ├── urls.py              # App routes
│   ├── templates/
│   │   └── store/           # HTML templates
│   └── static/              # CSS, JS, Images
├── users/
│   ├── models.py            # User profile model
│   ├── views.py             # Auth views
│   └── templates/users/     # Login, Register pages
├── requirements.txt
└── manage.py
```

---

## Live Demo

> **[buyzio.onrender.com](https://buyzio.onrender.com)**

---

## Author

<div align="center">
  <strong>Karthikeyan R R</strong><br/>
  BCA Student &middot; Full-Stack Developer<br/>
  Dr. M.G.R. Educational and Research Institute, Chennai<br/><br/>
  <a href="mailto:rr.karthikeyan2006@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-rr.karthikeyan2006%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white"/>
  </a>
  <a href="https://linkedin.com/in/karthikeyan-rr">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://github.com/karthi2006-46">
    <img src="https://img.shields.io/badge/GitHub-karthi2006--46-181717?style=flat-square&logo=github&logoColor=white"/>
  </a>
</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&animation=twinkling"/>
