from fastapi import FastAPI,HTTPException,status
from schemas import StudentCreate,StudentResponse,StudentUpdate
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

@app.get("/students",response_model=list[StudentResponse],status_code=status.HTTP_200_OK)
def get_students():
    return students

@app.get(
        "/students/{student_id}",
        response_model=StudentResponse,
        status_code=status.HTTP_200_OK
)
def get_by_id(student_id:int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="student not found"
    )

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def update_student(student_id: int, student_data: StudentUpdate):
    for student in students:
        if student.id == student_id:

            update_data = student_data.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                setattr(student, key, value)

            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

@app.delete(
        "/students/{student_id}",
        status_code=status.HTTP_200_OK
)
def delete_student(student_id:int):
    for index,stud in enumerate(students):
        if student_id == stud.id:
            students.pop(index)

            return {
                "details":"student deleted successfully..."
                }
        
    raise HTTPException(
        status_code=404,
        detail="Student not found"
        )