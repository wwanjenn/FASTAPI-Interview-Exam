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

@router.post("/ratings/", response_model= schemas.Rating)
def createRating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.createRating(db= db, rating= rating)

@router.get("/ratings/", response_model= list[schemas.Rating])
def readRating(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.getRatings(db, skip= skip, limit = limit)

@router.get("/ratings/{ratingId}", response_model= list[schemas.Rating])
def readRating(ratingId: int, db: Session = Depends(get_db)):
    dbRating = crud.getRating(db, ratingId= ratingId)
    if dbRating is None:
        raise HTTPException(status_code= 404, detail = "Rating not found")
    return dbRating

@router.put("/ratings/{ratingId}", response_model= list[schemas.Rating])
def updateRating(ratingId: int, rating: schemas.ratingUpdate, db: Session = Depends(get_db)):
    dbRating = crud.updateRating(db, ratingId= ratingId, rating= rating)
    if dbRating is None:
        raise HTTPException(status_code= 404, detail = "Rating not found")
    return dbRating

@router.delete("/ratings/{ratingId}", response_model= list[schemas.Rating])
def deleteRating(ratingId: int, db: Session = Depends(get_db)):
    dbRating = crud.deleteRating(db, ratingId= ratingId)
    if dbRating is None:
        raise HTTPException(status_code= 404, detail = "Rating not found")
    return dbRating

##########################################################################################################

@router.post("/comments/", response_model= schemas.Comment)
def createComment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.createComment(db= db, comment= comment)

@router.get("/comments/", response_model= list[schemas.Comment])
def readComments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.getComments(db, skip= skip, limit = limit)

@router.get("/comments/{commentId}", response_model= list[schemas.Comment])
def readComment(commentId: int, db: Session = Depends(get_db)):
    dbComment = crud.getComment(db, commentId= commentId)
    if dbComment is None:
        raise HTTPException(status_code= 404, detail = "Comment not found")
    return dbComment

@router.put("/comments/{commentId}", response_model= list[schemas.Comment])
def updateComment(commentId: int, comment: schemas.CommentUpdate, db: Session = Depends(get_db)):
    dbComment = crud.updateComment(db, commentId= commentId, comment= comment)
    if dbComment is None:
        raise HTTPException(status_code= 404, detail = "Comment not found")
    return dbComment

@router.delete("/comments/{commentId}", response_model= list[schemas.Comment])
def deleteComment(commentId: int, db: Session = Depends(get_db)):
    dbComment = crud.deleteComment(db, commentId= commentId)
    if dbComment is None:
        raise HTTPException(status_code= 404, detail = "Comment not found")
    return dbComment