from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def get_recipes_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).filter(models.Recipe.owner_id == owner_id).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipeId: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipeId).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).order_by(models.Recipe.created_at.desc()).offset(skip).limit(limit).all()

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    dbRecipe = models.Recipe(**recipe.model_dump())
    db.add(dbRecipe)
    db.commit()
    db.refresh(dbRecipe)
    return dbRecipe

def update_recipe(db:Session, recipeId: int, recipe: schemas.RecipeUpdate):
    dbRecipe = get_recipe(db, recipeId)
    if dbRecipe:
        if dbRecipe.owner_id != recipe.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in recipe.model_dump().items():
            setattr(dbRecipe, key, value)
        db.commit()
        db.refresh(dbRecipe)
    return dbRecipe

def delete_recipe(db: Session, recipeId: int):
    dbRecipe = get_recipe(db, recipeId)
    if dbRecipe:
        db.delete(dbRecipe)
        db.commit()
    return dbRecipe

def get_comment(db: Session, commentId: int):
    return db.query(models.Comment).filter(models.Comment.id == commentId).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).order_by(models.Comment.created_at.desc()).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: schemas.CommentCreate):
    dbComment = models.Comment(**comment.model_dump())
    db.add(dbComment)
    db.commit()
    db.refresh(dbComment)
    return dbComment

def update_comment(db:Session, commentId: int, comment: schemas.CommentUpdate):
    dbComment = get_comment(db, commentId)
    if dbComment:
        if dbComment.owner_id != comment.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in comment.model_dump().items():
            setattr(dbComment, key, value)
        db.commit()
        db.refresh(dbComment)
    return dbComment



def delete_comment(db: Session, commentId: int):
    dbComment = get_comment(db, commentId)
    if dbComment:
        db.delete(dbComment)
        db.commit()
    return dbComment


def get_rating(db: Session, ratingId: int):
    return db.query(models.Rating).filter(models.Rating.id == ratingId).first()

def get_rating(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rating).order_by(models.Rating.created_at.desc()).offset(skip).limit(limit).all()


def create_rating(db: Session, rating: schemas.RatingCreate):
    dbRating = models.Rating(**rating.model_dump())
    db.add(dbRating)
    db.commit()
    db.refresh(dbRating)
    return dbRating

def update_rating(db: Session, ratingId: int, rating: schemas.RecipeUpdate):
    dbRating = db.query(models.Recipe).filter(models.Rating.id == ratingId).first()
    if dbRating:
        if dbRating.owner_id != rating.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in rating.model_dump().items():
            setattr(dbRating, key, value)
        db.commit()
        db.refresh(dbRating)
    return dbRating

def delete_rating(db: Session, ratingId: int):
    dbRating = get_rating(db, ratingId)
    if dbRating:
        db.delete(dbRating)
        db.commit()
    return dbRating

def create_user(db: Session, user: schemas.UserCreate):
    dbUser = models.User(**user.model_dump())
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser


