from flask import Flask
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def hello_world():
  print("Testing Print")
  return 'Hello1, World!'

@app.route('/')
def build_plot():

    img = io.BytesIO()

    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    a=plt.plot(x,y)
    return a
@app.route('/')
def Test():
    return 'test done'



if __name__ == '__main__':
  app.run()
