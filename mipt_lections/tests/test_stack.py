import pytest
from mipt_lections.stack.stack import Stack


@pytest.fixture(scope="module")
def create_stack():
    stack = Stack()
    yield stack


def test_stack(create_stack):
    stack = create_stack
    stack.clear()

    assert stack.is_empty()

    stack.push(8)
    stack.push(2)
    stack.push(7)

    assert not stack.is_empty()
    assert stack.top() == 7
    assert stack.len() == 3
    assert stack.pop() == 7
    assert stack.pop() == 2
    assert stack.pop() == 8
    assert stack.len() == 0
    assert stack.is_empty()
