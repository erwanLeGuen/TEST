#!D:\Windows\EasyPHP17\eds-binaries\python\default\python.exe
'''
Created on 19 mai 2019

@author: Erwan
'''
import cgi

print 'Content-type: text/html'
print

print '<html><head><title>Mon super site</title></head><body>'
formulaire = cgi.FieldStorage()
if formulaire.getvalue('inputVal') != None:
    inputVal = formulaire.getvalue('inputVal')
    print 'valeur saisie : '+inputVal

print '</body></html>'