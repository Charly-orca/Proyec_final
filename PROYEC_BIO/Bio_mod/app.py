from flask import Flask, render_template, request, redirect, url_for
from conector.conexion_bk import conexion

app= Flask(__name__)

@app.route('/')
def principal():
    return render_template ('index.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/servicios')
def Servicios():
    return render_template('servicios.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        correo = request.form['correo']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (Nombre_completo, correo, usuario, contrasena) VALUES (%s, %s, %s, %s)",
                    (nombre_completo, correo, usuario, contrasena))
        conexion.commit()
        cursor.close()
        return redirect(url_for('principal'))
    return render_template('registro.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        correo = request.form['correo']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET Nombre_completo=%s, correo=%s, usuario=%s, contrasena=%s WHERE Id=%s",
                (nombre_completo, correo, usuario, contrasena, id))
        conexion.commit()
        cursor.close()
        return redirect(url_for('principal'))
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE Id=%s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    return render_template('update.html', usuario=usuario)

if __name__== '__main__':
    app.run(debug=True)