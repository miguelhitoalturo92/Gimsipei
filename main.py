from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')



# Manejo de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404



# Rutas
@app.route('/')
def index():
    return redirect('/login', 302)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_form')
def login_form():
    
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)