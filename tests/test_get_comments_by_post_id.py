import pytest
from utils import get_comments_by_post_id


# Тесты для функции get_comments_by_post_id(post_id)


integer_parameters_by_get_comments_by_post_id = [
    (1, [{'post_id': 1, 'commenter_name': 'hanna', 'comment': 'Очень здорово!', 'pk': 1},
         {'post_id': 1, 'commenter_name': 'jlia', 'comment': ':)', 'pk': 2},
         {'post_id': 1, 'commenter_name': 'ralf', 'comment': 'Класс!', 'pk': 3},
         {'post_id': 1, 'commenter_name': 'leo', 'comment': 'Интересно. А где это?', 'pk': 4}]),

    (2, [{'post_id': 2, 'commenter_name': 'johnny', 'comment': 'Класс!', 'pk': 5},
         {'post_id': 2, 'commenter_name': 'hank', 'comment': 'Хе хе !', 'pk': 6},
         {'post_id': 2, 'commenter_name': 'larry', 'comment': 'Забавное фото!', 'pk': 7},
         {'post_id': 2, 'commenter_name': 'leo', 'comment': 'Часть вижу такие фото у друзей! Это новый тренд?',
          'pk': 8}])
]

input_exceptions_by_get_comments_by_post_id = [
    ('', ValueError),
    (10, ValueError)
]


@pytest.mark.parametrize("post_id, output", integer_parameters_by_get_comments_by_post_id)
def test_get_comments_by_post_id_by_parameters(post_id, output):
    assert get_comments_by_post_id(post_id) == output, f"Ошибка для {post_id}"


@pytest.mark.parametrize("post_id, out", input_exceptions_by_get_comments_by_post_id)
def test_get_comments_by_post_id_by_exception(post_id, out):
    with pytest.raises(out):
        get_comments_by_post_id(post_id), f"Ошибка для {post_id}"
