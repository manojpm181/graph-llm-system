import networkx as nx
import pandas as pd

def safe(val):
    return "unknown" if pd.isna(val) else str(val)

def build_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        order = f"order_{safe(row.get('salesorder'))}"
        customer = f"customer_{safe(row.get('soldtoparty'))}"
        product = f"product_{safe(row.get('material'))}"

        G.add_node(order, type="order")
        G.add_node(customer, type="customer")
        G.add_node(product, type="product")

        G.add_edge(order, customer)
        G.add_edge(order, product)

    return G