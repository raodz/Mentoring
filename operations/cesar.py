import string
import json
from datetime import datetime
from operations.db_functions import add_to_history

SIGNS = string.ascii_letters + string.digits


class Cypher:
    @staticmethod
    def create_history():
        time = str(datetime.now())
        chars_to_replace = [":", ".", " "]
        for char in chars_to_replace:
            time = time.replace(char, "-")
        history_name = "history" + time + ".db"
        return history_name

    def cesar(
        self,
        original_txt: str,
        shift: int,
        history_file: str,
        encrypting_mode: bool = True,
    ) -> str:
        # if not history_file:
        #     history_file = self.create_history()

        mode = 1 if encrypting_mode else -1
        mode_name = "encrypting" if encrypting_mode else "decrypting"

        shifted_txt = ""
        for sign in original_txt:
            if sign in SIGNS:
                try:
                    shifted_sign = SIGNS[SIGNS.index(sign) + shift * mode]
                except IndexError:
                    shifted_sign = SIGNS[
                        SIGNS.index(sign) + (shift - len(SIGNS)) * mode
                    ]
            else:
                shifted_sign = sign
            shifted_txt += shifted_sign

        add_to_history(
            history_file,
            f"'{original_txt}'",
            f"'{str(shift)}'",
            f"'{mode_name}'",
            f"'{shifted_txt}'",
        )
        return shifted_txt

    @staticmethod
    def crypt_from_json(
        file_path: str, history_file: str = None, encrypting_mode: bool = True
    ):
        if not history_file:
            history_file = "history" + str(datetime.now()) + ".db"
        with open(file_path) as file:
            data_to_crypt = json.load(file)
            for data in data_to_crypt:
                txt, shift = data.get("txt", ""), data.get("shift", 0)
                shifted_data = Cypher().cesar(
                    txt, shift, encrypting_mode=encrypting_mode
                )
                print(f"{txt} shifted by {shift}: " f"{shifted_data}")


# Cypher().cesar('Anna', 4, 'history2023-08-17-18-17-17-474637.db')
