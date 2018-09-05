from flask import Flask , render_template
import io
import base64
import StringIO

app = Flask(__name__)



@devices_blueprint.route('/devices/test/')
def test():
   try:
      import matplotlib.pyplot as plt
      #return 'fine pyplot'
   except Exception as e:
      err=("type error: " + str(e) + a)
      return err
   img = StringIO.StringIO()
   y = [1,2,3,4,5]
   x = [0,2,1,3,4]
   plt.plot(x,y)
   plt.savefig(img, format='png')
   img.seek(0)
   plot_url = base64.b64encode(img.getvalue())
   return render_template('test.html', plot_url=plot_url)

if __name__ == '__main__':
  app.debug = True
  app.run()
