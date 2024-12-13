import os
import yextract

directory = 'testcases'

ls = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if f.endswith('.yaml'):
            ls.append(f)

#print(ls)
yextract.run(ls)


    