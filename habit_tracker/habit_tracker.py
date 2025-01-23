import json
from datetime import datetime, timedelta


class HabitTracker:
    def __init__(self, filename='habits.json'):
        self.filename = filename
        self.habits = self.load_habits()

    def load_habits(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_habits(self):
        with open(self.filename, 'w') as file:
            json.dump(self.habits, file)

    def add_habit(self, habit):
        if habit not in self.habits:
            self.habits[habit] = []
            self.save_habits()
            print(f"Привычка '{habit}' добавлена.")
        else:
            print(f"Привычка '{habit}' уже существует.")

    def track_habit(self, habit):
        if habit in self.habits:
            self.habits[habit].append(datetime.now().strftime('%Y-%m-%d'))
            self.save_habits()
            print(f"Вы отметили выполнение привычки '{habit}' на сегодня.")
        else:
            print(f"Привычка '{habit}' не найдена.")

    def show_habits(self):
        for habit, dates in self.habits.items():
            print(f"{habit}: {len(dates)} выполнений ({', '.join(dates)})")


if __name__ == "__main__":
    tracker = HabitTracker()

    while True:
        print("1. Добавить привычку")
        print("2. Отметить выполнение привычки")
        print("3. Показать привычки")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            habit = input("Введите название привычки: ")
            tracker.add_habit(habit)
        elif choice == '2':
            habit = input("Введите название привычки для отметки: ")
            tracker.track_habit(habit)
        elif choice == '3':
            tracker.show_habits()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
