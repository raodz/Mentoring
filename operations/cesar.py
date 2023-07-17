import string
from itertools import cycle
from operations.db_functions import add_to_history


def get_list_of_signs():
    letters = string.ascii_letters
    digits = "0123456789"
    signs = list(letters + digits)
    return signs


signs = get_list_of_signs()


def cesar_cypher(txt: str, shift: int, history_file: str, encrypting=True) -> str:
    """Use mode = 1 if you want to enscript txt and mode = -1 if you want to
    descript txt"""
    mode = 1
    mode_name = "encrypting"
    if not encrypting:
        mode = -1
        mode_name = "decrypting"
    signs = get_list_of_signs()
    shifted_txt = ""
    for sign in txt:
        if sign in signs:
            try:
                shifted_sign = signs[signs.index(sign) + shift * mode]
            except IndexError:
                shifted_sign = signs[signs.index(sign) + (shift - len(signs)) * mode]
        else:
            shifted_sign = sign
        shifted_txt += shifted_sign
    add_to_history(
        history_file,
        f"'{txt}'",
        f"'{str(shift)}'",
        f"'{mode_name}'",
        f"'{shifted_txt}'",
    )
    return shifted_txt
