from flask import Flask, redirect, render_template, session, request
import random
import time
import datetime

app = Flask(__name__)
app.secret_key = "trakd659dk"

#write root route/index
@app.route('/')
def index():
	#session["gold"] = 0

	if 'gold' not in session:
		session['gold'] = 0

	if 'myActionsList' not in session:
		session['myActionsList'] = []

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	ts = time.time()
	current_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	#add random amount of money
	#specify random range
	
	
	if request.form['get_gold'] == "farm":
		this_gold = random.randint(10, 20)
		session["gold"] += this_gold
		session['myActionsList'].insert(0,  "Earned "  + str(this_gold)+ " golds from the farm! " + str(current_time))
		
	elif request.form['get_gold'] == "cave":
		this_gold  = random.randint(5, 10)
		session["gold"] += this_gold
		session['myActionsList'].insert(0,  "Earned "  + str(this_gold)+ " golds from the cave! " + str(current_time))
		
		
	elif request.form['get_gold'] == "house":
		this_gold =random.randint(2, 5)
		session["gold"] += this_gold
		session['myActionsList'].insert(0,  "Earned "  + str(this_gold)+ " golds from the house! " + str(current_time))
		
	elif request.form['get_gold'] == "casino":
		this_gold =random.randint(-50, 50)
		session["gold"] += this_gold
		if this_gold <0:

			session['myActionsList'].insert(0,  "entered a Casino and lost  "  + str(this_gold)+ " golds ... Ouch." + str(current_time))
			
		else:
			session['myActionsList'].insert(0,  "Earned "  + str(this_gold)+ " golds from the casino! " + str(current_time))


		print(session['myActionsList'])
	print(this_gold)
	return redirect('/')


@app.route('/clear')
def clearSession():
	session["gold"] = 0
	session['myActionsList'] = []
	return redirect('/')
app.run(debug=True)
