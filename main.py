from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <iframe width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiODM2YTE1ZGYtZmMzYS00YWMyLWFkNjYtNTliOTNkYjhkODRjIiwidCI6ImRhNjdlZjFiLWNhNTktNGRiMi05YThjLWFhOGQ5NDYxN2ExNiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
    </body>
</html>'''

if __name__ == '__main__':
  app.run()
