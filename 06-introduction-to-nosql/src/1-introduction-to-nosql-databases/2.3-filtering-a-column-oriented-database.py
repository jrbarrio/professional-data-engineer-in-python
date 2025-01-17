# Return team, name, and year for all years greater than 2000
query = """
SELECT
	team,
    name,
    year
FROM olympic_medals 
WHERE year > 2000
;
"""

# Execute the query, print the results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)