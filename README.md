# Aduanepa-Fie Restaurant Booking System

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [User Stories](#user-stories)
7. [Database Schema](#database-schema)
8. [API Endpoints](#api-endpoints)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Future Enhancements](#future-enhancements)
12. [Contributing](#contributing)
13. [License](#license)

## Introduction

Aduanepa-Fie is a full-stack web application for a restaurant booking system. The name "Aduanepa-Fie" means "home of good food" in Twi, reflecting the restaurant's commitment to providing excellent culinary experiences. This system allows customers to view the restaurant's menu, make table reservations, and manage their bookings, while providing staff with tools to manage reservations efficiently.

## Features

- User registration and authentication
- Restaurant menu display
- Visually appealing menu with food images
- Table reservation system
- Booking management (view, create, update, cancel)
- Admin panel for staff to manage bookings and menu items
- Responsive design for mobile and desktop use

## Technologies Used

- Django 5.0.7
- Python 3.12
- SQLite (development) / PostgreSQL (production)
- HTML, CSS, JavaScript
- Bootstrap 5
- Whitenoise for static file serving
- Gunicorn for WSGI server
- Heroku

## Setup and Installation

1. Clone the repository:
   git clone https://github.com/your-username/aduanepa-fie.git
cd aduanepa-fie

2. Create a virtual environment and activate it:
   python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:

   SECRET_KEY=your_secret_key

   DEBUG=True

   ALLOWED_HOSTS=localhost,127.0.0.1

5. Run migrations: python manage.py migrate
6. Create a superuser: python manage.py createsuperuser

7. Run the development server: python manage.py runserver

   Visit `http://127.0.0.1:8000/` in your browser to see the application.

## Usage

- Register for an account or log in if you already have one.
- Browse the menu to see available dishes.
- Make a reservation by selecting a date, time, and number of guests.
- View and manage your bookings from your account dashboard.
- Admin users can access the admin panel at `/admin` to manage bookings, menu items, and user accounts.

## User Stories

- As a new user, I want to register for an account so that I can make restaurant bookings.
- As a registered user, I want to log in to my account so that I can access my bookings and make new ones.
- As a customer, I want to view the restaurant's menu so that I can decide if I want to dine there.
- As a logged-in customer, I want to make a table reservation for a specific date and time so that I can secure my dining experience.
- As a customer making a booking, I want to specify the number of guests so that the restaurant can allocate an appropriate table.
- As a logged-in customer, I want to view my current and upcoming bookings so that I can keep track of my reservations.
- As a logged-in customer, I want to cancel my booking if my plans change so that I can free up the table for others.
- As a customer, I want to receive a confirmation email after making a booking so that I have a record of my reservation.
- As a restaurant staff member, I want to view all bookings for a specific date so that I can prepare for the day's service.
- As a restaurant manager, I want to set the capacity for each table so that the booking system can accurately allocate tables.
- As a customer, I want to be notified if my preferred time slot is unavailable so that I can choose an alternative time.
- As a restaurant owner, I want to ensure that double bookings are prevented so that I can maintain an efficient service.
- As a logged-in customer, I want to modify my existing booking (date, time, or number of guests) so that I can adjust my plans if needed.
- As a restaurant staff member, I want to mark bookings as arrived so that I can keep track of no-shows.
- As a customer, I want to leave a review after my dining experience so that I can share my feedback with the restaurant and other potential customers.

## Database Schema

1. User
- Fields: username, email, password, etc. (Django's built-in User model)

2. Table
- Fields: number, capacity

3. MenuItem
- Fields: name, description, price

4. Booking
- Fields: user (FK), table (FK), date, time, guests, created_at, updated_at

5. Order (for future implementation)
- Fields: booking (FK), item (FK), quantity

## API Endpoints

- `/` - Home page
- `/menu/` - Restaurant menu
- `/book/` - Make a reservation
- `/my-bookings/` - View user's bookings
- `/cancel-booking/<int:booking_id>/` - Cancel a specific booking
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/accounts/register/` - User registration

## Testing

1. Unit Tests

   Unit tests are crucial for verifying the functionality of individual components or pieces of code, such as models, views, and utility functions.
   
   - Models : the behavior of each model was tested, including methods, field validations, and relationships between models. For Example:  A test that a Booking object can be created with valid data, and cannot be created with invalid data (e.g., missing required fields).

   - Views: Test the output of view functions, ensuring they return the correct templates, status codes, and context data. For example: A test that the home view returns a status code of 200 and uses the correct template.

   - Forms: Test that forms handle valid and invalid input correctly. For example: A test that the BookingForm can correctly validate guest numbers and dates.

2. Integration Tests

   Integration tests are used to verify that different parts of the system work together as expected. This includes testing the interaction between different components like views, templates, and models.

    - End-to-End Functionality: Test the entire booking flow, from selecting a date and time to confirming a booking, ensuring all parts work together. For example: A test that a user can navigate to the booking page, fill out a form, and successfully create a booking.

   - Database Integration: Ensure that the application correctly reads from and writes to the database. For example: A test that creating a new Booking via the form saves the correct data in the database.
   
3. User Acceptance Testing (UAT)

   UAT involves testing the system from the user's perspective to ensure that it meets their expectations and requirements.

   - Functional Testing: Test the core functionalities from a user's perspective, ensuring they can accomplish key tasks without issues. For example: Verify that users can register, log in, view the menu, book a table, and view/cancel their bookings.

   - Usability Testing: Evaluate the user interface and experience, ensuring that it is intuitive and easy to navigate. 

   - Security Testing: Ensure that the system is secure, particularly focusing on authentication and data protection. For example: Test that only authenticated users can access specific features like viewing or canceling their bookings.

## Deployment

This project is deployed on Heroku. To deploy your own instance:

1. Create a new Heroku app
2. Set up the necessary environment variables in Heroku's config vars
3. Connect your GitHub repository to the Heroku app
4. Enable automatic deploys or manually deploy your main branch

## Future Enhancements

- Implement a review system for customers
- Add a more detailed staff dashboard with analytics
- Integrate a payment system for pre-booking payments or deposits
- Implement a loyalty program for regular customers
- Allow restaurant staff to upload and update menu item images through the admin interface
- Implement image optimization for faster loading times

## Contributing

Contributions to Aduanepa-Fie are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.