import json
import concurrent.futures
import time
from deep_translator import GoogleTranslator

with open('prompts.json', 'r', encoding='utf-8') as f:
    prompts = json.load(f)

def trans(text):
    t = GoogleTranslator(source='fr', target='ar')
    return t.translate(text)

output = []
total = len(prompts)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    fut_t = {ex.submit(trans, p['t']): p['n'] for p in prompts}
    fut_p = {ex.submit(trans, p['p']): p['n'] for p in prompts}
    results = {}
    for future in concurrent.futures.as_completed({**fut_t, **fut_p}):
        n = fut_t.get(future) or fut_p.get(future)
        typ = 't' if future in fut_t else 'p'
        if n not in results:
            results[n] = {}
        try:
            results[n][typ] = future.result()
        except:
            results[n][typ] = ''
        done = sum(1 for v in results.values() if len(v) == 2)
        print(f'\r{done}/{total} prompts complete', end='', flush=True)

print()
for p in prompts:
    n = p['n']; r = results.get(n, {})
    output.append({'n': n, 't_fr': p['t'], 't_ar': r.get('t',''), 'p_fr': p['p'], 'p_ar': r.get('p','')})

with open('ar.json', 'w', encoding='utf-8') as f:
    json.dump({'prompts': output}, f, ensure_ascii=False, indent=2)

print(f'Saved {len(output)} prompts to ar.json')
