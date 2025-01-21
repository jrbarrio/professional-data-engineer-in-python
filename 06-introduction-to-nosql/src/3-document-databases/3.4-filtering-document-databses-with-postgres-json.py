# Build the query to select the rid and rating fields
query = """
SELECT
	review ->> 'statement' AS customer_review 
FROM nested_reviews 
WHERE review -> 'location' ->> 'branch' = 'Disneyland_California';
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)