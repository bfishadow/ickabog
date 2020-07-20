#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

try:
    strFilename = sys.argv[1]
except:
    print ("Missing filename.")
    print ("Usage: python3 _parse.py <input filename> > <output filename>")
    sys.exit(0)

def getBetween(str, str1, str2):
    strOutput = str[str.find(str1)+len(str1):str.find(str2)]
    return strOutput

with open(strFilename, 'rt') as objFile:
    strHTML = objFile.read()

strContentHTML = getBetween(strHTML, '<div class="col">', '<div class="row my-75">')
strContentHTML = strContentHTML.replace('<h1', '<h2')
strContentHTML = strContentHTML.replace('</h1>', '</h2>')
#strContentHTML = strContentHTML.replace('<h3>', '<p align="center"><img alt="Crown" src="../Images/Crown.png"/></p><p>')
strContentHTML = strContentHTML.replace('<h3>', '<p>')
strContentHTML = strContentHTML.replace('</h3>', '</p>')

print('<?xml version="1.0" encoding="utf-8"?>')
print('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"')
print('  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
print('')
print('<html xmlns="http://www.w3.org/1999/xhtml">')
print('<head>')
print('  <title></title>')
print('</head>')
print('')
print('<body>')
print ("<div><div>", strContentHTML)
print('</body>')
print('</html>')
