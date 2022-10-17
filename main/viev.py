# Импортируем все необходимые пакеты и функции для обработки имеющихся постов
from flask import Blueprint, render_template, request
from utils import *

# Создаем блюпринт
main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='templates',
                           url_prefix='/')


# Создаем роут для блюпринта обрабатывающий форму страницы
@main_blueprint.route('/')
def main_index():
    posts = get_posts_all()
    return render_template('index.html',
                           posts=posts)

@main_blueprint.route('/post/<post_id>')
def view_post(post_id):
    """
    Достаем из URL аргументы "s" и осуществляет поиск поста
    Используя функция, перебирает все посты и ищем совпадения с "s"
    Возвращает "заполненную" страницу HTML
    """
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_count = len(comments)
    return render_template('post.html',
                           post=post,
                           comments=comments,
                           comments_count=comments_count)

@main_blueprint.route('/search/<query>')
def search_by_substr(query):
    query_params = query
    found_posts = search_for_posts(query)
    count_found_posts = len(found_posts)
    return render_template('search.html',
                           found_posts=found_posts,
                           count_found_posts=count_found_posts,
                           query_params=query_params)

@main_blueprint.route('users/<username>')
def viev_posts_by_username(username):
    name = username
    posts = get_posts_by_user(username)
    return render_template('user-feed.html',
                           posts=posts,
                           name=name)
  
