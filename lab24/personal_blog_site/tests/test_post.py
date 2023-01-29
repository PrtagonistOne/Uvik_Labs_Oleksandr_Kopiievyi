import pytest

from post.models import Comment
from post.validation.custom_validation import validate_comment_content


@pytest.mark.parametrize("comment, expected_resul", [
    (Comment(content='Shitty post!'), True),
    (Comment(content='Fuck'), True),
    (Comment(content='Fuck off!'), True),
])
def test_profanity_validation(comment, expected_resul):
    # given
    # when
    result = validate_comment_content(comment.content)
    # then
    assert result == expected_resul
