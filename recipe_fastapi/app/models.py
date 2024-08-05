from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    ingredients = Column(String)
    steps = Column(String)
    time = Column(Integer)
    ratings = relationship("Rating", back_populates = "recipe")
    comments = relationship("Coment", back_populates = "recipe")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates= "recipes")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key= True, index= True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    rating = Column(Integer)
    recipe = relationship("Recipe", back_populates = "ratings")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key= True, index= True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    text = Column(String)
    recipe = relationship("Recipe", back_populates = "comments")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index= True)
    email = Column(String, unique= True, index= True)
    hasedPassword = Column(String)
    isActive = Column(Boolean, default = True)
    recipes = relationship("Recipe", back_populates= "owner")

