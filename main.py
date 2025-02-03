class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # Статус задачи (False - не выполнена, True - выполнена)

    def mark_completed(self):
        self.completed = True  # Отметить задачу как выполненную

    def __str__(self):
        status = "✅ Выполнено" if self.completed else "❌ Не выполнено"
        return f"{self.description} (Срок: {self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: {description}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.")
        else:
            print("Некорректный номер задачи.")

    def show_tasks(self):
        print("\nСписок текущих задач:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
        print()

    def show_pending_tasks(self):
        print("\nСписок невыполненных задач:")
        pending_tasks = [task for task in self.tasks if not task.completed]
        if not pending_tasks:
            print("Все задачи выполнены!")
        else:
            for i, task in enumerate(pending_tasks):
                print(f"{i + 1}. {task}")
        print()


# Тестовый интерфейс через консоль
def start_task_manager():
    manager = TaskManager()

    while True:
        print("\nМенеджер задач:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать все задачи")
        print("4. Показать только невыполненные задачи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения: ")
            manager.add_task(description, deadline)

        elif choice == "2":
            manager.show_tasks()
            try:
                index = int(input("Введите номер задачи, которую нужно отметить как выполненную: ")) - 1
                manager.mark_task_completed(index)
            except ValueError:
                print("Ошибка: Введите корректный номер.")

        elif choice == "3":
            manager.show_tasks()

        elif choice == "4":
            manager.show_pending_tasks()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Ошибка: Неверный выбор, попробуйте снова.")


start_task_manager()
