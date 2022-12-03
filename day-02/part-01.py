with open("input.txt", "r") as f:
  data = f.readlines()

shape_scores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

outcome_scores = {
  "LOSS": 0,
  "DRAW": 3,
  "WIN": 6
}

win_guide = {
  "A": "Y", 
  "B": "Z", 
  "C": "X"
}

correspondences = {
  "A": "X",
  "B": "Y",
  "C": "Z"
}

scores = []

for line in data:
  scores.append(0)
  op_play, sl_play = line[:-1].split(" ")
  scores[-1] += shape_scores[sl_play]
  
  if correspondences[op_play] == sl_play:
    scores[-1] += outcome_scores["DRAW"]
  elif win_guide[op_play] == sl_play:
    scores[-1] += outcome_scores["WIN"]
  else:
    scores[-1] += outcome_scores["LOSS"]

print(sum(scores))
