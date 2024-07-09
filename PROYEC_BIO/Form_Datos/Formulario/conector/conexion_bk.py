import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login_register_db"  # nombre de la base de datos
)

# Función para verificar la conexión a la base de datos
def verificar_conexion():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT Nombre_completo FROM usuarios")
        rows = cursor.fetchall()
        cursor.close()
        return True  
    except Exception as e:
        print("Error al verificar la conexión a la base de datos:", e)
        return False

#if verificar_conexion():
    print("La conexión a la base de datos se estableció correctamente.")
#else:
    print("Error: No se pudo establecer conexión.")
