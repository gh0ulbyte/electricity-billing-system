from flask import Flask
from app.core.config import Config
from app.core.extensions import db, migrate

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from app.routes.billing_routes import billing_bp
app.register_blueprint(billing_bp)

return app
