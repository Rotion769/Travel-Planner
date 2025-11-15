from .wikipedia import wiki_search_titles, wiki_opensearch_titles, wiki_category_members, wiki_fetch_text_for_title


if len(titles) < limit * 2:
for q in base_queries:
for t in wiki_opensearch_titles(q, limit=per_query):
if t not in seen:
titles.append(t); seen.add(t)
if len(titles) >= limit * 2:
break


if len(titles) < limit * 2:
cat_candidates = [
f"Tourist attractions in {destination}",
f"Museums in {destination}",
f"Parks in {destination}",
f"Monuments and memorials in {destination}",
f"Churches in {destination}",
f"Palaces in {destination}",
f"Bridges in {destination}",
f"Squares in {destination}",
]
for cat in cat_candidates:
for t in wiki_category_members(cat, limit=per_query):
if t not in seen:
titles.append(t); seen.add(t)
if len(titles) >= limit * 3:
break


bad_prefixes = ("Tourism in ", "History of ", "List of ", "Cuisine of ", "Transport in ", "Culture of ")
filtered = [t for t in titles if not any(t.startswith(p) for p in bad_prefixes)]


results = []
for t in filtered:
if len(results) >= limit:
break
text, url = wiki_fetch_text_for_title(t)
if not text:
continue
try:
snippet = bart_summarize(text, max_len=110, min_len=30)
except Exception:
snippet = text[:300]
if not snippet:
continue
results.append({"title": t, "snippet": snippet, "url": url})


return results[:limit]