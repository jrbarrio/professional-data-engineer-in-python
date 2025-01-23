import redis

# Create a connection to Redis cluster
r = redis.Redis(
  	host="localhost",
    port=6379,
    decode_responses=True
  )