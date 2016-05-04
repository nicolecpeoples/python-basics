from flask import Flask, render_template, redirect, request, session
import random # import the random module

app = Flask (__name__)
app.secret_key = "tadkg250atk"

@app.route('/', methods=['GET', 'POST'])
def index():
	session['user_guess'] = int(request.form['number'])
	session['random_number'] = random.randrange(0,101)
	
	if session['number'] == session['user_guess']:
		session['answer'] = "Amaaaaaazing"
	elif session['number'] > session['user_guess']:
		session['answer'] = "Tooo Low"
	else:
		session['answer'] = "Toooo High!"
	return render_template('index.html', user_guess = session['user_guess'], answer = session['answer'] )

@app.route('/submit', methods=['POST'])
def submit_guess():
	session_clear()
	get_number()

	return redirect('/' )

app.run(debug=True)