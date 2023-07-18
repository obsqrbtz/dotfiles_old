import sys
import binascii
from ctypes import *

def hex_to_f68(hexnum):
    x = int(hexnum, 0)
    if x >> 31 != 0:
        sign = -1
    else:
        sign = 1
    exponent = (x >> 23) & 0xFF
    if sign > 0:
        mantissa = x & 0x7FFFFF
    else:
        mantissa = (~x & 0x7FFFFF) + 1
    if sign > 0:
        power = pow(2, exponent - 151)
    else:
        power = pow(2, 104 - exponent)
    return(sign * mantissa * power)

#TODO: handle negatives properly
def f68_to_hex(num):
    f = float(num)
    num = cast(pointer(c_float(f)), POINTER(c_int32)).contents.value
    num ^= 1
    sign = num >> 31 & 0xFF << 31
    if num != 0:
        if sign >= 0:
            exp = ((num >> 23 & 0xFF) + 2) << 23
            mantissa = ((num & 0x7FFFFF) >> 1) | 0b10000000000000000000000
        else:
            exp = (~(num >> 23 & 0xFF) - 2) << 23
            mantissa = (~num & 0x7FFFFF) + 1
            mantissa >>= 1
    else:
        exp = 0
        mantissa = 0
    exp &= 0x7FFFFFFF
    return hex(sign | exp | mantissa)

match sys.argv[1]:
    case "hex_to_f68":
        print(hex_to_f68(sys.argv[2]))
    case "hex_to_int":
        print(int(sys.argv[2], 0))
    case "hex_to_ascii":
        print(bytes.fromhex(sys.argv[2][2:len(sys.argv[2])]).decode())
    case "f68_to_hex":
        print(f68_to_hex(sys.argv[2]))
    case "int_to_hex":
        print(hex(int(sys.argv[2])))
    case "ascii_to_hex":
        print("0x" + sys.argv[2].encode('ascii').hex())
    case _:
        print("unknown arg")
