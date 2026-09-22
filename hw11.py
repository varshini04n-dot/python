from tracker import create_record
from datetime import datetime
import json


records = [
    create_record("Chennai", "Visited Marina Beach", "05-06-2022"),
    create_record("Bangalore", "Visited Cubbon Park", "15-07-2022"),
    create_record("Kochi", "Visited Fort Kochi", "20-08-2022")
]


for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")


json_data = json.dumps(records)

print("JSON Data:")
print(json_data)


python_data = json.loads(json_data)

print("\nTravel Records:")

for record in python_data:
    print(
        record["city"],
        "-",
        record["comment"],
        "-",
        record["date"]
    )