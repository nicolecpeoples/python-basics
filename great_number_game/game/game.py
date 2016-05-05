from flask import Flask, render_template, redirect, request, session
import random # import the random module

app = Flask (__name__)
app.secret_key = "tadkg250atk"

@app.route('/', methods=['GET', 'POST'])
def index():


	return render_template('index.html')


@app.route('/submit', methods=['POST'])	
def submit_form():

	if 'random_number' not in session:
		session['random_number'] = random.randint(0,101)
	if 'msg' not in session:
		session['msg'] = ''
	if request.method == 'POST':
		if session['random_number'] == int(request.form['number']):
			session.pop('number')
			session['msg'] = "You are hecka winning!"
		elif session['random_number'] > int(request.form['number']):
			session['msg']= "A little low"
		else:
			session['msg'] = "A little high"

		
	return redirect('/')

app.run(debug=True)