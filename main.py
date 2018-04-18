from flask import Flask
import pdfkit
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
<html>
    <head>
        <title>Dashboard</title>
    </head>
    <body>
        <div id="HTMLtoPDF">
          <iframe height=600 width=1200 src="https://app.powerbi.com/view?r=eyJrIjoiODM2YTE1ZGYtZmMzYS00YWMyLWFkNjYtNTliOTNkYjhkODRjIiwidCI6ImRhNjdlZjFiLWNhNTktNGRiMi05YThjLWFhOGQ5NDYxN2ExNiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>        
</div>
        <button >Download</button>
    </body>
</html>'''

if __name__ == '__main__':
  app.run()
