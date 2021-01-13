from pydantic import BaseModel,validator
from typing import List, Optional,Union
# 创建数据模型

class ModerLoginBody(BaseModel):
    user:Union[int,str] = '110'
    password:str = 'qq123123'

    @validator('user')
    def validatorEmpty(cls, value):
        if value =='':
            raise ValueError('必须有值')
        return str(value)
    
    @validator('password')
    def validatorPassword(cls, value):
        if value =='':
            return 'qq123123'
        return value

class ModerGetCookiesBody(BaseModel):
    url:str
    token:str

    @validator('url', 'token')
    def validatorEmpty(cls, value):
        if value =='':
            raise ValueError('必须有值')
        return value



