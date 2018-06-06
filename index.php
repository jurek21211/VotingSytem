<?php
$servername = "sql.s13.vdl.pl";
$username = "bastionk_vote";
$password = "Glosowanie12";
$dbname = "bastionk_votingsystem";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
session_start();
echo isset($_SESSION['login']);
if (isset($_SESSION['login'])) {
    header('LOCATION:index.php');
    die();
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv='content-type' content='text/html;charset=utf-8'/>
    <title>Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h3 class="text-center">Login</h3>
    <?php
    if (isset($_POST['submit'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $card_id = array(2169576700, 1766824557, 2032311405, 2032775533, 1767844461, 1500354925, 1769991217);
        if (in_array($username, $card_id) && $password === 'password'){
            $_SESSION['login'] = true;
            $_SESSION['user'] = $username;
            header('LOCATION:admin.php');
            die();
        } {
            echo "<div class='alert alert-danger'>Username and Password do not match.</div>";
        }

      }
    ?>
    <form action="" method="post">
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" class="form-control" id="username" name="username" required>
        </div>
        <div class="form-group">
            <label for="pwd">Password:</label>
            <input type="password" class="form-control" id="pwd" name="password" required>
        </div>
        <button type="submit" name="submit" class="btn btn-default">Login</button>
    </form>
</div>
</body>
</html>