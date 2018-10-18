<?php
/**
 * Created by PhpStorm.
 * User: Bartek
 * Date: 5/28/2018
 * Time: 11:57 PM
 */
$servername = "sql.s13.vdl.pl";
$username = "bastionk_vote";
$password = "Glosowanie12";
$dbname = "bastionk_votingsystem";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
?>
<html>
<head>
    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
        .btn:hover {
            transform: scale(1.1);
        }
    </style>
    <title>redirecting...</title>
</head>
<body>
<div class="container" align="center">
    <h1 class="text-center">Vote</h1>
    <?php
    session_start();
    $sql = "SELECT Voted FROM `voters` WHERE `Card_ID` = {$_SESSION["user"]}";
    $result = $conn->query($sql);
    $conv = $result->fetch_assoc();
    if (isset($_POST['yes'])) {
        if ($conv["Voted"] === 'no') {
            $yes = "UPDATE `Polls` SET `yes_votes` = `yes_votes` + 1 WHERE `closed` = 'open'";
            $conn->query($yes);
            $conn->query("UPDATE `voters` SET `Voted` = 'yes' WHERE `voters`.`Card_ID` = {$_SESSION["user"]}");
            mysqli_close($conn);
            session_destroy();
            header('LOCATION:DisplayResult.php');
        } else {
            header('LOCATION:DisplayResult.php');
        }
    }
    if (isset($_POST['no'])) {
        if ($conv["Voted"] === 'no') {
            $yes = "UPDATE `Polls` SET `no_votes` = `no_votes` + 1 WHERE `closed` = 'open'";
            $conn->query("UPDATE `voters` SET `Voted` = 'yes' WHERE `voters`.`Card_ID` = {$_SESSION["user"]}");
            $conn->query($yes);
            mysqli_close($conn);
            session_destroy();
            header('LOCATION:DisplayResult.php');
        } else {
            header('LOCATION:DisplayResult.php');

        }
    }

    ?>
    <form method="POST" action=''>
        <button type="submit" name="yes" class="btn btn-success" style="width:100px;height:60px;">Yes</button>
        <button type="submit" name="no" class="btn btn-danger" style="width:100px;height:60px;">No</button>
    </form>

</div>

</body>
</html>