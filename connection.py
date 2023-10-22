import happybase

connection = happybase.Connection('127.0.0.1',9090)
table_name = 'test_table'

f = open("output.txt", "r")

table = connection.table(table_name)

for key, data in table.scan():
    print(key, data)


# for x in f:
#     item = x.split('"')
#     key = item[1]
#     value = item[2].strip()
#     row_key = item[1].split(':')[0]
#     data = {key: value}
#     # print(f"Row Key: {row_key}, Column Family: {key}, Value: {value}")
#     table.put(row_key, data)

f.close()
connection.close()
