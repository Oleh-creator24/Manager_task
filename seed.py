from datetime import datetime, timedelta
import random
from faker import Faker
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Manager_task.settings")
django.setup()

from django.utils import timezone
from Task.models import Task
from SubTask.models import SubTask
from Category.models import Category

fake = Faker()


def clear_data():
    """Очистка существующих данных"""
    SubTask.objects.all().delete()
    Task.objects.all().delete()
    Category.objects.all().delete()
    print("Старые данные очищены")


def create_categories():
    """Создание категорий"""
    categories = []

    for _ in range(10):
        cat = Category.objects.create(
            name=fake.unique.word(),
            description=fake.text(max_nb_chars=200)
        )
        categories.append(cat)

    print(f"Созданы категории: {len(categories)}")
    return categories


def create_tasks(categories):
    """Создание задач"""
    tasks = []

    for _ in range(20):
        task = Task.objects.create(
            title=fake.sentence(nb_words=4)[:199],
            description=fake.text(max_nb_chars=500),
            status=random.choice(['todo', 'in_progress', 'done']),
            due_date=timezone.now() + timedelta(days=random.randint(1, 30))
        )
        tasks.append(task)

    print(f"Созданы задачи: {len(tasks)}")
    return tasks


def create_subtasks(tasks):
    """Создание подзадач"""
    subtasks = []

    for task in tasks:
        for _ in range(random.randint(1, 4)):
            subtask = SubTask.objects.create(
                title=fake.sentence(nb_words=3)[:199],
                description=fake.text(max_nb_chars=300),
                task=task,
                is_completed=random.choice([True, False])
            )
            subtasks.append(subtask)

    print(f"Созданы подзадачи: {len(subtasks)}")
    return subtasks


def main():
    """Основная функция"""
    print("Начало заполнения базы данных...")

    # Очистка старых данных
    clear_data()

    # Создание данных
    categories = create_categories()
    tasks = create_tasks(categories)
    subtasks = create_subtasks(tasks)

    print("База данных успешно заполнена!")
    print(
        f"Итого: {Category.objects.count()} категорий, {Task.objects.count()} задач, {SubTask.objects.count()} подзадач")


if __name__ == "__main__":
    main()