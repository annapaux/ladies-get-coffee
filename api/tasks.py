# tasks.py (Celery file)
import time
from celery import task

@task
def incredible_distributed(model_input):
    time.sleep(2)
    complex_result = model_input + "xyz"
    return complex_result
