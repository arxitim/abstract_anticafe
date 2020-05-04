from datetime import timedelta, datetime
from pytz import timezone
from random import choice

from celery.task import periodic_task
from celery.schedules import crontab

from core.models import TableBookingQueue, Table
from abstract_anticafe.settings import TIME_ZONE


@periodic_task(run_every=(crontab(minute='*/15')), name="clean_table_booking_queue", ignore_result=True)
def clean_table_booking_queue():
    """
    Task, which removes all past bookings and changes the state of the tables (is_busy=False)
    """
    all_complete_booking = TableBookingQueue.objects.filter(dt_end__lt=datetime.now(tz=timezone(TIME_ZONE)))
    count = len(all_complete_booking)
    if not count:
        return "there is no complete bookings"
    else:
        for booking in all_complete_booking:
            booking.table.is_busy = False
            booking.table.save()

        all_complete_booking.delete()
        return f"all expired bookings deleted [ {count} ]"


@periodic_task(run_every=(crontab(minute='*/20')), name="emulate_strangers", ignore_result=True)
def emulate_strangers():
    """
    Emulates people visiting a cafe from the street and changes the state of the table
    """
    tables = Table.objects.all()
    free_tables = filter(lambda x: not x.is_busy, tables)

    busy_by_strangers = []
    for free_table in free_tables:
        if choice([True, False]):
            free_table.is_busy = True
            free_table.save()
            busy_by_strangers.append(free_table.short_description)

    return f"Tables {', '.join(busy_by_strangers)} are now busy by strangers"


@periodic_task(run_every=(crontab(minute='*/22')), name="emulate_freeing_table", ignore_result=True)
def emulate_freeing_table():
    """
    Emulates freeing up the table by strangers
    (It doesn't matter who the table was occupied with)
    """
    tables = Table.objects.all()
    free_tables = filter(lambda x: x.is_busy, tables)

    freeing_by_strangers = []
    for busy_table in free_tables:
        if choice([True, False, True]):
            busy_table.is_busy = False
            busy_table.save()
            freeing_by_strangers.append(busy_table.short_description)

    return f"Tables {', '.join(freeing_by_strangers)} are now free"
