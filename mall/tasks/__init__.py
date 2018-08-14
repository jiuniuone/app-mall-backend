import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django.dispatch import receiver

from acmin.utils.imports import import_submodules
from mall.signals import app_ready

logger = logging.getLogger(__name__)


@receiver(app_ready, dispatch_uid="app_ready")
def init_schedule(sender, **kwargs):
    # print("init_schedule")
    scheduler = BackgroundScheduler()
    # scheduler.add_job(order.do_charge_cronjob, 'interval', seconds=order.cronjob_interval, max_instances=3)
    # scheduler.add_job(video.do_import_cronjob, 'interval', seconds=video.cronjob_interval, max_instances=3)
    scheduler.start()
    logger.info("scheduler started")


@receiver(app_ready, dispatch_uid="app_ready2")
def init_schedule2(sender, **kwargs):
    # print("init_schedule")

    logger.info("scheduler2 started")

import_submodules(globals(), __name__, __path__)
