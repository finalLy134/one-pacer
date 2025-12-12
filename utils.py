import os
import platform

def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def bold(txt):
  return f"\u001b[1m{txt}\u001b[0m"

def green(txt):
  return f"\u001b[32m{txt}\u001b[0m"

def bold_green(txt):
  return bold(green(txt))