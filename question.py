import time
import keyboard
import config

from utils import bold_green, clear

class Question:
  def __init__(self, key: str, question: str, options: list[tuple[str, str, object]] = None, select: dict = None):
    """
    A Question can either have:
    - options: list of tuples (symbol, text, value)
    - select: dict with keys 'question', 'min', 'max'
    """
    self.key = key
    self.question = question
    self.options = options
    self.select = select
    self.run = True

    if not self.options and not self.select:
      raise ValueError("Question must have either options or select.")

  def is_options(self):
    return self.options is not None

  def is_select(self):
    return self.select is not None

  def update(self, selected: int):
    print(config.drawing)
    print(f"{self.key}.", self.question, end='\n\n')

    if self.is_options():
      for i, option in enumerate(self.options):
        symbol = option[0]
        option_msg = option[1]
        
        if i is selected:
          print(bold_green(f"({symbol}) {option_msg}"))
        else:
          print(f"({symbol}) {option_msg}")
      print("\n[↑/↓] Change, [ENTER] Confirm, [Q] Exit")

  def handle_options(self):
    selected = 0
    clear()
    self.update(selected)

    while self.run:
      try:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
          if event.name == 'q':
            print("Quitting...")
            self.run = False
            break
          else:
            if event.name == 'up':
              selected = (selected - 1) % len(self.options)
            elif event.name == 'down':
              selected = (selected + 1) % len(self.options)
            elif event.name == 'enter':
              return self.submit(selected)

            clear()
            self.update(selected)
      except KeyboardInterrupt:
        break

  def handle_selection(self, data):
    if not isinstance(data, dict):
      return data

    question = data['question']
    min_value = data['min']
    max_value = data['max']
    num_value = min_value

    hold_key = None
    hold_start = None

    while self.run:
      clear()
      print(config.drawing)
      print(question, end='\n\n')
      print(f"< {bold_green(num_value)} >")
      print("\n[←/→] Change, hold to accelerate, [ENTER] Confirm, [Q] Exit")

      event = keyboard.read_event(suppress=True)
      now = time.time()

      if event.event_type == "down":
        key = event.name

        if key == "q":
          self.run = False
          return None

        if key == "enter":
          return num_value

        if key in ("left", "right"):
          if hold_key != key:
            hold_key = key
            hold_start = now
          elapsed = now - hold_start
          if elapsed > 1.0:
            step = 25
          elif elapsed > 0.5:
            step = 5
          else:
            step = 1

          if key == "left":
            num_value = max(min_value, num_value - step)
          else:
            num_value = min(max_value, num_value + step)

      elif event.event_type == "up":
        if event.name in ("left", "right"):
          hold_key = None
          hold_start = None


  def submit(self, selected: int = 0):
    if self.is_options():
      value = self.options[selected][2]
      if isinstance(value, dict):
        return self.handle_selection(value)
      return value
    elif self.is_select():
      return self.select
