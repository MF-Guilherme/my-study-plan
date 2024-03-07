from Nivel_1.linear_search import linear_search

def test_linear_search_key_founded():
    key = 70
    expected_output = 'Key 70 founded at index 3'
    actually_output = linear_search(key)
    assert actually_output == expected_output
    

def test_linear_search_key_not_found():
    key = 1258
    expected_output = 'No match found'
    actually_output = linear_search(key)
    assert actually_output == expected_output