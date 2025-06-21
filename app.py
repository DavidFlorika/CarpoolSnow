# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/mycarpool')
def my_carpool():
    return render_template('my_carpool.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)