
from flask import Flask, render_template

app = Flask(__name__)

# '/' : This route will render the 'index.html' file and display the homepage.
@app.route('/')
def home():
    return render_template('index.html')

# '/tutorial1' : This route will render the 'tutorial1.html' file and display the basic newspaper layout tutorial.
@app.route('/tutorial1')
def tutorial1():
    return render_template('tutorial1.html')

# '/tutorial2' : This route will render the 'tutorial2.html' file and display the advanced newspaper creation tutorial.
@app.route('/tutorial2')
def tutorial2():
    return render_template('tutorial2.html')

# '/tutorial3' : This route will render the 'tutorial3.html' file and display the newspaper customization tutorial.
@app.route('/tutorial3')
def tutorial3():
    return render_template('tutorial3.html')

# '/contact' : This route will render the 'contact.html' file and display the contact information.
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
