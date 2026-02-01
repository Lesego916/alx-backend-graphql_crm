#!/bin/bash

cd /path/to/alx-backend-graphqlcrm

COUNT=$(python manage.py shell << EOF
from crm.models import Customer, Order
from django.utils import timezone
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)

inactive = Customer.objects.exclude(
    id__in=Order.objects.filter(order_date__gte=one_year_ago).values_list("customer_id", flat=True)
)

c = inactive.count()
inactive.delete()
print(c)
EOF
)

echo "$(date '+%d/%m/%Y-%H:%M:%S') Deleted customers: $COUNT" >> /tmp/customercleanuplog.txt
