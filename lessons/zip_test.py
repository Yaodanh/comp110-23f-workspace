"""Test my zip function."""
__author__ = "730707593"

from lessons.zip import zip


def test_empty_sum() -> None:
    """Test when list is empty."""
    assert zip([], []) == {}


def test_equal_length_lists() -> None:
    """Test when both input lists have the same length."""
    result1 = zip(["a", "b", "c"], [1, 2, 3])
    assert result1 == {"a": 1, "b": 2, "c": 3}


def test_unequal_length_lists() -> None:
    """Test when input lists have different lengths."""
    result2 = zip(["a", "b"], [1, 2, 3])
    assert result2 == {}
