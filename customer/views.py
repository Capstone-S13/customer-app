from flask import render_template, request, sesson, redirect, url_for
from .__init__ import app


@app.route('/')
def login():
    error =  None
    if request.method == 'POST':
		x=request.form['username']
		x_list=[Customer.query.all()[i].loginid for i in range(len(Customer.query.all()))]
		if x in x_list:
			z=Customer.query.filter_by(loginid=x).all()[0].passwd
			if(request.form['password']!=z):
				error = 'Invalid Credentials. Please try again.'
			else:
				session['username']=x #storing session variable
				return render_template('index.html')
    
		error = 'Invalid Credentials. Please try again.' 
    return render_template('login.html', error=error)