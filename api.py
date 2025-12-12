import time
import requests

info = {
  'anime_id': 21,
  'one_pace': {
    'episode_count': 475,
    'filler_count': 0,
    'episode_length': 17,
    'opening_length': 0,
    'ending_length': 0
  },
  'one_piece': {
    'episode_count': 1151,
    'filler_count': 91,
    'episode_length': 23.5,
    'opening_length': 1.75,
    'ending_length': 1.25
  }
}

def get_series_key(one_pace: bool):
  if one_pace:
    return 'one_pace'
  else:
    return 'one_piece'

def get_episode_length(one_pace: bool, opening: bool, ending: bool, speed: float):
  key = get_series_key(one_pace)
  length = info[key]['episode_length']

  if not opening:
    length -= info[key]['opening_length']
  if not ending:
    length -= info[key]['ending_length']

  return length / speed

def get_episodes(real_data: bool, one_pace: bool):
  if one_pace:
    return info['one_pace']['episode_count'], 0
  if not real_data:
    return info['one_piece']['episode_count'], info['one_piece']['filler_count']

  anime_id = info.get('anime_id')
  filler_count = 0
  episode_count = 0
  page = 1
  headers = {
    "User-Agent": "OnePacer/1.0"
  }

  while True:
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/episodes?page={page}&limit=100"
    try:
      response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
      print("Request failed:", e)
      break

    if response.status_code == 429:
      print("Rate limited by the server, waiting 5 seconds...")
      time.sleep(5)
      continue
    elif response.status_code != 200:
      print(f"Failed to fetch data (status {response.status_code})")
      break

    data = response.json()
    episodes = data.get('data', [])

    for episode in episodes:
      if episode.get('filler'):
        filler_count += 1
      episode_count += 1

    if data.get('pagination', {}).get('has_next_page'):
      page += 1
      time.sleep(0.5)
    else:
      break
  
  return episode_count, filler_count