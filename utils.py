def to_chess_notation(x, y):
  files = 'abcdefgh'
  rank = x+1
  file = files[y]

  return f"{file}{rank}"