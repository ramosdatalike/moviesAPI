## API Movies and Persons

used libraries and frameworks:
- Django framework (I used this framework because is a full stack web framework and have a admin framework ready to use)
- Django REST Framework
(I used this because its updated regularly and generates HTML pages to browse and execute the API endpoints in development stage.) 
- coreapi (I used this dependency for the API documentation creator included with Django Rest framework)
- python-dotenv (I used this library for keeping the secret key and the enviroment configuration separeted in the server and the localhost)


## Installation:
``` 
pip3 install django 
pip3 install djangorestframework
pip3 install coreapi
pip3 install python-dotenv
```
## .env file
Create .env file in the root directory next ti 
Generate a SECRET_KEY with this website:
https://djecrety.ir/
and after that write inside .env file:
``` 
SECRET_KEY = '<GENERATED SECRET_KEY>'
DJANGO_DEBUG = True
```
## Run migrations and run server
``` 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
API Documentation: 
for full documentation after run the server go to url:
```
http://127.0.0.1:8000/docs/
```
![plot](./cine/documentation/1.png)
![plot](./cine/documentation/2.png)
![plot](./cine/documentation/3.png)
![plot](./cine/documentation/4.png)
![plot](./cine/documentation/5.png)

