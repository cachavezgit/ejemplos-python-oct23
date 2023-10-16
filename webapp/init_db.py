from mysql.connector import connect, Error

conexion_mysql = None

try:
    conexion_mysql = connect(
        host="24.199.90.148",
        user="wilson",
        password="password",
        database="blog"
    )
except Error as e:
    print(e)

cursor = conexion_mysql.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",("Primer Post", "Contenido del primer post"))
cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",("Segundo Post", "Contenido del segundo post"))

conexion_mysql.commit()
conexion_mysql.close()

