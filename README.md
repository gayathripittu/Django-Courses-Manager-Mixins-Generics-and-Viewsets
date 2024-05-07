# Django Courses Management System

## Project Overview

This Django Courses Management System is a web application that manages course details efficiently. It showcases three different approaches provided by Django REST Framework (DRF) — Mixins, Generics, and Viewsets — to build APIs. This project demonstrates code reusability and efficient data handling across three separate implementations, each utilizing different aspects of the framework.


## Three Architectural Approaches:

### 1. Mixins
In the Mixins approach (`Mixins_Views.py`),  multiple mixin classes are used in combination with `generics.GenericAPIView` to build the API views. This approach provides great flexibility as it allows for mixing and matching different functionalities to create highly customized views without much standard code.

- **CourseList**:
  Uses mixins to list all courses and to add a new course.
  - Combines `ListModelMixin` and `CreateModelMixin` to respectively list and create courses.
  - Methods: `get` for listing courses, post for creating a new course.
- **Course Detail**:
  - Uses RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin for fetching, updating, and deleting courses, respectively.
  - Methods: get for retrieving a course detail, put for updating a course, delete for deleting a course.

### 2. Generics 
The Generics approach (`Generics_Views.py`) uses pre-built views provided by DRF, making it easier to create web APIs without writing a lot of code. It helps reduce repetition and makes maintaining the code simpler.

- **CourseList**:
  Uses mixins to list all courses and to add a new course.
  - **CourseList**:
    - Inherits from ListCreateAPIView, facilitating the listing of courses and creation of new courses.

- **Course Detail**:
  - Inherits from `RetrieveUpdateDestroyAPIView` for handling the retrieve, update, and delete operations of a course through a single class
    
  

### 3. Viewsets 
In the Viewsets approach (`Viewsets_Views.py`), the `ModelViewSet` is utilized, which is a highly concise way to create an API that allows for all CRUD operations without explicitly defining method handlers for get, post, put, and delete.
- **CourseView**:
  - Inherits from `ModelViewSet` which automatically provides **`list`**, **`create`**, **`retrieve`**, **`update`**, and **`destroy`** actions.
  - Reduces the amount of code by handling all actions through a single class.

## API Endpoints

Each part of the system has its own endpoints:

### Mixins
- **List/Create Courses**: `GET` and `POST` `/courses/`
- **Retrieve/Update/Delete a Course**: `GET, PUT, DELETE` `/courses/<id>/`


### Generics
- **List/Create Courses**: `GET` and `POST` `/courses/`
- **Retrieve/Update/Delete a Course**: `GET, PUT, DELETE` `/courses/<id>/`

### Viewsets
- All CRUD operations: `/courses/` (with appropriate HTTP methods)

