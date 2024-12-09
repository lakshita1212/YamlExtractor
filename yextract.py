import yaml
import sys

args = sys.argv
lst = []

def run(args):
    for i in range(len(args)-1):
        lst = []
        data = yaml.safe_load(open(args[1+i]))
        print("File Name:\n",args[1+i])

        for job in data['jobs']:
            count = 0
            for step in data['jobs'][job]['steps']:
                count += 1
                #print(f'{job}: step {count}: {step}')
                lst.append([f'{job}: step {count}: {step}'])

                #if 'run' in step:
                    #print(f"MATCH: {step['run']}")
        print(lst)
        print("\n\n")

    



run(args)
'''
import yaml
import sys

args = sys.argv
def run(args):
    infile = open(args[1],"r")
    outfile = open('output.txt',"w")
    for i in range(len(args)-1):
        data = yaml.safe_load(open(args[1+i]))
        print(args[1+i])
        outfile.write(args[1+i])

        for job in data['jobs']:
            count = 0
            for step in data['jobs'][job]['steps']:
                count += 1
                #print(f'{job}: step {count}: {step}')
                #outfile.write(f'{job}: step {count}: {step}')

            #if 'run' in step:
                #outfile.write(f"MATCH: {step['run']}")
                #print(f"MATCH: {step['run']}")



run(args)
'''