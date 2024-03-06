list = [10, 50, 30, 70, 80, 20, 90, 40]

key = int(input('Enter the key you want to search: '))

for i, number in enumerate(list):
    if number == key:
        print(f'Key {number} founded at index {i}')
        break
    if i + 1 == len(list):
        print('No match found')
        break
