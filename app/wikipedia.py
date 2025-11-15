import requests


key = f"summary:{title}"
c = get_cache(key)
if c is not None:
return c


try:
quoted = quote(title, safe="")
resp = requests.get(WIKI_SUMMARY.format(quoted), headers=HEADERS, timeout=6)


if resp.status_code == 404:
set_cache(key, (None, None))
return None, None


if resp.status_code == 403:
# fallback
try:
q = requests.get(WIKI_SEARCH, params={
"action": "query",
"prop": "extracts",
"explaintext": 1,
"titles": title,
"format": "json"
}, headers=HEADERS, timeout=6)
j = q.json()
pages = j.get("query", {}).get("pages", {})
for pid, p in pages.items():
extract = p.get("extract", "")
page_title = p.get("title", title)
url = f"https://en.wikipedia.org/wiki/{quote(page_title, safe='')}"
text = (p.get("description","") + ". " if p.get("description") else "") + extract
if text:
set_cache(key, (text.strip(), url))
return text.strip(), url
except Exception:
pass
set_cache(key, (None, None))
return None, None


if resp.status_code != 200:
set_cache(key, (None, None))
return None, None


j = resp.json()
extract = j.get("extract", "") or ""
desc = j.get("description", "") or ""
text = (desc + ". " if desc else "") + extract
url = f"https://en.wikipedia.org/wiki/{quote(j.get('title',''), safe='')}"
set_cache(key, (text.strip() or None, url))
return (text.strip() or None), url
except ValueError:
set_cache(key, (None, None))
return None, None
except Exception:
set_cache(key, (None, None))
return None, None