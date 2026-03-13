#Question 1-5
# Django Blog Application – Assignment

## Overview
This project is a **Blog Application built using Django**. The application allows administrators to create and manage blog posts through the Django admin panel. Each blog post contains a title, slug, body content, author information, publish date, and status (Draft or Published).

Only posts with **Published status** are visible on the main blog page. Users can click a post to view its full details.

---

## Objectives
- Understand Django project and application structure
- Create models and perform migrations
- Use Django admin for managing data
- Implement relationships using ForeignKey
- Implement views, templates, and URL routing
- Create SEO-friendly URLs

---

## Technologies Used
- Python
- Django
- SQLite Database
- HTML (Django Templates)

---

## Requirements

Make sure the following are installed on your system:

- Python 3.x
- pip (Python package manager)
- Django

You can install Django using:

```bash
pip install django
```

To verify installation:

```bash
python -m django --version
```

---

## Project Structure

```
college_blog/
│
├── college_blog/
│   ├── settings.py
│   ├── urls.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       └── blog/
│           ├── base.html
│           └── post/
│               ├── list.html
│               └── detail.html
│
├── db.sqlite3
└── manage.py
```

---

## Post Model

The **Post model** stores blog post data in the database.

### Fields

| Field | Description |
|------|-------------|
| title | Title of the blog post |
| slug | URL friendly title |
| body | Content of the post |
| publish | Publish date and time |
| created | Automatically stores creation time |
| updated | Automatically stores modification time |
| status | Draft or Published |
| author | Links the post with a user |

Posts are ordered by **latest publish date first**.

---

## Custom Manager

A custom manager **PublishedManager** is used to return only posts with status **Published**.

Example:

```python
Post.published.all()
```

This ensures that only published posts are shown on the website.

---

## Installation and Setup

Follow these steps to run the project.

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd college_blog
```

or simply download and open the project folder.

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Django

```bash
pip install django
```

---

### 4. Apply Database Migrations

Run the following commands to create database tables:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 5. Create Admin User

Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

Enter:

```
Username
Email
Password
```

---

### 6. Run Development Server

```bash
python manage.py runserver
```

---

### 7. Open the Application

Homepage:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials.

---

## Expected Output

- Admin panel accessible
- Posts can be added from the admin panel
- Homepage displays only **published posts**
- Clicking a post opens the detail page
- URLs contain **date and slug**

Example:

```
http://127.0.0.1:8000/2026/03/13/my-first-post/
```

---

## Conclusion

This project demonstrates how to build a **basic blog application using Django**. It integrates models, views, templates, URLs, and Django's admin interface to manage and display blog posts efficiently.

#Question 6-10
# Django Student Management System

## Project Overview

This project is a **Django-based Student Management System** developed as part of a Django assignment. The application demonstrates the implementation of Django's **Model–View–Template (MVT) architecture**, database migrations, administrative interface customization, and relational database modeling.

The system allows administrators to manage **students and departments**, while users can view a list of students and detailed information about each student.

---

## Project Structure

```
college_project/
│
├── college_project/
│   ├── settings.py
│   ├── urls.py
│
├── studentApp/
│   ├── migrations/
│   ├── templates/
│   │   └── studentApp/
│   │       ├── student_list.html
│   │       └── student_detail.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
└── manage.py
```

---

## Features

* Django project setup with a dedicated application (`studentApp`)
* Student model with fields:

  * name
  * age
  * roll_number
  * created
* Department model for organizing students
* Relationship between **Student and Department**
* Automatic timestamp for student creation
* Alphabetical ordering of students
* Admin panel customization with:

  * list display
  * filtering
  * search functionality
  * ordering
* Student list page displaying all students
* Student detail page displaying complete information
* URL routing for navigation between pages

---

## Database Models

### Student Model

Fields included in the Student model:

| Field       | Type          | Description                         |
| ----------- | ------------- | ----------------------------------- |
| name        | CharField     | Student name                        |
| age         | IntegerField  | Student age                         |
| roll_number | CharField     | Unique student roll number          |
| created     | DateTimeField | Automatically records creation time |
| department  | ForeignKey    | Links student to a department       |

### Department Model

| Field | Type      | Description     |
| ----- | --------- | --------------- |
| name  | CharField | Department name |

Deleting a department will automatically delete all associated students using **CASCADE deletion**.

---

## Installation and Setup

### 1. Clone or Download the Project

```
git clone <repository-url>
cd college_project
```

### 2. Install Dependencies

Make sure Python and Django are installed.

```
pip install django
```

### 3. Run Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User

```
python manage.py createsuperuser
```

### 5. Run the Development Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## Application URLs

| URL               | Description                            |
| ----------------- | -------------------------------------- |
| `/students/`      | Displays the list of students          |
| `/students/<id>/` | Displays details of a specific student |
| `/admin/`         | Django administration panel            |

---

## Expected Outcomes

* Students are ordered alphabetically by name
* New fields appear in the admin panel
* Database schema updated successfully
* Student–Department relationship implemented
* Deleting a department removes related students
* Student list page displays data dynamically
* Student detail page shows full information
* Navigation between pages works correctly
* Admin panel supports search, filters, and ordering

---

## Technologies Used

* Python
* Django Framework
* SQLite Database
* HTML Templates

---

## Author

Aryan
Django Assignment – Student Management System
