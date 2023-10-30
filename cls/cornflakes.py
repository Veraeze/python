def equal_strings(first: str, second: str):
    store = []
    for i in first:
        for j in second:
            if i == j:
                store.append(j)
    return len(store) == len(first)

