# Build the query to select the review_id and rating fields
query = """
	SELECT 
    	review -> 'location' AS location, 
        review ->> 'statement' AS statement 
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)