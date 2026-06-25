from fastapi import FastAPI,HTTPException,status
from schemas import StudentCreate,StudentResponse
from data import students

app=FastAPI()


@app.get("/")
def root():
    return{
        "message":"Student API Running"
    }

@app.post("/students",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
def new_student(student:StudentCreate):

    new_id=len(students)+1

    new_student=StudentResponse(
        id=new_id,
        name=student.name,
        age=student.age,
        email=student.email 
          )
    students.append(new_student)
    return new_student