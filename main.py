from flask import Flask
import io
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
  try:
    import matplotlib
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err

if __name__ == '__main__':
  app.run()
