from flask import Flask , render_template
import io
import base64


app = Flask(__name__)

@app.route('/')
def pan():
   try:
      import pandasas as pd
   except Exception as e:
      err=("type error: " + str(e) + a)
      return err
   df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
   ax = df.plot.bar(x='lab', y='val', rot=0)
   return df

   try:
      return 'b'
   except Exception as e:
      err=("type error: " + str(e) + a)
      return err
   return str(y)
if __name__ == '__main__':
  app.debug = True
  app.run()
