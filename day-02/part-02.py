with open("input.txt", "r") as f:
  data = f.readlines()

outcome_scores = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

shape_scores = {
  "A": 1,
  "B": 2,
  "C": 3
}

win_guide = {
  "A": "B",
  "B": "C",
  "C": "A"
}

scores = []

for line in data:
  scores.append(0)
  op_play, outcome = line[:-1].split(" ")
  scores[-1] += outcome_scores[outcome]

  if outcome == "Y":
    scores[-1] += shape_scores[op_play]
  elif outcome == "Z":
    scores[-1] += shape_scores[win_guide[op_play]]
  else:
    scores[-1] +=  3 if (op_play == "A") else (shape_scores[op_play] + 2) % 3

print(sum(scores))
