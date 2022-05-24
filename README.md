# abz_agency DRF

Tasks: https://drive.google.com/file/d/1qUzx0m_Koj83k_G8BScCNK7opazbuDzk/view 

# Задачи

1. База данных PostreSQL, находится в docker контейнере.
2. Иерархия сотрудников выводится в древовидной форме. url: */staff/tree
3. Доступно приложение Должности. url: */position_at_work
4. Заполнение базы данных записями. 50_000 сотрудников, 5 должностей.
5. Список всех сотрудников, продумано ограничение количества пользователей на страницу (pagination) . url: */staff
6. Добавлена возможность сортировки, поиска и фильтрации на странице всех сотрудников.
7. Создано приложение для аутентификации пользователя, регистрации и разграничением доступа по правам, изначально у пользователей доступены все права.
8. Сделаны crud операции для приложения сотрудники, должности.
9. Есть возможность загружать фотографию сотрудника, на фотографию сотрудника накладывается водяной знак в виде мниатюрной фотографии сотрудника.
10. При удалении карточки начальника, его подчиненные распределеяются на другого пользователя с такой же должность.
11. Настроен swagger. url: */swagger
12. Сделана Django admin panel
13. Написаны тесты
