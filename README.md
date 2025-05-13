User Management System - Django REST Framework

Project Purpose

This project is a robust user management system built with Django and Django REST Framework. It provides a secure API backend for handling user accounts with full CRUD functionality, including user creation, deletion, password changes, and profile updates. The system is designed to be integrated with frontend applications or used as a microservice in larger architectures.

Tech Stack

- Backend Framework: Django 4.x
- API Framework: Django REST Framework (DRF)
- Database: SQLite (default for development, easily configurable for PostgreSQL/MySQL)
- Authentication: Token Authentication (DRF's built-in)
- Validation: Django model validators + DRF serializers
- Testing: Postman collection included

Features Implemented

1. User Creation: Secure user registration endpoint
2. User Deletion: Account removal functionality
3. Password Management: Secure password change endpoint
4. Profile Updates: Modify user details
5. Data Validation: Comprehensive input validation
6. API Documentation: Self-documenting through DRF's browsable API

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
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

### Running the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|--------------------------|
| `/api/users/` | POST | Create new user | No |
| `/api/users/{id}/` | GET | Get user details | Yes |
| `/api/users/{id}/` | PUT/PATCH | Update user details | Yes |
| `/api/users/{id}/` | DELETE | Delete user | Yes |
| `/api/change-password/` | POST | Change password | Yes |
| `/api/token/` | POST | Obtain authentication token | No |

## Postman Collection

The repository includes a Postman collection (`UserManagement.postman_collection.json`) with pre-configured requests for all API endpoints. Import this into Postman to quickly test all available operations.

Testing

To run the test suite:
```bash
python manage.py test
```

## Configuration

Environment variables can be configured in `settings.py` or through a `.env` file:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `DATABASE_URL`: For production database configuration

## Deployment Notes

For production deployment:
1. Set `DEBUG = False`
2. Configure a production database (PostgreSQL recommended)
3. Set up proper HTTPS configuration
4. Consider using:
   - Gunicorn or uWSGI as application server
   - Nginx as reverse proxy
   - WhiteNoise for static files
