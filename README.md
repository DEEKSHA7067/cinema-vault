# CinemaVault

CinemaVault is a modular console-based Python application for movie ticket booking, seat selection, food pre-ordering, and billing management designed as a BTech academic project.

## Features

- Secure manager login with password protection (`0030`)
- Customer registration and login system
- CRUD operations on movies: add, view, delete
- Set movie showtimes and ticket prices
- Book tickets with seat selection and 3D glasses option
- Food menu management with food pre-booking functionality
- Simulated payment process for tickets
- Movie rating and review system
- Loyalty points reward system for customers
- Automated bill/receipt generation covering ticket and food purchases

## Technologies Used

- Python 3.x for the entire project
- Modular programming with multiple `.py` files for separation of concerns
- Standard Python data structures (dictionaries, lists) for in-memory storage

## Installation and Running

1. Clone or download the repository to your local computer.
2. Ensure Python 3.x is installed. (Test with `python --version`)
3. Navigate to the project directory in a terminal.
4. Run the program with:
    ```
    python main.py
    ```
5. For Manager access, input password: `0030`
6. For customers, register a new account from the main menu and then login.

## Usage Overview

- Manager can add/delete/view movies and manage the food menu.
- Customers can browse movies, book tickets, pre-book food, pay, review movies, and generate bills.
- Clear, text-based menus guide user interaction.
- Error handling ensures robust operation.

## Project Structure

- `main.py` : Main entry point and menu system with role-based login.
- `data.py` : Shared data storage using dictionaries and lists.
- `users.py` : User registration and authentication.
- `movies.py` : Movie management including showtimes, prices, and reviews.
- `booking.py` : Ticket booking, cancelation, 3D glasses option, payments.
- `seats.py` : View seat availability.
- `food.py` : Food menu management and pre-booking.
- `receipt.py`: Bill/receipt generation combining ticket and food orders.

## Testing

- Thorough testing done through various user and manager scenarios.
- Board cases for invalid seats, duplicate bookings, payment without booking handled.
- Customer login with invalid credentials prompts error.
- Manager login denies access without correct password.

## Known Limitations

- Data is stored in memory; restarting resets all bookings and registrations.
- No graphical UI; console-based interaction only.
- Single-user sessions per run.

## Future Enhancements

- Persist data using a database or file storage.
- Add graphical seat selection and UI.
- Send email/SMS confirmation for bookings.
- Implement multi-theater support and advance booking time slots.

## Author

Somya Asati
BTech CSE(Cyber Security and digital forensic) 
VIT Bhopal

---

