from apscheduler.schedulers.background import BackgroundScheduler
import time
def job():
    print('μΌνλμ€',str(time.localtime().tm_hour))
sched = BackgroundScheduler()
sched.start()
sched.add_job(job,'interval',second=3,id='test_1')

while True:
    print('running main process.......')
    time.sleep(1)