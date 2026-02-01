from celery import shared_task
import requests
from datetime import datetime

@shared_task(name="crm.tasks.generatecrmreport")
def generatecrmreport():
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

    with open("/tmp/crmreportlog.txt", "a") as f:
        f.write(f"{timestamp} - Report: {customers} customers, {orders} orders, {revenue} revenue\n")
