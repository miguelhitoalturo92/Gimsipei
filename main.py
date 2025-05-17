from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')


# Conexión

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_bd'
conexion = MySQL(app)

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
        print(username)
        print(password)
        return render_template('login.html')
    else:    
        return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True, port=8000)