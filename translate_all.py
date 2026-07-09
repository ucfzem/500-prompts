import json, time, concurrent.futures
from deep_translator import GoogleTranslator

with open('prompts.json') as f:
    prompts = json.load(f)

def translate_one(text, src, tgt):
    try:
        t = GoogleTranslator(source=src, target=tgt)
        return t.translate(text)
    except:
        time.sleep(3)
        try:
            t = GoogleTranslator(source=src, target=tgt)
            return t.translate(text)
        except:
            return ''

def translate_all(src, tgt, label):
    print(f'=== Translating {label} ===')
    total = len(prompts)
    results = [{} for _ in range(total)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        fut_map = {}
        for i, p in enumerate(prompts):
            fut_map[ex.submit(translate_one, p['t'], src, tgt)] = (i, 't')
            fut_map[ex.submit(translate_one, p['p'], src, tgt)] = (i, 'p')
        done = 0
        for future in concurrent.futures.as_completed(fut_map):
            i, typ = fut_map[future]
            try:
                results[i][typ] = future.result()
            except:
                results[i][typ] = ''
            done += 1
            if done % 100 == 0:
                print(f'{done}/{total*2}')
    out = [{'n': prompts[i]['n'], f't_{tgt}': results[i].get('t',''), f'p_{tgt}': results[i].get('p','')} for i in range(total)]
    with open(f'{tgt}.json', 'w') as f:
        json.dump({'prompts': out}, f, ensure_ascii=False, indent=2)
    print(f'Saved {tgt}.json')

translate_all('fr', 'en', 'English')
translate_all('fr', 'es', 'Spanish')
print('All done!')
