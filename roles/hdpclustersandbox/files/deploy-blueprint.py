import requests
import functools
import os
import yaml
import json
from pprint import pprint

auth = ('admin', 'admin')


def here(path):
    return os.path.join(os.path.dirname(__file__), path)


def query(path, method, auth, data=None, json=None, headers=None):
    headers = headers or {}
    headers['X-Requested-By'] = 'ambari'
    if 'http://' in path:
        path = path[path.find('/api/v1')+8:]
    res = getattr(requests, method)(
        'http://master1:8080/api/v1/%s' % path, auth=auth, data=data,
        headers=headers,
        json=json
    )
    if res.text:
        return res.json()
    return {}


get = functools.partial(query, method='get', auth=auth)
post = functools.partial(query, method='post', auth=auth)
delete = functools.partial(query, method='delete', auth=auth)

# list stacks
stacks = get('stacks')['items']

# get all components
components = []
for s in get('stacks/HDP/versions/2.6')['services']:
    components += get(s['href'])['components']

components = [c['StackServiceComponents'] for c in components]

existing_blueprints = get('blueprints')

if 'sandbox' in [b['Blueprints']['blueprint_name'] for b in existing_blueprints['items']]:
    delete('blueprints/sandbox')

blueprint = yaml.load(open(here('blueprint.yml')))
post('blueprints/sandbox', data=json.dumps(blueprint),
     headers={'Content-Type': 'text/plain'})

cluster = yaml.load(open(here('cluster.yml')))
pprint(post('clusters/SandboxCluster', data=json.dumps(cluster),
            headers={'Content-Type': 'text/plain'}))

with open('/root/ambari-cluster-deployed', 'w') as f:
    f.write('ok')
