import random
import math

class Solver:
  def __init__(self, mdp):
    # any initialisation you might like
    self.mdp = mdp

  def solve(self):
    # Initialize
    gamma = self.mdp.gamma()

    # Arbitrarily select a policy pi
    pi = {s : random.choice(self.mdp.A()) for s in self.mdp.S()}

    # Initialize V(s) to 0 for all s in S
    V = {s : 0 for s in self.mdp.S()}

    # Construct set of rewards R
    R = set()
    
    for s in self.mdp.S():
      R.add(self.mdp.R(s))
      
    # Consider selected policy as suboptimal
    policy_stable = False

    # Iterate while optimal policy is obtained
    while not policy_stable:
      
      # Select very small theta (to check convergence)
      theta = 0.001
      delta = math.inf

      # Iterate until maximum difference between current and previous value goes below theta
      while delta >= theta:
        delta = 0
        # Calculate V(s) for all s for given policy pi
        for s in self.mdp.S():
          v = V[s]
          summation = 0
          for s_prime in self.mdp.S():
            for r in R:
              p = 0
              if(self.mdp.R(s_prime) == r):
                p = self.mdp.P(s, pi[s], s_prime)
              summation = summation + p*(r + gamma*V[s_prime])
          V[s] = summation
          delta = max(delta, abs(v - V[s]))
        
      
      # Look for better policy
      policy_stable = True
      for s in self.mdp.S():
        
        old_action = pi[s]
        maxval = V[s]
        max_action = old_action
        for a in self.mdp.A():
          summation = 0
          for s_prime in self.mdp.S():
            for r in R:
              p = 0
              if(self.mdp.R(s_prime) == r):
                p = self.mdp.P(s, a, s_prime)
              summation = summation + p*(r + gamma*V[s_prime])
          if summation > maxval:
            maxval = summation
            max_action = a

        if max_action != old_action:
          pi[s] = max_action
          policy_stable = False

    return pi


