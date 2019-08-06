#
# Running this file gives the FSM for the system
# "red": 0 is without the red light -> car transitions from X2 to X3
# "red": 1 is with the red light -> car tstops at X2 and stays there
# "notclear": 0 the intersection is clear, the car continues (valid at X2 and X3)
# "notclear": 1 the intersection is not clear, it the car is in X2 or X3 it stays there
#

from __future__ import print_function
from intersection_signal_fsm import ExampleFSM

M = ExampleFSM()
print('In order, the input variables: '+', '.join(M.input_vars))
for i in range(5):
    input_values = {"red": 0,"notclear": 0}
    #input_values |= {"notclear": 0}
    print(M.move(**input_values))