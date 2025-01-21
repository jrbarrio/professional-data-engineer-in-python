# Update the query to select the nested reviewer field
query = """
SELECT 
	review -> 'location' ->> 'branch' AS branch,
    review -> 'location' ->> 'reviewer' AS reviewer
FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)