from app.models.invoice import Invoice
from app.core.extensions import db
from app.services.billing_engine import BillingEngine

class InvoiceServise:

  def__init__(self):
    self.engine = BillingEngine()

  def create_invoice(self, customer:name, consumption, tiers, fixed_charge):
    total= self.engine.calculate(
      consumption_keh=consumption, 
      tiers=tiers,
      fixed_charge=fixed_charge
    )
    invoice = Invoice(
      customer_name=customer_name
      consumption_kwh=consumption,
      total_amount=total
    )
    db.session.add(invoice)
    db.session.commit()

    return invoice
