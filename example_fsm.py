#
# Running this file gives the FSM for the system
# "red": 0 is without the red light -> car transitions from X0 to X4 step by step
# "red": 1 is with the red light -> car transitions from X0 to X1 and X2 and stays there

from __future__ import print_function
from singlelane_signal_fsm import ExampleFSM

M = ExampleFSM()
print('In order, the input variables: '+', '.join(M.input_vars))
for i in range(5):
    input_values = {"red": 0}
    print(M.move(**input_values))