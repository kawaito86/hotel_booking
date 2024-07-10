Hotel Booking System
For my final project for CS50's Web Programming with Python and JavaScript, I decided to create a Hotel Booking System. This application aims to provide an efficient, user-friendly platform for managing hotel bookings, complete with real-time room availability, dynamic pricing, and automated email notifications.

Overview
The Problem
Many small hotels and bed-and-breakfasts struggle to manage their bookings efficiently, often relying on manual processes that are time-consuming and error-prone. These businesses may not have the resources to invest in expensive, enterprise-level booking systems, yet they require robust solutions to manage their operations and enhance customer satisfaction.

The Solution
To address this issue, I developed a Hotel Booking System that allows hotel managers to easily handle room bookings, manage availability, and communicate with guests through automated emails. The system is designed to be intuitive and scalable, making it suitable for small to medium-sized establishments.

Distinctiveness and Complexity
Distinctiveness
This project is unique in its comprehensive approach to handling hotel bookings, integrating features such as real-time room availability, dynamic pricing based on seasonal demand, and automated email notifications. These features distinguish it from simpler booking systems that do not account for fluctuating prices or offer automated communication with guests.

Complexity
The complexity of this project is evident in several key areas:

Dynamic Pricing: The system calculates room prices dynamically based on predefined rules, adjusting rates for high and low seasons automatically.
Real-Time Availability: The application ensures that only available rooms can be booked, updating availability in real-time to prevent overbooking.
Automated Email Notifications: Upon booking confirmation, guests receive detailed emails with their booking information, reducing the need for manual communication.
Admin Panel: The admin interface allows hotel managers to manage rooms, update details, adjust availability, and set seasonal pricing rules efficiently.
File Descriptions
booking/
models.py: Defines the data models for Room and Booking, including methods for dynamic pricing.
views.py: Handles the logic for displaying available rooms, booking rooms, and sending confirmation emails.
forms.py: Contains the forms used for booking.
urls.py: Maps URLs to the corresponding views.
templates/: HTML templates for rendering the web pages.
hotel_booking/
settings.py: Configuration settings for the Django project.
urls.py: URL configurations for the project.
Root Directory
manage.py: Django's command-line utility for administrative tasks.
requirements.txt: Lists the dependencies required to run the application.
How to Run the Application
Clone the repository:

bash
Copy code
git clone https://github.com/kawaito86/hotel_booking.git
cd hotel_booking
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open a web browser and go to http://127.0.0.1:8000/ to view the user interface.
Access the admin panel at http://127.0.0.1:8000/admin/.
Additional Information
Email Configuration
To enable email notifications, configure the email settings in settings.py:

python
Copy code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = your_smtp_port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
Environment Variables
For production deployment, ensure to set the necessary environment variables, such as DEBUG, ALLOWED_HOSTS, and database configurations, to enhance security and performance.

Database
The project uses SQLite for development purposes. For production, consider using a more robust database system like PostgreSQL.

Deployment
This application can be deployed on platforms like Heroku, PythonAnywhere, or any cloud service provider that supports Django applications. Ensure to configure static files, environment variables, and the database accordingly for a smooth deployment.

Detailed Features
User Authentication
Django's built-in authentication system was used to create a secure login, logout, and registration system. The password reset functionality is also implemented using Django's standard authentication system, with custom HTML templates for user-friendly interaction.

Admin Dashboard
The admin dashboard is designed for hotel staff to manage rooms, bookings, and customer information. Staff can upload room details, manage availability, and adjust pricing dynamically. The dashboard also allows uploading and storing booking confirmations and guest details.

Booking Management
Staff can upload booking information using CSV files and manage booking records efficiently. Guests can view room availability in real-time and book rooms directly from the website. Upon booking, an email confirmation is sent to the guest with all relevant details.

Mobile-Responsive Design
The application is designed to be mobile-responsive, ensuring a seamless experience for users accessing the system from various devices.
