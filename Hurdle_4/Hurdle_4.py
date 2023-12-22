def turn_right():
  turn_left()
  turn_left()
  turn_left()
while not at_goal():
  while wall_in_front() and not right_is_clear():
      turn_left()
      if not wall_in_front():
          move()
  while wall_on_right() and not at_goal():
      if front_is_clear():
          move()
      else:
          turn_left()
  while not wall_on_right():
      turn_right()
      move()

