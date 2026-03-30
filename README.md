# 🚀 Task Management System (FastAPI + JWT Authentication)

A scalable backend system built using FastAPI that allows users to manage tasks efficiently with secure authentication.

---

## 🔥 Features

* User Signup & Login (JWT Authentication)
* Secure Password Hashing
* Create, Update, Delete Tasks
* Get All Tasks / Filter by Status
* Protected Routes (Only Authenticated Users)
* RESTful API Design
* Modular Backend Architecture

---

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite / PostgreSQL
* JWT (Authentication)
* Passlib (Password Hashing)

---

## 📂 Project Structure

```
task-manager/
│── main.py
│── models.py
│── schemas.py
│── crud.py
│── database.py
│── auth.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/task-management-system-fastapi.git
cd task-management-system-fastapi
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
```

### 4. Run the Server

```
uvicorn main:app --reload
```

---

## 🌐 API Documentation

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

1. Signup → `/signup`
2. Login → `/login` → Get JWT Token
3. Click **Authorize** in Swagger UI
4. Use token → Access protected APIs

---

## 📌 Sample API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /signup     | Register user |
| POST   | /login      | Login user    |
| POST   | /tasks      | Create task   |
| GET    | /tasks      | Get all tasks |
| PUT    | /tasks/{id} | Update task   |
| DELETE | /tasks/{id} | Delete task   |

---

## 🎯 Key Highlights

* Designed scalable backend using FastAPI
* Implemented JWT authentication and secure APIs
* Built modular architecture (models, schemas, CRUD)
* Used SQLAlchemy ORM for efficient DB operations

---

## 👨‍💻 Author

Gubbala P V Durga Malleswara Rao
📧 [gubbalapavan9347@gmail.com](mailto:gubbalapavan9347@gmail.com)
🔗 GitHub: https://github.com/yourusername
