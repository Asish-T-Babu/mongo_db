from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["ecommerce"]

# Use the users collection 
users_collection = db["users"]

# Inser t a single document into the users collection
result = users_collection.insert_one({
    "name": "Asish",
    "age": 25
})

print(result.inserted_id)

# Insert multiple documents into the users collection
result = users_collection.insert_many([
    {
        "name": "Asish",
        "age": 25
    },
    {
        "name": "John",
        "age": 30
    }
])

print(result.inserted_ids)

# Find a single document in the users collection
user = users_collection.find_one({
    "email": "asish@gmail.com"
})

print(user)

# Find multiple documents in the users collection
users = users_collection.find({
    "role": "developer"
})

for user in users:
    print(user)

# Comparison operators
# Find multiple documents in the users collection with age greater than or equal to 25
# We can able to use all the mongoDB comparison operators like $eq, $ne, $gt, $gte, $lt, $lte, $in, $nin in the query to filter the documents based on the field.
users = users_collection.find({
    "age": {"$gte": 25}
})

for user in users:
    print(user)

# Update a single document in the users collection
result = users_collection.update_one(
    {"email": "asish@gmail.com"},
    {"$set": {"age": 26}}
)
print(result.matched_count)
print(result.modified_count)

# To increment a field in a document, we can use the $inc operator. The $inc operator increments the value of a field by a specified amount. If the field does not exist, it will be created and set to the specified amount.
users_collection.update_one(
    {"email": "asish@gmail.com"},
    {"$inc": {"login_count": 1}}
)

# Delete a single document in the users collection
result = users_collection.delete_one({
    "email": "asish@gmail.com"
})
print(result.deleted_count)