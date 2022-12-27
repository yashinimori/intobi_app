def prepare_data(*args, **kwargs):
    data = kwargs.pop("data")
    user = kwargs.pop("user")
    if isinstance(data, list):
        for item in data:
            item.setdefault("user", user)
    elif isinstance(data, dict):
        data.setdefault("user", user)
    return data
