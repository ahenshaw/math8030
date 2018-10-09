\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2 x12 + 3 x13 + 3 x15 + 2 x23 + 4 x24 + x34 + 2 x35 + x56 + 3 x46
Subject To
 R0: x12 + x13 + x15 = 1
 R1: - x12 + x23 + x24 = 3
 R2: - x13 - x23 + x34 + x35 = 0
 R3: - x15 - x35 + x56 = 0
 R4: - x24 - x34 + x46 = 0
 R5: - x56 - x46 = -4
Bounds
End
