from datetime import datetime
from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
import requests

def log_crm_heartbeat():
    try:
        requests.post("http://localhost:8000/graphql", json={"query": "{ hello }"})
    except:
        pass

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{datetime.now()} CRM is alive\n")

def updatelowstock():
    import requests
    from datetime import datetime

    mutation = """
    mutation {
      updateLowStockProducts {
        products {
          name
          stock
        }
      }
    }
    """

    r = requests.post("http://localhost:8000/graphql", json={"query": mutation})
    data = r.json()

    with open("/tmp/low_stock_updates_log.txt", "a") as f:
        for p in data["data"]["updateLowStockProducts"]["products"]:
            f.write(f"{datetime.now()} {p['name']} {p['stock']}\n")
