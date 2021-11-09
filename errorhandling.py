import sys

file_name='recipes.txt'
try:
    my_file = open(file_name,'x')
    my_file.write('Albondigas')
    my_file.close() 
except FileExistsError:
    print(f"the file {file_name} already exists")
    sys.exit(1)
except:
    print(f"Unable to write the file")
    sys.exit(1)
else:
    print(f"file recipes created")
finally:
    print(f"Excecution complete")