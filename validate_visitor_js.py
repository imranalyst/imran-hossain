import re
import pathlib
from js2py import EvalJs

html = pathlib.Path(r'c:\Users\gh\OneDrive\Desktop\imran-hossain\index.html').read_text(encoding='utf-8')
script_blocks = re.findall(r'<script>(.*?)</script>', html, re.S)
if not script_blocks:
    raise SystemExit('No script blocks found')

context = EvalJs()
context.execute("var document = { getElementById: function(){ return { textContent: '', addEventListener: function(){} }; } }; var localStorage = { getItem: function(){ return null; }, setItem: function(){} }; var sessionStorage = { getItem: function(){ return null; }, setItem: function(){} }; var fetch = function(){ return Promise.resolve({ ok: true, json: function(){ return { count: 1 }; } }); };")

for i, script in enumerate(script_blocks, 1):
    try:
        context.execute(script)
    except Exception as e:
        raise SystemExit(f'Script block {i} failed: {e}')

print('JS syntax OK')
