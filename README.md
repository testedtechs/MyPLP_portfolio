# Portfolio Website with Contact Form  
Live Project is running on
https://myplp.netlify.app/
Database is running on https://www.freesqldatabase.com

## Project Overview

This is a simple portfolio website with a contact form that allows visitors to send messages. The messages are stored in a MySQL database. The project consists of:

- `index.html` - The main page that includes the contact form.
- `contact.php` - The backend script that processes form submissions and stores them in the database.
The project started with using php as the backend to handle message submission into the datatbase, but when deploying, i realised netlify doesn't work with php files.
had to go back to the AI to help refactor the code using javascript only

## Features

- Responsive portfolio layout.
- Contact form with validation.
- MySQL database integration to store messages.
- PHP backend for handling form submissions.

## Setup Instructions

### 1. Create the Database

Log in to your FreeSQLDatabase.com account and create a new database.

Then run this SQL in phpMyAdmin to create the required table:

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

### 2. Configure the Netlify Serverless Function

Create a file at:
📁 netlify/functions/contact.js

const mysql = require("mysql2/promise");

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: "Method Not Allowed" }),
    };
  }

  const { name, email, message } = JSON.parse(event.body);

  const dbConfig = {
    host: "sql.freesqldatabase.com",
    user: "your_db_user",
    password: "your_db_password",
    database: "your_db_name",
  };

  try {
    const connection = await mysql.createConnection(dbConfig);
    const query = "INSERT INTO contact (name, email, message) VALUES (?, ?, ?)";
    await connection.execute(query, [name, email, message]);
    await connection.end();

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Message received successfully!" }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Database error: " + error.message }),
    };
  }
};

✅ Install the required package locally using:

npm init -y
npm install mysql2

Ensure package.json and package-lock.json are committed before deploying to Netlify.

### 3. Connect the Contact Form to the Function

Update your contact.html form to send data to the Netlify function:

<form id="contactForm" class="container-fluid py-5">
  <input type="text" name="name" id="name" placeholder="Your name" required />
  <input type="email" name="email" id="email" placeholder="Your email" required />
  <textarea name="message" id="message" placeholder="Your message" required></textarea>
  <button type="submit">Send Message</button>
</form>
<p id="responseMessage"></p>

<script>
document.getElementById("contactForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  const response = await fetch("/.netlify/functions/contact", {
    method: "POST",
    body: JSON.stringify({ name, email, message }),
    headers: { "Content-Type": "application/json" },
  });

  const result = await response.json();
  document.getElementById("responseMessage").innerText = result.message || result.error;
});
</script>

### 4. Deploy the Site

    Push your project to GitHub.

    Connect your repo to Netlify.

    In your project root, include a netlify.toml:

[build]
  functions = "netlify/functions"

## Development Decisions

Initially, this project was built using a PHP backend for the contact form. However, I replaced it with a serverless function using Node.js on Netlify to make it cloud-native, more scalable, and compatible with Netlify hosting.

Keeping HTML and logic separated improves structure, security, and maintainability.

## Future Improvements

- Add an admin panel to view submitted messages.
- Implement email notifications for new messages.
- Improve UI design using CSS frameworks like Tailwind or Bootstrap.

## Author

Ogunbekun Imoleayo

