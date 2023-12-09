from pypika import Query, Table

query = Query.from_('users').select('*')

print(query.get_sql())