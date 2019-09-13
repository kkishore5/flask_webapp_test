
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/analysis')
def data_analysis():
    x = pd.DataFrame(np.random.randn(5,6), columns = list('ABCDEF'))
    return render_template("data_analysis.html", data = x.to_html())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
