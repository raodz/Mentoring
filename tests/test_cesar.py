import pytest
from operations.cesar import Cypher


@pytest.mark.parametrize(
    "text, shift, expected_enscryption",
    [
        ("Ala ma kota", 2, "Cnc oc mqvc"),
        ("Zalety i przywary", 4, "3epixC m tvDCAevC"),
        ("Zima 1999", 1, "0jnb 2aaa"),
        ("Idę na 100%!", 3, "Lgę qd 433%!"),
        ("Żółć", 14, "Żółć"),
        (" ", 5, " "),
        ("", 7, ""),
    ],
)
def test_should_return_enscrypted_text(text, shift, expected_enscryption):
    actual_enscryption = Cypher.cesar(text, shift, "fake_history_file.db")
    assert actual_enscryption == expected_enscryption


@pytest.mark.parametrize(
    "text, shift, expected_enscryption",
    [
        ("Cnc oc mqvc", 2, "Ala ma kota"),
        ("3epixC m tvDCAevC", 4, "Zalety i przywary"),
        ("0jnb 2aaa", 1, "Zima 1999"),
        ("Lgę qd 433%!", 3, "Idę na 100%!"),
        ("Żółć", 14, "Żółć"),
        (" ", 5, " "),
        ("", 7, ""),
    ],
)
def test_should_return_descrypted_text(text, shift, expected_enscryption):
    actual_enscryption = Cypher.cesar(text, shift, "fake_history_file.db", False)
    assert actual_enscryption == expected_enscryption


@pytest.mark.parametrize(
    "text, shift, expected_enscryption",
    [
        ("Ala ma kota", 2, "Cnc oc mqvc"),
        ("Zalety i przywary", 4, "3epixC m tvDCAevC"),
        ("Zima 1999", 1, "0jnb 2aaa"),
        ("Idę na 100%!", 3, "Lgę qd 433%!"),
        ("Żółć", 14, "Żółć"),
        (" ", 5, " "),
        ("", 7, ""),
    ],
)
def test_should_return_enscrypted_text_for_function_with_no_history(
    text, shift, expected_enscryption
):
    actual_enscryption = Cypher.cesar(text, shift)
    assert actual_enscryption == expected_enscryption
