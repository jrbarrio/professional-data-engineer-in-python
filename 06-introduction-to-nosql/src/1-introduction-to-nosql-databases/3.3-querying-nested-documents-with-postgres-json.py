# Build the query to select the statement and location fields
query = """
	SELECT 
    	review -> 'statement' AS statement, 
        review -> 'location' AS location 
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)