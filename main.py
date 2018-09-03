from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  print("Testing Print")
  return 'Hello1, World!'


if __name__ == '__main__':
  app.run()
