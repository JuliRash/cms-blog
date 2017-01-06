from flask import Flask 
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate , MigrateCommand 
from flask_script import Manager 
db = SQLAlchemy(app)
# flask migrate cnfiguration
migrate = Migrate(app , db)
manager = Manager(app)
manager.add_command('db' , MigrateCommand)
# database connection with posgresql database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://idowu:julius@localhost/blog'
