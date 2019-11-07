import csv


def get_top_performers(file_path: str, number_of_top_students=5) -> None:
    """Receives file path and returns names of top performer students"""
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        students = [student['student name'] for student in sorted(list(reader),
                    key=lambda x: x['average mark'], reverse=True)]
        return students[:number_of_top_students]


if __name__ == "__main__":
    print(get_top_performers('data/students.csv'))
