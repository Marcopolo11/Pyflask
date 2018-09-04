from flask import Flask
import matplotlib.pyplot
import io
import base64

app = Flask(__name__)
@app.route('/')
def hello_world():
  print("Testing Print")
  return 'Hello, World!'
if __name__ == '__main__':
    app.run()
