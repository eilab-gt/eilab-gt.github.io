import sys
import json
import yaml
with open(sys.argv[2], "w") as f:
	f.write(yaml.dump(yaml.load(json.dumps(json.loads(open(sys.argv[1]).read()))), default_flow_style=False))