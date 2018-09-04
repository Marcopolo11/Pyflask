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
      img = io.BytesIO()

      y = [1,2,3,4,5]
      x = [0,2,1,3,4]
      matplotlib.pyplot.plot(x,y)
      matplotlib.pyplot.savefig(img, format='png')
      img.seek(0)

      plot_url = base64.b64encode(img.getvalue()).decode()

      return '<img src="data:image/png;base64,{}">'.format(plot_url)
    except Exception as e:
      err=("type error: " + str(e) + a)
      return err
  
if __name__ == '__main__':
    app.run()
