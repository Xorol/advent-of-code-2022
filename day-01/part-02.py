BLANK_LINE = '\n'

with open("input.txt", "r") as f:
  data = f.readlines()

lncount = 0
elves = [0]

for line in data:
  if line == BLANK_LINE:
    elves.append(0)
    lncount += 1
    continue
  elves[lncount] += int(line[:-1])

print(sum(sorted(elves, reverse=True)[:3]))
