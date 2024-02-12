<?php
// Command to execute the Python script
$command = "python3 /var/www/html/TP1-Redis-INFO834/AdminServices/TP1Redis.py";

// Execute the command and capture the output
$output = exec($command);

// Output the result
echo "Result of Python script execution: " . $output;
?>
