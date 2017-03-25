import yaml
import json
import os


def convert_yaml_to_json(filepath='logging.yml'):
    with open(filepath, 'r') as fp:
        config = yaml.load(fp)

    base, _ = os.path.splitext(filepath)
    with open(base + '.json', 'w') as fp:
        json.dump(config, fp, indent=2)
