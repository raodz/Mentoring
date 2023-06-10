from datetime import datetime

class Case:
    first_case = {
        'name': 'first_case',
        'created_task': '2021-10-26T19:48:12+00:00',
        'end_task': None
    }

    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26 T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }

    def __init__(self):
        pass
        # self.name = name
        # self.created_task = created_task
        # self.end_task = end_task

    def retrieve_seconds(self, case):
        start = datetime.strptime(case['created_task'], '%H:%M:%S')
        if case['end_task'] == None:
            end = datetime.now()
        else:
            end = datetime.strptime(case['end_task'], '%H:%M:%S')
        return start - end

def main():
    some_case = Case()
    print(some_case)

if __name__ == '__main__':
    main()

# Do ogarnięcia