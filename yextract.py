import yaml
import sys

args = sys.argv

data = yaml.safe_load(open(args[1]))

for job in data['jobs']:
    count = 0
    for step in data['jobs'][job]['steps']:
        count += 1
        print(f'{job}: step {count}: {step}')

        if 'run' in step:
            print(f"MATCH: {step['run']}")
