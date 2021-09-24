import sys
import math

class CPU(object):
    def __init__(self, a, b, c, d):
        self.registers = {'a':a, 'b':b, 'c':c, 'd':d, "pc":0}
    def GetValue(self, operand):
        if operand in self.registers:
            return self.registers[operand]
        return int(operand)
        
    def Run(self, assembly, n):
        while self.registers["pc"] < n:  
            instruction=assembly[self.registers["pc"]].split(' ')
            if "MOV"==instruction[0]:
                self.registers[instruction[1]] = self.GetValue(instruction[2])
                self.registers["pc"]+=1
            elif "ADD"==instruction[0]:
                self.registers[instruction[1]] = self.GetValue(instruction[2]) + self.GetValue(instruction[3])
                self.registers["pc"]+=1
            elif "SUB"==instruction[0]:
                self.registers[instruction[1]] = self.GetValue(instruction[2]) - self.GetValue(instruction[3])
                self.registers["pc"]+=1
            elif "JNE"==instruction[0]:
                self.registers["pc"]+=1
                if self.registers[instruction[2]] != self.GetValue(instruction[3]):
                    self.registers["pc"]=self.GetValue(instruction[1])

        
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b, c, d = [int(i) for i in input().split()]
n = int(input())
instructions=[]
for i in range(n):
    instructions.append(input())
cpu=CPU(a, b, c, d)
cpu.Run(instructions, len(instructions))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(cpu.registers['a']) + ' '+ str(cpu.registers['b']) + ' '+ str(cpu.registers['c']) + ' '+ str(cpu.registers['d']))
