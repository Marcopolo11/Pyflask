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
  matplotlib.pyplot.plot(x,y)
  #matplotlib.pyplot.savefig(img, format='png')
  matplotlib.pyplot.savefig('/static/images/new_plot.png')
  #img.seek(0)
  #plot_url = base64.b64encode(img.getvalue()).decode()
  #a=matplotlib.pyplot.plot(x,y)
  #return a
  try:
  return render_template('testplot.html', name = 'new_plot', url ='/static/images/new_plot.png')
  except Exception as e:
    err=("type error: " + str(e) + a)
    return err

if __name__ == '__main__':
  app.debug = True
  app.run()
