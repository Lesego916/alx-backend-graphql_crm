INSTALLED_APPS += [
    'django_celery_beat',
]


CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.logcrmheartbeat'),
    ('0 */12 * * *', 'crm.cron.updatelowstock'),
]

