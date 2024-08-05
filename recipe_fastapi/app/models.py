from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    ingredients = Column(String)
    steps = Column(String)
    time = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
    # Relationships
    ratings = relationship("Rating", back_populates="recipe")
    comments = relationship("Comment", back_populates="recipe")
    owner = relationship("User", back_populates="recipes")

class Rating(Base):
    __tablename__ = "ratings"
    
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    rating = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    recipe = relationship("Recipe", back_populates="ratings")
    user = relationship("User", back_populates="ratings")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    recipe = relationship("Recipe", back_populates="comments")
    user = relationship("User", back_populates="comments")

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Ensure this is suitable for indexing
    password = Column(String)
    
    # Relationships
    recipes = relationship("Recipe", back_populates="owner")
    ratings = relationship("Rating", back_populates="user")
    comments = relationship("Comment", back_populates="user")
