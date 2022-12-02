files = {}
for _ in range(int(input("Enter the number of files: "))):
    name, *action = input("File names and allowed operations: ").split()
    files[name] = action
access = {'read': 'R', 'write': 'W', 'execute': 'X'}
for _ in range(int(input("Enter the number of file requests: "))):
    acc, nam = input("Requests of the \"file operation\" type: ").split()
    print('OK' if access[acc] in files[nam] else 'Access denied')
