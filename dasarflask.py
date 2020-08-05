from flask import Flask
from flask import render_template
app = Flask(__name__)

#STATIS
@app.route('/')
def hello():
    return render_template('index.html')

#DINAMIS
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
