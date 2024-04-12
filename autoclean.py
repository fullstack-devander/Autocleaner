import os

config = open('autoclean.conf', 'r')
paths = config.readlines()

for path in paths:
  folder = r"{}".format(path)
  print("Looking for: %s", folder)
  if os.path.exists(folder):
    content = [f for f in os.listdir(folder)]
    print(content)
  else:
    print("NOT EXISTS")