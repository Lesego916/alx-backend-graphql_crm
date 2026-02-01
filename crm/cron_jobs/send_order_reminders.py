from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql("""
query {
  allOrders {
    edges {
      node {
        id
        customer {
          email
        }
      }
    }
  }
}
""")

result = client.execute(query)

with open("/tmp/order_reminders_log.txt", "a") as f:
    for edge in result["allOrders"]["edges"]:
        order = edge["node"]
        f.write(f"{datetime.now()} Order {order['id']} -> {order['customer']['email']}\n")

print("Order reminders processed!")
