import snowflake.connector
con = snowflake.connector.connect(
    user=username,
    password=your_account_password,
    account=your_account_name
)
print('---connected to database-----')

try:
    cs = con.cursor()
    cs.execute("use db_name")
    cs.execute("use  schema schema_name")
    cs.execute("select id from table_name ")
    for (id) in cs:
        print('{0}'.format(id))
finally:
    cs.close()
