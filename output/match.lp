\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x11 + 3 x12 + 5 x13 - x14 + 2 x16 + 2 x21 + 3 x22 + 5 x23 + 6 x24 + x25
   + 3 x26 + x31 + x32 + 3 x33 + 7 x34 + x35 + 2 x36 + 7 x41 + x43 + x44
   + 5 x45 + 7 x46 + 5 x51 + 5 x52 + x53 + x54 + 2 x55 + x56 - x61 + 3 x62
   + 2 x63 + 8 x64 - x65 + 8 x66
Subject To
 R0: x11 + x12 + x13 + x14 + x15 + x16 = 1
 R1: x21 + x22 + x23 + x24 + x25 + x26 = 1
 R2: x31 + x32 + x33 + x34 + x35 + x36 = 1
 R3: x41 + x42 + x43 + x44 + x45 + x46 = 1
 R4: x51 + x52 + x53 + x54 + x55 + x56 = 1
 R5: x61 + x62 + x63 + x64 + x65 + x66 = 1
 R6: x11 + x21 + x31 + x41 + x51 + x61 = 1
 R7: x12 + x22 + x32 + x42 + x52 + x62 = 1
 R8: x13 + x23 + x33 + x43 + x53 + x63 = 1
 R9: x14 + x24 + x34 + x44 + x54 + x64 = 1
 R10: x15 + x25 + x35 + x45 + x55 + x65 = 1
 R11: x16 + x26 + x36 + x46 + x56 + x66 = 1
Bounds
Binaries
 x11 x12 x13 x14 x15 x16 x21 x22 x23 x24 x25 x26 x31 x32 x33 x34 x35 x36
 x41 x42 x43 x44 x45 x46 x51 x52 x53 x54 x55 x56 x61 x62 x63 x64 x65 x66
End
