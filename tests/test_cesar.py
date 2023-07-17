import pytest
from operations.cesar import get_list_of_signs, cesar_cypher


@pytest.mark.parametrize(
    "idx, expected_sign",
    [
        (0, "a"),
        (10, "k"),
        (25, "z"),
        (26, "A"),
        (36, "K"),
        (51, "Z"),
        (52, "0"),
        (57, "5"),
        (61, "9"),
    ],
)
def test_should_return_correct_sign_for_index(idx, expected_sign):
    signs = get_list_of_signs()
    assert signs[idx] == expected_sign


@pytest.mark.parametrize(
    "text, shift, expected_enscription",
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
def test_should_return_enscripted_text(text, shift, expected_enscription):
    actual_enscription = cesar_cypher(text, shift, "fake_history_file.db")
    assert actual_enscription == expected_enscription


@pytest.mark.parametrize(
    "text, shift, expected_enscription",
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
def test_should_return_descripted_text(text, shift, expected_enscription):
    actual_enscription = cesar_cypher(text, shift, "fake_history_file.db", False)
    assert actual_enscription == expected_enscription
