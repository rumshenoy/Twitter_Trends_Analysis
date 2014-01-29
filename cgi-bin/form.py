#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"

print """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>Project</title>
<link rel="stylesheet" type="text/css" href="css/style1.css" media="screen" />
</head>
<body>
<div id="header">
<h1>Twitter TrendsMap</h1>
<h1>Set Inputs</h1>
 <div id="menu">
  <ul id="nav">
   <li><a href="index.html">Home</a></li>
   <li><a href="country.html">Country Trends</a></li>
   <li><a href="city.html">City Trends</a></li>
   <li><a href="form.py">Inputs</a></li>
  </ul>
 </div>
</div>
<div id="content">
<div id="right">

"""
form = cgi.FieldStorage()
#message = form.getvalue("Location")

form = cgi.FieldStorage() 

# Get data from fields
print """

<style TYPE="text/css" > 
    <!--
	* { margin: 0; padding: 0; }
	body {font-family: Verdana, Arial; font-size: 12px; line-height: 18px; }
	a { text-decoration: none; }
	.container{margin: 20px auto; width: 900px; background: #fff;}
	h3 { margin-bottom: 15px; font-size: 22px; text-shadow: 2px 2px 2px #ccc; }
	
	#inputform {
	
	width: 500px;
	padding: 20px;
	background: #f0f0f0;
	overflow:auto;
	
	border: 1px solid #cccccc;
	-moz-border-radius: 7px;
	-webkit-border-radius: 7px;
	border-radius: 7px;	
	
	-moz-box-shadow: 2px 2px 2px #cccccc;
	-webkit-box-shadow: 2px 2px 2px #cccccc;
	box-shadow: 2px 2px 2px #cccccc;
	
	}
	
	.field{margin-bottom:7px;}
	
	label {
	font-family: Arial, Verdana; 
	text-shadow: 2px 2px 2px #ccc;
	display: block; 
	float: left; 
	font-weight: bold; 
	margin-right:10px; 
	text-align: right; 
	width: 120px; 
	line-height: 25px; 
	font-size: 15px; 
	}
	
	.input{
	font-family: Arial, Verdana; 
	font-size: 15px; 
	padding: 5px; 
	border: 1px solid #b9bdc1; 
	width: 300px; 
	color: #797979;	
	}
	
	.input:focus{
	background-color:#E7E8E7;	
	}
	
	.textarea {
	height:150px;	
	}
	
	.hint{
	display:none;
	}
	
	.field:hover .hint {  
	position: absolute;
	display: block;  
	margin: -30px 0 0 455px;
	color: #FFFFFF;
	padding: 7px 10px;
	background: rgba(0, 0, 0, 0.6);
	
	-moz-border-radius: 7px;
	-webkit-border-radius: 7px;
	border-radius: 7px;	
	}
	
	.button{
	float: right;
	margin:10px 55px 10px 0;
	font-weight: bold;
	line-height: 1;
	padding: 6px 10px;
	cursor:pointer;   
	color: #fff;
	
	text-align: center;
	text-shadow: 0 -1px 1px #64799e;
	
	background: #a5b8da;
	background: -moz-linear-gradient(top, #a5b8da 0%, #7089b3 100%);
	background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#a5b8da), to(#7089b3));
	
  	border: 1px solid #5c6f91;
	-moz-border-radius: 10px;
	-webkit-border-radius: 10px;
	border-radius: 10px;
  
	-moz-box-shadow: inset 0 1px 0 0 #aec3e5;
	-webkit-box-shadow: inset 0 1px 0 0 #aec3e5;
	box-shadow: inset 0 1px 0 0 #aec3e5;
	
	}
	
	.button:hover {
	background: #848FB2;
    cursor: pointer;
	}
    -->
   </style>
<form name = "inputform" action="cgi-bin/connect.py" method="post">


<div class="field">
<p>
<label>Select Location :</label>
</p>
<select name="location">
<option value="12586539" selected>Mumbai</option>
<option value="12586571">Bangalore</option>
<option value="20070458">Delhi</option>
<option value="12586798">Kolkata</option>
</select>
</div>

<div class="field">
<p>
<label>Select File :</label>
</p>
<select name="file">
<option value="tweets.txt" selected>tweets.txt</option>
<option value="pirates.txt">pirates.txt</option>
<option value="firefox.txt">firefox.txt</option>
</select>
</div>



<div class="field">
<label>Create a Trend?:</label>
<input type="checkbox" onclick="codename()" name="checkboxname" value="ON">
</div>
<br>

<div class="field">
<label>Enter a Specific Word?:</label>
<input type="text" disabled size="10" name="customTrend">
</div>

<br>
<br>
<div class="field">
<label>Word Frequency</label>
<input disabled maxlength="4" name="freq">  
</div>	  	


<input class="button" type="submit" redirect = "country.html" value="Submit"/>
</form>
</div>
</div>

<SCRIPT LANGUAGE="JavaScript"><!--
function codename() {

if(document.inputform.checkboxname.checked)
{
document.inputform.customTrend.disabled=false;
document.inputform.freq.disabled=false;
}
else
{
document.inputform.customTrend.disabled=true;
document.inputform.freq.disabled=true;
}
}
      
//-->
</SCRIPT>
</body>
</html>
""" 
#% cgi.escape(message)
#print "<p>name:", form["Location"].value

