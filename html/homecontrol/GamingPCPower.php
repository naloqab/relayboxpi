<?php

$Power = $_GET["Power"];

exec ("sudo python3 /var/www/GamingPCPower.py $Power");

?>