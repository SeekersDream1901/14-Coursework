import pytest
from utils import get_posts_by_user


poster_name_parameters = [
    ("leo", [{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
              'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwa'
                     'G90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
              'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог!'
                         ' Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем '
                         'это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они '
                         'на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, '
                         'дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь '
                         'изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы '
                         'совсем неинтересно.', 'views_count': 376, 'likes_count': 154, 'pk': 1},
             {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
              'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlf'
                     'Hx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
              'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это '
                         'я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики '
                         '#инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты '
                         'понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
              'views_count': 287, 'likes_count': 99, 'pk': 5}]),
    ("larry", [{'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
                'pic': 'https://images.unsplash.com/photo-1581235854265-41981cb85c88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MH'
                       'xwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
                'content': 'Утром проснулся раньше всех – вижу у бассейна на вешалке висит оранжевое пальто. О, думаю'
                           ' – как это мое пальто за мной забралось так далеко – за целых 5000 километров. Присмотрелся'
                           ' – а это зонтик. И как только успел его сюда притащить! За завтраком сижу напротив своего'
                           ' попутчика, и все не решаюсь спросить его: «Может быть, мы все-таки не попутчики? Может, '
                           'нам надо разъехаться в разные стороны? Вы не боитесь, что я сейчас сбегу?». Он не боится. '
                           'Он вообще ничего не боится, кроме одного – когда у него в машине не работает сигнализация. '
                           'А если она не работает, то он садится в машину и продолжает идти своим путем.',
                'views_count': 366, 'likes_count': 198, 'pk': 4},
               {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
                'pic': 'https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wY'
                       'WdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
                'content': 'Утром отправились на катере обследовать ближайшие острова – острова в основном каменные,'
                           ' бесполезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан.'
                           ' В течение 10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, '
                           'держась за трос. Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже'
                           ' прибыли домой, я попросил, чтобы на следующий день нам устроили на катере экскурсию по '
                           'морю. Нас провели по морскому дну от одного острова к другому, показали различные '
                           'интересные объекты, которые встречаются в этом районе.',
                'views_count': 141, 'likes_count': 45, 'pk': 8}]
     )
]

poster_name_exceptions = [
    ("", ValueError),
    ("qw", ValueError)
]


@pytest.mark.parametrize('poster_name, output', poster_name_parameters)
def test_get_posts_by_user_by_parameters(poster_name, output):
    assert get_posts_by_user(poster_name) == output, f"Ошибка для {poster_name}"


@pytest.mark.parametrize('poster_name, output', poster_name_exceptions)
def test_get_posts_by_user_by_exceptions(poster_name, output):
    with pytest.raises(output):
        get_posts_by_user(poster_name), f"Ошибка для {poster_name}"
