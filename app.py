import database_functions
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
    return render_template('animals.html')
@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

if __name__ == '__main__':
    database_functions.create_table()
    app.run(debug=True, port=8000)





