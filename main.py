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
  #a=matplotlib.pyplot.plot(x,y)
  #return a
  matplotlib.pyplot.plot(x,y)
  matplotlib.pyplot.savefig(img, format='png')
  img.seek(0)
  plot_url = base64.b64encode(img.getvalue()).decode()
  return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
  app.debug = True
  app.run()
