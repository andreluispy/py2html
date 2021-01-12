from py2html.main import * # Import py2html

page = web()
page.create()

page.label('Hello World')

page.compile()