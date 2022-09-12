with open('test_file.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('new_test.txt', 'w') as f:
    f.write('hola')
