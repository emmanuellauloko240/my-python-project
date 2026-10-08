resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

        # break
def get_positive_number(prompt):
    while True:
        try:
            typed = int(input(get_positive_number))
            print(typed)
            return
        except:
            print("error")

def find_resource(looking_for):
    looking_for = (looking_for.strip().upper())
    for resource in resources:
        if resource["id"] == looking_for:
            return resource
    return None

# print(input(get_positive_number))
# print(find_resource("R999"))
# print(find_resource("r001"))