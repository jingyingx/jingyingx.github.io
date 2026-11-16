#!/usr/bin/env python3
"""Serve the HTML Jekyll pages locally without installing Ruby dependencies.
Uses the same academic layout and content as Jekyll; supports its three placeholders.
Run: python3 scripts/preview.py --port 4000
"""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse, html, re
ROOT = Path(__file__).resolve().parents[1]
PAGES = {'/': 'index.md', '/research/': 'research.md', '/publications/': 'publications.md', '/teaching/': 'teaching.md'}
class Preview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs): super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        path=self.path.split('?',1)[0]
        if path.rstrip('/')+'/' in PAGES and path not in PAGES:
            self.send_response(301); self.send_header('Location',path+'/'); self.end_headers(); return
        if path not in PAGES:
            if not (path.startswith('/assets/') or (path.endswith('.pdf') and '/' not in path[1:])):
                self.send_error(404); return
            return super().do_GET()
        source=(ROOT/PAGES[path]).read_text()
        _,front,content=source.split('---',2)
        fields=dict(re.findall(r'^(\w+):\s*(.*?)\s*$',front,re.M))
        layout=(ROOT/'_layouts/academic.html').read_text()
        for key in ('title','description'):
            value=html.escape(fields[key].strip('"'))
            layout=layout.replace('{{ page.'+key+' }}',value).replace('{{ page.'+key+' | escape }}',value)
        layout=layout.replace('{{ page.browser_title | default: page.title | escape }}', html.escape(fields.get('browser_title',fields['title']).strip('"')))
        output=layout.replace('{{ content }}',content).encode()
        self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Content-Length',str(len(output))); self.end_headers(); self.wfile.write(output)
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--port',type=int,default=4000); args=parser.parse_args()
    print(f'Local preview: http://127.0.0.1:{args.port}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Preview).serve_forever()
