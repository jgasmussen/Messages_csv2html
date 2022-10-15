#!/usr/bin/env python3

######################################################
#            Messages.csv to HTML Thread             #
#                 BETA Version 0.1                   #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#         EGA Technology Specialists, LLC.           #
#                   GNU GPL v 3.0                    #
######################################################

import sys
import csv

HTML_Template = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0 auto;
  max-width: 800px;
  padding: 0 20px;
}

.container {
  border: 2px solid #bbbbbb;
  background-color: #ffffff;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
}

.darker {
  border-color: #bbbbbb;
  background-color: #0066ff;
  text-align: right
}

.container::after {
  content: "";
  clear: both;
  display: table;
}

</style>
</head>
<body>

<h2>Text Messages</h2>\n"""

HTML_Template_End_of_File  = """</body>
</html>\n"""

with open(sys.argv[2], 'a') as out:
  out.write(HTML_Template)

with open(sys.argv[1], 'r') as messages:
  csv_input = csv.DictReader(messages)
  for row in csv_input:
    Direction = row['Direction']
    Sender = row['Sender']
    Recipient = row['Recipient']
    TimeUTC = row['Time (UTC)']
    Time_local = row['Time (local)']
    Message = row["Message"]

    items = [Direction, Sender, Message, Time_local]
    if items[0] == "Incoming":
      with open(sys.argv[2], 'a') as out:
        out.write('<div class="container">') 
        out.write('<p>')
        out.write(items[1]+'</p>')
        out.write('<p>')
        out.write(items[2]+'</p>')
        out.write('<p>')
        out.write(items[3]+'</p>')
        out.write('</div>')
  
    elif items[0] == "Outgoing":
      with open(sys.argv[2], 'a') as out:
        out.write('<div class="container darker">') 
        out.write('<p>')
        out.write(items[1]+'</p>')
        out.write('<p>')
        out.write(items[2]+'</p>')
        out.write('<p>')
        out.write(items[3]+'</p>')
        out.write('</div>')

with open(sys.argv[2], 'a') as out:
	out.write(HTML_Template_End_of_File)