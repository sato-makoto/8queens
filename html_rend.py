include eightqueen_func as eq

def html_header():
 print '' 

def h1_out(eq.width):
  print '<h1>{} Queens</h1>'.format(eq.width)

def first_line(eq.width):
  print '<table>'

def css_class_name():
 classtaple = ('none', 'left', 'white', 'gray')
 return classtaple

def table_first_line(eq.width):
  print '<tr>\n  <td class="none"></td>'
  for x in range(eq.width):
    print '<td class="none">{}</td>'.format(x)
  print '</tr>'

def a_line_out(queens_list, eq.width):
  wgtaple = classtaple[2:]
  for x in range(eq.width):
    for y in queens_list:
      if x = y[1]:

def html_footer():
 print '' 


