import database_functions
from flask import request
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/animals')
def animals():
    conn = database_functions.connection()
    all_animals=database_functions.get_all_animals(conn)
    print(all_animals)
    return render_template('animals.html', len=len(all_animals), all_animals=all_animals)

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_in_validate', methods = ['POST'])
def sign_in_validate():
    conn = database_functions.connection()
    email=request.form.get('email')
    psw=request.form.get('psw')
    psw_repeat=request.form.get('psw-repeat')
    if database_functions.verify_sign_in(conn, email)==True:
        database_functions.insert_in_clients(conn, email, psw)
        return "Contul a fost creat!"
    else:
        return "Exista deja un utilizator cu acest email!"


@app.route('/login')
def log_in():
    return render_template('login.html')

@app.route('/log_in_validate', methods = ['POST'])
def log_in_validate():
    conn = database_functions.connection()
    email=request.form.get('email')
    psw=request.form.get('psw')
    database_functions.verify_log_in(conn, email, psw)
    if database_functions.verify_log_in(conn, email, psw)==True:
        pass





if __name__ == '__main__':
    #database_functions.create_table()
    app.run(debug=True, port=8000)





