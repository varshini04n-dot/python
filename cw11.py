from tripdata import get_trip
from datetime import datetime
import json

trips = [
    get_trip("Chennai", "15-05-2023", "Visited Marina Beach"),
    get_trip("Bangalore", "20-06-2023", "Visited Cubbon Park"),
    get_trip("Kochi", "10-07-2023", "Enjoyed the backwaters")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips)

print(json_data)