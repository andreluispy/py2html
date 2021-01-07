class web():
    '''
    Class to create web page

    functions:

    WebPage:
        create
        compile
    
    Layout:
        html
        label
        href
    '''
    def __init__(self):
        '''
        Defalt param(not used for users)
        '''
        self.content = []
    
    def create(self, title='py2html site', lang='en'):
        '''
        creat: create webpage

        parameters:
            title = page title
            lang = page language
        '''
        self.title = title
        self.lang = lang
    
    #Layout Creator
    def html(self, code):
        '''
        Insert html code

        parameters:
            code = html code
        '''
        self.content.append(code)
    def label(self, text='label', css=''):
        '''
        Insert label

        parameters:
            text = label text
            css = html css
        '''
        self.content.append('<p style="'+css+'">'+text+'</p>')
    def href(self, text, link, css=''):
        '''

        Create href(link)

        parameters:
            text = href text
            link = href link
            css = html css
        '''
        self.content.append('<a href='+link+' style="'+css+'">'+text+'</a>')

    def compile(self, name='page.html'):
        '''
        Generate html code

        parameters:
            name = html file name, ex: compile(name='index.html')
        '''
        html = open(name, 'w')
        html.write('<DOCTYPE html>\n')
        html.write('<html>\n')

        html.write('    <head lang="'+self.lang+'">\n')
        html.write('        <title>'+self.title+'</title>\n')
        html.write('        <meta charset="UTF-8">\n')
        html.write('        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        html.write('    </head>\n')

        html.write('    <body>\n')
        for c in self.content:
            html.write('        '+c+'\n')
        html.write('    </body>\n')

        html.write('</html>\n')
        html.close()