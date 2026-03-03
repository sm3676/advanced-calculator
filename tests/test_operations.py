import pytest
from app.operations import OperationFactory


@pytest.mark.parametrize(
    "operation, a, b, expected",
    [
        ("add", 5, 3, 8),
        ("subtract", 5, 3, 2),
        ("multiply", 5, 3, 15),
        ("divide", 6, 3, 2),
        ("power", 2, 3, 8),
        ("modulus", 5, 2, 1),
        ("int_divide", 7, 2, 3),
        ("percent", 50, 100, 50),
        ("abs_diff", 10, 3, 7),
    ],
)
def test_operations(operation, a, b, expected):
    op = OperationFactory.create(operation)
    result = op.execute(a, b)

    assert result == expected


def test_root_operation():
    op = OperationFactory.create("root")
    result = op.execute(27, 3)

    assert result == 3


def test_divide_by_zero():
    op = OperationFactory.create("divide")

    with pytest.raises(Exception):
        op.execute(5, 0)


def test_invalid_operation():
    with pytest.raises(Exception):
        OperationFactory.create("unknown")