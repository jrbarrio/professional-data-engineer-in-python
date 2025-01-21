# Extract fields from JSON, and filter by reviewer location
query = """
    SELECT
    	review_id,
        review #> '{location, branch}' AS branch,
        review ->> 'statement' AS statement,
        rating
    FROM nested_reviews
    WHERE json_extract_path_text(review, 'location', 'reviewer') = 'Australia'
    ORDER BY rating DESC;
"""

data = pd.read_sql(query, db_engine)
print(data)