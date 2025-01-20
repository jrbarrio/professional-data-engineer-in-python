# Build a query to create a JSON-object
query = """
SELECT
	row_to_json(row(review_id, rating, year_month))
FROM reviews;
"""

# Execute the query, and output the results
results = pd.read_sql(query, db_engine)
print(results.head(10))