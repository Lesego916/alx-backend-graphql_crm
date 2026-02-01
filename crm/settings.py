INSTALLED_APPS = [
    "django_crontab",
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.logcrmheartbeat'),
    ('0 */12 * * *', 'crm.cron.updatelowstock'),
]

