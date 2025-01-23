# Store the city key-value pair
redis_conn.set("city", "London")

# Store the sunshine key-value pair
redis_conn.set("sunshine", "7")

# Retrieve values stored at the city and sunshine keys
city = redis_conn.get("city")
sunshine = redis_conn.get("sunshine")

print(city)
print(sunshine)