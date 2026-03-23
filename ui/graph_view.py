from pyvis.network import Network

def color_map(node_type):
    return {
        "order": "#4FC3F7",
        "customer": "#BA68C8",
        "product": "#4DD0E1"
    }.get(node_type, "gray")

def visualize_graph(G, highlight_nodes=None):

    net = Network(
        height="650px",
        width="100%",
        bgcolor="#0e1117",
        font_color="white"
    )

    net.barnes_hut()

    for node, data in G.nodes(data=True):

        color = color_map(data["type"])
        size = 15

        if highlight_nodes and any(str(h) in node for h in highlight_nodes):
            color = "yellow"
            size = 25

        net.add_node(
            node,
            label=node,
            title=f"Type: {data['type']}",
            color=color,
            size=size
        )

    for u, v in G.edges():
        net.add_edge(u, v)

    net.save_graph("graph.html")
    return "graph.html"