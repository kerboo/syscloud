from auth import app
from auth import db
from flask_script import Manager

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()



if __name__=="__main__":
    manager.run()
