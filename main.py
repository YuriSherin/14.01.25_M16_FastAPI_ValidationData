from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()     # Создаем объект класса FastAPI



@app.get('/')
async def read_http_main() -> str:
    """Маршрутизация - корневой каталог"""
    message = {'http_main': 'Главная страница'}
    return message['http_main']


@app.get('/user/admin')
async def read_admin() -> str:
    """Маршрутизация - каталог /user/admin"""
    message = {'admin':'Вы вошли как администратор'}
    return message['admin']


@app.get('/user/{user_id}')
async def read_user(user_id:Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> str:
    """Маршрутизация с динамическим параметром и валидацией возвращаемых данных"""
    users = {'user_name': f'Вы вошли как пользователь № {user_id}'}
    return users['user_name']


@app.get('/user/{username}/{age}')
async def read_user_info(username:Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                         age:Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    """Маршрутизация с динамическими параметрами и валидацией возвращаемых данных"""
    user_info = {'username': username, 'age': age}
    return f'Информация о пользователе. Имя: {user_info["username"]}, Возраст: {user_info["age"]}'
