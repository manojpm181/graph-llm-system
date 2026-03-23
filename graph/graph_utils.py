def extract_nodes_from_result(df):
    nodes = []

    if df is None:
        return nodes

    for col in df.columns:
        for val in df[col]:
            if val:
                nodes.append(str(val))

    return nodes