# import the libs
import happybase


# made connection with hbase on localhost:9090
connection = happybase.Connection('127.0.0.1',9090)

# tables names
user_table = 'user_table'
post_table = 'post_table'

# read the content of txt file included on the root.
f = open("output.txt", "r")


# check if the tables exists.
table_list = [t.decode('utf-8') for t in connection.tables()]

# create the table if not exist (user table)
if user_table not in table_list :
    connection.create_table(
        user_table,
        {
            'user_details':dict()
        }
    )
# create the table if not exist (post table)
if post_table not in table_list :
    connection.create_table(
        post_table,
        {
            'post_details':dict()
        }
    )

# make connection to tables
table_user = connection.table(user_table)
table_post = connection.table(post_table)

# retreive if there is any data 
for data in table_user.scan():
    print(data)
for data in table_post.scan():
    print(data)
# get the data base on the column family and row key
# ps = table.row(row='fr',columns=['post:language'])
# print(ps)

# insert into the tables
for x in f:
    # get line from the content the text file splited by "
    item = x.split('"')
    # get the column name from the line
    column = item[1].split(':')[0]
    # get the row key from the line
    row_key = item[1].split(':')[1]
    # get the value from the line
    values = item[1].split(':')[0]
    if  values == 'following_count' or values == 'followers_count' or values == 'status_count':
        table_user.put(row_key, {"user_details:" + column:item[2].strip()})
    elif values =='username' or values == 'created_at' or values == 'url':
        table_user.put(row_key, {"user_details:" + column:item[3].strip()})
    elif values =='language' or values == 'tag' or values == 'visibility':
        table_post.put(row_key, {"post_details:" + column:item[3].strip()})
    elif values == 'media' or values == 'favourites_count' or values == 'reblogs_count':
        table_post.put(row_key, {"post_details:" + column:item[2].strip()})

f.close()
connection.close()
