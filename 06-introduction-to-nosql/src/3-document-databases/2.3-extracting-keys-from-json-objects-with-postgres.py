# Build a query to find the unique keys in the review column
query = """
SELECT
	DISTINCT json_object_keys(review)
FROM nested_reviews;
"""

# Execute the query, show the results
results = pd.read_sql(query, db_engine)
print(results)