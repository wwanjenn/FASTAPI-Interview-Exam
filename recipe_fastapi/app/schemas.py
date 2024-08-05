from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    ingredients: str
    steps: str
    time: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    rating: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    recipe_id: int
    
    class Config:
        orm_mode= True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    recipe_id: int

    class Config:
        orm_mode = True
        