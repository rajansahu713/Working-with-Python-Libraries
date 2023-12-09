from pypika import Query, Table


query = Query.from_('employees').select('id', 'name', 'age', 'salary')

print(query.get_sql())