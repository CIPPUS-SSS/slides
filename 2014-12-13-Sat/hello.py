from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route("/user/<username>")
def show_user_name(username):
    return 'User %s' % username;

if __name__=="__main__":
    app.run()
