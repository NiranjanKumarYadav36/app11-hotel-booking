#                 Hotel Booking System

## Overview
This repository contains a simple Hotel Booking System implemented in Python, using Pandas for data manipulation. The system allows users to book hotels, validate credit cards, and make spa reservations.

## Table of Contents
* Getting Started
* Usage
*  Structure

## Getting Started
To get started with this project, follow the steps below:

**1. Clone the Repository:**

``git clone https://github.com/NiranjanKumarYadav36/app11-hotel-booking.git`
``

**2. Install Dependencies:**

`pip install -r requirements.txt`

**3. Run the Application:**

`python main.py`

## Usage

**1. Enter Hotel ID:**

 * Run the application and input the ID of the hotel you want to book.

**2. Provide Credit Card Information:**

 * Enter credit card details (a dummy credit card is used in the provided code).

**3. Authenticate Credit Card:**

 * Authenticate the credit card using a password (a dummy password is used in the provided code).

**4. Book Hotel:**

 * If the hotel is available and the credit card is valid, the hotel will be booked.

**5. Generate Reservation Ticket:**

 * Enter your name, and a reservation ticket will be generated.

**6. Book Spa Package (Optional):**

 * Optionally, you can book a spa package after booking the hotel.

**7. Generate Spa Ticket (if applicable):**

 * If a spa package is booked, a spa ticket will be generated.

## Project Structure
* `main.py`: The main script for running the hotel booking system.

* `hotels.csv`, `cards.csv`, `card_security.csv`: Data files containing information about hotels, credit cards, and card security.

* `README.md`: This file providing information about the project.

* `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a Pull Request.