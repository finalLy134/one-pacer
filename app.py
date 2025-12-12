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
    answers.get(key) for key in ['real_data', 'one_pace', 'per_day', 'current', 'fillers', 'openings', 'endings', 'speed']
  )

  utils.clear()
  print(drawing)
  print("Calculating it for you...\n\n")

  episode_count, filler_count = api.get_episodes(real_data, one_pace)
  remaining = episode_count - current
  if not fillers:
    remaining -= filler_count
  time_remaining = remaining * api.get_episode_length(one_pace, openings, endings, speed)

  days = int(time_remaining // 1440)
  hours = int((time_remaining % 1440) // 60)
  minutes = int(time_remaining % 60)

  print(f"It will take you approximately {days} days, {hours} hours and {minutes} minutes to finish One Piece.")