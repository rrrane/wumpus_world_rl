import solver
import wumpus_mdp

mdp = wumpus_mdp.WumpusMDP([(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(0,2),(0,1)], [(1,2)], (2,1), (2,2), (1,1))
s = solver.Solver(mdp)
policy = s.solve()

for p in policy:
  print(p, ':', policy[p])




