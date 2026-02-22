from app.core.extensions import db
from datetime import datetime

class Invoice(db.Model):
  __tablename__="invoices"

id = db.Column(db.Integer, primary_key=True)
customer_name = db.Column(db.String(), nullable=False)
consumption_kwh = db.Column(db.Float, nullable=False)
total_amount = db.Column(db.Float, nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
