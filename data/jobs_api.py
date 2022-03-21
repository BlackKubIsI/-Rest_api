from . import db_session
from .jobs import Jobs

from flask import Blueprint, jsonify

bluprint = Blueprint("jobs_api", __name__, template_folder="templates")


@bluprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print([i for i in jobs])
    return jsonify({
        "jobs": [item.to_dict(only=("id", "team_leader", "job", "work_size", "collaborators",
                                    "departament", "start_date", "end_date", "is_finished")) for item in jobs]
    })
