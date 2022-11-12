def prettify(data, indent=0):
    for k, v in data.items():
        print(" " * indent, f"{k}:", end='')
        if isinstance(v, dict):
            print()
            prettify(v, indent + 1)
        else:
            print(" " * (indent + 1), v)
    print()
