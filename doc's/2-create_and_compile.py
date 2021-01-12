from py2html.main import *

page = web()

# Create Parameters:
#   title = page title
#   lang = page lang
#   bg = page background color
#   fg = Text Color of headers
page.create(title='Page Title', lang='en', bg='black', fg='white')

page.header('My Site')
page.label('Hello World')

# Compile Parameters
#   name = html file name
page.compile(name='my-site.html')