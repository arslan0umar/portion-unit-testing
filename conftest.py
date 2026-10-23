def pytest_collection_modifyitems(config, items):
    order = {"smoke": 1, "ecp": 2, "bva": 3, "csv": 4, "regression": 5}
    def key(item):
        for name, rank in order.items():
            if item.get_closest_marker(name):
                return rank
        return 6
    items.sort(key=key)
