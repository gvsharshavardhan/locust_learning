from locust import HttpUser, between, task, SequentialTaskSet


class UserBehavious(SequentialTaskSet):
    @task
    def launchURL(self):
        with self.client.get("/mercurysignon.php", name="launch", catch_response=True) as resplaunch:
            # print(respLaunch.text)
            # print(respLaunch.status_code)
            # print(respLaunch.headers)
            print("resplaunch : " + resplaunch.text)
            if ("Mercury Tours") in resplaunch.text:
                resplaunch.success()
            else:
                resplaunch.failure("failed to launch")

    @task
    def login(self):
        with self.client.post("/login.php", name="login", data={"action": "process",
                                                                "userName": "qamile1@gmail.com",
                                                                "password": "qamile",
                                                                "login.x": "34",
                                                                "login.y": "11"}, catch_response=True) as respLogin:
            if ("Find a Flights") in respLogin:
                respLogin.success()
            else:
                respLogin.failure("failed to login")

        # print(respLogin.text)
        # print(respLogin.status_code)
        # print(respLogin.headers)


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com"
    tasks = [UserBehavious]
