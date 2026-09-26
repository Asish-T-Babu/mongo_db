from pymongo import AsyncMongoClient

client = AsyncMongoClient(
    "mongodb://localhost:27017"
)

db = client["ecommerce"]

users_collection = db["users"]

async def insert_user():
    # result = await users_collection.insert_one({
    #     "name": "Asish",
    #     "age": 25
    # })
    # print(result.inserted_id)

    # Async find() is slightly different

    # This is important.
    cursor = users_collection.find({})

    async for user in cursor:
        print(user)

    # or
    users = await users_collection.find({}).to_list()
    print(users)

    # or
    users = await users_collection.find({}).to_list(length=None)
    print(users)


if __name__ == "__main__":
    import asyncio
    asyncio.run(insert_user())