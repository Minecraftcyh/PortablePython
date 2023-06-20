import PortablePython as pp
import json

j=json.dumps(pp.language,
             indent=4,
            ensure_ascii=False,
          	sort_keys=True,
            separators=(",",":"))

print(j)