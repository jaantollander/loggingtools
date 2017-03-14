import yaml
import json

with open('logging.yaml', 'r') as fp:
    config = yaml.load(fp)

with open('logging.json', 'w') as fp:
    json.dump(config, fp, indent=2)
