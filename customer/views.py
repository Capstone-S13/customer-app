#contains the code for oruting of the app to different references and 
# also rendering of HTML files

from flask_sqlalchemy import SQLAlchemy
from __init__ import app
from flask import Flask, render_template,request,session, redirect, url_for
from strgen import StringGenerator as SG
#Here I have used strgen to geneate random IDs for my customers

#The models need to be imported from manager before use for CRUD operations
from database import db
from database import Customer,Product

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
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