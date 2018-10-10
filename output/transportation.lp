\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5 x11 + 2 x12 + 6 x13 + 5 x14 + 7 x21 + 12 x22 + 5 x23 + 6 x24 + 8 x31
   + 9 x32 + 7 x33 + 8 x34
Subject To
 R0: x11 + x12 + x13 + x14 = 25
 R1: x21 + x22 + x23 + x24 = 30
 R2: x31 + x32 + x33 + x34 = 50
 R3: x11 + x21 + x31 = 17
 R4: x12 + x22 + x32 = 38
 R5: x13 + x23 + x33 = 20
 R6: x14 + x24 + x34 = 30
Bounds
Generals
 x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34
End
