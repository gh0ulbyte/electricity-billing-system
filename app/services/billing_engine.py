class BillingEngine:

  def calculate(self, consumption_kwh, tiers, fixed_charge, category_coef=1.0, zone_coef=1.0):
    energy_total=0
    remaining=consumtion_kwh

    for tier in sorted(tiers, key=lambda t: t.min_kwh):
      if remaining <=0:
        break

      upper= tier.max_kwh if tier.max_kwh else remaining
      available = upper - tier.min_kwh if tier.max_kwh else remaining

      kwn = min(remaining, available)
      energy_total += kwh * tier.price_per_kwh
      remaining -= kwn

  subtotal = energy_total + fixed_charge
  return round(subtotal*category_coef*zone_coef, 2)
  
