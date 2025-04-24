# 🐍 Qalalab Server (Django Backend)

Это серверная часть проекта **Qalalab**, созданная на Django 3.2.6. Backend отвечает за обработку данных и взаимодействие с фронтендом на React.

## 📦 Стек технологий

- Python 3.9+
- Django 3.2.6
- SQLite (по умолчанию)
- Gunicorn (для продакшена)
- WhiteNoise (для обслуживания статических файлов)
- Docker / Docker Compose

---

## ⚙️ Установка (локально)

### 1. Клонируйте проект
```bash
git clone https://your-repo-url.com/qalalab_server.git
cd qalalab_server
```

### 2. Создайте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Выполните миграции
```bash
python manage.py migrate
```

### 5. Запустите сервер разработки
```bash
python manage.py runserver
```

Доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Запуск через Docker

### 1. Соберите и запустите контейнеры
```bash
docker-compose up --build
```

### 2. Приложение будет доступно:
- Backend (Django): [http://localhost:8000](http://localhost:8000)

---

## 📁 Структура проекта

```
qalalab_server/
├── blog/                 # Приложение "Блог"
├── qalalab_server/       # Основной конфиг проекта
├── db.sqlite3            # База данных SQLite (по умолчанию)
├── manage.py             # Стартовый файл Django
└── requirements.txt      # Python зависимости
```

---

## 📄 Переменные окружения

Вы можете настроить переменные через `.env` или `docker-compose.yml` при необходимости:

- `DEBUG` — режим отладки (`True` / `False`)
- `SECRET_KEY` — секретный ключ Django
- `ALLOWED_HOSTS` — список разрешённых хостов
- `DATABASE_URL` — строка подключения к БД (если используется PostgreSQL)

---

## 📝 Полезные команды

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

---

## 📦 Сборка фронтенда (React)

Фронтенд находится в директории `qalalab-ui`. Он собирается с помощью:

```bash
cd qalalab-ui
npm install
npm run build
```

Результат попадет в `qalalab-ui/build`, откуда и обслуживается Django.

---

## 📬 Контакты

Разработчик: Мурат  
Email: [murat.kosshi@gmail.com](mailto:example@example.com)