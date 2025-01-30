# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date, status):
        self.description = description
        self.due_date = due_date
        self.status = status

    def add_task(self):
        self.description = input("Введите описание задачи: ")
        self.due_date = input("Введите срок выполнения задачи: ")

    def mark_completed(self):
        self.status = False

    def list_current_tasks(self):
        for task in tasks:
            if self.status == True:
                print(f"Описание задачи: {self.description}")
                print(f"Срок выполнения задачи: {self.due_date}")


tasks = []

while True:
    print("1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Показать список текущих задач")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = Task("", "", True)
        task.add_task()
        tasks.append(task)
    elif choice == "2":
        task.mark_completed()
    elif choice == "3":
        task.list_current_tasks()
    elif choice == "4":
        break



