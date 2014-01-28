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
  //echo $row['trend'] ;
  //echo "<br />";
	array_push($myarray,array($row['tweet'],(int)$row['frequency']));
	//array_push($trend,$row['tweet']);

  }
//print_r($trend);
mysql_close($con);
//array_push($myarray,$trend);
//array_push($myarray,$freq);
echo json_encode($myarray);

?>
