# Write a query to return all columns, limiting to 10 rows
query = "SELECT * FROM olympic_medals LIMIT 10;"

# Execute the query
results = conn.cursor().execute(query).fetch_pandas_all()

# Print the results of the query
print(results)