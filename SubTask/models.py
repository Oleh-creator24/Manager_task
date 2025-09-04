from django.db import models

class SubTask(models.Model):
    """Отдельная часть основной задачи (Task)"""

    class Status(models.TextChoices):
        NEW = "New", "New"
        IN_PROGRESS = "In progress", "In progress"
        PENDING = "Pending", "Pending"
        BLOCKED = "Blocked", "Blocked"
        DONE = "Done", "Done"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    task = models.ForeignKey(
        "Task.Task",  # связь с основной задачей
        on_delete=models.CASCADE,
        related_name="subtasks"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} [{self.task.title}]"
