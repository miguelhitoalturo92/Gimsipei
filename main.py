from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__, template_folder='src/templates/', static_folder='src/static/')


# Conexión

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_jwt'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



# Manejo de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404



# Rutas
@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
     return render_template('auth/login.html')
 
 
@app.route('/user', methods=['GET','POST'])
def user():
    return render_template('auth/user.html')




if __name__ == '__main__':
    app.secret_key="leonardo"
    app.run(debug=False)