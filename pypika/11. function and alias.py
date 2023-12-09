from pypika import Query, Table, functions as fn

# Define tables
products = Table('products')

# Construct a query with functions and aliasing
query = Query.from_(products).select(fn.Count('*').as_('total_products'))

# Output the generated query
print(query.get_sql())