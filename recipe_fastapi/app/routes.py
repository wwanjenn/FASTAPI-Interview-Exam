from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter()

@router.post("/recipes/", response_model= schemas.Recipe)
def createRecipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.createRecipe(db= db, recipe= recipe)

@router.get("/recipes/", response_model= list[schemas.Recipe])
def readRecipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.getRecipes(db, skip= skip, limit = limit)

@router.get("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def readRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.getRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.put("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def updateRecipe(recipeId: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    dbRecipe = crud.updateRecipe(db, recipeId= recipeId, recipe= recipe)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.delete("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def deleteRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.deleteRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

###########################################################################################################

@router.post("/recipes/", response_model= schemas.Recipe)
def createRecipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.createRecipe(db= db, recipe= recipe)

@router.get("/recipes/", response_model= list[schemas.Recipe])
def readRecipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.getRecipes(db, skip= skip, limit = limit)

@router.get("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def readRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.getRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.put("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def updateRecipe(recipeId: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    dbRecipe = crud.updateRecipe(db, recipeId= recipeId, recipe= recipe)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.delete("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def deleteRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.deleteRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

##########################################################################################################

@router.post("/recipes/", response_model= schemas.Recipe)
def createRecipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.createRecipe(db= db, recipe= recipe)

@router.get("/recipes/", response_model= list[schemas.Recipe])
def readRecipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.getRecipes(db, skip= skip, limit = limit)

@router.get("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def readRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.getRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.put("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def updateRecipe(recipeId: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    dbRecipe = crud.updateRecipe(db, recipeId= recipeId, recipe= recipe)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe

@router.delete("/recipes/{recipeId}", response_model= list[schemas.Recipe])
def deleteRecipe(recipeId: int, db: Session = Depends(get_db)):
    dbRecipe = crud.deleteRecipe(db, recipeId= recipeId)
    if dbRecipe is None:
        raise HTTPException(status_code= 404, detail = "Recipe not found")
    return dbRecipe
