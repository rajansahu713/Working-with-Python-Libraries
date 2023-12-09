from pypika import Query, Table

# Define tables
orders = Table('orders')
customers = Table('customers')

# Construct a subquery
subquery = Query.from_(orders).select('SUM(amount)').where(orders.customer_id == customers.id)

# Main query using the subquery
query = Query.from_(customers).select(customers.name, subquery).where(subquery > 1000)

# Output the generated query
print(query.get_sql())