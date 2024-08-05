from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def get_recipes_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).filter(models.Recipe.owner_id == owner_id).offset(skip).limit(limit).all()

def getRecipe(db: Session, recipeId: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipeId).first()

def getRecipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models. Recipe).offset(skip).limit(limit).all()

def createRecipe(db: Session, recipe: schemas.RecipeCreate):
    dbRecipe = models.Recipe(**recipe.model_dump())
    db.add(dbRecipe)
    db.commit()
    db.refresh(dbRecipe)
    return dbRecipe

def updateRecipe(db:Session, recipeId: int, recipe: schemas.RecipeUpdate):
    dbRecipe = getRecipe(db, recipeId)
    if dbRecipe:
        if dbRecipe.owner_id != recipe.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in recipe.model_dump().items():
            setattr(dbRecipe, key, value)
        db.commit()
        db.refresh(dbRecipe)
    return dbRecipe

def deleteRecipe(db: Session, recipeId: int):
    dbRecipe = getRecipe(db, recipeId)
    if dbRecipe:
        db.delete(dbRecipe)
        db.commit()
    return dbRecipe

def getComment(db: Session, commentId: int):
    return db.query(models.Comment).filter(models.Comment.id == commentId).first()

def getComments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def createComment(db: Session, comment: schemas.CommentCreate):
    dbComment = models.Comment(**comment.model_dump())
    db.add(dbComment)
    db.commit()
    db.refresh(dbComment)
    return dbComment

def updateComment(db:Session, commentId: int, comment: schemas.CommentUpdate):
    dbComment = getComment(db, commentId)
    if dbComment:
        if dbComment.owner_id != comment.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in comment.model_dump().items():
            setattr(dbComment, key, value)
        db.commit()
        db.refresh(dbComment)
    return dbComment



def deleteComment(db: Session, commentId: int):
    dbComment = getComment(db, commentId)
    if dbComment:
        db.delete(dbComment)
        db.commit()
    return dbComment


def getRating(db: Session, ratingId: int):
    return db.query(models.Rating).filter(models.Rating.id == ratingId).first()

def getRating(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rating).offset(skip).limit(limit).all()


def createRating(db: Session, rating: schemas.RatingCreate):
    dbRating = models.Rating(**rating.model_dump())
    db.add(dbRating)
    db.commit()
    db.refresh(dbRating)
    return dbRating

def updateRating(db: Session, ratingId: int, rating: schemas.RecipeUpdate):
    dbRating = db.query(models.Recipe).filter(models.Rating.id == ratingId).first()
    if dbRating:
        if dbRating.owner_id != rating.owner_id:
            raise HTTPException(status_code=403, detail="Not authorized to update this recipe")
        for key, value in rating.model_dump().items():
            setattr(dbRating, key, value)
        db.commit()
        db.refresh(dbRating)
    return dbRating

def deleteRating(db: Session, ratingId: int):
    dbRating = getRating(db, ratingId)
    if dbRating:
        db.delete(dbRating)
        db.commit()
    return dbRating

def createUser(db: Session, user: schemas.UserCreate):
    dbUser = models.User(**user.model_dump())
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return dbUser


