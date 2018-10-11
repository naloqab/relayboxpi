<?php
exec ("sudo python /var/www/GetStatusUpdate.py", $output);

$Status = $output;
echo "<script>";
echo "\nvar R1 = '", $Status[0], "';";
echo "\nvar R2 = '", $Status[1], "';";
echo "\nvar R3 = '", $Status[2], "';";
echo "\nvar R4 = '", $Status[3], "';";
echo "\nvar R5 = '", $Status[4], "';";
echo "\nvar R6 = '", $Status[5], "';";
echo "\nvar R7 = '", $Status[6], "';";
echo "\nvar R8 = '", $Status[7], "';";
echo "\nvar L = '", $Status[8], "';";
echo "\nvar GPC = '", $Status[9], "';";
echo "\n</script>";
?>