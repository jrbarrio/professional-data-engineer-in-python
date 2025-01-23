# Loop through each of the cities
for city in cities:
	# Grab the temperature
    temperature = redis_conn.get(f"{city}_temp")
    
    # Check if the temperature is None
    if temperature is None:
    	# Store an unknown temperature
        redis_conn.set(f"{city}_temp", "unknown temperature")
        print(f"Unknown temperature in {city}")
    
    else:
      	# Otherwise, print the temperature
    	print(f"The temperature in {city} is {temperature}")
