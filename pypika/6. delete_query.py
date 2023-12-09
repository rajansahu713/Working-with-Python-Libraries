from pypika import Query, Table

# Define a table
users = Table('users')

# Construct a DELETE query
query = Query.from_(users).where(users.age < 30).delete()

# Output the generated query
print(query.get_sql())