import sys
import yaml
import os


#Replace from current directory running script to os environment variable
with open(os.path.join(sys.path[0], 'config.yaml'), "r") as f:
    settings = yaml.load(f)

    