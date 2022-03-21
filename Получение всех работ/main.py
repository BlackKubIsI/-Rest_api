from data.jobs import Jobs
from data.users import User
from data import db_session, jobs_api

from flask import Flask, Blueprint, request, render_template, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "random_key"

if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.bluprint)
    app.run(port=8080, host="127.0.0.1", debug=True)