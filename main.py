import os
from operations.cesar import Cypher


class Facade:
    def __init__(self):
        self.__is_running = True
        self.choices = {
            "1": self._single_encrypt,
            "2": self._single_decrypt,
            "3": self._multiple_encrypt,
            "4": self._multiple_decrypt,
            "5": self._show_history,
            "9": self._end_program,
        }
        self._no_path = True

        # pomysł: zamiast od razu zapisywać do pliku, tworzyć najpierw tabelę w Pythonie
        # i na koniec ją opcjonalnie przepisywać do pliku

        while self._no_path:
            self.history = input(
                "Provide a path to the history file or press "
                "ENTER to create a new one"
            )
            if os.path.isfile(self.history) or self.history == "":
                self._no_path = False
        if self.history == "":
            self.history = Cypher.create_history()

        self._loop()

    def _loop(self):
        while self.__is_running:
            self._show_menu()
            self._get_and_execute_choice()

    def _show_menu(self):
        menu = (
            "Welcome to Cesar 1.0!\n"
            "1. Encrypt single text\n"
            "2. Decrypt single text\n"
            "3. Encrypt many texts from .json file\n"
            "4. Decrypt many texts from .json file\n"
            "5. Show history\n"
        )
        print(menu)

    def _get_and_execute_choice(self):
        user_choice = input("Choose a mode")

        self.choices.get(user_choice, self._show_error)()

    def _show_error(self):
        print("Incorrect choice - Try again!")

    def _single_encrypt(self):
        original_txt = input("Provide the text to encrypt")
        shift = int(input("Provide the shift of the encryption"))
        shifted_txt = Cypher().cesar(original_txt, shift, history_file=self.history)
        # problem: operacja nie dodaje się do historii, mimo że w samym cesar.py działa
        print(f"{original_txt} shifted by {shift}: {shifted_txt}")

    def _single_decrypt(self):
        original_txt = input("Provide the text to decrypt")
        shift = int(input("Provide the shift of the decryption"))
        shifted_txt = Cypher().cesar(
            original_txt, shift, encrypting_mode=False, history_file=self.history
        )
        print(f"{original_txt} shifted back by {shift}: {shifted_txt}")

    def _multiple_encrypt(self):
        file_path = input("Provide the file path")
        Cypher().crypt_from_json(file_path, history_file=self.history)

    def _multiple_decrypt(self):
        file_path = input("Provide the file path")
        Cypher().crypt_from_json(
            file_path, encrypting_mode=False, history_file=self.history
        )

    def _show_history(self):
        pass

    def _end_program(self):
        # pytasz uzywtnika czy zapisac historie (Y/n)
        # KOmunikat jakis

        self.__is_running = False


def main():
    Facade()


if __name__ == "__main__":
    main()
