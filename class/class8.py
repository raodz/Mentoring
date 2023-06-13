from datetime import datetime, timedelta


class Case:
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%S+00:00'

    def __init__(self, name, created_task, end_task):
        self.name = name
        self.created_task = created_task
        self.end_task = end_task

    def retrieve_seconds(self) -> timedelta:
        start = datetime.strptime(self.created_task, self.TIME_FORMAT)
        # kwestia +00:00
        try:
            end = datetime.strptime(self.end_task, self.TIME_FORMAT)
        except TypeError:
            end = datetime.now()

        return end - start


def main():
    first_case = {
        'name': 'first_case',
        'created_task': '2021-10-26T19:48:12+00:00',
        'end_task': None
    }

    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }

    for data in [first_case, second_case]:
        case = Case(data['name'], data['created_task'], data['end_task'])
        print(case.retrieve_seconds())


if __name__ == '__main__':
    main()
