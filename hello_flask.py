from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/hello')
def hello2():
  return '<h1>Hello world from Flask!</h1> <br> <p>Genevieve M. : afaik</p>'

@app.route('/Francisco')
def hello3():
  return render_template('index.html')

