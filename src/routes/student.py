from fastapi import APIRouter, status, Depends, HTTPException
from src.db.database import get_db
from src.models.student import StudentResponse
from src.db.models import Student
from sqlalchemy.orm import Session
from src.core.exceptions import NotFoundError

router = APIRouter(tags=["Student"], prefix="/students")

@router.get("/", status_code=status.HTTP_200_OK)
def get_students(db: Session= Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get("/{student_id}", status_code=status.HTTP_200_OK)
def get_students(student_id: int, db: Session= Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise NotFoundError(error_msg="Student with id {student_id} not found")
    
    return student