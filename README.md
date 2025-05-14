User Management System - Django REST Framework

Project Purpose

This project is a robust user management system built with Django and Django REST Framework. It provides a secure API backend for handling user accounts with full CRUD functionality, including user creation, deletion, password changes, and profile updates.

Tech Stack

- Backend Framework: Django 4.x
- API Framework: Django REST Framework (DRF)
- Database: SQLite
- Authentication: Token Authentication (DRF's built-in)
- Validation: Django model validators + DRF serializers
- Testing: Postman collection

Features Implemented

1. User Creation: Secure user registration endpoint
2. User Deletion: Account removal functionality
3. Password Management: Secure password change endpoint
4. Profile Updates: Modify user details
5. Data Validation: Comprehensive input validation

Setup Instructions

Prerequisites

- Python 3.9+
- pip (Python package manager)
- Virtualenv (recommended)

Installation

1. Clone the repository:
   ```bash
   git clone (https://github.com/SaliMerc/user-management-system/)
   cd UserManagement
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   Linux: source venv/bin/activate
   On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

Running the Development Server
```bash
python manage.py runserver
```
The API will be available at `http://localhost:8000/api/`

Postman Collection

The repository includes a Postman collection (`(https://salinemercy.postman.co/workspace/Saline-Mercy's-Workspace~7d90ad68-1f65-4df4-8a66-051acda73610/collection/44878844-360eed90-9448-43d6-927c-6652947211ca?action=share&creator=44878844&active-environment=44878844-53432727-a9e3-49c3-83d5-22bf63b190a0)`) with pre-configured requests for all API endpoints. 

Deployment Notes

For production deployment:
1. Set `DEBUG = False`
2. Configure a production database (PostgreSQL recommended)
3. Set up proper HTTPS configuration
4. Consider using:
   - Gunicorn or uWSGI as application server
   - Nginx as reverse proxy
   - WhiteNoise for static files
