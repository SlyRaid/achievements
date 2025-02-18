import json
import requests


def get_users(api):
    response = requests.get(api)
    response.raise_for_status()
    return response.json()


def compare_achievements(data1, data2):
    unique_achievements = {}

    for username in data1.keys():
        achievements1 = data1[username]['achievements']
        achievements2 = data2.get(username, {}).get('achievements', {})

        if achievements1 != achievements2:
            added = {key: achievements2[key] for key in achievements2 if key not in achievements1}
            unique_achievements[username] = {'metadata': data1[username]['metadata'],
                                             'achievements': dict(added)}

    return unique_achievements


api_url = "https://base.media108.ru/training/sample/"
first_try = get_users(api_url)
second_try = get_users(api_url)
unique_achiev = compare_achievements(first_try, second_try)

print(json.dumps(unique_achiev, ensure_ascii=False, indent=2))

with open('new_sample.json', 'w', encoding='utf-8') as file:
    json.dump(unique_achiev, file, ensure_ascii=False, indent=2)
