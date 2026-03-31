from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints, field_validator
from password_strength import PasswordPolicy

from app.apps.core.schema import IdSchema


class UserPasswordSchema(BaseModel):
    password: str = Field(examples=["Hh12345!%"])

    @field_validator("password")
    @classmethod
    def validate_password_complexity(cls, value) -> str:
        password_policy = PasswordPolicy.from_names(
            length=8,
            uppercase=1,
            numbers=1,
            special=1
        )
        errors = password_policy.test(value)
        if not errors:
            return value

        error_messages = []

        for error in errors:
            error_name = error.name()
            if error_name == "length":
                error_messages.append(f"Password length must be at least 8")
            elif error_name == "uppercase":
                error_messages.append(f"Password must contain at least 1 uppercase letter")
            elif error_name == "numbers":
                error_messages.append(f"Password must contain at least 1 numbers")
            elif error_name == "special":
                error_messages.append(f"Password must contain at least 1 special characters")
        raise ValueError("; ".join(error_messages))



class BaseUserSchema(BaseModel):
    email: EmailStr = Field(description="Email of the user", examples=["example@mail.com"])
    name: Annotated[
        str,
        StringConstraints(
            pattern=r"^[0-9a-zа-яA-ZА-ЯЇїЯяІіГг\u2019_. ]+$",
            strip_whitespace=True,
            max_length=50,
            min_length=3
        )
    ] = Field(description="User's name", examples=["Walter"])


class RegisterUserSchema(UserPasswordSchema, BaseUserSchema):
    pass


class RegisteredUserSchema(IdSchema, BaseUserSchema):
    pass
