from flask import Flask
from matplotlib import pyplot
import io
import base64

app = Flask(__name__)


@app.route('/')
def build_plot():
    img = io.BytesIO()

    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    a=plt.plot(x,y)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    return a


if __name__ == '__main__':
    app.run()
