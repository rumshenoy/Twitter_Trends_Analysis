#!/usr/bin/python
print "Content-type: text/html"

import cgi, cgitb
import os

form = cgi.FieldStorage()

if form.getvalue('location'):
   location = form.getvalue('location')
else:
   location = "Not entered"

if form.getvalue('file'):
   filename = form.getvalue('file')
else:
   filename = "Not entered"


if form.getvalue('checkboxname'):
   ask_flag = True
else:
   ask_flag = False

if form.getvalue('customTrend'):
   customTrend = form.getvalue('customTrend')
else:
   customTrend = "Not Entered"

if form.getvalue('freq'):
   freq = form.getvalue('freq')
else:
   freq = "Not Entered"

if ask_flag:
   os.system("python py/selectRandSent.py "+customTrend+" "+freq+" "+filename)
   os.system("python py/nltk_find_trends.py txt/tune.txt"+" "+location)

else:
  os.system("python py/nltk_find_trends.py "+filename+" "+location)


print "Content-type:text/html\r\n\r\n"
print """<meta http-equiv="refresh" content="2;url=/country.html">"""


print "<html>"
print "<head>"
print "<title>Dropdown Box - Sixth CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Selected location is %s</h2>" % location
print "<h2> Selected filename is %s</h2>" % filename
print "<h2> CheckBox value is : %s</h2>" % ask_flag
print "<h2> Trend word is : %s</h2>" % customTrend
print "<h2> Trend freq is : %s</h2>" % freq
print "</body>"
print "</html>"

