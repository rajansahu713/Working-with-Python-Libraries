
from pypika import Query, Table, Case

# Define a table
students = Table('students')

# Construct a query with a CASE statement
query = Query.from_(students).select(
    students.name,
    Case()
    .when(students.score > 90, 'A')
    .when(students.score > 80, 'B')
    .else_('C').as_('grade'))

print(query.get_sql())

