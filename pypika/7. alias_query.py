from pypika import Query, Table


query = Query.from_('users').select('name', 'age').select('age*2', alias='twice_age')


print(query.get_sql())