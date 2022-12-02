BLANK_LINE = '\n'

with open("input.txt", "r") as f:
  data = f.readlines()

running_total = 0
highest_elf = 0

for line in data:
  if line == BLANK_LINE:
    if running_total > highest_elf:
      highest_elf = running_total
    running_total = 0
    continue
  running_total += int(line[:-1])

print(highest_elf)
