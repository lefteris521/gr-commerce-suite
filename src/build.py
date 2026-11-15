"""Build index.html (el, main) and en.html (en) from template.html + strings.<lang>.json.

Fails if the template uses a key that a language does not define, or if a language
defines keys the template never uses. Run:  python -I src/build.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = {'el': 'index.html', 'en': 'en.html'}  # Greek is the main address
KEY = re.compile(r'\{\{([a-z0-9_.]+)\}\}')

template = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
used = set(KEY.findall(template))
errors = []
for lang, name in OUT.items():
    strings = json.load(open(os.path.join(HERE, f'strings.{lang}.json'), encoding='utf-8'))
    missing = sorted(used - strings.keys())
    unused = sorted(strings.keys() - used)
    if missing:
        errors.append(f'{lang}: missing keys {missing}')
    if unused:
        errors.append(f'{lang}: unused keys {unused}')
    if missing:
        continue
    html = KEY.sub(lambda m: strings[m.group(1)], template)
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(html)
    print(f'wrote {name}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
