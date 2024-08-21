# Импортируем класс Flask из модуля flask
from flask import Flask

# Создаем экземпляр приложения Flask
# Аргументом передается имя текущего модуля (__name__),
# это необходимо для правильной настройки путей и ресурсов в приложении
app = Flask(__name__)

# Используем декоратор @app.route для создания маршрута
# Этот маршрут будет сопоставлен с корневым URL ('/')
@app.route('/')
def home():
    # Функция, которая выполняется, когда пользователь переходит на корневой URL
    # Возвращает строку 'Hello, Flask!' в качестве ответа
    return 'Hello, Flask!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'


# Проверяем, запущен ли этот файл как основной (а не импортирован как модуль)
# Если это так, запускаем встроенный сервер Flask
if __name__ == '__main__':
    # Запускаем приложение Flask в режиме отладки (debug=True)
    # В режиме отладки сервер будет автоматически перезапускаться при изменении кода
    app.run(debug=True)
