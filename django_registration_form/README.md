# Django Registration Form

A complete Django registration form application with SQLite database and Bootstrap styling.

## Features

- **User Registration**: Username, email, and password fields
- **Form Validation**:
  - Username: 3+ characters, unique, alphanumeric + underscores only
  - Email: Unique email validation
  - Password: Minimum 8 characters, 1 uppercase letter, 1 digit
  - Password confirmation matching
- **SQLite Database**: Built-in Django database
- **Bootstrap 5 Styling**: Modern, responsive UI
- **Admin Interface**: Manage registrations through Django admin

## Project Structure

```
django_registration_form/
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── registration_project/     # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── templates/
│       ├── base.html        # Base template with Bootstrap
│       └── index.html       # Home page
└── users/                    # Users app
    ├── models.py            # UserRegistration model
    ├── forms.py             # RegistrationForm with validation
    ├── views.py             # Registration views
    ├── urls.py              # App URLs
    ├── admin.py             # Admin configuration
    ├── apps.py
    └── templates/users/
        ├── register.html    # Registration form page
        └── success.html     # Success page
```

## Installation & Setup

### 1. Install Django

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install Django==4.2.0
```

### 2. Navigate to Project Directory

```bash
cd django_registration_form
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (Optional - for Admin Access)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Usage

### User Registration

1. Navigate to `http://127.0.0.1:8000/register/`
2. Fill in the registration form:
   - **Username**: Choose a unique username (3+ characters)
   - **Email**: Enter a valid email address
   - **Password**: Create a strong password (8+ chars, 1 uppercase, 1 digit)
   - **Confirm Password**: Re-enter your password
3. Click **Register**
4. On successful registration, you'll be redirected to the success page

### Admin Panel

1. Create a superuser: `python manage.py createsuperuser`
2. Access admin at: `http://127.0.0.1:8000/admin/`
3. View all registrations and user accounts

## Password Requirements

- Minimum 8 characters
- At least 1 uppercase letter (A-Z)
- At least 1 digit (0-9)
- Passwords must match in both fields

## Form Validation

- **Username**: Must be unique, 3+ characters, alphanumeric + underscores
- **Email**: Must be valid and unique
- **Password**: Strength validation as above
- **Confirm Password**: Must match the password field

## Database

SQLite database is automatically created at: `db.sqlite3`

No additional database setup required!

## Files Overview

### models.py
Defines the `UserRegistration` model that extends Django's built-in User model to store additional registration data.

### forms.py
Contains the `RegistrationForm` class with comprehensive field validation:
- Custom clean methods for each field
- Password strength validation
- Duplicate user/email checking

### views.py
- `register()`: Handles GET (display form) and POST (process registration)
- `success()`: Success page after registration
- `home()`: Home page

### urls.py
Routes for the application:
- `/` - Home page
- `/register/` - Registration form
- `/success/` - Success page

### templates/
Bootstrap-styled HTML templates with form rendering and validation messages.

## Security Notes

- Change `SECRET_KEY` in `settings.py` before production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement HTTPS in production
- Consider adding email verification

## Future Enhancements

- Email verification
- Login/Logout functionality
- User profile page
- Password reset
- OAuth2 integration
- Two-factor authentication

## License

Free to use and modify for learning purposes.
