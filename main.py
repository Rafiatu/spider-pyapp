# Show examples of how you would use ALL your implementations here
# first import all necessary dependencies.
from celery import Celery
from src.db import DB
from src.spider import scrape
from decouple import config


# database = DB()
# database.connect()
# database.connect()
# database.setup()
# database.seed()
print(scrape(1))
#
# app = Celery('main', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'))
#
# @app.task
# def test():
#   return scrape(2)
