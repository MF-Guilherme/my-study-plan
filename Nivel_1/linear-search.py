def linear_search(key):
    db = [10, 50, 30, 70, 80, 20, 90, 40]

    for i, number in enumerate(db):
        if number == key:
            return f'Key {number} founded at index {i}'
        if i + 1 == len(db):
            return 'No match found'
