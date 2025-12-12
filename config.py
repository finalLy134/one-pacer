drawing = """
    ╔═╗╔╗╔╔═╗  ╔═╗╔═╗╔═╗╔═╗╦═╗
    ║ ║║║║║╣   ╠═╝╠═╣║  ║╣ ╠╦╝
    ╚═╝╝╚╝╚═╝  ╩  ╩ ╩╚═╝╚═╝╩╚═
           Amitai Dvora
           
"""

questions: dict[dict] = {
  'real_data': {
    'question': 'Fetch real episode data from the web? (May take ~1 minute)',
    'options': [
      ('A', 'Yes', True),
      ('B', 'No', False),
    ]
  },
  'one_pace': {
    'question': 'Are you watching One Pace?',
    'options': [
      ('A', 'No', False),
      ('B', 'Yes', True),
    ]
  },
  'per_day': {
    'question': 'How much episodes are you willing to watch per day?',
    'options': [
      ('A', '1 per day', 1),
      ('B', '2 per day', 2),
      ('C', '3 per day', 3),
      ('D', '4 per day', 4),
      ('E', 'Other', {
        'question': 'Select episodes per day amount:',
        'min': 1,
        'max': 70
      })
    ]
  },
  'current': {
    'select': {
      'question': 'Which episode are you currently on?',
      'min': 1,
      'max': 1151
    }
  },
  'fillers': {
    'question': 'Do you skip filler episodes?',
    'options': [
      ('A', 'Yes', True),
      ('B', 'No', False),
    ]
  },
  'openings': {
    'question': 'Do you watch openings?',
    'options': [
      ('A', 'Yes', True),
      ('B', 'Only first time', False),
      ('C', 'No', False),
    ]
  },
  'endings': {
    'question': 'Do you watch endings?',
    'options': [
      ('A', 'Yes', True),
      ('B', 'Only first time', False),
      ('C', 'No', False),
    ]
  },
  'speed': {
    'question': 'What is your average episode speed?',
    'options': [
      ('A', '1.0x', 1.0),
      ('B', '1.25x', 1.25),
      ('C', '1.5x', 1.5),
      ('D', '2.0x', 2.0),
    ]
  },
}