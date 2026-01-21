def is_numeric_flexible(value):
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        try:
            float(value)
            return True
        except ValueError:
            return False
    return False

def is_in_range(value):
  return 0 < value <= 10

def add(a, b, c=0):
  if not is_numeric(a):
    return (-1)
  if not is_numeric(b):
    return (-1)
  if not is_numeric(c):
    return (-1)
  if not is_in_range(a):
    return (-2)
  if not is_in_range(b):
    return (-2)
  if not is_in_range(c):
    return (-2)
  try:
    return int(a + b) + int(c)
  except:
    return "error"
