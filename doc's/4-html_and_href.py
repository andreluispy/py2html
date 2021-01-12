from py2html.main import *

page = web()
page.create()

# HTML Parameters
#   Code = html code to insert
page.html(code='<p>Hello World</p>')

# HREF Parameters
#   text = href text
#   link = href link
page.href(text='google', link='google.com')

page.compile()