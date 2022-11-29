from app import app, db
from flask import Response

@app.route("/reset", methods=['POST'])
def reset():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 'OK', 200, {'Content-Type':'application/json'}
