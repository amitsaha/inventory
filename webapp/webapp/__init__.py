from flask import Flask
app = Flask(__name__)

from webapp.database import init_db, session
init_db()

import webapp.views

@app.teardown_request
def shutdown_session(exception=None):
    session.remove()
