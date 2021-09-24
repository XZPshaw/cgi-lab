#!/usr/bin/env python3
import cgi, cgitb

import os
from templates import login_page,secret_page,after_login_incorrect
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
'''
if (uname == username and pword == password):
	#print("Content-type:text/html\r\n\r\n")
	print("Set-Cookie:UserID = {};".format(username))
	print("Set-Cookie:Password = {};".format(password))
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
if 'HTTP_COOKIE' in os.environ:
   '''
   for cookie in os.environ['HTTP_COOKIE'].split(';'):
      key, value = cookie.split('=')
      if key == "UserID":
         user_id = value
      if key == 'Password':
         cookie_pw = value
   '''
   cookies = os.environ['HTTP_COOKIE'].split(';')
   user_id = str(cookies[0].split('=')[1])
   cookie_pw = str(cookies[1].split('=')[1])


if user_id == uname and cookie_pw == pword:
	print(secret_page(user_id,cookie_pw))
elif user_id != uname and cookie_pw != pword:
	print(login_page())
else:
	print(after_login_incorrect())

