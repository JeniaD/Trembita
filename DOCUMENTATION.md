# Документація
Цей документ пояснює використання деяких частей коду задля полегшення розробки

## API endpoints
- `/register`
- `/login`
- `/post`
- `/like`
- `/unlike`

| Ендпоінт | Методи | Параметри | Повертає | Опис |
|---|---|---|---|---|
| `api/register` | POST | name, username, password, email | `access_token` | Реєстрація в Трембіті (буде змінено) |
| `api/login` | POST | username, password | `access_token` | Вхід в обліковий запис |
| `api/post` | POST | content | `201 {"message": "success"}` | Опублікувати октаву |
| `api/like` | POST | postID | `201 {"message": "success"}` чи `404 {"message": "Post not found"}` | Залишити лайк на октаві |
| `api/unlike` | POST | postID | `201 {"message": "success"}` чи `404 {"message": "Post not found"}` | Прибрати лайк з октави |
