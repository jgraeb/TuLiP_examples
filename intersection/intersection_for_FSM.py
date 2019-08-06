# Author: Josefine Graebener (jgraeb)
# 
# Car driving through an intersection and turning left
# Environment is the traffic signal (red or !red) and if the path is clear (!notclear or clear)
#
#
# The synthesized FSM for this example is based on the states of the car and not the exact location:
#   Approaching Intersection X1
#   Signal                   X2
#   Entering Intersection    X3
#   Turn Left                X4
#   Leave Intersection       X5


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
sys.states.add_from(['X0','X1', 'X2', 'X3', 'X4','X5','X10','X100'])
sys.states.initial.add('X1')    # start in state X1 (Approaching)

# Define the allowable transitions
#sys.transitions.add_comb({'X0'}, {'X1','X0'})
sys.transitions.add_comb({'X1'}, {'X2','X1','X0'})
sys.transitions.add_comb({'X2'}, {'X3','X2'})
sys.transitions.add_comb({'X3'}, {'X10','X4'})
sys.transitions.add_comb({'X4'}, {'X4','X5','X100'})
sys.transitions.add_comb({'X5'}, {'X5','X100'})
#sys.transitions.add_comb({'X0'}, {'X1'})
#sys.transitions.add_comb({'X10'}, {'X4'})
#sys.transitions.add_comb({'X100'}, {'X5'})

# Add atomic propositions to the states
sys.atomic_propositions.add_from({'approach','signal','enter','turnleft','leave'})
#sys.states.add('X0', ap={'init'})
sys.states.add('X1', ap={'approach'})
sys.states.add('X2', ap={'signal'})
sys.states.add('X3', ap={'enter'})
sys.states.add('X4', ap={'turnleft'})
#sys.states.add('X4', ap={'straight'})
sys.states.add('X5', ap={'leave'})
#sys.states.add('X0', ap={'stop1'})
#sys.states.add('X10', ap={'stop2'})
#sys.states.add('X100', ap={'stop3'})

# if IPython and Matplotlib available
# sys.plot() 

# @environ_section@
env_vars = {'red'}                           # light can be red or not red
env_vars |= {'road_clear'}                   # road is clear or not clear
#env_vars |= {'crosswalk_clear'}              # crosswalk is clear or not clear
#env_vars |= {'intersection_clear'}           # intersection is clear or not clear
#env_vars |= {'exitroad_clear'}               # exit road is clear or not clear
env_init = set()                             # empty set
env_prog = {'road_clear'}                    # always eventually road is clear
#env_prog |= {'!red && crosswalk_clear'}      # always eventually not red signal and clear crosswalk
#env_prog |= {'intersection_clear'}           # always eventually intersection is clear
#env_prog |= {'exitroad_clear'}               # always eventually exitroad is clear
env_safe = set()                             # empty set

# System specification
# @specs_setup_section@
# Augment the system description to make it GR(1)
sys_vars = set()         # infer the rest from TS
sys_init = set()         # initialized as true
sys_prog = {'leave'}             # []<>leave intersection
sys_safe = {'((approach && !road_clear) -> X(approach))'}# && ((stop1 && !road_clear) -> X(stop1)) && ((!crosswalk_clear && signal) -> X(signal)) && ((enter && !intersection_clear) -> X(enter)) && ((turnleft && !exitroad_clear)-> X(stop3)) && ((leave && !exitroad_clear)->X(stop3)) && ((stop3 && !exitroad_clear)->stop3)'}


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
if not ctrl.save('intersection_for_fsm_signal.png'):
    print(ctrl)
# @plot_print_end@

# appended as in documentation chapter 6
dumpsmach.write_python_case("intersection_for_fsm_signal_fsm.py", ctrl, classname="ExampleFSM")
