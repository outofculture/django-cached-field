from celery import shared_task
from celery.utils.log import get_task_logger
import re

try:
    # Django 1.9
    from django.apps import apps

    get_model = apps.get_model
except ImportError:
    # Django 1.7 and before
    from django.db.models import get_model

logger = get_task_logger(__name__)
# TODO 20150119: this needs to handle custom named recalculation fields
recalc_needed_re = re.compile("(.*)_recalculation_needed$")


@shared_task
def offload_cache_recalculation(app, model, obj_id, **kwargs):
    model = get_model(app, model)
    try:
        obj = model.objects.get(pk=obj_id)
        for f in model._meta.fields:
            match = recalc_needed_re.search(f.name)
            if match and getattr(obj, f.name):
                basename = match.groups()[0]
                getattr(obj, "recalculate_{0:s}".format(basename))()
    except model.DoesNotExist:
        logger.warning(
            ('{}.{} with pk {} does not exist.  Was offload_cache_recalculation ' +
             'called before initial object creation or after object deletion?').format(
                    app, model, obj_id))
