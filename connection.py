import happybase
connection = happybase.Connection('127.0.0.1',9090)
table = connection.table('employee')

for key, data in table.scan():
    print(key, data) 