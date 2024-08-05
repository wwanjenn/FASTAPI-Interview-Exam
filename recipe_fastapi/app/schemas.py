from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Recipe Models
class RecipeBase(BaseModel):
    name: str
    ingredients: str
    steps: str
    time: int  # Renamed from preparation_time to time for consistency
    owner_id: int
    created_at: Optional[datetime] = None  # Set default to None, as it may not be provided by the user

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[str] = None
    steps: Optional[str] = None
    time: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    class Config:
        orm_mode = True

# Rating Models
class RatingBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    recipe_id: int
    owner_id: int
    created_at: Optional[datetime] = None

class RatingCreate(RatingBase):
    pass

class RatingUpdate(BaseModel):
    rating: Optional[int] = None

class Rating(RatingBase):
    id: int
    class Config:
        orm_mode = True

# Comment Models
class CommentBase(BaseModel):
    text: str
    recipe_id: int
    owner_id: int
    created_at: Optional[datetime] = None

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    text: Optional[str] = None

class Comment(CommentBase):
    id: int
    class Config:
        orm_mode = True

# User Models
class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    recipes: List[Recipe] = []

    class Config:
        orm_mode = True
