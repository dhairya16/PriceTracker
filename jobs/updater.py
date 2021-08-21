from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_db_update

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_db_update, 'interval', minutes=1)
	scheduler.start()