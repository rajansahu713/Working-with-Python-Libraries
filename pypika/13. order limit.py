
from pypika import Query, Table

# Define a table
products = Table('products')

# Construct a query with ordering and limiting
query = Query.from_(products).select('name', 'price').orderby('price').limit(10)

# Output the generated query
print(query.get_sql())