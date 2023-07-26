from flask import render_template, Blueprint

errors = Blueprint("errors", __name__)

@errors.errorhandler(404)
def PageNotFound(error):
    return render_template("error.html", error=error), 404
