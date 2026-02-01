# CRM Celery Report Setup

## Requirements
- Redis
- Python packages from requirements.txt

## Setup Steps

1. Install Redis

sudo apt install redis-server

2. Install dependencies

pip install -r requirements.txt

3. Run migrations

python manage.py migrate

4. Start Celery worker

celery -A crm worker -l info

5. Start Celery Beat

celery -A crm beat -l info

6. Verify logs

Check:

/tmp/crmreportlog.txt
