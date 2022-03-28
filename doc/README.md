
# Инструкция по запуску предложения

- ## Клонирование проекта
  Убедитесь, что Python версии 3 установлен на вашем компьютере или ноутбуке.<br>
  Установка Python3 на [Windows](https://www.youtube.com/watch?v=IU4-19ofajg), []()
 	 <br>
  **Git clone** <br>
  `>>> git clone https://github.com/WayupKG/Digital-School.git`<br>
  `>>> cd Digital-School`
  
- ## Установка виртуального окружения
  Убедитесь, что virtualenv установлен на вашем компьютере или ноутбуке.<br>
  `>>> python3 -m venv venv`<br>
  `>>> source venv/bin/activate`
  
- ## Установка зависимостей
  Он установит все необходимые зависимости в проекте.<br>
  `>>> pip3 install -r req.txt`
  
- ## Создание вертуальных переменные
  Что бы указать секретные переменные откройте файл .env <br>
  
  
- ## Миграции 
  Для запуска миграций. <br>
  `>>> python3 manage.py makemigrations`<br>
  `>>> python3 manage.py migrate`
  
- ## Создание суперпользователя
  Для создания суперпользователя напишите команду. <br>
  `>>> python3 manage.py createsuperuser` <br>
  После выполнения этой команды она запросит имя пользователя и пароль.
  Вы можете получить доступ к панели администратора из `localhost:8000/admin/`

- ## Запуск проекта
   Он будет работать на порту 8000 по умолчанию.<br>
  `>>> python3 manage.py runserver` 
 
### Ссылка на сайт [Digital-School](http://web-code.online/)
