<?php

$RelayNumber = $_GET["RelayNumber"];
$RelayStatus = $_GET["RelayStatus"];

exec ("sudo python /var/www/Relay.py $RelayNumber $RelayStatus");

?>