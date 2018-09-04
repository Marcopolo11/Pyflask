import flask
import io
import base64

app = flask.Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
  print("Testing Print")
  a='Hello1'
  b='2World!'
  try:
    import matplotlib
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err
  
  try:
    return b
  except Exception as e:
    err=("type error: " + str(e))
    return err
  

if __name__ == '__main__':
    app.run()
