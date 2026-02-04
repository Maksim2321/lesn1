import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# ===== capitalize =====

def test_capitalize_positive(utils):
    """Позитив: обычная строка"""
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_with_numbers(utils):
    """Позитив: строка с цифрами"""
    assert utils.capitalize("123test") == "123test"


def test_capitalize_empty_string(utils):
    """Негатив: пустая строка"""
    assert utils.capitalize("") == ""


def test_capitalize_none(utils):
    """Негатив: None"""
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ===== trim =====

def test_trim_positive(utils):
    """Позитив: удаление пробелов в начале"""
    assert utils.trim("   skypro") == "skypro"


def test_trim_without_spaces(utils):
    """Позитив: строка без пробелов"""
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces(utils):
    """Негатив: строка из одних пробелов"""
    assert utils.trim("   ") == ""


def test_trim_none(utils):
    """Негатив: None"""
    with pytest.raises(AttributeError):
        utils.trim(None)


# ===== contains =====

def test_contains_positive(utils):
    """Позитив: символ есть в строке"""
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative(utils):
    """Негатив: символа нет в строке"""
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string(utils):
    """Негатив: пустая строка"""
    assert utils.contains("", "a") is False


def test_contains_none(utils):
    """Негатив: None"""
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# ===== delete_symbol =====

def test_delete_symbol_single_char(utils):
    """Позитив: удаление одного символа"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring(utils):
    """Позитив: удаление подстроки"""
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found(utils):
    """Негатив: символ не найден"""
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_none(utils):
    """Негатив: None"""
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
