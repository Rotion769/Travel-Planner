from .models import mode_classifier
from .config import CANDIDATE_MODES
from .utils import sanitize_interests




def decide_mode(days, interests, max_budget=None, mode_hint=None):
if mode_hint in CANDIDATE_MODES:
return mode_hint
ints = ", ".join(sanitize_interests(interests)) or "general"
prompt = f"Plan a {days}-day trip considering interests: {ints}. Budget: {max_budget if max_budget else 'unknown'}."
try:
res = mode_classifier(prompt, candidate_labels=CANDIDATE_MODES, multi_label=False)
label = res.get("labels", [None])[0]
score = res.get("scores", [0])[0]
if label and score >= 0.45: return label
except Exception:
pass
try:
return "adventure" if int(days) <= 6 else "budget-friendly"
except:
return "budget-friendly"