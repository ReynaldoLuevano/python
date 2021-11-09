with open('xmen.txt','w+') as my_file:
    my_file.write('Bestia\n')
    my_file.write('Tormenta\n')
    my_file.writelines([
    'Wolverine\n',
    'Cyclope\n',
    'Gambito\n'
    ])

my_file =  open('xmen.txt','r')
with my_file:
    print(my_file.read())
    