from flask import Flask
import pdfkit
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
<html>
    <head>
        <title>Dashboard</title>
        <script src="js/jspdf.js"></script>
        <script src="js/jquery-2.1.3.js"></script>
        <script src="js/pdfFromHTML.js"></script>
    </head>
    <body>
        <div id="HTMLtoPDF">
<h3> hbafxjfn </h3>
</div>
        <button onclick="HTMLtoPDF()">Download</button>
    </body>
</html>'''

if __name__ == '__main__':
  app.run()
