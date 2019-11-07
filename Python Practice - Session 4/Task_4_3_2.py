import csv


def record_acording_to_age(file_path: str) -> None:
    """Receives the file path with srudents info and writes CSV student
       information to the new file in descending order of age.
    """
    with open(file_path) as input_file,\
         open('students_acording_to_age.csv', 'w') as output_file:
        reader = csv.DictReader(input_file)
        students = sorted(list(reader), key=lambda x: x['age'], reverse=True)

        writer = csv.DictWriter(output_file, delimiter=',', fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    record_acording_to_age('data/students.csv')
