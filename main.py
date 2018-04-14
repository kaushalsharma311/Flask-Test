from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
<html>
    <head>
        <title>Dashboard</title>
        <script>
                function resizeIframe(obj) {
                                              obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
                }
        </script>
    </head>
    <body>
          <iframe height=600 width=1200 src="https://app.powerbi.com/groups/me/reports/abeb657d-d64e-4516-b0ac-686e0fe6cfe9/ReportSection" frameborder="0" allowFullScreen="true"></iframe>        
        <form method="POST">
            <input class="btn" type="submit" value="submit">
        </form>
    </body>
</html>'''

if __name__ == '__main__':
  app.run()
