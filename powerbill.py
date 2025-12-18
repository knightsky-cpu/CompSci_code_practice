days = input("how many days are in this month?: ")
days = int(days)
hours = 24
watts = input("how many watts do you use per hour?: ")
watts = int(watts)
kilowatts = watts / 1000    # kilowatts per hour
kilowatts = int(kilowatts)
kilowatt_hours = kilowatts * hours  # kilowatt hours per day use
kilowatt_hours = int(kilowatt_hours)
total_kwh = kilowatt_hours * days   # kilowatt hours per month use average
total_kwh = int(total_kwh)
cost_per_kwh = input("what is the cost of a kilowatt?: ")
cost_per_kwh = float(cost_per_kwh)
power_bill = total_kwh * cost_per_kwh
cost_per_hour = kilowatts * cost_per_kwh

print("this is what you will spend for electricity this month", f"${power_bill:.2f}")
print("your total energy consumption for the month is", f"{total_kwh} kwh", "and your energy use per day is", f"{kilowatt_hours} kwh", "and your energy use per hour is", f"{kilowatts} kw")
print("it costs you", f"${cost_per_hour:.2f}", "per hour for electricty to power your home")


# this spell was conjured up by the terminal wizard wifiknight 
