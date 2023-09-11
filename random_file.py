import random
import logging

#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
logging.info(f"Random List : {randomlist}")
