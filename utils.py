import json


def get_posts_all(path='data/posts.json'):
    """
    Загружает все посты из имеющихся и возвращает их
    :param path: Файл JSON
    :return: Все имеющиеся посты в JSON
    """
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(poster_name):
    """
    Возвращает посты определенного пользователя.
    Вызывает ошибку ValueError если такого пользователя нет или список пуст, если у пользователя нет постов.
    """
    posts_found = []
    all_posts_in_file = get_posts_all()

    for post in all_posts_in_file:
        if poster_name.lower() == post['poster_name'].lower():
            posts_found.append(post)
        elif poster_name == "":
            raise ValueError('Введена пустая строка')

    if len(posts_found) == 0:
        raise ValueError('У пользователя нет постов или пользователя не существует')

    return posts_found


def load_all_comments(path='data/comments.json'):
    """
    Читает файл с комментариями.
    Возвращает все комментарии.
    """
    with open(path, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return comments


def get_comments_by_post_id(post_id):
    """
    Возвращает комментарии определенного поста.
    Вызывает ошибку ValueError если такого поста нет и список пуст, если у поста нет комментариев.
    """
    found_comments = []
    all_comments = load_all_comments()

    for comment in all_comments:

        if int(post_id) == comment['post_id']:
            found_comments.append(comment)
        elif post_id == '':
            raise ValueError('Введена пустая строка')

    if len(found_comments) == 0:
        raise ValueError('Такого поста нет или комментарии отсутствуют')

    return found_comments


def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову.
    """
    found_posts = []
    posts = get_posts_all()

    for post in posts:
        if query.lower() in post["content"].lower().split():
            found_posts.append(post)

    return found_posts


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору.
    """
    posts = get_posts_all()

    for post in posts:
        if int(pk) == post["pk"]:
            return post
