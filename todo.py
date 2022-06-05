todo = ['wake up', 'get bathroom', 'make exercise', 'have breakfast',
'perform different tasks', 'help colleagues', 'relax with family']

print(*todo[:3:2], todo[3], todo[-1], sep='\n')
print(todo[:3])
print(todo[3:])
todo.append('go to bed')
todo[0], todo[-1] = todo[-1], todo[0]
user_task = input('What the task do you prefer to add? ')
todo.append(user_task)
todo2 = todo
todo3 = list(todo)
todo4 = todo[:]
todo5 = todo.copy()
print(id(todo))
print(id(todo2))
print(id(todo3))
print(id(todo4))
print(id(todo5))
