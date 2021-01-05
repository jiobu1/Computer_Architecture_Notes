import sys

# a machine that simply executes an instruction

# op-code - they represent the instruction that is supposed to be executed
PRINT_HI = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 # save a value in a given register
PRINT_REGISTER = 5 # print value stored in register
ADD = 6 # takes in two registers, A and B and adds both values contained in the registers and stores it in reg A
PUSH = 7 # takes in a register and stores the value in that register on top of the stack
POP = 8 # takes in a register and stores the topmost element in the stack in it
CALL = 9
RET = 10
PRINT_SUBROUTINE_INSTRUCTION = 11

def load_memory():
    program = [
        PRINT_HI,
        SAVE, # SAVE 65 into reg 2
        7,
        2,
        CALL, # jump to the address stored in register 2
        2,
        HALT,  # stop the program
        PRINT_SUBROUTINE_INSTRUCTION,
        SAVE,
        500,
        0,
        RET # jump back to address stored in the top of the stack (7, which is HALT)
    ]

    space_for_stack = 128 - len(program)
    memory = program + [0] * space_for_stack
    return memory

memory = load_memory()
program_counter = 0 # points to the current instruction we need to execute next
running = True
registers = [0] * 8
stack_pointer_register = 7 # register number that contains address of stack pointer
registers[stack_pointer_register] = len(memory) - 1

# keep looping while not halted
while running:
    command_to_execute = memory[program_counter]

    if command_to_execute == PRINT_HI:
        print("hi")
        program_counter += 1
    elif command_to_execute == PRINT_NUM:
        number_to_print = memory[program_counter + 1]
        print(f"{number_to_print}")
        program_counter += 2
    elif command_to_execute == HALT:
        running = False
        program_counter += 1
    elif command_to_execute == SAVE:
        value_to_save = memory[program_counter + 1]
        register_to_save_it_in = memory[program_counter + 2]
        registers[register_to_save_it_in] = value_to_save
        program_counter += 3
    elif command_to_execute == PRINT_REGISTER:
        register_to_print = memory[program_counter + 1]
        print(f"{registers[register_to_print]}")
        program_counter += 2
    elif command_to_execute == ADD:
        register_a = memory[program_counter + 1]
        register_b = memory[program_counter + 2]
        sum_of_registers = registers[register_a] + registers[register_b]
        registers[register_a] = sum_of_registers
        program_counter += 3
    elif command_to_execute == PUSH:
        registers[stack_pointer_register] -= 1 # decrement stack pointer
        register_to_get_value_in = memory[program_counter + 1]
        value_in_register = registers[register_to_get_value_in]
        memory[registers[stack_pointer_register]] = value_in_register
        program_counter += 2
    elif command_to_execute == POP:
        register_to_pop_value_in = memory[program_counter + 1]
        registers[register_to_pop_value_in] = memory[registers[stack_pointer_register]]
        registers[stack_pointer_register] += 1
        program_counter += 2
    elif command_to_execute == CALL:
        # stores the address of the next instruction on the top of the stack
        registers[stack_pointer_register] -= 1 # self.registers[SP] -= 1
        address_of_next_instruction = program_counter + 2
        memory[registers[stack_pointer_register]] = address_of_next_instruction
        # It jumps to the address stored in that register
        register_to_get_address_from = memory[program_counter + 1] 
        program_counter = registers[register_to_get_address_from] #self.pc = self.registers[operand_a]
    elif command_to_execute == RET:
        # doesn't take in any operands, set the program counter to the topmost element of the stack and pop it
        program_counter = memory[registers[stack_pointer_register]]
        registers[stack_pointer_register] += 1 #
    elif command_to_execute == PRINT_SUBROUTINE_INSTRUCTION:
        print("I'm in a subroutine")
        program_counter += 1
    else:
        print(f"Unknown instruction {command_to_execute}")
        sys.exit(1)

print(f"registers: {registers}")
print(f"memory: {memory}")