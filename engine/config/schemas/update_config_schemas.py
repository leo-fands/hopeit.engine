from hopeit.app.config import AppConfig
from hopeit.server.config import ServerConfig
import json

with open('app-config-schema-draftv6.json', 'w') as fb:
    fb.write(json.dumps(AppConfig.json_schema(), indent=2))

with open('server-config-schema-draftv6.json', 'w') as fb:
    fb.write(json.dumps(ServerConfig.json_schema(), indent=2))
