<?php

// code to print out the temperature database in tabular form

$username="root";
$password="root";
$database="templog";
$server="localhost";
$con=mysqli_connect($server,$username,$password,$database);
//mysql_select_db($database);
  
$query="SELECT * FROM `temp-at-interrupt` ORDER BY `Date` DESC, `Time` DESC;"; 
$result=mysqli_query($con,$query);

?>
<html>
   <head>
      <title>Sensor Data</title>
   </head>
<body>
   <h1>Temperature readings</h1>

   <table border="1" cellspacing="1" cellpadding="1">
		<tr>
			<td>&nbsp;Date&nbsp;</td>
			<td>&nbsp;Time&nbsp;</td>
			<td>&nbsp;Temperature&nbsp;</td>
		</tr>

      <?php 
		  if($result!==FALSE){
		     while($row = mysqli_fetch_array($result)) {
		        printf("<tr><td> &nbsp;%s </td><td> &nbsp;%s&nbsp; </td><td> &nbsp;%s&nbsp; </td></tr>", 
		           $row["date"], $row["time"], $row["temperature"]);
		     }
		     mysqli_free_result($result);
		     mysqli_close($con);
		  }
      ?>

   </table>
</body>
</html>
