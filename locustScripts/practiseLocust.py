from locust import User, constant, task


class MyMobileUser(User):
    wait_time = constant(1)

    def on_start(self):
        print("starting")

    def on_stop(self):
        print("stoping")

    @task
    def mobileUser1(self):
        print("mobile user1")


class MyWebUser(User):
    wait_time = constant(1)

    def on_start(self):
        print("starting 2")

    def on_stop(self):
        print("stoping 2")

    @task
    def webUser1(self):
        print("web user1")
