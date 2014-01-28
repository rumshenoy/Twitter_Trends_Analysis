<?php


$searchthis = $_GET['value'];

$matches = array();

$handle = @fopen("/home/ramya/Anasuya/pirates.txt", "r");
if ($handle)
{
    while (!feof($handle))
    {
        $buffer = fgets($handle);
        if(strpos($buffer, $searchthis) !== FALSE)
            $matches[] = $buffer;
	
    }
    fclose($handle);
}

//show results:
echo json_encode($matches);
?>
