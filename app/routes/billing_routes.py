from flask import Blueprint, render_template, request
from app.models.tariff import TariffTier
from app.services.invoice_service import InvoiceService

billing_bp = Blieprint("billing", __name__)

@billing_bp.route("/", methods = ["GET , "POST"])

def simulate():

  service = InvoiceService()
  tiers = TariffTier.query.all()
  result = None

  if request.method == "POST":
    name = request.from ["name"]
    consumption = floar(request.form["consuption"])
    fixed_charge = floar(request.form["fixed_charge"])

    invoice = service.create_invoice(
      customer_name=name,
      consumtion=consumption,
      tiers=tiers,
      fixed_charge=fixed_charge
      )
      result = invoice.total_amount

  return render_template("simulator.html", result=result)
                                
