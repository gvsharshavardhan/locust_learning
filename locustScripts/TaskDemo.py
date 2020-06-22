from locust import task, constant, User


def task1(userclass):
    print("task 1")


def task2(userclass):
    print("task 2")


class TaskTest(User):
    wait_time = constant(1)
    tasks = {task1: 1, task2: 4}
