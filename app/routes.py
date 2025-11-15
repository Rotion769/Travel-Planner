from flask import Blueprint, request, jsonify
if not dest:
return err("destination required")
from .rag import rag_recommended_places
places = rag_recommended_places(dest, ints, limit=limit)
return jsonify({"ok": True, "destination": dest, "count": len(places), "results": places})




@api_bp.route("/share_itinerary", methods=["POST"])
def share():
data = request.get_json(force=True, silent=True) or {}
user_id = data.get("user_id")
if not user_id: return err("user_id required")
ensure_user_local(user_id)
it = USERS[user_id]["itinerary"]
if not it: return err("No itinerary found.",404)


dest, days, mode = it['destination'], it['days'], it['mode']
interests = ", ".join(it["interests"]) if it["interests"] else "general interests"


lines=[]
lines.append(f"**Your {days}-Day {mode.title()} Trip to {dest}**\n")
lines.append(f"This trip is tailored for someone interested in **{interests}**. Here's what your experience looks like:\n")


for dp in it["day_plans"]:
lines.append(f"**Day {dp['day']}**")
for a in dp["activities"]:
when = a.get("time_of_day",
"")
cost = f" (~{a['estimated_cost']})" if a.get("estimated_cost") else ""
lines.append(f"- {when.capitalize()+': ' if when else ''}{a['title']}{cost}")
lines.append("")


lines.append("Enjoy your trip! Safe travels and unforgettable memories await!")


return jsonify({"ok":True,"summary_text":"\n".join(lines)})




@api_bp.route("/budget_estimate", methods=["POST"])
def budget():
data = request.get_json(force=True, silent=True) or {}
days = data.get("days")
if not days: return err("days required")
mode = data.get("mode")
from .agent import decide_mode
if mode not in ["budget-friendly","adventure","luxury"]:
mode = decide_mode(days, data.get("interests"), data.get("max_budget"), None)
est = estimate_budget_inr(days, mode, int(data.get("num_people",2)), data.get("flight_per_person"))
return jsonify({"ok":True,"mode":mode,"estimate":est})




@api_bp.route("/", methods=["GET"])
def root():
return jsonify({"ok":True,"service":"Travel Planner API (BART)","version":"0.6-rag10"})