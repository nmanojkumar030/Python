from datetime import datetime
# import time
from time import sleep
import random


odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]


for i in range(5):
    right_this_time = datetime.today().minute

    if right_this_time in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    sleep_time = random.randint(1,60)
    sleep(sleep_time)
