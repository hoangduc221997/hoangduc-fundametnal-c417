from pymongo import MongoClient

#1conect to data base
uri = "mongodb://admin:221997@ds255319.mlab.com:55319/c4e17dz"
client = MongoClient(uri)

#2. Get default databse
db = client.get_default_database()

#3. get blog collection
blog = db["blog"]

#4 write a new blog
post = {
    'title':"Hôm nay trời không nắng cũng không mưa :)",
    'content':"Tôi ở nhà code",
}
all_posts = blog.find()

for post in all_posts:
    print (post) 
