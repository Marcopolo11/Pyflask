
import flask
import io
import base64

app = flask.Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
  print("Testing Print")
  return flask.render_template('Hello1', '2World!')

if __name__ == '__main__':
    app.run()
