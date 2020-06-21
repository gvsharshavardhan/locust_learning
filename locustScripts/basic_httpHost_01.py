from locust import HttpUser, task, between, constant, constant_pacing
from datetime import datetime


class MyUser(HttpUser):
    # wait_time = between(1, 2)
    wait_time = constant(3)

    host = "http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        # print("i am logging in!!")
        print(datetime.now())
