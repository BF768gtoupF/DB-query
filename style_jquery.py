import pymysql
import os,sys
import cgi, csv
import matplotlib
import numpy as np
import pandas as pd
import io
import cgitb
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
cgitb.enable()

matplotlib.use('Agg')

import matplotlib.pyplot as plt
# print content-type





print("Content-type: text/html\n")

print('''<html>
    <head>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <div id="myTop" class="w3-container w3-top w3-theme w3-large">
    <span id="myIntro" class="w3-hide">GMMH Database</span></p>
    </div>  
<script>
// Change style of top container on scroll
window.onscroll = function() {myFunction()};
function myFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("myTop").classList.add("w3-card-4", "w3-animate-opacity");
    document.getElementById("myIntro").classList.add("w3-show-inline-block");
  } else {
    document.getElementById("myIntro").classList.remove("w3-show-inline-block");
    document.getElementById("myTop").classList.remove("w3-card-4", "w3-animate-opacity");
  }
}
</script>
    <header class="w3-container w3-theme" style="padding:64px 32px">
    <h1 class="w3-xxxlarge">Gut Microbiota - Mental Health Database</h1>
    </header>
        <meta charset="utf-8" /> 
        <!-- jQuery -->
        <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
        <!-- CSS -->
        <style>
            /* comments within a style block are written like this */
            /* asterisk below selects all elements, use it for styles that aren't inherited, like box-sizing */
            /* box-sizing: border-box allows setting sizes for element content, padding, and border */
            * { 
                box-sizing: border-box;
            }
            /* body selects the body element */
            /* styles set here are inherited into some subelements of the body, unless overridden */
            body {
              font: 20px Arial;
            }
            /* input elements inside a form do not inherit the body font */
            /* sets styles for input buttons */
            input {
              border: 1px solid transparent;
              background-color: #f1f1f1; /* slightly gray */
              padding: 10px;
              font-size: 20px;
            }
            /* overrides input styles above for the submit input button */
            input[type=submit] {
              background-color: DodgerBlue; 
              color: #fff; /* white; */
            }
            /* sets styles for a select element dropdown option */
            select {
              font-size: 16px;
              width: 200px;
            }
            /* sets styles for a table, table header cell (th), and a table data cell (td) */
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                padding: 15px;
            }
            /* sets width for the entire table */
            table {
                width: 400px;
            }
            /* sets text alignment for a table header cell */
            th {
                text-align: left;
            }
            /* sets text alignment for a table data cell */
            td {
                text-align: left;
            }
            /* overrides default background color for every other table row (tr) */
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
        
        
    </head>''')
print("<title>View a heatmap</title>")
print('''<style>
body {margin:30;padding:30}
</style>
''')
print("<body>")

print("<h1>Enter the info you wish to view</h1>")


print('''<form action="https://bioed.bu.edu/cgi-bin/students_20/jiliu/project.py" method="POST" >
	Rank:<select name="Rank">
    <option value="Species">Species</option>
    <option value="Genus">Genus</option>
    <option value="Family">Family</option>
    <option value="Order">Order</option>
    <option value="Class">Class</option>
    <option value="Phylum">Phylum</option>
    </select><br />
    Mouse Type::<select name="Mouse Type">
    <option value="Pure">Pure</option>
    <option value="Mix">Mix</option>
    </select><br />
    Disease Status::<select name="Disease Status">
    <option value="AD">Alzheimer's Disease</option>
    <option value="Wild Type">Wild Type</option>
    </select><br />
	<input type="submit" value="View HeatMap">
    
	</form>''')



   

form = cgi.FieldStorage()

#get uploaded data to cgi
print("Content-Type: text/html")

#for row in csv_reader:
    
####dataformat
######



print("</body></html>")
