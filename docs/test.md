# Тестування працездатності системи

## Звіт підготовлений на основі взаємодії з Data

## Короткий зміст

- [Тестування працездатності системи](#тестування-працездатності-системи)
- [GET](#get)
- [POST](#post)
- [PUT](#put)
- [DELETE](#delete)
- [PATCH](#patch)

### GET

Get-запит на отримання всіх даних
![](../test/images/getData.jpg)

Get-запит на отримання даних за id
![](../test/images/getDataId.jpg)

### POST
Post-запит на додавання даних з усіма заповненими полями
![](../test/images/Filled_Post.jpg)

Post-запит на додавання даних без id, upload_date, last_edit_date

*Примітка. Полю id призначено autoincrement, поле upload_date за замовчуванням отримує поточні дату та час, а поле last_edit_date за замовчуванням має значення null.*
![](../test/images/NoIdPost.jpg)

### PUT
Put-запит на оновлення id, name, description

*Дані категорії до оновлення*
![](../test/images/GetForPut.jpg)

*Оновлення даних категорії*
![](../test/images/put.jpg)

### DELETE
Delete-запит на видалення категорії

*Перевірка існування категорії*
![](../test/images/getForDelete.jpg)

*Видалення категорії*
![](../test/images/delete.jpg)

*Перевірка видалення категорії*
![](../test/images/Delete_approved.jpg)

### PATCH
Patch-запит на оновлення id

*Оновлення id*
![](../test/images/PatchName.jpg)

















