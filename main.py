from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
<html>
    <head>
        <title>Dashboard</title>
    </head>
    <body>
        <iframe width="800" height="600" src="https://app.powerbi.com/groups/me/reports/76c60a26-95fc-4126-9d86-536e7fc7bf9e/ReportSection" frameborder="0" allowFullScreen="true"></iframe>
        <form method="POST">
            <input class="btn" type="submit" value="submit">
        </form>
    </body>
</html>'''

if __name__ == '__main__':
  app.run()
