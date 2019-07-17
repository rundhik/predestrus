from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_rbac import RBAC

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True, port=9000, load_dotenv=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
login = LoginManager(app)
login.login_view = 'masuk'
login.login_message = 'Anda harus masuk untuk mengakses halaman'
rbac = RBAC(app)

from app import routes, models, errors