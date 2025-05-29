def add(data):
    data["sum"] = data["a"] + data["b"]
    return data

if __env:  # Taktile environment
    data = add(data)
