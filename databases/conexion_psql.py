import psycopg2

conexion_psql = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="mysecretpassword",
            port="5432",
            database="infodb"
        )

cursor = conexion_psql.cursor()

cursor.execute("select * from data")

resultado = cursor.fetchall()

for r in resultado:
    print(r)
