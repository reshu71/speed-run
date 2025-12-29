import json

raw_data = """
[
    {"id": 1, "name": "Alice", "meta": "age:30,role:admin"},
    {"id": 2, "name": "Bob", "meta": "age:25,role:user"},
    {"id": 3, "name": "Charlie", "meta": "role:user,age:40"},
    {"id": 4, "name": "Dave", "meta": "role:guest"}, 
    {"id": 5, "name": "Eve", "meta": "age:35,role:admin"}
]
"""

def parse_age(meta_string):
    # Splits "age:30,role:admin" into parts
    parts = meta_string.split(',')
    for part in parts:
        if "age" in part:
            # EXTRACT VALUE: "age:30" -> "30"
            return int(part.split(':')[1])
    return 0

def get_average_age(users):
    total_age = 0
    count = 0
    
    for user in users:
        age = parse_age(user['meta'])
        
        # FIX: Only count if age is valid
        if age > 0:
            total_age += age
            count += 1
        
    return total_age / count

def main():
    users = json.loads(raw_data)
    avg = get_average_age(users)
    print(f"Average Age: {avg}")

if __name__ == "__main__":
    main()