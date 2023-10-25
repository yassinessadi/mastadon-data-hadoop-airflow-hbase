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
# for data in table_user.scan():
#     print(data)
# for data in table_post.scan():
#     print(data)
# get the data base on the column family and row key
# ps = table.row(row='fr',columns=['post:language'])
# print(ps)



# Initialize a dictionary to store user followers
user_followers = {}
# get data from table user
rows = table_user.scan()
# Iterate over the rows and store user followers
for row_key, data in rows:
    followers_count = int(data[b'user_details:followers_count'])
    username = data[b'user_details:username'].decode('utf-8')
    user_followers[username] = followers_count
# Sort users based on follower count
sorted_users = sorted(user_followers.items(), key=lambda x: x[1], reverse=True)

# Specify the number of top users you want to retrieve
num_top_users = 5  
# Print the top users with the highest number of followers
print(f"Top {num_top_users} users with the highest number of followers:")

for i, (username, followers_count) in enumerate(sorted_users[:num_top_users]):
    print(f"{i+1}. User: {username} | Followers: {followers_count}")


print("------------------------User engagement------------------------------")


# Retrieve post data
post_rows = table_post.scan()

# Iterate over post rows
for post_row_key, post_data in post_rows:
    # Extract relevant data from post data
    user_id = post_data[b'post_details:user_id'] #.decode('utf-8')
    reblogs_count = int(post_data[b'post_details:reblogs_count'])
    favourites_count = int(post_data[b'post_details:favourites_count'])
    

    # Retrieve user data from user_table
    user_data = table_user.row(user_id,columns=["user_details:followers_count", "user_details:username"])
    # print(user_data)

    # Check if user data exists for the post
    if user_data:
        followers_count = int(user_data[b'user_details:followers_count'])
        username = user_data[b'user_details:username'].decode('utf-8')
        followers_count = 1 if followers_count == 0 else followers_count
        # Calculate engagement rate
        engagement_rate = (favourites_count + reblogs_count) / followers_count

        # Print the engagement rate for the user
        print(f"Engagement rate for user {username}: {round(engagement_rate*100,2)}%")
    else:
        print(f"No post data found for user {username}")

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
    elif values == 'media' or values == 'favourites_count' or values == 'reblogs_count' or values == 'user_id':
        table_post.put(row_key, {"post_details:" + column:item[2].strip()})

f.close()
connection.close()
