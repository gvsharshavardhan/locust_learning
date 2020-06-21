locust -f locustScripts/basic_locust_weight_02.py -u 4 -r 1 -t 10s --headless --logfile logfiles/mylog.l
og --loglevel DEBUG


-u : no of users
-r : ramping users per second
-t : time till the test run
--headless : runs without opening ui
--logfile : logging in to a file
--loglevel : level at which logs need to be recorded
--only-summary : prints only tasks stmts
