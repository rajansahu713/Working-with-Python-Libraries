from pypika import Query, Table

# Define a table
users = Table('users')

# Construct an INSERT query
query = Query.into(users).columns('name', 'age').insert('Alice', 30)

# Output the generated query
print(query.get_sql())