# Документація
Цей документ пояснює використання деяких частей коду задля полегшення розробки

## API endpoints
- `/register`
- `/login`
- `/post`
- `/like`
- `/unlike`
- `/users/*`

| Ендпоінт | Методи | Параметри | Повертає | Опис | Необхідна авторизація |
|---|---|---|---|---|---|
| `api/users/username/*` | GET | - | `name`, `username`, `about`, `creationDate`, `active`, `private`, `following`, `followers` | Інформація про користувача з ніком... |&#10004;|
| `api/users/id/*` | GET | - | `name`, `username`, `about`, `creationDate`, `active`, `private`, `following`, `followers` | Інформація про користувача з ID... |&#10004;|
| `api/register` | POST | name, username, password, email | `access_token` | Реєстрація в Трембіті (буде змінено) |&#10004;|
| `api/login` | POST | username, password | `access_token` | Вхід в обліковий запис |&#10004;|
| `api/post` | POST | content | `{"message": "success"}` | Опублікувати октаву |&#10004;|
| `api/like` | POST | postID | `{"message": "success"}` | Залишити лайк на октаві |&#10004;|
| `api/unlike` | POST | postID | `{"message": "success"}` | Прибрати лайк з октави |&#10004;|

## Status codes
- 201 - успішний запит
- 404 - сторінку не знайдено
