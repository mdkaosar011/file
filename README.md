# Django Social Media Application

A basic social media application built with Django, allowing users to create, update, and delete posts, including images, and manage user profiles.

## Features

- User authentication and profile management
- Create, update, and delete posts with images
- Django message Framework



## Technologies Used

- Django 5.1.6
- SQLite
- Pillow 11.1.0

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser (if needed):

   ```sh
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```sh
   python manage.py runserver
   ```

## Default Credentials

For testing purposes, you can use the following credentials:

- **Admin Panel**: `/admin/`
  - **Username**: `admin`
  - **Password**: `admin`
- **Test User**:
  - **Username**: `xyz`
  - **Password**: `password.xyz`



## Usage

- Visit `http://127.0.0.1:8000/` to access the application.

##

