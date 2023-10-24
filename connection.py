import happybase

connection = happybase.Connection('127.0.0.1',9090)
table_name = 'test_table'
table_name1 = 'test_table1'

f = open("output.txt", "r")

table = connection.table(table_name)

connection.create_table(
    table_name1,
    {
        'post_details':dict()
    }
)

table1 = connection.table(table_name1)

# for data in table.scan():
#     print(data)
# ps = table.row(row='fr',columns=['post:language'])
# print(ps)
for x in f:
    # print(x)
    item = x.split('"')
    key = item[1]
    row_key = item[1].split(':')[0]
    if  row_key == 'following_count' or row_key == 'followers_count' or row_key == 'status_count':
        print(key.split(":")[1],key.split(":")[0],item[2])
        # table.put(key.split(':')[1], {"user_details:" + key.split(":")[0]:item[2].strip()})
    elif row_key =='username' or row_key == 'created_at' or row_key == 'url':
        print(key.split(":")[1],key.split(":")[0],item[3])
        # table.put(key.split(':')[1], {"user_details:" + key.split(":")[0]:item[3].strip()})
    elif row_key =='language' or row_key == 'tag' or row_key == 'visibility':
        # print(key.split(":")[1],key.split(":")[0],item[3].strip())
        table1.put(key.split(':')[1], {"post_details:" + key.split(":")[0]:item[3].strip()})
    elif row_key == 'media' or row_key == 'favourites_count' or row_key == 'reblogs_count':
        # print(key.split(":")[1],key.split(":")[0],item[2].strip())
        table1.put(key.split(':')[1], {"post_details:" + key.split(":")[0]:item[2].strip()})
    # value = item[2].strip()
    # # print(f"Row Key: {key.split(':')[1]}, Column Family: {row_key}, Value: {value}")
    # data = {row_key:value}
    # print(data)
    # table.put(key.split(':')[1], data)

f.close()
connection.close()
