# Car driving through an intersection and turning left
# Environment is the traffic signal (red or !red) and if the path is clear (!notclear or clear)
#
#  Goal at X7 and start at X1
#
#         | 7 |
#         | _ |
#         | 6 |
# --------  _  --------
# | 1 | 2 | 3 | 4 | 5 | 
#_________  _  ________
#         | 8 |   
#         | - |
#         | 9 |

from __future__ import print_function

import logging

from tulip import transys, spec, synth
# get FSM package
from tulip import dumpsmach

logging.basicConfig(level=logging.WARNING)
logging.getLogger('tulip.spec.lexyacc').setLevel(logging.WARNING)
logging.getLogger('tulip.synth').setLevel(logging.WARNING)
logging.getLogger('tulip.interfaces.omega').setLevel(logging.WARNING)

# Create a finite transition system
sys = transys.FTS()

# Define the states of the system
sys.states.add_from(['X1', 'X2', 'X3', 'X4','X5','X6','X7','X8','X9', 'X10'])
sys.states.initial.add('X1')    # start in state X0

# Define the allowable transitions
#sys.transitions.add_comb({'X0'}, {'X1','X0'})
sys.transitions.add_comb({'X1'}, {'X2','X1'})
sys.transitions.add_comb({'X2'}, {'X3', 'X1','X2'})
sys.transitions.add_comb({'X3'}, {'X4', 'X2','X3','X6','X8'})
sys.transitions.add_comb({'X4'}, {'X3','X4','X5'})
sys.transitions.add_comb({'X5'}, {'X5','X4'})
sys.transitions.add_comb({'X6'}, {'X3','X6','X7'})
sys.transitions.add_comb({'X7'}, {'X7','X6'})
sys.transitions.add_comb({'X8'}, {'X3','X8','X9'})
sys.transitions.add_comb({'X9'}, {'X9','X8'})


# Add atomic propositions to the states
sys.atomic_propositions.add_from({'signal','goal','intersection'})
#sys.states.add('X0', ap={'init'})
sys.states.add('X2', ap={'signal'})
sys.states.add('X3', ap={'intersection'})
sys.states.add('X7', ap={'goal'})

# if IPython and Matplotlib available
# sys.plot() 

# @environ_section@
env_vars = {'red'}#,'enoughtime'}      # light can be green or red
env_vars |= {'notclear'}
env_init = set()                # empty set
env_prog = {'!red && !notclear'}#, 'enoughtime'}      # always eventually red, always eventually green
#env_prog |= {'!notclear'}
env_safe = set()#{'((red && !green) || (green && !red))'}        # never green and red at the same time

# System specification
#
# The system specification is that the car should drive to the goal
# but only cross from cell 2 into cell 3 if the light is green
#     []<> goal && []((in X2 && red) -> stay in state X2)

#sys_vars = {'X0reach'}          # infer the rest from TS
#sys_init = {'X0reach'}
#sys_prog = {'home'}             # []<>home
#sys_safe = {'(X (X0reach) <-> lot) || (X0reach && !park)'}
#sys_prog |= {'X0reach'}


# @specs_setup_section@
# Augment the system description to make it GR(1)
sys_vars = set()#{'X0reach'}          # infer the rest from TS
sys_init = set()#{'X0reach'}          # initialized as true
sys_prog = {'goal'}             # []<>goal
sys_safe = {'((signal && notclear)->X(signal)) && ((intersection && notclear)-> X(intersection)) && ((signal && red)->X(signal)) && (goal -> X(goal))'} #((intersection && notclear)-> X(intersection)) &&
#sys_prog |= {'X0reach'}


# Create the specification
specs = spec.GRSpec(env_vars, sys_vars, env_init, sys_init,
                    env_safe, sys_safe, env_prog, sys_prog)

specs.moore = True
# synthesizer should find initial system values that satisfy
# `env_init /\ sys_init` and work, for every environment variable
# initial values that satisfy `env_init`.
specs.qinit = '\E \A'
ctrl = synth.synthesize(specs, sys=sys)
assert ctrl is not None, 'unrealizable'
# @synthesize_end@

#
# Generate a graphical representation of the controller for viewing,
# or a textual representation if pydot is missing.
#
# @plot_print@
if not ctrl.save('intersection_signal.png'):
    print(ctrl)
# @plot_print_end@

# appended as in documentation chapter 6
dumpsmach.write_python_case("intersection_signal_fsm.py", ctrl, classname="ExampleFSM")
