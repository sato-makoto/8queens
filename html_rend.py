import eightqueen_func as eq
# -*- coding: utf-8 -*-


classtaple = ('none', 'left', 'white', 'gray')


def html_header():
 header_file = 'html_header'
 h = open(header_file)
 return h

def html_footer():
 footer_file = 'html_footer'
 f = open(footer_file)
 return f

def h1_out(width):
 return '<h1>{} Queens</h1>'.format(eq.width)


def first_line():
  return '<table>'

def table_first_line(width):
  print '<tr>\n  <td class="none"></td>'
  for x in range(width):
    print '  <td class="none">{}</td>'.format(x)
  print '</tr>'

def lines_out(queens_list,width):
  wglist = classtaple[2:]
  q = ''
  for x in range(width):
    begin_color = x%2
    print '<tr>\n <td class="left">{}</td>'.format(x)
    for y in queens_list:
      if y[0] == x:
         q = '♕'
      else:
         q = ''
      print '  <td class="{}">{}</td>'.format(wglist[begin_color], q)
      begin_color = (begin_color + 1) % 2
    print '</tr>'
