import os, time, json
with open("set-miner/offline.json", encoding="utf-8") as set:
    load = set.read()
    loads = json.loads(load)
    name = loads['name']
    NAME = f'{name}'
    __title__ = 'requests'
    __description__ = 'Python HTTP for Humans.'
    __url__ = 'https://requests.readthedocs.io'
    __version__ = f"'______{NAME}______'"
    __build__ = 0x022501
    __author__ = 'Kenneth Reitz'
    __author_email__ = 'me@kennethreitz.org'
    __license__ = 'Apache 2.0'
    __copyright__ = 'Copyright 2020 Kenneth Reitz'
    __cake__ = u'\u2728 \U0001f370 \u2728'
    #print(f'{__version__}')
    f = open("__version__.py", mode='w+', encoding="utf-8")
    print("__title__ = 'requests'", file=f)
    print("__description__ = 'Python HTTP for Humans.'", file=f)
    print("__url__ = 'https://requests.readthedocs.io'", file=f)
    print("__version__ = ",f"{__version__}", file=f)
    print("__build__ = 0x022501", file=f)
    print("__author__ = 'Kenneth Reitz'", file=f)
    print("__author_email__ = 'me@kennethreitz.org'", file=f)
    print("__license__ = 'Apache 2.0'", file=f)
    print("__copyright__ = 'Copyright 2020 Kenneth Reitz'", file=f)
    print("__cake__ = u'\u2728 \U0001f370 \u2728'", file=f)

  