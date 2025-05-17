from flask import Flask, render_template, redirect, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')


# Conexión

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_jwt'
conexion = MySQL(app)
if conexion:
    print("Conectado")
else:
    print("No se encontro la bd")

# Manejo de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404



# Rutas
@app.route('/')
def index():
    return redirect('/login', 302)



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username)
        # print(password)
        try:
            
            cursor = conexion.connection.cursor()
            
            sql=("SELECT * FROM usuarios where correo= %s and password = %s",(username,password))
            cursor.execute(sql)
            data = cursor.fetchone()
            if data:
               return render_template('admin/dashboard.html')
            data.close() 
        except Exception as e:
            return jsonify({"message":"error"})       
    else:    
        return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True, port=8000)