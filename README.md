# Japanese Courses School Platform

Платформа для изучения японского языка с системой личных кабинетов, загрузкой учебных материалов и комментированием курсов.

## Технологический стек
- **Backend**: Django 4.x
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Security**: Auth, File Management, SAST (Bandit)

## Инструкция по запуску
1. Клонируйте репозиторий:
   `git clone <ссылка>`
2. Создайте файл окружения:
   `cp .env.example .env`
3. Запустите проект:
   `docker-compose up --build`
4. Сайт доступен по адресу: `http://127.0.0.1:8000`