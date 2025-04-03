# Portfolio Website with Contact Form  
Live Project is running on
https://myplp.netlify.app/
Database is running on https://www.freesqldatabase.com

## Project Overview

This is a simple portfolio website with a contact form that allows visitors to send messages. The messages are stored in a MySQL database. The project consists of:

- `index.html` - The main page that includes the contact form.
- `contact.php` - The backend script that processes form submissions and stores them in the database.

## Features

- Responsive portfolio layout.
- Contact form with validation.
- MySQL database integration to store messages.
- PHP backend for handling form submissions.

## Setup Instructions

### 1. Create the Database

Run the following SQL commands to set up the database:

```sql
CREATE DATABASE portfolio_db;
USE portfolio_db;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Configure the Backend

Ensure that `contact.php` is correctly configured with your database credentials:

```php
$conn = new mysqli("localhost", "root", "", "portfolio_db");
```

Modify the `localhost`, `root`, and password fields as needed.

### 3. Run the Project

- Place `index.html` and `contact.php` in the same directory.
- Start a local server (e.g.MySQL, WAMP or XAMPP).
- Open `index.html` in a browser.
- Test the contact form by submitting a message.

## Development Decisions

Initially, I attempted to merge `index.html` and `contact.php` into a single file, embedding the PHP logic within the HTML. However, I later decided to keep them separate to maintain better code structure and separation of concerns.

This separation allows for better scalability and easier debugging while keeping the HTML clean and reusable.

## Future Improvements

- Add an admin panel to view submitted messages.
- Implement email notifications for new messages.
- Improve UI design using CSS frameworks like Tailwind or Bootstrap.

## Author

Ogunbekun Imoleayo

