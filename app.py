import math
import api
import utils

from question import Question
from config import questions, drawing

stopped = False
answers = {}

for index, key in enumerate(questions.keys()):
  q = questions.get(key)
  q_txt = q.get('question')
  q_options = q.get('options')
  q_select = q.get('select')

  question = Question(int(index + 1), q_txt, q_options, q_select)

  if question.is_options():
    answers[key] = question.handle_options()
  else:
    answers[key] = question.handle_selection(question.select)

  if not question.run:
    stopped = True
    break

if not stopped:
  real_data, one_pace, per_day, current, fillers, openings, endings, speed = (
    answers.get(key)
    for key in [
      'real_data',
      'one_pace',
      'per_day',
      'current',
      'fillers',
      'openings',
      'endings',
      'speed'
    ]
  )

  utils.clear()
  print(drawing)
  print("Calculating it for you...\n")

  episode_count, filler_count = api.get_episodes(real_data, one_pace)

  remaining = episode_count - current
  if not fillers:
    remaining -= filler_count

  episode_minutes = api.get_episode_length(
    one_pace, openings, endings, speed
  )

  total_minutes = remaining * episode_minutes

  total_days_time = int(total_minutes // 1440)
  total_hours = int((total_minutes % 1440) // 60)
  total_minutes_left = int(total_minutes % 60)

  minutes_per_day = per_day * episode_minutes

  calendar_days = math.ceil(total_minutes / minutes_per_day)

  print(
    f"You will finish in ~{calendar_days} calendar days "
    f"watching {per_day} episode(s) per day.\n\n"
    f"Daily watch time: ~{minutes_per_day:.1f} minutes/day\n"
    f"Total watch time: "
    f"{total_days_time}d {total_hours}h {total_minutes_left}m."
  )