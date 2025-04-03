<?php
header("Content-Type: application/json");

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

$conn = new mysqli("sql5.freesqldatabase.com", "sql5771151", "gChwbALzlf", "sql5771151");

// Check if JSON data is received
$data = json_decode(file_get_contents("php://input"), true);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if ($data === null) {
        echo json_encode(["status" => "error", "message" => "Invalid JSON received"]);
        exit;
    }

    if (isset($data["name"], $data["email"], $data["message"])) {
        $name = $data["name"];
        $email = $data["email"];
        $message = $data["message"];

        $stmt = $conn->prepare("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $name, $email, $message);

        if ($stmt->execute()) {
            echo json_encode(["status" => "success", "message" => "Message sent successfully!"]);
        } else {
            echo json_encode(["status" => "error", "message" => "Database error: " . $stmt->error]);
        }
    } else {
        echo json_encode(["status" => "error", "message" => "Missing required fields"]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request method"]);
}
?>
