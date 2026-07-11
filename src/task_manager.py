class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def create_task(self, title, description, priority="Média"):
        if not title:
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        task = {
            "id": self.counter,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "A Fazer"
        }
        self.tasks[self.counter] = task
        
        
        print(f"\n[CREATE] Nova carga adicionada: {task}")
        
        self.counter += 1
        return task

    def read_tasks(self):
        tasks_list = list(self.tasks.values())
        
        
        print(f"\n[READ] Listando todas as cargas do sistema: {tasks_list}")
        
        return tasks_list

    def update_status(self, task_id, new_status):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = new_status
            
            
            print(f"\n[UPDATE] Status da carga ID {task_id} alterado para: {new_status}")
            
            return self.tasks[task_id]
        raise KeyError("Tarefa não encontrada.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            removed = self.tasks.pop(task_id)
            
            
            print(f"\n[DELETE] Registro de carga ID {task_id} removido com sucesso!")
            
            return removed
        raise KeyError("Tarefa não encontrada.")