#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import FastAPI, File, UploadFile, Form, Body
import os
from orchestrator import Course

app = FastAPI()

@app.post("/generate-course")
async def add_course(course_data: dict = Body(...)):
    course_title = course_data.get("course_title")
    course_topic = course_data.get("course_topic")
    Course(department_id=department_id, course_title=course_title, course_id=course_id, url_name=url_name, course_topic=course_topic)
    return {"message": "Course added successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)


