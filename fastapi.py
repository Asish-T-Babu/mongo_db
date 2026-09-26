from fastapi import APIRouter, HTTPException
from app.database import users_collection

router = APIRouter()


@router.get("/users/{email}")
async def get_user(email: str):

    user = await users_collection.find_one({
        "email": email
    })

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user