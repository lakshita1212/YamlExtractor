import yaml
import sys
import os
import pathlib

args = sys.argv


def run(args):
    for i in range(len(args)-1):
        count = 0
        data = yaml.safe_load(open(args[1+i]))

        yaml_filename = pathlib.Path(args[1]).name
        direcname = "test_" + yaml_filename
        os.mkdir(direcname)

        for job in data['jobs']:

            count = 0
            for step in data['jobs'][job]['steps']:
                count += 1
                if 'run' in step:
                    shell_script = step['run'] + "\n"
                    filename = f"{direcname}/test_{yaml_filename}{count}.sh"
                    my_file = open(filename, "a")
                    my_file.write(shell_script)

#run(args)
