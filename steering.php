<?php
$servername = "sql.s13.vdl.pl";
$username = "bastionk_vote";
$password = "Glosowanie12";
$dbname = "bastionk_votingsystem";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

session_start();
$sql = "SELECT Voted FROM `voters` WHERE `Card_ID` = {$_SESSION["user"]}";
$result = $conn->query($sql);
$conv = $result->fetch_assoc();

if (!isset($_SESSION['login'])) {
    header('LOCATION:login.php');
    die();
}
if ($conv["Voted"] === 'yes') {
    session_destroy();
    mysqli_close($conn);
    header('LOCATION:DisplayResult.php');
} else {
    mysqli_close($conn);
    header('LOCATION:vote.php');
}

exit()
?>
<html>
<head>
    <title>redirecting...</title>
</head>
<body>
</body>
</html>
