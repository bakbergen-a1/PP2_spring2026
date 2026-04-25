import json

def load_leaderboard():
    try:
        return json.load(open("tsis3/leaderboard.json"))
    except:
        return []

def save_score(name, score, distance):
    try:
        data = json.load(open("tsis3/leaderboard.json"))
    except:
        data = []

    data.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    json.dump(data, open("tsis3/leaderboard.json", "w"))