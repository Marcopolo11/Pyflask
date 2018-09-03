from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  print("Testing Print")
  return 'Hello, World!'

@app.route('/')
def Test():
    return 'test done'



if __name__ == '__main__':
  app.run()
