<?php
$con = mysql_connect("localhost","root","");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
$woeid = $_GET['woeid'];

mysql_select_db("nltk_trends", $con);

$result = mysql_query("SELECT * FROM topwords WHERE woeid = $woeid LIMIT 10");
$trend = array();
$freq = array();
$myarray = array();
array_push($myarray,array('Trend','Frequency'));


while($row = mysql_fetch_array($result))
  {
	array_push($myarray,array($row['tweet'],(int)$row['frequency']));
  }
mysql_close($con);
echo json_encode($myarray);
?>
