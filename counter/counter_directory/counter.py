from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "ThisIsMySecretKey"

def countSession():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1

	return session['counter']

@app.route('/')
def index():
	countSession()	
	return render_template('counter.html')

@app.route('/visits', methods = ['POST'])
def get_user_visits():

	return redirect('/')

@app.route('/clear')
def clearSession():
	session.clear()
	session['counter'] = 0
	return redirect('/')

@app.route('/addtwo')
def add_two_sessions():
	session['counter'] += 2
	return redirect('/')

app.run(debug=True)