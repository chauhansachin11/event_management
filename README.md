# Event Management App

The Event Management App is a web application built with Django that allows users to view and book tickets for various events. The app has two types of users: Admin and User.

## Features

### Admin
- Create, update, and manage events
- View event summaries

### User
- View a list of events
- Book tickets for events within the booking window
- View booked tickets

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Change to the project directory: `cd event-management-app`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment:
   - On macOS and Linux: `source env/bin/activate`
   - On Windows: `.\env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Set up the database:
   - Please makesure to update the setting.py file with your database username and password.
   - Make migrations: `python manage.py makemigrations`
   - Apply migrations: `python manage.py migrate`

## Usage

1. Start the Django development server: `python manage.py runserver`
2. Open your web browser and go to: `http://localhost:8000`

## Admin Access

To access the admin panel:

1. Create a superuser: `python manage.py createsuperuser`
2. Enter your desired username and password
3. Go to: `http://localhost:8000/admin` and log in using your superuser credentials

## API Endpoints

The Event Management App provides the following API endpoints:

- POST /signup/ - User signup
- POST /login/ - User login
- GET /logout/ - User logout
- GET /user_home/ - User home page with a list of events and the ability to book tickets
- GET /event/{event_id}/ - Event details and summary
- POST /book_event/{event_id}/ - Book a ticket for an event
- GET /ticket/{ticket_id}/ - View details of a ticket
- GET /admin/home/ - Admin home page with a list of events
- POST /admin/create_event/ - Create a new event
- PUT /admin/update_event/{event_id}/ - Update an existing event



