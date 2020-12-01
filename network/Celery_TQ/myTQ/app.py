from celery import Celery

app = Celery('app',
             broker='amqp://10.19.17.188:5673',
             backend='redis://10.19.17.188:6379',
             )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

@app.task
def add(x, y):
    return (x + y)*2

