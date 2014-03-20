from webapp import app
from webapp.database import session
from webapp.models import System
from flask import request, Response
from sqlalchemy.orm.exc import NoResultFound

@app.route('/')
def index():
    return str(System.query.all())

@app.route('/add', methods=['POST', 'PATCH'])
def add():
    
    data = request.get_json()
    mac = data['mac']
    cpuinfo = data['cpuinfo']

    try:
        s = System.query.filter(System.mac == mac).one()
    except NoResultFound:
        s = System(mac=mac, cpuinfo=cpuinfo)
        session.add(s)
    else:
        s.cpuinfo = cpuinfo
    
    session.commit()
    
    return 'Added', 200

@app.route('/system/<mac>')
def system(mac):
    try:
        s = System.query.filter(System.mac == mac).one()
    except NoResultFound:
        return 'Not found', 404
    else:
        return Response(s.cpuinfo, mimetype='text/text')
