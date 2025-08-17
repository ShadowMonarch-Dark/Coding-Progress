import requests
import datetime

# 🔹 Your platform usernames
leetcode_username = "Jin-Woo_Shadow"
codeforces_username = "Monarch_Monster"
atcoder_username = "ShaDowGoD"

today = datetime.date.today()

# --------- Fetch Codeforces stats ---------
def fetch_codeforces():
    url = f"https://codeforces.com/api/user.info?handles={codeforces_username}"
    r = requests.get(url).json()
    rating = r["result"][0].get("rating", "Unrated")
    rank = r["result"][0].get("rank", "Unranked")
    return rating, rank

# --------- Fetch LeetCode stats ---------
def fetch_leetcode():
    url = f"https://leetcode-stats-api.herokuapp.com/{leetcode_username}"
    r = requests.get(url).json()
    solved = r.get("totalSolved", "N/A")
    ranking = r.get("ranking", "N/A")
    return solved, ranking

# --------- Fetch AtCoder stats ---------
def fetch_atcoder():
    url = f"https://kenkoooo.com/atcoder/atcoder-api/results?user={atcoder_username}"
    r = requests.get(url).json()
    if not r:
        return "Unrated", "0 contests"
    contests = len(r)
    return f"{contests} contests", "Check profile for rating"

# --------- Get stats ---------
cf_rating, cf_rank = fetch_codeforces()
lc_solved, lc_rank = fetch_leetcode()
ac_info, ac_note = fetch_atcoder()

# --------- Write to auto-progress.md ---------
content = f"""
# 📊 Auto-Updated Progress
_Last updated: {today}_

## LeetCode
- Problems Solved: {lc_solved}
- Global Rank: {lc_rank}

## Codeforces
- Rating: {cf_rating}
- Rank: {cf_rank}

## AtCoder
- {ac_info}
- {ac_note}
"""

with open("progress/auto-progress.md", "w", encoding="utf-8") as f:
    f.write(content)
