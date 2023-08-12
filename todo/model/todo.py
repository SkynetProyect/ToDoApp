class Todo:
    completed: bool = False
    tags: list[str, None]

    def __init__(self, code_int, tittle, description):
        self.code_id: int = code_int
        self.tittle: str = tittle
        self.description: str = description

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag in self.tags:
            pass
        else:
            self.tags.append(tag)

    def __str__(self):
        return [f"{self.code_id} - {self.tittle}"]


class TodoBook:

    def __init__(self):
        self.todos = {int: Todo}  # Ahora es de tipo diccionario

    def add_todo(self, tittle: str, description: str):
        identificativo: int = len(self.todos) + 1
        objeto = Todo()
        self.todos[identificativo] = objeto  # diccionario["clave"] = valor
        return identificativo

    def pending_todos(self):
        pass

    def completed_todos(self):
        pass

    def tags_todo_count(self):
        pass