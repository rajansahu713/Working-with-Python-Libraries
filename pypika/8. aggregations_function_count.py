from pypika import Query, Table

query = Query.from_('orders').select('customer_id', 'COUNT(*)').groupby('customer_id')

print(query.get_sql())