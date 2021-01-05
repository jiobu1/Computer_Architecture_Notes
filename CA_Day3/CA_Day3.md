# Objective 1 - Describe the CPU stack and how it can be useful

### Overview
Most CPUs have a built-in stack that's useful for keeping temporary data, making subroutine calls, and handling interrupts. We'll learn how the stack operates. Since the number o registers is limited on a CPU, the stack is a useful place to store data temporarily. We'll examin a sample scenario where this is the case.

### Follow Along
The stack is a data structure so useful that CPU designers typically include it in their instruction sets.

Common uses are:
* Temporarily storing values if you need to free registers for other uses.
* Saving registers so they can be restored after a function call or interrupt handler.
* Allocating space for local variables in a subroutine call.

The minimalist stack consists of just a few things:
* An array for storing values (a chunk of RAM)
* A pointer to the top element of teh stack (known as the *stack pointer* or commonly `SP`).
* `PUSH` or `POP` instructions.
* Usually there's no specific instruction for peeking at the value at the top of the stack. A standard memory access instruction, such as `LD is used for taht purpose, if necessary.

In many architectures, the stack begins at a high address in RAM and `grows downward`. That is, the `SP` is *decremented* when additional items are pushed on the stack. If it helps, imagine that gravity is reversed and your stack is growing down from the ceiling as you push onto it.

To `PUSH` a value in a register onto the stack:
* Decrement `SP`
* Store the value in the register into RAM at the address stored in `SP`

To `POP` a value from the stack into aregister:
* Retrieve teh value from RAM at the address stored in `SP`, and store that value in the register.
* Increment `SP`

*Challenge*

What happens if you PUSH too many items on the stack?
What happens if you POP from an empty stack?
How can you detect if the stack is empty?
What information must be saved on the stack when the CPU is servicing an interrupt? Why?

# Objective 2 - Describe how interrupts work and why they're useful

### Overview
Normally the CPU is busy porcessing instructions, getting some tough, serious work done. But from time to time, a *peripheral*
(a device attached to the motherboard that's not part of the CPU) gets some work done and hast to notify the CPU that the work is complete.

IT does this through a mechanism called an *interrupt*. When the CPU needs to be notified, the peripheral raises a signal that the CPU detects. The CPU then stops its regular processing, and redirects to another program elsewhere in memory to *handle* (or servie) the interrupt.

Interrupts prevent the CPU from needing to continuously *poll* all the peripherals, freeing it up for computation.

When the interrupt comes in, the XPU saves allits work on the stack so that it can continue processing where it left off after the interrupt handler has completed.

We'll exame some common peripherals and show how they work with the CPU.

### Follow Along
*Note that is is a simplified view, but a good start on the basics*

When a peripheral needs attention from the CPU because it has complete a task, it gets the CPU's attention though an *interrupt*.

Before exectuing its regularyly-scheduled instruction, thw CPU checks to see if any interrupts have occurred.

If any have, the CPU saves all its work (i.e pushes all the registers and flags and program counter, and anything else it was working on onto the stack) and then begins executing the *interrupt handler* code which is located somewhere else in memory.

The job of the interrupt handler is to do whatever needs doing with the data that's arrivd from the peripheral. Sometimes it's adding a keystroke to a buffer. Sometimes it's telling the operating system that a block of data from teh disk is ready to hand over to a program.

Once the interrupt handler is complete, we say the interrupt has been *serviced*. Then all the registers and flags are popped off the stack and the CPU resumes execution where it left off, as if noting happened.

If a peripheral is low-bandwidth, i.e. it doesn't need to transfer more than a few bytes of data (keyboards, mice, etc), a common patter is:
* CPU receives an interrupt
* CPU looks into RAM (in the case of *memory-mapped peripherals*) to get the value from the peripheral.
    * Some CPUs are a concept called *I/O ports* to get the bytes from the peripheral instead.

For devices that need to send more than a few bytes of data to the CPU (disks, SSDs, etc) they use interrupts in conjunction with something called *Direct Memory Access* (DMA) to communicate with the CPU.

*Challenge*

Describe how a program would get input from a keyboard if interrupts did not exist.

Same question, except using interrupts.

How often would an external temperature sensor want to interrupt the CPU with new information? Why not more or less frequently?
























































