from pydantic import BaseModel, Field
from typing import Optional , Annotated


class Order(BaseModel):
    user_id: Annotated[str, Field(min_length=3)]
    user_phone_number : Annotated[str, Field(min_length=10 , max_length=10)]
    email: str
    total_cost : Annotated[float, Field(gt=0)]
    items:Annotated[list[str], Field(min_length=1)]

