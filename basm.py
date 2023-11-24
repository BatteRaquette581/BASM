from argparse import ArgumentParser

ADD = 0b0000
SUB = 0b0001
NEG = 0b0010
INC = 0b0011
DEC = 0b0100
PASS = 0b0101
AND = 0b0110
OR = 0b0111
XOR = 0b1000
NOT = 0b1001
ONE = NOT
ARS = 0b1010
LOS = 0b1011
ROT = 0b1100
ROC = 0b1101
ZER = 0b1110

IMD = 0b00000000
ALU = 0b01000000
COP = 0b10000000
COD = 0b11000000

FRM = 0b000
FR1 = 0b001
FR2 = 0b010
FR3 = 0b011
FR4 = 0b100
FR5 = 0b101
FR6 = 0b110
FIN = 0b111

TRM = 0b000000
TR1 = 0b001000
TR2 = 0b010000
TR3 = 0b011000
TR4 = 0b100000
TR5 = 0b101000
TR6 = 0b110000
TOU = 0b111000

NVR = 0b000
EQ0 = 0b001
LT0 = 0b010
LE0 = 0b011
ALS = 0b100
NEQ = 0b101
GE0 = 0b110
GT0 = 0b111

instructions = []
arg_parser = ArgumentParser(
    prog = "basm",
    description = "A BCPU assembly assembler."
)
arg_parser.add_argument("filepath")
with open(arg_parser.parse_args().filepath, "r") as f:
    mlcomment = False
    for l in f.readlines():
        b = []
        for elem in l.split():
            if elem.startswith("//"): break
            if "*/" in elem: mlcomment = False
            clean = elem.upper()
            try:
                clean = clean[:elem.index("/*")]
            except ValueError:
                pass
            try:
                clean = clean[elem.index("*/") + 2:]
            except ValueError:
                pass
            if not mlcomment and clean: b.append(eval(clean))
            if "/*" in elem: mlcomment = True
        if b: instructions.append(sum(b))
print("v3.0 hex words plain")
print(" ".join([hex(ins).lstrip("0x").zfill(2) for ins in instructions]))
