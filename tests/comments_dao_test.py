import pytest
from app.main.dao.comments_dao import CommentsDAO

comments_dao = CommentsDAO("app/main/data/comments.json")
comments_keys_names = ["post_id","commenter_name","comment","pk"]

def test_comments_type():
    """Тест по типу list"""
    assert type(comments_dao.get_all()) == list, "Это не список!"



def test_comments_keys_names():
    """Тест кол-ва и имен ключей"""
    for comment in comments_dao.get_all():
        give_comment_len = len(comment.keys())
        true_comment_len = len(comments_keys_names)
        assert give_comment_len == true_comment_len, "Ошибка в кол-ве ключей"
        assert set(comment.keys()) == set(comments_keys_names), "Ошибка в названии ключей!"


posts_id = ["1",2,"three",4.05,0,-1,9999999]

@pytest.mark.parametrize("post_id", posts_id)
def test_comments_by_post_id(post_id):
    for comment in comments_dao.get_by_post_id(post_id):
        assert comment["post_id"] == post_id