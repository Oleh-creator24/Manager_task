from django.db import models

class Category(models.Model):
    """Категория задачи"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """Задача для выполнения"""

    class Status(models.TextChoices):
        NEW = "New", "New"
        IN_PROGRESS = "In progress", "In progress"
        PENDING = "Pending", "Pending"
        BLOCKED = "Blocked", "Blocked"
        DONE = "Done", "Done"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="tasks", blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "created_at"],
                name="unique_task_title_per_date",
            )
        ]

    def __str__(self):
        return f"{self.title} ({self.status})"
