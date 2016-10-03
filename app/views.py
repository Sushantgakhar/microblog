from flask import render_template, redirect, flash
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index/')

def index():
    user = {'nickname' : 'Sushant'}
    posts = [
	{
		'author' : {'nickname' : 'Susan'},
		'body' : 'Beautiful day in Portland!'
	},
	{
		'author' : {'nickname' : 'John'},
		'body' : 'The avengers movie was so cool'
	}
 	]
    return render_template('index.html', user=user, title = 'Home', posts = posts, providers=app.config['OPENID_PROVIDERS'])
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index') 
    return render_template('login.html', form=form, title='Sign In', providers=app.config['OPENID_PROVIDERS'])

