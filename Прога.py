import datetime

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # "manager" or "employee"

class Task:
    def __init__(self, title, description, created_by):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_at = datetime.datetime.now()
        self.status = "Pending"
        self.completed_at = None

    def complete(self):
        self.status = "Completed"
        self.completed_at = datetime.datetime.now()

class TaskManager:
    def __init__(self):
        self.users = {}
        self.tasks = []
        self.current_user = None

    def register_user(self, username, password, role):
        if username in self.users:
            print("Пользователь с таким именем уже существует.")
            return
        self.users[username] = User(username, password, role)
        print(f"Пользователь {username} зарегистрирован.")

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print(f"Пользователь {username} успешно авторизован.")
            return True
        print("Неверное имя пользователя или пароль.")
        return False

    def add_task(self, title, description):
        if not self.current_user or self.current_user.role != "manager":
            print("Доступ запрещен. Только руководитель может добавлять задачи.")
            return
        task = Task(title, description, self.current_user.username)
        self.tasks.append(task)
        print(f"Задача '{title}' добавлена.")

    def assign_task(self, task_title, employee_username):
        if not self.current_user or self.current_user.role != "manager":
            print("Доступ запрещен. Только руководитель может выдавать задачи.")
            return
        for task in self.tasks:
            if task.title == task_title and task.status == "Pending":
                task.created_by = employee_username
                print(f"Задача '{task_title}' выдана сотруднику {employee_username}.")
                return
        print("Задача не найдена или уже выполнена.")

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title and task.created_by == self.current_user.username:
                task.complete()
                print(f"Задача '{task_title}' выполнена.")
                return
        print("Задача не найдена или не принадлежит вам.")

    def list_tasks(self):
        for task in self.tasks:
            print(f"Задача: {task.title}, Статус: {task.status}, Создана: {task.created_at}, Создатель: {task.created_by}")

    def report_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.status == "Completed"]
        for task in completed_tasks:
            print(f"Задача: {task.title}, Завершена: {task.completed_at}, Создатель: {task.created_by}")

def main():
    manager_username = "admin"
    manager_password = "admin"
    
    task_manager = TaskManager()
    task_manager.register_user(manager_username, manager_password, "manager")
    
    while True:
        print("\n1. Войти\n2. Зарегистрироваться\n3. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if task_manager.authenticate_user(username, password):
                while True:
                    if task_manager.current_user.role == "manager":
                        print("\n1. Добавить задачу\n2. Выдать задачу\n3. Вывести задачи\n4. Отчет о выполненных задачах\n5. Выйти")
                    else:
                        print("\n1. Просмотреть свои задачи\n2. Завершить задачу\n3. Выйти")
                    
                    action = input("Выберите действие: ")
                    
                    if action == "1" and task_manager.current_user.role == "manager":
                        title = input("Введите название задачи: ")
                        description = input("Введите описание задачи: ")
                        task_manager.add_task(title, description)
                    
                    elif action == "2" and task_manager.current_user.role == "manager":
                        title = input("Введите название задачи для выдачи: ")
                        employee_username = input("Введите имя сотрудника: ")
                        task_manager.assign_task(title, employee_username)

                    elif action == "1" and task_manager.current_user.role == "employee":
                        task_manager.list_tasks()

                    elif action == "2" and task_manager.current_user.role == "employee":
                        title = input("Введите название завершенной задачи: ")
                        task_manager.complete_task(title)

                    elif action == "4" and task_manager.current_user.role == "manager":
                        task_manager.report_completed_tasks()

                    elif action == "5":
                        break

                    else:
                        print("Некорректный выбор.")
        
        elif choice == "2":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль (manager/employee): ")
            task_manager.register_user(username, password, role)
        
        elif choice == "3":
            break

if __name__ == "__main__":
    main()