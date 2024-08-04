from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import relationship
from.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    ingredients = Column(String)
    steps = Column(String)
    time = Column(Integer)
    ratings = relationship("Rating", back_populates = "recipe")
    comments = relationship("Coment", back_populates = "recipe")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key= True, index= True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    rating = Column(Integer)
    recipe = relationship("Recipe", back_populates = "ratings")

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key= True, index= True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    text = Column(String)
    recipe = relationship("Recipe", back_populates = "comments")


