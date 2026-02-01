from celery import shared_task
import requests
from datetime import datetime

@shared_task(name="crm.tasks.generatecrmreport")
def generate_crm_report():
    query = """
    query {
        customers {
            id
        }
        orders {
            totalamount
        }
    }
    """

    response = requests.post(
        "http://localhost:8000/graphql/",
        json={"query": query}
    )

    data = response.json()["data"]

    customers = len(data["customers"])
    orders = len(data["orders"])
    revenue = sum(order["totalamount"] for order in data["orders"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(f"{timestamp} - Report: {customers} customers, {orders} orders, {revenue} revenue\n")
