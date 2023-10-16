from flask import Flask, render_template

print(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    #return "Prueba de Flask"
    return render_template("index.html")

@app.route('/about')
def about():
    #return "Prueba de Flask"
    return render_template("about.html")