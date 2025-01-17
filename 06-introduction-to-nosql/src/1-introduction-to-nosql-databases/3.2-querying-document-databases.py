# Update the query to select the review field
query = """
	SELECT 
    	review
    FROM nested_reviews;
"""

# Execute the query
data = pd.read_sql(query, db_engine)

# Print the first element of the DataFrame
print(data.iloc[0, 0])
