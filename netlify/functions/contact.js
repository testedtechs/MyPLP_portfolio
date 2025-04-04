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
    host: "sql5.freesqldatabase.com",
    user: "sql5771151",
    password: "gChwbALzlf",
    database: "sql5771151",
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
