class Task:
    id_counter = 1

    def __init__(self, title, description=''):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.description = description
        self.completed = False