import json
import os

FILE_NAME = "student_marks.json"
SUBJECTS = ["English", "Physics", "Chemistry", "Mathematics", "Optional Subject"]


def get_valid_marks(prompt, max_value):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= max_value:
                return value
            print(f"Please enter a value between 0 and {max_value}.")
        except ValueError:
            print("Please enter a valid integer.")


def load_records():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_records(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


def main():
    student_records = load_records()

    while True:
        student_name = input("\nEnter student name (or type 'exit' to finish): ").strip()

        if student_name.lower() == "exit":
            break

        student_data = {}

        for subject in SUBJECTS:
            internal = get_valid_marks(f"Enter {subject} internal marks (out of 20): ", 20)
            final = get_valid_marks(f"Enter {subject} final exam marks (out of 80): ", 80)

            total = internal + final
            student_data[subject] = {
                "internal": internal,
                "final": final,
                "total": total
            }

        student_records[student_name] = student_data
        save_records(student_records)

        print(f"\nMarks for {student_name}:")
        overall_total = 0

        for subject, marks in student_data.items():
            print(f"{subject}: {marks['total']}/100")
            overall_total += marks['total']

        print(f"Overall total: {overall_total}/500")
        print(f"Saved successfully to {FILE_NAME}")

    print("\nAll saved records:")
    print(json.dumps(student_records, indent=4))


if __name__ == "__main__":
    main()