from app import app, db, api, Event, AccountController

if __name__ == '__main__':
    api.add_resource(Event, "/event")
    api.add_resource(AccountController, "/balance")
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
    