# CMPT 417/427
# Rubiks Cube solving
# General cube class
# Ryan Vansickle

# import numpy as np
# based on preil research, standard python lists are actually
# faster than numpy here unless we go to big n

class Cube:
  n = 0
  # dimensions of cube
  path = []
  # path to solution (if exists, to be passed to next search step instances)
  
  # 6 faces of cube, (F)ore (B)ack (L)eft (R)ight (U)p (D)own
  F = [[]]
  B = [[]]
  L = [[]]
  R = [[]]
  U = [[]]
  D = [[]]
    
  
  
  def __init__(self, n, [F, B, L, R, U, D]):
    self.n = n
    