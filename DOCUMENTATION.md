# Документація
Цей документ пояснює використання деяких частей коду задля полегшення розробки

## API endpoints
- `/register`
- `/login`
- `/post`
- `/like`
- `/unlike`
- `/users/*`
- `/updateProfile`
- `/topPosts`

| Ендпоінт | Методи | Параметри | Повертає | Опис | Необхідна авторизація |
|---|---|---|---|---|---|
| `api/users/username/*` | GET | - | `name`, `username`, `about`, `creationDate`, `active`, `private`, `following`, `followers` | Інформація про користувача з ніком... |&#10004;|
| `api/users/id/*` | GET | - | `name`, `username`, `about`, `creationDate`, `active`, `private`, `following`, `followers` | Інформація про користувача з ID... |&#10004;|
| `api/register` | POST | name, username, password, email | `access_token` | Реєстрація в Трембіті (буде змінено) |\u274c|
| `api/login` | POST | username, password | `access_token` | Вхід в обліковий запис |\u274c|
| `api/post` | POST | content | `{"message": "success"}` | Опублікувати октаву |&#10004;|
| `api/like` | POST | postID | `{"message": "success"}` | Залишити лайк на октаві |&#10004;|
| `api/unlike` | POST | postID | `{"message": "success"}` | Прибрати лайк з октави |&#10004;|
| `api/updateProfile` | POST | name, username, about | `{"message": "success"}` | Змінити дані профілю. Поля, які не будуть змінені теж мають бути відправлені |&#10004;|
| `api/topPosts` | GET | - | Масив `{id, content, creationDate, likesCount}` | 50 популярних постів |&#10004;|

## Status codes
- 200, 201 - успішний запит
- 404 - сторінку не знайдено
