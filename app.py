# Импортируем необходимые библиотеки и блюпринты
from flask import Flask, send_from_directory, render_template


from main.viev import main_blueprint


# Передаем в переменную файл с постами и папку
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
# Регистрируем блюпринты
app.register_blueprint(main_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.errorhandler(404)
def page_not_found(e):
    return f"Код 404"

@app.errorhandler(500)
def page_not_found(e):
    return f"Код 500"

app.run(debug=True)

