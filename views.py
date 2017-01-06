from app import app
from flask import render_template , url_for , sessions , flash , make_response , request


@app.route('/')
def index():
	name = request.args.get('name')
	number = request.args.get('number')
	if not name:
		name = '<unknown>'
	return render_template('index.html' ,number=number ,  name=name)
	