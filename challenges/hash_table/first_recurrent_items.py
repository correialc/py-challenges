def find_first_recurrent_items(items):
    found_items = dict()

    for item in items:
        if item not in found_items:
            found_items[item] = True
        else:
            return item

    return None
