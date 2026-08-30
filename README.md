# 4 REST API

Django REST API สำหรับจัดการข้อมูลโรงเรียน ห้องเรียน ครู และนักเรียน โดยใช้ Django, Django REST Framework และ django-filter

## 1. Requirements

- Python 3.10 หรือสูงกว่า
- Git
- Virtual Environment (แนะนำ)

## 2. Clone Project

```bash
git clone https://github.com/prachotx/swd-backend-test-prachot-4.git
cd swd-backend-test-prachot-4
```

## 3. Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Database Migration

```bash
python manage.py migrate
```

## 5. Create Superuser (ถ้าต้องการใช้งาน admin)

```bash
python manage.py createsuperuser
```

## 6. Run Server

```bash
python manage.py runserver
```

## 7. API Endpoints

### School

```text
GET    /api/v1/schools/
GET    /api/v1/schools/<id>/
POST   /api/v1/schools/
PUT    /api/v1/schools/<id>/
PATCH  /api/v1/schools/<id>/
DELETE /api/v1/schools/<id>/
```

- Search by name: `/api/v1/schools/?search=โรงเรียน`

### Classroom

```text
GET    /api/v1/classrooms/
GET    /api/v1/classrooms/<id>/
POST   /api/v1/classrooms/
PUT    /api/v1/classrooms/<id>/
PATCH  /api/v1/classrooms/<id>/
DELETE /api/v1/classrooms/<id>/
```

### Teacher

```text
GET    /api/v1/teachers/
GET    /api/v1/teachers/<id>/
POST   /api/v1/teachers/
PUT    /api/v1/teachers/<id>/
PATCH  /api/v1/teachers/<id>/
DELETE /api/v1/teachers/<id>/
```

Filter ตัวอย่าง:

```text
/api/v1/teachers/?school=1
/api/v1/teachers/?classroom=2
/api/v1/teachers/?gender=F
```

### Student

```text
GET    /api/v1/students/
GET    /api/v1/students/<id>/
POST   /api/v1/students/
PUT    /api/v1/students/<id>/
PATCH  /api/v1/students/<id>/
DELETE /api/v1/students/<id>/
```

Filter ตัวอย่าง:

```text
/api/v1/students/?school=1
/api/v1/students/?classroom=2
/api/v1/students/?gender=M
```