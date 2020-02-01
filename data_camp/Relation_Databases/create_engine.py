import sqlalchemy
from sqlalchemy import create_engine

# Creat engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names
print(table_names)