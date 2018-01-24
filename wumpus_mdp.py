import math
class WumpusMDP:
  # wall_locations is a list of (x,y) pairs
  # pit_locations is a list of (x,y) pairs
  # wumnpus_location is an (x,y) pair
  # gold_location is an (x,y) pair
  # start_location is an (x,y) pair representing the start location of the agent


  def __init__(self, wall_locations, pit_locations, wumpus_location, gold_location, start_location):
    self.wall_locations = wall_locations
    self.pit_locations = pit_locations
    self.wumpus_location = wumpus_location
    self.gold_location = gold_location
    self.start_location = start_location
    self.states = self.get_states()
    pass

  def A(self):
    return ['do_nothing','left','right','up','down','shoot_left','shoot_right','shoot_up','shoot_down']
    pass # return list of actions

  def S(self):
    return self.states
    pass # return list of states

  def P(self, s, a, u):

    if ((s[4] == 0 and ((u[4] == 0 and not ((u[0], u[1]) in self.pit_locations or (((u[0], u[1]) == self.wumpus_location) and s[2] == 1))) or\
                        (u[4] == 1 and (((u[0], u[1]) in self.pit_locations) or ((u[0], u[1]) == self.wumpus_location) and s[2] == 1)))) or\
        (s[4] == 1 and u[4] == 1)) and (s[2], s[3]) == (u[2], u[3]) and (s[5] == u[5] or u[5] == s[5] + 1):
      if a == 'left' and s[1] == u[1] and s[0] == u[0] + 1:
        return 0.9
      if a == 'left' and s[1] == u[1] and s[0] == u[0] - 1:
        return 0.034
      if a == 'left' and s[1] == u[1] + 1 and s[0] == u[0]:
        return 0.033
      if a == 'left' and s[1] == u[1] - 1 and s[0] == u[0]:
        return 0.033

      if a == 'right' and s[1] == u[1] and s[0] == u[0] - 1:
        return 0.9
      if a == 'right' and s[1] == u[1] and s[0] == u[0] + 1:
        return 0.034
      if a == 'right' and s[1] == u[1] + 1 and s[0] == u[0]:
        return 0.033
      if a == 'right' and s[1] == u[1] - 1 and s[0] == u[0]:
        return 0.033

      if a == 'up' and s[1] == u[1] - 1 and s[0] == u[0]:
        return 0.9
      if a == 'up' and s[1] == u[1] + 1 and s[0] == u[0]:
        return 0.034
      if a == 'up' and s[1] == u[1] and s[0] == u[0] + 1:
        return 0.033
      if a == 'up' and s[1] == u[1] and s[0] == u[0] - 1:
        return 0.033

      if a == 'down' and s[1] == u[1] + 1 and s[0] == u[0]:
        return 0.9
      if a == 'down' and s[1] == u[1] - 1 and s[0] == u[0]:
        return 0.034
      if a == 'down' and s[1] == u[1] and s[0] == u[0] + 1:
        return 0.033
      if a == 'down' and s[1] == u[1] and s[0] == u[0] - 1:
        return 0.033

    if a == 'do_nothing' and s == u:
      return 1.0

    if s[4] == u[4] and s[5] == u[5]:
      if a == 'shoot_left':
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (0,0) and self.wumpus_location[0] < s[0] and self.wumpus_location[1] == s[1]:
          return 1.0
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (1,0) and not (self.wumpus_location[0] < s[0] and self.wumpus_location[1] == s[1]):
          return 1.0

      if a == 'shoot_right':
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (0,0) and self.wumpus_location[0] > s[0] and self.wumpus_location[1] == s[1]:
          return 1.0
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (1,0) and not (self.wumpus_location[0] > s[0] and self.wumpus_location[1] == s[1]):
          return 1.0

      if a == 'shoot_up':
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (0,0) and self.wumpus_location[0] == s[0] and self.wumpus_location[1] > s[1]:
          return 1.0
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (1,0) and not (self.wumpus_location[0] == s[0] and self.wumpus_location[1] > s[1]):
          return 1.0

      if a == 'shoot_down':
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (0,0) and self.wumpus_location[0] == s[0] and self.wumpus_location[1] < s[1]:
          return 1.0
        if (s[0], s[1]) == (u[0], u[1]) and (s[2], s[3]) == (1, 1) and (u[2], u[3]) == (1,0) and not (self.wumpus_location[0] == s[0] and self.wumpus_location[1] < s[1]):
          return 1.0
        
    return 0.0
    pass # return probability of transitioning from state s to state u when taking action a

  def R(self, s):
    if (s[0], s[1]) in self.pit_locations or ((s[0], s[1]) == self.wumpus_location and s[2] == 1) or s[4] == 1:
      return -100.0
    if (s[0], s[1]) == self.gold_location or s[5] == 1:
      return 100.0
    return -1.0
    pass # return reward for state s

  def initial_state(self):
    return (self.start_location[0], self.start_location[1], 1, 1, 0)
    pass # return initial state

  def gamma(self):
    return 0.99

  def get_states(self):
    max_h, max_v = 0, 0
    min_h, min_v = math.inf, math.inf
    for w in self.wall_locations:
      if w[0] > max_h:
        max_h = w[0]
      if w[0] < min_h:
        min_h = w[0]
      if w[1] > max_v:
        max_v = w[1]
      if w[1] < min_v:
        min_v = w[1]

    
    y = min_v + 1

    states = []
    
    while y < max_v:
      x = min_h + 1
      while x < max_h:
        states.append((x, y, 0, 0, 0, 0))
        states.append((x, y, 0, 1, 0, 0))
        states.append((x, y, 1, 0, 0, 0))
        states.append((x, y, 1, 1, 0, 0))
        states.append((x, y, 0, 0, 1, 0))
        states.append((x, y, 0, 1, 1, 0))
        states.append((x, y, 1, 0, 1, 0))
        states.append((x, y, 1, 1, 1, 0))
        states.append((x, y, 0, 0, 0, 1))
        states.append((x, y, 0, 1, 0, 1))
        states.append((x, y, 1, 0, 0, 1))
        states.append((x, y, 1, 1, 0, 1))
        states.append((x, y, 0, 0, 1, 1))
        states.append((x, y, 0, 1, 1, 1))
        states.append((x, y, 1, 0, 1, 1))
        states.append((x, y, 1, 1, 1, 1))
        x = x + 1
      y = y + 1
    return states
  

# EXAMPLE USAGE:
#mdp = WumpusMDP([(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(0,2),(0,1)], [(1,2)], (2,1), (2,2), (1,1))
