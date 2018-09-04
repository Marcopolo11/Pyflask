import flask
try:
  import io
except Exception as e:
  err=("type error: " + str(e))
  return err
try:
  import base64
except Exception as e:
  err=("type error: " + str(e))
  return err
try:
  import matplotlib
except Exception as e:
  err=("type error: " + str(e))
  return err


app = flask.Flask(__name__)
app.debug = True

  
@app.route('/')
def build_plot():
    try:
      return 'its fine'
    except Exception as e:
      err=("type error: " + str(e) + a)
      return err
  
if __name__ == '__main__':
    app.run()
