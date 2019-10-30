

def build_tree(left_nodes, right_nodes, thresholds, values, features, indent):

    root_node = 0
    root_depth = 1

    def _build_tree(_left_nodes, _right_nodes, _thresholds, _values, _features, _indent, node, depth):

        tree = ""
        current_indent = indent * depth

        if _thresholds[node] != -2.:
            if depth > root_depth:
                tree += "\n"
            tree += "{indent}if features[{feature_index}] < {thresholds}{{".format(
                indent=current_indent if depth > root_depth else "",
                feature_index=_features[node],
                thresholds=_thresholds[node]
            )

            if _left_nodes[node] != -1.:
                tree += _build_tree(
                    _left_nodes, _right_nodes, _thresholds, _values, _features, _indent, _left_nodes[node], depth + 1)
            tree += "\n{indent}}} else {{".format(indent=current_indent)

            if _right_nodes[node] != -1.:
                tree += _build_tree(
                    _left_nodes, _right_nodes, _thresholds, _values, _features, _indent, _right_nodes[node], depth + 1)
            tree += "\n{indent}}}".format(indent=current_indent)
        else:
            tree += "".join(
                [
                    "\n{indent}predictions[{class_index}] = {class_value}".format(
                        indent=current_indent,
                        class_index=i,
                        class_value=float(rate))
                    for i, rate in enumerate(_values[node][0])
                ])
        return tree
    return _build_tree(left_nodes, right_nodes, thresholds, values, features, indent, node=root_node, depth=root_depth)
