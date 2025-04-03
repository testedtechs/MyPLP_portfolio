import json
import pymysql

def handler(event, context):
    if event["httpMethod"] != "POST":
        return {"statusCode": 405, "body": json.dumps({"error": "Method Not Allowed"})}

    # Parse JSON request body
    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError:
        return {"statusCode": 400, "body": json.dumps({"error": "Invalid JSON format"})}

    name = body.get("name")
    email = body.get("email")
    message = body.get("message")

    if not name or not email or not message:
        return {"statusCode": 400, "body": json.dumps({"error": "All fields are required"})}

    try:
        # Connect to MySQL Database
        conn = pymysql.connect(
            host="sql.freedatabase.com",  # Update this
            user="your_username",
            password="your_password",
            database="portfolio_db",
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            sql = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, message))
            conn.commit()

        conn.close()

        return {"statusCode": 200, "body": json.dumps({"message": "Message sent successfully!"})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
