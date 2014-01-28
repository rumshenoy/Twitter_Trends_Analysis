<?php
$con = mysql_connect("localhost","root","");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
$woeid = $_GET['woeid'];
mysql_select_db("nltk_trends", $con);
$result = mysql_query("SELECT * FROM topwords WHERE woeid = $woeid ORDER BY frequency DESC LIMIT 10");
$trend = array();
$freq = array();
$myarray = array();
while($row = mysql_fetch_array($result))
  {
  //echo $row['trend'] ;
  //echo "<br />";
	//array_push($trend,$row['tweet']);
	//array_push($freq,$row['frequency']);
	array_push($myarray,array($row['tweet'],$row['frequency']));
	

  }
//print_r($trend);
mysql_close($con);
//array_push($myarray,$trend);
//array_push($myarray,$freq);
//echo json_encode($myarray);
echo json_encode($myarray);
?>
