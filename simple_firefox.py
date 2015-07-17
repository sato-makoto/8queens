#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eightqueen_func as eq
import html_rend as html
from selenium import webdriver
from time import sleep
import os

x, y, pairs, myset = eq.allclear()

inputdata='data.txt'

browser = webdriver.Firefox()
working_dir = os.getcwd() + '/'
myqueen_html = 'foo.html'

def make_matrix(dataline):
  mylist = eq.main(eq.width)
  output = open(myqueen_html, 'w')
  head = html.html_header()
  for x in head:
    output.write(x[:-1])
  output.write(html.h1_out(eq.width))
  output.write('\n')
  output.write(html.p_out())
  output.write('\n')
  output.write(html.first_line())
  output.write('\n')
  output.write(html.table_first_line(eq.width))
  output.write('\n')
  output.write(html.lines_out(mylist, eq.width))
  foot = html.html_footer()
  for x in foot:
    output.write(x[:-1])
  output.close()

input = open(inputdata, 'r')

for x in inputrite(range(10):
  make_matrix(dline)
  browser.get('file://' +  working_dir + myqueen_html)
  sleep (3)
browser.close()
