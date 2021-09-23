#!/usr/bin/env python3

import os,json
from templates import login_page
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World</p>")

'''
#Q1
print("Q1:")
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print("json_object:")
print(json_object)


#Q2
for param in os.environ.keys():
	if(param == "QUERY_STRING"):
		#print(f"<em>{param}</em> = {os.environ[parm]}</li>")
		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
'''	
'''
#Q3
for param in os.environ.keys():
	if(param == "HTTP_USER_AGENT":
		print("<b>%20s</b>: %s<br>"% (param, os.environ[param]))
		
'''


#Q4
print(login_page())
