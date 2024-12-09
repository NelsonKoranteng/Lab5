# Lab-5

This is a web application built with Django that allows users to create, view, update, and delete blog posts. It includes features like user authentication, responsive design, and additional functionalities like comments and user profiles.

Features
Authentication:

User registration, login, and logout functionality.
CRUD Operations:

Create, read, update, and delete blog posts.
Comments:

Add, view, and manage comments on blog posts.
Search:

Search blog posts by title or content.
Responsive Design:

Fully responsive layout that works across various screen sizes.
Stretch Goals:

User profiles with personal information and list of blog posts.
Social media sharing of blog posts.
Blog post rating functionality.
Technologies Used
Backend: Django 5.1.4 (Python 3.11)
Database: SQLite (default Django database)
Frontend: HTML5, CSS3, Bootstrap
Authentication: Django's built-in user authentication system
Getting Started
Prerequisites
Python 3.10 or higher
Virtual environment manager (e.g., venv)
Installation Steps
Clone the Repository:


git clone <repository_url>
cd blog_project
Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:


pip install -r requirements.txt
Apply Migrations:


python manage.py makemigrations
python manage.py migrate
Create a Superuser:

python manage.py createsuperuser
Run the Development Server:

python manage.py runserver
Access the Application: Open a web browser and navigate to http://127.0.0.1:8000/.

