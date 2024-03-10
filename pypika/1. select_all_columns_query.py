"""Query to select all columns from the 'users' table.

Prints the generated SQL query string.
"""
from pypika import Query, Table

query = Query.from_('users').select('*')

print(query.get_sql())