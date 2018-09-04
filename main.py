import flask
import io
import base64

app = flask.Flask(__name__)
app.debug = True


#@app.route('/')
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
  
@app.route('/')
def build_plot():
    try:
      img = io.BytesIO()

      y = [1,2,3,4,5]
      x = [0,2,1,3,4]
      plt.plot(x,y)
      plt.savefig(img, format='png')
      img.seek(0)

      plot_url = base64.b64encode(img.getvalue()).decode()

      return '<img src="data:image/png;base64,{}">'.format(plot_url)
    except Exception as e:
      err=("type error: " + str(e) + a)
      return err
  
if __name__ == '__main__':
    app.run()
