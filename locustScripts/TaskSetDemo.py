from locust import TaskSet, task, constant, User

"""
approach one 1
"""

#
#
# class mytasks(TaskSet):
#
#     @task
#     def task1(self):
#         print("task 1")
#
#     @task
#     def task2(self):
#         print("task 2")
#
#
# class mobileUser(User):
#     wait_time = constant(1)
#     tasks = [mytasks]

"""
approach two 2
"""


class mobileUser(User):
    wait_time = constant(1)

    @task
    class mytasks(TaskSet):

        @task
        def task1(self):
            print("task 1")

        @task
        def task2(self):
            print("task 2")
