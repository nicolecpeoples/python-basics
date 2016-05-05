from flask import Flask, redirect, render_template, session, request, flash
app = Flask (__name__)
app.secret_key = "formValidation"

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

	#if the name field in the post data is empty
	#display a validation error
	if len(request.form['full_name']) < 1:
		flash("name cannot be empty!") #just pass a string to the flash function
	#else
	else:
	#display success message
		flash("success! Your name is {}".format(request.form['full_name']))
	return redirect('/')

app.run(debug=True)