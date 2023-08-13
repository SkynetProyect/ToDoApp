class Todo:
    completed: bool = False
    tags: list[str, None]

    def __init__(self, code_int, tittle, description):
        """Este es el constructor que crea y recibe la informacion sobre la tarea/objeto Todo"""
        self.code_id: int = code_int
        self.tittle: str = tittle
        self.description: str = description

    def mark_completed(self):
        """Esta funcion marca como completdo el objeto Todo"""
        self.completed = True

    def add_tag(self, tag: str):
        """ Esta funcion recibe en "tag" un string, revisa si ese tag ya se encuentra en la lista de tags,
        y segun esto la agrega a la lista.  Asi tags solo contiene una lista de tareas diferentes"""

        if tag in self.tags:  # confirma si ya esta en la lista
            pass
        else:
            self.tags.append(tag)  # agrega a la lista

    def __str__(self):
        """Esta funcion retorna el codigo ID y el titulo del objeto Todo"""
        return [f"{self.code_id} - {self.tittle}"]


class TodoBook:

    def __init__(self):
        self.todos: dict[int:Todo] = {}  # Ahora es de tipo diccionario

    def add_todo(self, tittle: str, description: str):
        identificativo: int = len(self.todos) + 1
        objeto = Todo
        self.todos[identificativo] = objeto(identificativo, tittle, description)  # diccionario["clave"] = valor(_init_)
        return identificativo

    def pending_todos(self):
        _lista: list[Todo] = []
        ''' Atributo completed con valor falso, del diccionario todos, formar lista.'''

        for iterador in self.todos:
            if not self.todos[iterador].completed:
                _lista.append(self.todos[iterador])
            else:
                pass
        return _lista

    def completed_todos(self):
        _lista: list[Todo] = []
        ''' Atributo completed con valor true de objeto todo, del diccionario todos, formar lista.'''

        for iterador in self.todos:
            if self.todos[iterador].completed:
                _lista.append(self.todos[iterador])
            else:
                pass
        return _lista

    def tags_todo_count(self):
        temporal = self.todos
        diccionario: dict[str:int] = {}

        for iterador in temporal:
            for i in temporal[iterador].tags:
                conteo: int = 0
                if i not in diccionario:
                    for secundario in temporal:
                        if temporal[iterador] == temporal[secundario]:
                            pass
                        else:
                            for j in temporal[secundario].tags:
                                if i == j:
                                    conteo += 1
                                else:
                                    pass
                else:
                    pass
                diccionario[i] = conteo
            del temporal[iterador]
        return diccionario
