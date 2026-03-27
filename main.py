from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas, crud
import auth


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Create Task
@app.post("/tasks", response_model=schemas.TaskResponse)
def create(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# ✅ Get All Tasks
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_all(status: str = None, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    if status:
        tasks = [t for t in tasks if t.status == status]
    return tasks


# ✅ Get Task by ID
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_one(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ✅ Update Task
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


# ✅ Delete Task
@app.delete("/tasks/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user, auth)

@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.username, user.password, auth)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username = payload.get("sub")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

@app.post("/tasks")
def create(task: schemas.TaskCreate,
           db: Session = Depends(get_db),
           user: str = Depends(get_current_user)):
    return crud.create_task(db, task)
