<?php
/**
 * Created by PhpStorm.
 * User: Bartek
 * Date: 5/28/2018
 * Time: 11:58 PM
 */
$servername = "sql.s13.vdl.pl";
$username = "bastionk_vote";
$password = "Glosowanie12";
$dbname = "bastionk_votingsystem";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$yes = "SELECT yes_votes FROM Polls WHERE poll_name = ( SELECT MAX(poll_name) FROM Polls WHERE closed = 'closed' )";
$yesvotes = $conn->query($yes);
$yesvotes = $yesvotes->fetch_assoc();
$no = "SELECT no_votes FROM Polls WHERE poll_name = ( SELECT MAX(poll_name) FROM Polls WHERE closed = 'closed' )";
$novotes = $conn->query($no);
$novotes = $novotes->fetch_assoc();
$percentage =  (int)$novotes["no_votes"]/((int)$novotes["no_votes"] + (int)$yesvotes["yes_votes"]);
$dataPoints = array(array("label" => "No", "y" => (100*$percentage)), array("label" => "yes", "y" => (100-(100*$percentage))));
?>
<!DOCTYPE HTML>
<html>
<head>
    <title>Results</title>
    <script>
        window.onload = function () {


            var chart = new CanvasJS.Chart("chartContainer", {
                animationEnabled: true,
                title: {
                    text: "Results"
                },
                subtitles: [{
                    text: "latest poll"
                }],
                data: [{
                    type: "pie",
                    yValueFormatString: "#,##0.00\"%\"",
                    indexLabel: "{label} ({y})",
                    dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
                }]
            });
            chart.render();

        }
    </script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>