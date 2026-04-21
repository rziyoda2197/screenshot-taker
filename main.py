import heapq

class Task:
    def __init__(self, id, priority, deadline):
        self.id = id
        self.priority = priority
        self.deadline = deadline

class PriorityQueueTaskManager:
    def __init__(self):
        self.tasks = []
        self.task_ids = {}

    def add_task(self, id, priority, deadline):
        task = Task(id, priority, deadline)
        heapq.heappush(self.tasks, (-priority, deadline, id))
        self.task_ids[id] = task

    def remove_task(self, id):
        if id in self.task_ids:
            del self.task_ids[id]
            self.tasks = [(priority, deadline, id) for priority, deadline, id in self.tasks if id != id]
            heapq.heapify(self.tasks)

    def get_next_task(self):
        if self.tasks:
            _, deadline, id = heapq.heappop(self.tasks)
            return self.task_ids[id]
        else:
            return None

    def update_task_priority(self, id, new_priority):
        if id in self.task_ids:
            task = self.task_ids[id]
            self.remove_task(id)
            self.add_task(id, new_priority, task.deadline)

    def update_task_deadline(self, id, new_deadline):
        if id in self.task_ids:
            task = self.task_ids[id]
            self.remove_task(id)
            self.add_task(id, task.priority, new_deadline)

    def print_tasks(self):
        for priority, deadline, id in self.tasks:
            print(f"Task {id} - Priority: {-priority}, Deadline: {deadline}")

# Test
task_manager = PriorityQueueTaskManager()
task_manager.add_task(1, 3, 5)
task_manager.add_task(2, 2, 3)
task_manager.add_task(3, 1, 1)
task_manager.print_tasks()
print(task_manager.get_next_task().id)
task_manager.update_task_priority(2, 4)
task_manager.print_tasks()
print(task_manager.get_next_task().id)
task_manager.update_task_deadline(3, 10)
task_manager.print_tasks()
print(task_manager.get_next_task().id)
```

Bu kodda biz quyidagilar qilamiz:

- `Task` classi tasklarni ifodalaydi, ularning id, priority va deadlinelari mavjud.
- `PriorityQueueTaskManager` classi tasklarni qayta tartiblash uchun priority queuedan foydalanadi. U quyidagi metodlarni qo'llaydi:
  - `add_task`: taskni qo'shish uchun
  - `remove_task`: taskni o'chirish uchun
  - `get_next_task`: quyidagi taskni qaytarish uchun
  - `update_task_priority`: taskning priorityini yangilash uchun
  - `update_task_deadline`: taskning deadlineini yangilash uchun
  - `print_tasks`: tasklarni chiqarish uchun

Kodni test qilish uchun biz quyidagilar qilamiz:

- `task_manager` obyektini yaratamiz
- 3 ta taskni qo'shamiz
- Tasklarni chiqaramiz
- Quyidagi taskni qaytarib olamiz
- Taskning priorityini yangilaymiz
- Tasklarni chiqaramiz
- Quyidagi taskni qaytarib olamiz
- Taskning deadlineini yangilaymiz
- Tasklarni chiqaramiz
