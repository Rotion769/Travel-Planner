def estimate_budget_inr(days, mode, num_people=2, flight_per_person=None):
days = int(days)


lodgings = {
"budget-friendly": 1200,
"adventure": 2000,
"luxury": 6500
}
meals = {
"budget-friendly": 500,
"adventure": 800,
"luxury": 2200
}
activities = {
"budget-friendly": 400,
"adventure": 1200,
"luxury": 2800
}


stay_cost = lodgings.get(mode, 1200) * num_people * max(1, days - 1)
food_cost = meals.get(mode, 500) * num_people * days
act_cost = activities.get(mode, 400) * num_people * days
flight_cost = (float(flight_per_person) * num_people) if flight_per_person else 0.0


total = stay_cost + food_cost + act_cost + flight_cost


return {
"currency": "INR",
"breakdown": {
"lodging": f"₹ {stay_cost:,}",
"meals": f"₹ {food_cost:,}",
"activities": f"₹ {act_cost:,}",
"flights": f"₹ {int(flight_cost):,}" if flight_cost else "₹ 0"
},
"total_estimate": f"₹ {int(total):,}"
}