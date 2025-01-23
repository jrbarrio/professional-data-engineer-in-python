# Create a dictionary containing weather data
london_weather_mapping = {
	"temperature": 42,
	"humidity": 88,
	"visibility": "low"
}

# Store the london_weather key-value pair
redis_conn.hset(
    "london_weather",
	mapping=london_weather_mapping
)

# Retrieve and print the london_weather key-value pair
print(redis_conn.hgetall("london_weather"))