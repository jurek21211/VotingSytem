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
    <title>redirecting...</title>
</head>
<body>
<div class="container" align="center">
    <h3 class="text-center">Vote</h3>
    <?php
    session_start();
    if (isset($_POST['yes'])) {
        $yes = "UPDATE `Polls` SET `yes_votes` = `yes_votes` + 1 WHERE `closed` = 'open'";
        $conn->query($yes);
        $conn->query("UPDATE `voters` SET `Voted` = 'yes' WHERE `voters`.`Card_ID` = {$_SESSION["user"]}");
        mysqli_close($conn);
        session_destroy();
        header('LOCATION:DisplayResult.php');
    }
    if (isset($_POST['no'])) {
        $yes = "UPDATE `Polls` SET `no_votes` = `no_votes` + 1 WHERE `closed` = 'open'";
        $conn->query("UPDATE `voters` SET `Voted` = 'yes' WHERE `voters`.`Card_ID` = {$_SESSION["user"]}");
        $conn->query($yes);
        mysqli_close($conn);
        session_destroy();
        header('LOCATION:DisplayResult.php');
    }
    ?>
    <form method="POST" action=''>
        <button type="submit" name="yes" class="btn btn-default">Yes</button>
        <button type="submit" name="no" class="btn btn-default">No</button>
    </form>

</div>

</body>
</html>