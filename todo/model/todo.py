class Todo:
    def __init__(self, code_int, tittle, description):
        """Este es el constructor que crea y recibe la informacion sobre la tarea/objeto Todo"""
        self.completed: bool = False
        self.code_id: int = code_int
        self.tittle: str = tittle
        self.description: str = description
        self.tags: list[str] = []

    """Esta funcion marca como completdo el objeto Todo"""

    def mark_completed(self):
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

    def add_todo(self, tittle: str, description: str) -> int:
        # Generar un id que sea igual al número de elementos en el diccionario todos más uno.
        identificativo: int = len(self.todos) + 1
        # Crear un objeto de la clase Todo
        objeto = Todo
        # Agregar el objeto de la clase Todo al diccionario utilizando como clave el id generado
        self.todos[identificativo] = objeto(identificativo, tittle, description)  # diccionario["clave"] = valor(_init_)
        # Retornar el id
        return identificativo

    """ 
       En la clase TodoBook, defina un método de instancia pending_todos que retorne una lista de objetos de la clase 
       Todo. En el cuerpo del método, utilice un list comprehension para crear una lista con todos los objetos del 
       diccionario todos que tienen el atributo completed con valor False.
       """

    def pending_todos(self) -> list[Todo]:
        return [i for i in self.todos.values() if not i.completed]

    def completed_todos(self) -> list[Todo]:
        return [i for i in self.todos.values() if i.completed]

    """ En la clase TodoBook, defina un método de instancia tags_todo_count el cual retorna un diccionario donde las 
    claves son string y los valores enteros. 
    En el cuerpo del método implemente un algoritmo para construir un diccionario que indique, por cada tag,
    cuántos objetos Todo tienen dicho tag asignado."""

    def tags_todo_count(self) -> dict[str, int]:
        diccionario: dict[str:int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag not in diccionario.keys():
                    diccionario[tag] = 1
                else:
                    diccionario[tag] += 1
        return diccionario
