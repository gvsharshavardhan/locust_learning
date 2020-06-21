from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)

    @task
    def login_url(self):
        print("i am learing locust!!")
