import flask

app = flask.Flask(__name__)

# the default route 
@app.route("/")
def index():
	headline = "Welcome to my page!!"
	return flask.render_template("bootstrap.html", headline=headline)

@app.route("/bye")
def bye():
	headline = "Thank you for visting my page!!!"
	return flask.render_template("bootstrap.html", headline=headline)


@app.route("/mena")
def mena():
	return "What is up MENA!!!!"

