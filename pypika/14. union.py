from pypika import Query, Table

# Define tables
table1 = Table('table1')
table2 = Table('table2')

# Construct a query with UNION
query = Query.from_(table1).select('*').union(Query.from_(table2).select('*'))

# Output the generated query
print(query.get_sql())