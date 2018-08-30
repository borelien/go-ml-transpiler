import re


ID_PATTERN = re.compile("\d*:")
NODE_PATTERN = re.compile(r"(\d+):\[(.+)\]")
LEAF_PATTERN = re.compile(r"(\d+):(leaf=.+)")
EDGE_PATTERN = re.compile(r"yes=(\d+),no=(\d+),missing=(\d+)")
EDGE_PATTERN2 = re.compile(r"yes=(\d+),no=(\d+)")


def _parse_node(text):
    match = NODE_PATTERN.match(text)
    if match is not None:
        return match
    match = LEAF_PATTERN.match(text)
    if match is not None:
        return match
    raise ValueError("Unable to parse node: {0}.".format(text))


def _parse_edge(text):
    try:
        match = EDGE_PATTERN.match(text)
        if match is not None:
            yes, no, missing = match.groups()
            return yes, no, missing
    except:
        pass

    match = EDGE_PATTERN2.match(text)
    if match is not None:
        yes, no = match.groups()
        return yes, no, None
    raise ValueError("Unable to parse edge: {0}.".format(text))


def build_tree(tree, indent, missing_condition):

    rood_id = "0"
    root_depth = 1

    def _build_tree(nodes, node_id, depth):

        tree = ""
        current_indent = indent * depth

        if nodes[node_id]["leaf"]:
            tree += "\n{indent}return {value}".format(indent=current_indent, value=float(nodes[node_id]["value"]))
            return tree
        else:
            if depth > root_depth:
                tree += "\n"
            tree += "{indent}if (features[{feature_index}] < {threshold}) {condition_direction}({missing_condition}) {{".format(
                indent=current_indent,
                feature_index=nodes[node_id]["value"]["feature"][1:],
                threshold=nodes[node_id]["value"]["threshold"],
                condition_direction="&& !" if nodes[node_id]["value"]["missing"] != nodes[node_id]["value"]["yes"] else "|| ",
                missing_condition=missing_condition.format(feature_index=nodes[node_id]["value"]["feature"][1:]))

            tree += _build_tree(nodes, nodes[node_id]["value"]["yes"], depth + 1)
            tree += "\n{indent}}} else {{".format(indent=current_indent)
            tree += _build_tree(nodes, nodes[node_id]["value"]["no"], depth + 1)
            tree += "\n{indent}}}".format(indent=current_indent)
        return tree

    _nodes = {}
    i = 0
    while i < len(tree):

        try:
            idx = ID_PATTERN.match(tree[i]).group()[:-1]
        except IndexError:
            raise ValueError("Model format is not supported.")

        _node = _parse_node(tree[i])
        node_split = _node.group(2).split("=")

        if node_split[0] == "leaf":
            _nodes[idx] = {"leaf": True, "value": node_split[1]}
        else:
            i += 1
            f, t = _node.group(2).split("<")
            yes, no, missing = _parse_edge(tree[i])
            _nodes[idx] = {
                "leaf": False,
                "value": {"yes": yes, "no": no, "missing": missing, "feature": f, "threshold": t}
            }
        i += 1
    if rood_id not in _nodes:
        raise ValueError('root node "{}" cannot be found.')
    return _build_tree(nodes=_nodes, node_id=rood_id, depth=root_depth)
