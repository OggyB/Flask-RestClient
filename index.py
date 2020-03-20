from flask import Flask, render_template, request, redirect, session
import requests
import json
from forms import MyForm
from client import User
from endPoints import EndPoint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'apiKey'


# Login Page
@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm(request.form)

    if (request.method == "POST"):

        mail = request.form.get("email")
        password = request.form.get("password")

        user = User(mail, password)

        token = user.getToken()

        if (token != False):
            session['token'] = token
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        return render_template('login.html', form=form)


# HomePage
@app.route("/dashboard", methods=["GET"])
def homepage():
    user = User('', '')

    if (user.ıs_auth(session['token']) is not False):

        return render_template('homepage.html')
    else:
        return redirect('/')


# Get Client
@app.route("/dashboard/getclient", methods=["GET", "POST"])
def getclient():
    user = User('', '')

    if  (user.ıs_auth(session['token']) is not False):
        if request.method == "POST":

            endpoint = EndPoint(session['token'])
            data = endpoint.getClient(request.form.get('transactionId'))
            return render_template('getClient.html', data=data)
        else:
            return render_template('getClient.html')

    else:
        return redirect('/')

# Get Transaction Report
@app.route("/dashboard/gettransactionreport",methods=["GET","POST"])
def getTransactionReport():
    user = User('', '')
    if  (user.ıs_auth(session['token']) is not False):
        if request.method == "POST":

            endpoint = EndPoint(session['token'])
            data = endpoint.getTransactionsReport(request.form.get('fromDate'), request.form.get('toDate'))
            return render_template('getTransactionReport.html', data=data)
        else:
            return render_template('getTransactionReport.html')

    else:
        return redirect('/')

#Get Transaction
@app.route("/dashboard/gettransaction",methods=["GET","POST"])
def getTransaction():
    user = User('', '')

    if (user.ıs_auth(session['token']) is not False):
        if request.method == "POST":

            endpoint = EndPoint(session['token'])
            data = endpoint.getTransaction(request.form.get('transactionId'))
            return render_template('gettransaction.html', data=data)
        else:
            return render_template('gettransaction.html')

    else:
        return redirect('/')

# Get Transaction Query
@app.route("/dashboard/gettransactionquery",methods=["GET","POST"])
def getTransactionQuery():
    user = User('', '')
    if (user.ıs_auth(session['token']) is not False):
        if request.method == "POST":

            endpoint = EndPoint(session['token'])
            data = endpoint.getTransactionQuery(request.form.get('fromDate'), request.form.get('toDate'))
            return render_template('getTransactionQuery.html', data=data)
        else:
            return render_template('getTransactionQuery.html')

    else:
        return redirect('/')


if __name__ == ("__main__"):
    app.run(debug=True)
