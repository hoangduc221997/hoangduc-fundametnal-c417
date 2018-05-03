from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (uri)

db = client.get_default_database()
posts = db["posts"]

post = {
    'title':'Play Dan',
    'author' : 'Duc dz',
    'content':''' Em là cô bé vàng trong làng đập đá,
    anh là chú thỏ nhỏ trong mỏ kẹo ke
    hehe '''
}
posts.insert_one(post)
