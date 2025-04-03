const mysql = require("mysql2/promise");

exports.handler = async function (event) {
    if (event.httpMethod !== "POST") {
        return { statusCode: 405, body: "Method Not Allowed" };
    }

    const { name, email, message } = JSON.parse(event.body);

    if (!name || !email || !message) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: "All fields are required." }),
        };
    }

    try {
        const connection = await mysql.createConnection({
            host: "sql.freedatabase.com", // Change this
            user: "your_username",
            password: "your_password",
            database: "portfolio_db",
        });

        const query = "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)";
        await connection.execute(query, [name, email, message]);

        await connection.end();

        return {
            statusCode: 200,
            body: JSON.stringify({ message: "Message sent successfully!" }),
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: "Database error: " + error.message }),
        };
    }
};
