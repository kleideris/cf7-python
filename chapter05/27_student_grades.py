students = {
    'Alice': [85, 92, 100],
    # 'Bob': [],
    'Bob': [90, 72, 80],
    'Charlie': [90, 95, 94],
    'Diana': [95, 98, 100],
    'Eve': [50, 60, 55]
}

def main():
    while True:
        try:
            threshold = int(input("Please insert a threshold (int): "))
            if threshold == 0:
                break
        except ValueError:
            print("Invalid input.")
            continue
        average_grades = {
            student: round(sum(grades) / len(grades), 2)
            for student, grades in students.items()
            if grades and sum(grades) / len(grades) > threshold  # TODO na dw an douleyei me or!
            }
        
        for student, avg_grade in average_grades.items():
            print(f"{student}: {avg_grade}")

if __name__ == "__main__":
    main()    