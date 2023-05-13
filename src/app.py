from flask import Flask, render_template, redirect, url_for, request
import os
import database as db

##direccion absoluta del directorio app
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unir carpetas a directorio app
template_dir = os.path.join(template_dir, 'src', 'templates')
#instancia de directorio para lanzamiento en servidor
app = Flask(__name__, template_folder=template_dir)



#ruta app
@app.route('/')
def home():
    try:
        cursor = db.database.cursor()
        cursor.execute("select * from usuarios")
        resultado = cursor.fetchall()
        #datos a diccionarios
        insertObject = []
        columName = [column[0] for column in cursor.description]
        for dato in resultado:
            insertObject.append(dict(zip(columName, dato)))
        cursor.close()
        return render_template('index.html', data=insertObject)
    except Exception as e:
        return str(e)

#guardar usuario
@app.route('/user', methods=['POST'])
def addUser():
    try:
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        contrasenia = request.form['pass']

        if usuario and nombre and contrasenia:
            cursor = db.database.cursor()
            sql = "INSERT INTO usuarios (usuario, nombre, contrasenia) values (%s,%s,%s)"
            data= (usuario, nombre, contrasenia)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('home'))
    except Exception as e:
        return str(e)

@app.route('/delete/<string:id>')
def delete(id):
    try:
        cursor = db.database.cursor()
        sql = "DELETE FROM usuarios WHERE id=%s"
        data = (id,)
        cursor.execute(sql, data)
        db.database.commit()
        return redirect(url_for('home'))
    except Exception as e:
        return str(e)
   
@app.route('/edit/<string:id>' ,methods=['POST'])
def edit(id):
    try:
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        contrasenia = request.form['pass']

        if usuario and nombre and contrasenia:
            cursor = db.database.cursor()
            sql = "UPDATE usuarios SET usuario = %s, nombre=%s, contrasenia=%s WHERE id=%s"
            data= (usuario, nombre, contrasenia, id)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('home'))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True,port=40000)
    