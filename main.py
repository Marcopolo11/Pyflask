from flask import Flask
import io
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
  try:
    import matplotlib
    #return 'fine'
      
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err
  
  img = io.BytesIO()
  y = [1,3]
  x = [0,2]
  a=matplotlib.pyplot.plot(x,y)
  return a

if __name__ == '__main__':
  app.debug = True
  app.run()
