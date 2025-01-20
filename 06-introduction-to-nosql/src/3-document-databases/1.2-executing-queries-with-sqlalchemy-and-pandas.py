import pandas as pd
import sqlalchemy

# Create a connection to the reviews database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/disneyland")

# Execute a query against the nested_reviews table
results = pd.read_sql("SELECT * FROM nested_reviews;", db_engine)
print(results)