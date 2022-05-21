import pytest
from app.main.dao.posts_dao import PostsDAO

posts_dao = PostsDAO("app/main/data/data.json")

def test_posts_type():
    """Проверка типа всех постов"""
    assert type(posts_dao.get_all()) == list, "Это не список!"


posts_keys_names = ["poster_name",
                    "poster_avatar",
                    "pic",
                    "content",
                    "views_count",
                    "likes_count",
                    "pk"]

def test_posts_keys_names():
    """Тест кол-ва и имен ключей"""
    for post in posts_dao.get_all():
        give_post_len = len(post.keys())
        true_post_len = len(posts_keys_names)
        assert give_post_len == true_post_len, "Ошибка в кол-ве ключей"
        assert set(post.keys()) == set(posts_keys_names), "Ошибка в названии ключей!"



posters_names = ["hank","larry","johnny","noname"]

@pytest.mark.parametrize("poster_name", posters_names)
def test_post_type_by_user(poster_name):
    """Проверка типа постов владельцем которых являеся user_name"""
    assert type(posts_dao.get_by_user(poster_name)) == list, "Это не список!"



posts_pk = [(-3,False),
            ("1",False),
            (2,True),
            ("three",False),
            (4.56,False),
            (0,False),
            (9000000,False),
            (1,True)]

@pytest.mark.parametrize("pk, is_correct", posts_pk)
def test_post_by_pk(pk, is_correct):
    """Проверка типа постов по pk и результатов выполнения"""
    assert type(posts_dao.get_by_pk(pk)) == dict, "Это не словарь!"
    assert bool(posts_dao.get_by_pk(pk)) == is_correct, "Не совпадают результаты!"

