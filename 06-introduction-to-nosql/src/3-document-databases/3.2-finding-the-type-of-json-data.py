# Find the data type of the location field
query = """
SELECT
    json_typeof(review -> 'location') AS location_type
FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)