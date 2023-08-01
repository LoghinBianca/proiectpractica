import database_functions
from flask import request, make_response
from flask import Flask, render_template, redirect
app = Flask(__name__)

login_clients={}



@app.route('/')
def hello_world():
    email = request.cookies.get('email')
    print(email)
    if email==None:
        return render_template('index.html')
    if email in login_clients.keys():
        if login_clients[email]==True:
            return render_template('index.html', email=email)


@app.route('/index')
def index():
    email = request.cookies.get('email')
    print(email)
    if email == None:
        return render_template('index.html')
    if email in login_clients.keys():
        if login_clients[email] == True:
            return render_template('index.html', email=email)

@app.route('/about')
def about():
    email = request.cookies.get('email')
    print(email)
    if email == None:
        return render_template('about.html')
    if email in login_clients.keys():
        if login_clients[email] == True:
            return render_template('about.html', email=email)

@app.route('/contact')
def contact():
    email = request.cookies.get('email')
    print(email)
    if email == None:
        return render_template('contact.html')
    if email in login_clients.keys():
        if login_clients[email] == True:
            return render_template('contact.html', email=email)

@app.route('/animals')
def animals():
    conn = database_functions.connection()
    all_animals=database_functions.get_all_animals(conn)
    print(all_animals)
    email = request.cookies.get('email')
    print(email)
    if email == None:
        return render_template('animals.html', len=len(all_animals), all_animals=all_animals)
    if email in login_clients.keys():
        if login_clients[email] == True:
            return render_template('animals.html', len=len(all_animals), all_animals=all_animals, email=email)


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
        login_clients[email]=True
        resp=make_response("logged")
        resp.set_cookie("email", email)
        return resp

@app.route('/buy', methods = ['POST'])
def buy():
    identificator=request.form.get("buy")
    conn = database_functions.connection()
    database_functions.delete_by_id(conn,identificator)
    return redirect('/animals')





if __name__ == '__main__':
    #database_functions.create_table()
    app.run(debug=True, port=8000)





