from datetime import timedelta, datetime

from celery.task import periodic_task
from celery.schedules import crontab

from core.models import TableBookingQueue


@periodic_task(run_every=(crontab(minute='*/15')), name="clean_table_booking_queue", ignore_result=True)
# @periodic_task(run_every=timedelta(seconds=30), name="clean_table_booking_queue", ignore_result=True)
def clean_table_booking_queue():
    all_complete_booking = TableBookingQueue.objects.filter(dt_end__lt=datetime.now())
    count = len(all_complete_booking)
    if not count:
        return "there is no complete bookings"
    else:
        all_complete_booking.delete()
        return f"all expired bookings deleted [ {count} ]"
