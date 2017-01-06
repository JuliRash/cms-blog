from flask import Blueprint 
from flask import render_template 

entries = Blueprint('entries',__name__,template_folder='templates')

@entries.route('/')
def index():
	return render_template('entries/posts.html')