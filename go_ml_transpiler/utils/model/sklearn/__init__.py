

def build_tree(left_nodes, right_nodes, thresholds, values, features, indent, float_type):

    root_node = 0
    root_depth = 1

    def _build_tree(_left_nodes, _right_nodes, _thresholds, _values, _features, _indent, node, depth, _float_type):

        tree = ""
        current_indent = indent * depth

        if _thresholds[node] != -2.:
            if depth > root_depth:
                tree += "\n"
            tree += "{indent}if features[{feature_index}] < {float_type}({threshold}){{".format(
                indent=current_indent if depth > root_depth else "",
                feature_index=_features[node],
                threshold=_thresholds[node],
                float_type=_float_type)

            if _left_nodes[node] != -1.:
                tree += _build_tree(
                    _left_nodes,
                    _right_nodes,
                    _thresholds,
                    _values,
                    _features,
                    _indent,
                    _left_nodes[node],
                    depth + 1,
                    _float_type)
            tree += "\n{indent}}} else {{".format(indent=current_indent)

            if _right_nodes[node] != -1.:
                tree += _build_tree(
                    _left_nodes,
                    _right_nodes,
                    _thresholds,
                    _values,
                    _features,
                    _indent,
                    _right_nodes[node],
                    depth + 1,
                    _float_type)
            tree += "\n{indent}}}".format(indent=current_indent)
        else:
            tree += "".join(
                [
                    "\n{indent}predictions[{class_index}] = {float_type}({class_value})".format(
                        indent=current_indent,
                        class_index=i,
                        class_value=float(rate),
                        float_type=_float_type)
                    for i, rate in enumerate(_values[node][0])
                ])
        return tree
    return _build_tree(
        left_nodes,
        right_nodes,
        thresholds,
        values,
        features,
        indent,
        root_node,
        root_depth,
        float_type)
