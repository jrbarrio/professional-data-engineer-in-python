# Return the statement and reviewer fields, filter by the 
# nested branch field
query = """
    SELECT 
        json_extract_path(review, 'statement'),
        json_extract_path_text(review, 'location', 'reviewer')
    FROM nested_reviews
    WHERE json_extract_path_text(review, 'location', 'branch') = 'Disneyland_California';
"""

data = pd.read_sql(query, db_engine)
print(data)