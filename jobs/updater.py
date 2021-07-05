from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from jobs.jobs import scrape_schedule


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_schedule, 'interval', seconds=5, max_instances=2)
    scheduler.start()

