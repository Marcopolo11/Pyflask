from flask import Flask
import flask
import io
import base64

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
  print("Testing Print")
  #return 'Hello1, World!'
  return flask.redirect('/graphcall')


@app.route('/graphcall')
def graphcall():
  return flask.render_template(other='other', red='redirected!')
if __name__ == '__main__':
    app.run()
