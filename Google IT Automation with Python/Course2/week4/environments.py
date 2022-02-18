import os

print('Home: ' + os.environ.get('HOME', ''))
print('Shell: ' + os.environ.get('SHELL', ''))
print('Fruit: ' + os.environ.get('FRUIT', ''))