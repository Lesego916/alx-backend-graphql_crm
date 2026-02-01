from datetime import datetime
import requests

def logcrmheartbeat():
    try:
        requests.post("http://localhost:8000/graphql", json={"query": "{ hello }"})
    except:
        pass

    with open("/tmp/crmheartbeatlog.txt", "a") as f:
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

    with open("/tmp/lowstockupdates_log.txt", "a") as f:
        for p in data["data"]["updateLowStockProducts"]["products"]:
            f.write(f"{datetime.now()} {p['name']} {p['stock']}\n")
