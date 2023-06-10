import datetime

class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.creation_time = datetime.datetime.now()

    def __str__(self):
        return f'{self.content} - by {self.author} {self.creation_time}'

class Notebook:
    def __init__(self):
        self.notes = []

    def add_new_note(self, author, content):
        self.notes.append(Note(author, content))

    def add_existing_note(self, note):
        self.notes.append(note)

    def get_notes_number(self):
        return len(self.notes)

    def show_all_notes(self):
        if len(self.notes) == 0:
            print('The notebook is empty')
        else:
            for note in self.notes:
                print(note)

def main():
    some_notebook = Notebook()
    some_notebook.show_all_notes()
    print(some_notebook.get_notes_number())
    some_note = Note('John', 'The first note')
    some_notebook.add_existing_note(some_note)
    some_notebook.add_new_note('John', 'The second note')
    some_notebook.show_all_notes()
    print(some_notebook.get_notes_number())

if __name__ == '__main__':
    main()
