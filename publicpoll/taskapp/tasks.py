
from celery.decorators import task, periodic_task

from administration.models import Poll
from publicpoll.models import Statistics

@task(name='update_statistics', max_retries=3)
def update_statistics(poll_pk, question, value):
    """Send account verification link to given user."""
    poll = Poll.objects.get(pk = poll_pk)
    stat,created = Statistics.objects.get_or_create(poll = poll, question = question,
                  defaults={'true_counter': 0, 'false_counter' : 0})
    if value:
        stat.true_counter += 1
    else:
        stat.false_counter += 1
    stat.save()
