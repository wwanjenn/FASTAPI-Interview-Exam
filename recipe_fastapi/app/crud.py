from sqlalchemy.orm import Session
import models, schemas

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
        for key, value in recipe.model_dump().items():
            setattr(dbRecipe, key, value)
        db.commit()
        db.refresh(dbRecipe)
    return dbRecipe

def deleteRecipe(db: Session, recipeId: int):
    dbRecipe = getRecipe(db, recipeId)
    if dbRecipe:
        db.delete(dbRecipe)
    return dbRecipe
