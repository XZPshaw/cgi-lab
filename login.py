#!/usr/bin/env python3
import cgi, cgitb

import os
from templates import login_page,secret_page
from secret import username,password


#print(login_page())
form = cgi.FieldStorage()

#Q4 report the value from posted data
uname = form.getvalue("username")
pword = form.getvalue("password")

'''
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>report values of the POSTed data</title>")
print("</head>")
print("<body>")
print("<b>The input username:%s</b>" % (uname))
print("<b>The input password:%s</b>" % (pword))
print("</body>")
print("</html>")
'''


#Q5
if (uname == username and pword == password):
	#print("Content-type:text/html\r\n\r\n")
	print("Set-Cookie:UserID = {};\r\n".format(username))
	print("Set-Cookie:Password = {};\r\n".format(password))
	#print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
	#print("Set-Cookie:Path = /perl;\r\n")
	print("Content-type:text/html\r\n\r\n")
	print('<html>')
	print('<head>')
	print('<title>SET COOCKIE</title>')
	print('</head>')
	print('<body>')
	print('<b>COOCKIE IS SET!</b>')
	print('</body>')
	print('</html>')

'''
#Q6
user_id = None
cookie_pw = None
if os.environ.has_key('HTTP_COOKIE'):
   for cookie in map(strip, split(os.environ['HTTP_COOKIE'], ';')):
      (key, value ) = split(cookie, '=');
      if key == "UserID":
         user_id = value

      if key == "Password":
         cookie_pw = value
         
if user_id == uname and cookie_pw == pword:
	print(templates.secret_page(user_id,cookie_pw))

'''
	
