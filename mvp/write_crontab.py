from crontab import CronTab

cron = CronTab(user='anderson')

jobs = cron.find_comment('show dir and user')

for job in jobs:
    cron.remove(job)
    print(job.command)

job = cron.new(command='echo `date`: basedir $PWD - user `whoami` >> /tmp/cron.txt', comment="show dir and user")
job.minute.every(1)
cron.write()