# Документація
Цей документ пояснює використання деяких частей коду задля полегшення розробки
## Web endpoints
- `/home`
- `/profile`
- `/trending`
- `/notifications`
- `/other`
- `/messages`
- `/profile/<username>`
- `/post`
- `/subscribe`
- `/uploads/avatars/<filename>`
- `/uploads/<filename>`
- `/login`
- `/register`
- `/logout`

## `base.html`
Шаблон `base.html` це базовий шаблон, на якому базується відображання сторінок.
### Блоки
Назва сторінки
```html
{% block title %} Трембіта {% endblock title %}
```

"Шапка" сторінки
```html
{% block navbar %} ... {% endblock navbar %}
```

Посилання в "шапці"
```html
{% block navbarLinks %}
<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>
<a href="#" class="w3-bar-item w3-button w3-padding-large w3-theme-d4"><i class="fa fa-home w3-margin-right"></i>Trembita</a>
<a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white" title="News"><i class="fa fa-globe"></i></a>
<a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white" title="Account Settings"><i class="fa fa-user"></i></a>
<a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white" title="Messages"><i class="fa fa-envelope"></i></a>
{% endblock navbarLinks %}
```

Сповіщення в "шапці"
```html
{% block navbarNotifications %}
<a href="#" class="w3-bar-item w3-button">One new friend request</a>
<a href="#" class="w3-bar-item w3-button">John Doe posted on your wall</a>
<a href="#" class="w3-bar-item w3-button">Jane likes your post</a>
{% endblock navbarNotifications %}
```

Кількість сповіщень в "шапці"
```html
{% block notificationsCount %}{% endblock notificationsCount %}
```

Мобільна "шапка"
```html
{% block mobileNavbar %}
<div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 1</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 2</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 3</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">My Profile</a>
</div>
{% endblock mobileNavbar %}
```
