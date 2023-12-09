from pypika import Query, Table

# Define a table
users = Table('users')

# Construct an UPDATE query
query = Query.update(users).set(users.age, 32).where(users.name == 'Alice')

# Output the generated query
print(query.get_sql())