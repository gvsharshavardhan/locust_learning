from locust import User, task, between, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("connecting to db")


@events.test_stop.add_listener
def script_stop(**kwargs):
    print("disconnecting to db")


class MyUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("i am loggin in!!")

    @task
    def do_task(self):
        print("i am learing locust!!")

    def on_stop(self):
        print("i am logging out!!")
