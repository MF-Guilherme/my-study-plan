from Nivel_1.calculate_age import calculate_age

def test_calculate_age():
    present = '07/12/2017'
    birth = '07/09/1996'
    expected_output = 'Present Age = Years: 21  Months: 3  Days: 0'
    actual_output = calculate_age(present, birth)
    assert actual_output == expected_output