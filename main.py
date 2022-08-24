from flask import Flask, render_template, request,g , session, redirect, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

# Defining the home page of our site
@app.route("/", methods=['GET', 'POST'])  # this sets the route to this page
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'deepak123':
            session['user'] = request.form['username']
            return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    if g.user:
        return render_template('dashboard.html', user = session['user'])
    
    return redirect(url_for('index'))


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('index.html')
    
@app.before_request
def before_request():
    g.user = None
    
    if 'user' in session:
        g.user = session['user']


if __name__=="__main__":
    app.run(host ='0.0.0.0', port=5000 ,debug=True )