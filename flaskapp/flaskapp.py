from flask import Flask
from flask import render_template, url_for
import os
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "data", "2011.json")
	data = json.load(open(json_url))
	print data
	return render_template('index3.html', data=data)


@app.route('/user/<username>')
def get_username(username):
    return 'Hello World!, %s' % username

if __name__ == '__main__':
	app.debug = True
	app.run()