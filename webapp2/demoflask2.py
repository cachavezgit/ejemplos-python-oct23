from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route('/')
def demo():
    return "Prueba de Flask 2!!!!!"