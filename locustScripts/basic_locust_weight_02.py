from locust import User, between, task, constant, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("connecting to db")


@events.test_stop.add_listener
def script_stop(**kwargs):
    print("disconnecting to db")


class MyWebUser(User):
    wait_time = constant(2)
    weight = 3

    def on_start(self):
        print("i am loggin into web!!")

    @task
    def task1_web(self):
        print("task 1 into web")

    @task
    def task2_web(self):
        print("task 2 into web")

    def on_stop(self):
        print("i am logging out from web!!")


class MyMobileUser(User):
    wait_time = constant(2)
    weight = 1

    def on_start(self):
        print("i am loggin into mobile!!")

    @task
    def task1_mobile(self):
        print("task 1 into mobile")

    @task
    def task2_mobile(self):
        print("task 2 into mobile")

    def on_stop(self):
        print("i am logging out from mobile!!")
