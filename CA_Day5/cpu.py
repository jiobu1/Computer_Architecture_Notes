"""CPU functionality."""

import sys
import operator

class CPU:
    """Main CPU class."""


    #load immediate (save the value)
    #constructing cpu and other functions

    def __init__(self):
        self.ram =  [0] * 256               # 256 bytes of memories
        self.reg = [0] * 8                  # 8 registers
        self.pc = 0                         # program counter
        self.halted = False                 # halt
        self.sp = 0xF4                      # stack pointer

    def ram_read(self, mar):               # MAR (Memory Address Register)
        return self.ram[mar]               # contains address being read or written to

    def ram_write(self, mdr, mar):         # MDR (Memory Data Register)
        self.ram[mar] = mdr                # data that was read or data to write

    def LDI(self):                         # store a value in a register
        self.reg[self.ram_read(self.pc+1)] = self.ram_read(self.pc+2)
        self.pc += 3

    def PRN(self):                         # print value in a register
        print(f'value: {self.reg[self.ram_read(self.pc+1)]}')
        self.pc += 2

    def HLT(self):                         # Halt
        self.halted = True
        self.pc += 1

    def PUSH(self):
        self.sp -= 1                      #decrement by 1
        reg_a = self.ram_read(self.pc+1)
        self.ram_write(self.reg[reg_a], self.sp) #save the value in that RAM address
        self.pc += 2

    def POP(self):
        if self.sp == 0xF4:
            return 'Stack is Empty'
        self.reg[self.ram_read(self.pc+1)] = self.ram_read(self.sp)    #assign the value to that register
        self.sp += 1                                                   #increment stack pointer by one
        self.pc +=2

    #CALL return addr gets pushed on the stack
    def CALL(self):
        self.reg[self.sp] -= 1

        return_addr = self.ram_read(self.pc+2)
        self.ram_write(return_addr, self.reg[self.sp])

        reg_a = self.ram_read(self.pc+1)
        subroutine_addr = self.reg[reg_a]
        self.pc = subroutine_addr

    #RETURN return addr gets popped off the stack
    def RET(self):
        return_addr = self.reg[self.sp]
        self.reg[self.sp] += 1
        self.pc = return_addr

    def MUL(self):
        operand_a = self.ram_read(self.pc+1)
        operand_b = self.ram_read(self.pc+2)
        self.alu("MUL", operand_a, operand_b)
        self.pc +=3


    # Run the CPU
    def run(self):
        self.pc = 0
        #hash table because it's cooler than if-elif
        run_instruction = {
            1: self.HLT,
            17: self.RET,
            71: self.PRN,
            69: self.PUSH,
            70: self.POP,
            80: self.CALL,
            130: self.LDI,
            162: self.MUL,
        }

        while not self.halted:
            IR = self.ram_read(self.pc)     # Instruction Register (IR)
            run_instruction[IR]()
            self.trace()

        self.halted = True

    def load(self):
        address = 0
        with open(sys.argv[1]) as func:
            for line in func:
                string_val = line.split("#")[0].strip()
                if string_val == '':
                    continue
                v = int(string_val, 2)
                self.ram[address] = v
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        #again, hash table because it is cooler than if-else
        ops = {
            "ADD" : lambda x,y: x+y,
            "MUL" : lambda x,y: x*y,
            "DIV" : lambda x,y: x/y,
            "SUB" : lambda x,y: x-y
        }
        try:
            self.reg[reg_a] = ops[op](self.reg[reg_a], self.reg[reg_b])
            return self.reg[reg_a]
        except:
            raise("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
