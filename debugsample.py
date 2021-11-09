import pdb

def map (func, values):
    output_vales = []
    index = 0
    while index < len(values):
        pdb.set_trace()
        output_vales.append(func(values[index]))
        index+=1
    return output_vales

def addone(val):
        return val +1

print(map(addone,list(range(10))))