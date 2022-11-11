def pretty(d, indent=0):
    formatted_str = ''
    for key, value in d.items():
        formatted_str += '\t' * indent + str(key) + ':'
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            formatted_str += '\t' * (indent + 1) + str(value) + '\n'
    return formatted_str.strip()
