from datetime import datetime
from .utils import new_id, sanitize_interests
from .rag import rag_recommended_places
import random


ACTIVITY_POOL = {
"general": [
("City orientation walk", "morning", "walk", 0),
("Local market exploration", "afternoon", "culture", 5),
("Scenic viewpoint visit", "evening", "relax", 0),
("Park picnic", "afternoon", "relax", 10),
("River/harbor short cruise", "afternoon", "leisure", 20),
("Photography stroll", "morning", "experience", 0),
],
"food": [
("Street-food tasting tour", "evening", "food", 12),
("Hands-on cooking class", "afternoon", "experience", 50),
("Local bakery & dessert crawl", "morning", "food", 8),
("Farmers' market visit", "morning", "food", 0),
("Chef's table dinner", "evening", "food", 70),
],
"history": [
("Guided history tour", "morning", "museum", 18),
("Old town heritage walk", "afternoon", "walk", 0),
("Landmark museum visit", "afternoon", "museum", 15),
("Historic monument visit", "morning", "culture", 10),
("Archaeological site visit", "morning", "culture", 12),
],
"adventure": [
("Hiking trail", "morning", "adventure", 25),
("Cycling countryside", "morning", "adventure", 15),
("Kayaking or boating", "afternoon", "adventure", 35),
("Rock-climbing session", "afternoon", "adventure", 40),
("Zipline or canopy tour", "afternoon", "adventure", 45),
],
"luxury": [
("Spa & wellness session", "afternoon", "relax", 90),
("Fine dining reservation", "evening", "food", 120),
("Private guided tour", "morning", "experience", 110),
("Boutique shopping experience", "afternoon", "shopping", 150),
],
"nightlife": [
("Rooftop bar", "evening", "nightlife", 30),
("Night market & music", "evening", "nightlife", 15),
("Live cultural performance", "night", "culture", 25),
]
}




}