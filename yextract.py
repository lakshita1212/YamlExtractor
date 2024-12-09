import yaml
import sys

args = sys.argv

def run(args):
    for i in range(len(args)-1):
        data = yaml.safe_load(open(args[1+i]))
        print("File Name: \n\n",args[1+i])

        for job in data['jobs']:
            count = 0
            for step in data['jobs'][job]['steps']:
                count += 1
                print(f'{job}: step {count}: {step}')

                if 'run' in step:
                    print(f"MATCH: {step['run']}")


run(args)