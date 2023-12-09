from pypika import Query, Table

query = Query.from_('products').select('category', 'MAX(price)').groupby('category')

print(query.get_sql())