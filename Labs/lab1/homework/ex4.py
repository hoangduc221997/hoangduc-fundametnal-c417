import matplotlib
matplotlib.use("TkAgg")
from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()

customers = db["customers"]
events_c = 0
ad_c = 0
wom_c = 0
all_customers = customers.find()

for post in all_customers:
    if post ["ref"]=="events":
        events_c +=1
    if post["ref"]=="wom":
        wom_c +=1
    if post["ref"]=="ads":
        ad_c += 1
print(events_c,ad_c,wom_c)

ref_counts = [events_c,ad_c,wom_c]
ref_names =["Events","Ads","Wob"]
pyplot.pie(ref_counts,labels = ref_names)
pyplot.show()
