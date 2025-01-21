# Attempt to query the statement, nested branch, and nested
# zipcode fields from the review column
query = """
	SELECT 
    	json_typeof(review #> '{statement}'),
        review #>> '{location, branch}' AS branch,
        review #>> '{location, zipcode}' AS zipcode
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)