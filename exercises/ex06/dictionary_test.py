"""Test my functions."""
__author__ = "730707593"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_empty_invert() -> None:
    """Test when dictionary is empty."""
    assert invert({}) == {}


def test_invert() -> None:
    """Test invert function."""
    dict1 = {"a": "b", "c": "d"}
    assert invert(dict1) == {"b": "a", "d": "c"}


def test_invert2() -> None:
    """Test invert function."""
    dict7 = {"Yaodan": "4.0", "T": "S"}
    assert invert(dict7) == {"4.0": "Yaodan", "S": "T"}


def test_empty_count() -> None:
    """Test when dictionary is empty."""
    dict10 = {}
    assert count(dict10) == {}


def test_count() -> None:
    """Test count function."""
    result6 = count(["Danny", "Suni"])
    assert count(result6) == {"Danny": 1, "Suni": 1}


def test_count2() -> None:
    """Test count function."""
    result1 = count(["D", "A", "N"])
    assert count(result1) == {"D": 1, "A": 1, "N": 1}


def test_empty_color() -> None:
    """Test when dictionary is empty."""
    assert favorite_color({}) == ""


def test_color() -> None:
    """Test favorite_color function."""
    dict2 = {"Mark": "blue", "Kris": "blue", "Anna": "green"}
    assert favorite_color(dict2) == "blue"


def test_color2() -> None:
    """Test favorite_color function."""
    dict6 = {"A": "red", "B": "red", "C": "orange"}
    assert favorite_color(dict6) == "red"


def test_empty_alpha() -> None:
    """Test when dictionary is empty."""
    assert alphabetizer({}) == {}


def test_alpha() -> None:
    """Test alphabetizer function."""
    result2 = alphabetizer(["apple", "air", "art", "cat", "car"])
    assert result2 == {"a": ["apple", "air", "art"], "c": ["cat", "car"]}


def test_alpha2() -> None:
    """Test alphabetizer function."""
    result8 = alphabetizer(["apple", "air", "blue", "bob"])
    assert result8 == {"a": ["apple", "air"], "b": ["blue", "bob"]}


def test_empty_att() -> None:
    """Test when dictionary is empty."""
    dict11 = {"": [""]}
    assert update_attendance(dict11, "", "") == {"": ["", ""]}


def test_attendance1() -> None:
    """Test update_attendance function."""
    dict19 = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    result10 = update_attendance(dict19, "Friday", "Jenny")
    assert result10 == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Friday": ["Jenny"]}


def test_attendance2() -> None:
    """Test update_attendance function."""
    dict9 = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    result = update_attendance(dict9, "Wednesday", "Tom")
    assert result == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Tom"]}