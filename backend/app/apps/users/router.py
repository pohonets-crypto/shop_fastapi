from fastapi import APIRouter, status

from app.apps.users.schema import RegisterUserSchema, RegisteredUserSchema

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserSchema) -> RegisteredUserSchema:
    created_user = RegisteredUserSchema(id=123, **new_user.dict())
    return created_user
