import sys
from flask import Flask, render_template, request, redirect
sys.path.append('../')
from emailSpecific import email_specific
app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html")

@app.route("/request11", methods = ['POST'])
def request11():
	email_specific('Student {} with registered email {} have requested a 1:1'.format(request.form['studenthubhandle'],request.form['email']),'Student {} with registered email {} have requested a 1:1'.format(request.form['studenthubhandle'],request.form['email']))
	print(request.form)
	return redirect('https://calendly.com/feng3245/30min')	

if __name__ == "__main__":
	app.run()