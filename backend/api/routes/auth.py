from fastapi import APIRouter
from pydantic import BaseModel
from db.memory_store import create_user

router = APIRouter()

class LoginRequest(BaseModel):
    name: str

@router.post("/login")
def login(req: LoginRequest):
    user_id = create_user(req.name)
    return {"user_id": user_id}