from typing import Union
from typing import Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    code: int = 200
    status: str

class UserResponse(BaseResponse):
    data: Optional[Union[dict, list]]

class UserResponsePagination(UserResponse):
    page: Optional[dict]