from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def index():
    if not 'eventlist' in session:
        session['eventlist'] = []
    if not 'sum' in session:
        session['sum'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['location'] == "farm":
        session['location'] = random.randint(10,20)
        session['eventlist'].append("Earned {} golds from the farm!".format(session['location']))
        session['sum'] += session['location']

    if request.form['location'] == "cave":
        session['location'] = random.randint(5,10)
        session['eventlist'].append("Earned {} golds from the cave!".format(session['location']))
        session['sum'] += session['location']


    if request.form['location'] == "house":
        session['location'] = random.randint(2,5)
        session['eventlist'].append("Earned {} golds from the house!".format(session['location']))
        session['sum'] += session['location']


    if request.form['location'] == "casino":
        session['location'] = random.randint(-50,50)
        session['eventlist'].append("Earned {} golds from the casino!".format(session['location']))
        session['sum'] += session['location']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)