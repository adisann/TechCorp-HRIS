from huey.contrib.djhuey import task
from .methods import process_payrolls

@task()
def process_payrolls_task():
    process_payrolls()