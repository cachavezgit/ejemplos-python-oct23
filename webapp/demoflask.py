from mysql.connector import connect, Error
from flask import Flask, render_template, abort, request, redirect, url_for

print(__name__)
app = Flask(__name__)

def get_db_connection():
    conexion_mysql = connect(
        host="24.199.90.148",
        user="wilson",
        password="password",
        database="blog"
    )
    return conexion_mysql

@app.route('/')
def index():
    #return "Prueba de Flask"
    conexion_mysql = get_db_connection()
    
    cursor = conexion_mysql.cursor()
    query = 'Select * from posts'
    cursor.execute(query)
    posts = cursor.fetchall()
    conexion_mysql.close()

    return render_template("index.html", posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    conexion_mysql = get_db_connection()
    cursor = conexion_mysql.cursor()
    cursor.execute('Select * from posts where id = %s',(post_id,))
    post = cursor.fetchone()
    conexion_mysql.close()

    if post is None:
        abort(404)

    return render_template("post.html", post=post)

@app.route("/create", methods=('GET','POST'))
def create():
    if request.method == 'POST':
        titulo = request.form['title']
        contenido = request.form['content']
        conexion_mysql = get_db_connection()
        cursor = conexion_mysql.cursor()
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",(titulo,contenido))
        conexion_mysql.commit()
        conexion_mysql.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/about')
def about():
    #return "Prueba de Flask"
    return render_template("about.html")