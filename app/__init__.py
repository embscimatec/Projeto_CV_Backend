from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db) #recebe as migrações e o banco de dados que trabalhará com isso

manager = Manager(app) #cuidará dos comandos que serão dados para a inicialização da aplicação
manager.add_command('db', MigrateCommand)

from app.controllers import default