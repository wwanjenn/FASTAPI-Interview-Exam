import datetime
from pydantic import BaseModel, Field
from typing import List

class RecipeBase(BaseModel):
    name: str
    ingredients: str
    steps: str
    time: int
    owner_id: int
    created_at: datetime

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    recipe_id: int
    owner_id: int

class RatingCreate(RatingBase):
    pass

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    
    class Config:
        orm_mode= True

class CommentBase(BaseModel):
    text: str
    recipe_id: int
    owner_id: int

class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id: int
    isActive: bool
    recipes: List[Recipe] = []
    
    class Config:
        orm_mode = True