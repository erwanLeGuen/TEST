#!D:\Windows\EasyPHP17\eds-binaries\python\default\python.exe
'''
Created on 19 mai 2019

@author: Erwan
'''
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')