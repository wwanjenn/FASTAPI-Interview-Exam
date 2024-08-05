from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import get_db

router = APIRouter()

# Recipes Routes

@router.get("/recipes/{owner_id}/", response_model=list[schemas.Recipe])
def get_recipes_by_owner(owner_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Recipe).filter(models.Recipe.owner_id == owner_id).order_by(models.Recipe.created_at.desc()).offset(skip).limit(limit).all()

@router.post("/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    if recipe.owner_id is None:
        raise HTTPException(status_code=400, detail="Owner ID is required")
    return crud.create_recipe(db, recipe)

@router.get("/recipes/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recipes(db, skip=skip, limit=limit)

@router.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.get_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@router.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    db_recipe = crud.update_recipe(db, recipe_id=recipe_id, recipe=recipe)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@router.delete("/recipes/{recipe_id}", response_model=schemas.Recipe)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = crud.delete_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# Ratings Routes

@router.post("/ratings/", response_model=schemas.Rating)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.create_rating(db=db, rating=rating)

@router.get("/ratings/", response_model=list[schemas.Rating])
def read_ratings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_ratings(db, skip=skip, limit=limit)

@router.get("/ratings/{rating_id}", response_model=schemas.Rating)
def read_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.get_rating(db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

@router.put("/ratings/{rating_id}", response_model=schemas.Rating)
def update_rating(rating_id: int, rating: schemas.RatingUpdate, db: Session = Depends(get_db)):
    db_rating = crud.update_rating(db, rating_id=rating_id, rating=rating)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

@router.delete("/ratings/{rating_id}", response_model=schemas.Rating)
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.delete_rating(db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return db_rating

# Comments Routes

@router.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@router.get("/comments/", response_model=list[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_comments(db, skip=skip, limit=limit)

@router.get("/comments/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentUpdate, db: Session = Depends(get_db)):
    db_comment = crud.update_comment(db, comment_id=comment_id, comment=comment)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.delete("/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.delete_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

# User Routes

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
