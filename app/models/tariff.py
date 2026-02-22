from app.core.extensions import db

class TariffTier(db.Model):
  __tablename__="tariff_tiers"

  id = db.Column(db.Integer, primary_key=True)
  min_kwh = db.Column(db.Float, nullable=False)
  max_kwh = db.Column(db.Float, nullable=True)
  price_per_kwh =db.Column(db.Float, nullable=False)
  
