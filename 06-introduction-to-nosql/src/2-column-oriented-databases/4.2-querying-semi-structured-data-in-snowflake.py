# Build a query to pull city and country names
query = """
SELECT
	city_meta:city,
    city_meta:country
FROM host_cities;
"""

# Execute query and output results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)