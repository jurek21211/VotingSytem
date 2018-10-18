<?php
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
    $servername = "sql.s13.vdl.pl";
    $username = "bastionk_vote";
    $password = "Glosowanie12";
    $dbname = "bastionk_votingsystem";

    // Create connection\


    $conn = new mysqli($servername, $username, $password, $dbname);
    $allowed = false;

    if (isset($_POST['submit'])) {
        $conn = new mysqli($servername, $username, $password, $dbname);
        $allowed = false;

        $username = $_POST['username'];
        $password = $_POST['password'];
        $sql = "SELECT Card_ID FROM voters WHERE Card_ID = $username";
		$result = $conn -> query($sql);
		$conv = $result -> fetch_assoc();

		if ($conv['Card_ID'] == $_POST['username']){
            $allowed = true;
            //if user name found in database
            mysqli_close($conn);
            if (allowed){
                $_SESSION['login'] = true;
                $_SESSION['user'] = $username;
                header('LOCATION:steering.php');
                die();
            } {
                echo "<div class='alert alert-danger'>Username and Password do not match.</div>";
            }
        }
        else {
            $allowed = false;
            mysqli_close($conn);
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