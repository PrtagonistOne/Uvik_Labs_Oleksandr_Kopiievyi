def prettify(data, indent=0):
    pretty_string = ''
    for k, v in data.items():
        pretty_string += f'{" " * indent} {k}:'
        if isinstance(v, dict):
            # pretty_string += '\n'
            prettify(v, indent + 1)
        else:
            pretty_string += f'{" " * (indent + 1)} {v}\n'
    # pretty_string += '\n'
    return pretty_string
