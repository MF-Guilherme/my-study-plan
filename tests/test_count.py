from Nivel_1.count import counter

def test_counter():
    word = '*GeEkS4GeEkS*'
    expected_output = (f'Upper case letters : 6\n'
              f'Lower case letters : 4\n'
              f'Numbers : 1\n'
              f'Special Characters : 2')
    actually_output = counter(word)
    assert actually_output == expected_output