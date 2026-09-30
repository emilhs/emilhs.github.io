#!/usr/bin/env python3
"""Refresh the Speed Skating folder in index.html with every result from SpeedskatingResults.com.

Usage: python3 scripts/update_skating.py
"""
import json
import pathlib
import re
import urllib.request

SKATER = 46506
DISTANCES = [500, 1000, 1500, 3000, 5000, 10000]
API = "https://speedskatingresults.com/api/json/skater_results.php?skater={}&distance={}"
PAGE = pathlib.Path(__file__).resolve().parent.parent / "index.html"

races = []
for d in DISTANCES:
    req = urllib.request.Request(API.format(SKATER, d), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as res:
        for r in json.load(res)["results"]:
            races.append({"date": r["date"], "distance": d, "time": r["time"],
                          "name": r["name"], "location": r["location"],
                          "link": r["link"].replace("http://", "https://www.", 1)})
races.sort(key=lambda r: (r["date"], r["distance"]))

data = json.dumps(races, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = PAGE.read_text()
html = re.sub(r"/\*DATA\*/.*?/\*END\*/", lambda _: f"/*DATA*/{data}/*END*/", html, flags=re.S)
PAGE.write_text(html)
print(f"Wrote {len(races)} races to {PAGE}")
