# author: Josefine Graebener (jgraeb)
# 
# Tulip specification for a simple traffic light
# Light can change from green to yellow to red 
# Car will drive along the lane with the traffic light at X2 and only drive at green and yellow
#
#
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
sys.states.add_from(['X0', 'X1', 'X2', 'X3', 'X4'])
sys.states.initial.add('X0')    # start in state X0

# Define the allowable transitions
sys.transitions.add_comb({'X0'}, {'X1','X0'})
sys.transitions.add_comb({'X1'}, {'X0','X2','X1'})
sys.transitions.add_comb({'X2'}, {'X3', 'X1','X2'})
sys.transitions.add_comb({'X3'}, {'X4', 'X2','X3'})
sys.transitions.add_comb({'X4'}, {'X3','X4'})

# Add atomic propositions to the states
sys.atomic_propositions.add_from({'signal','goal'})
#sys.states.add('X0', ap={'init'})
sys.states.add('X2', ap={'signal'})
sys.states.add('X4', ap={'goal'})

# if IPython and Matplotlib available
# sys.plot() 

# @environ_section@
env_vars = {'red'}      # light can be green or red
env_vars |= {'yellow'} 
env_vars |= {'green'} 
env_init = set()          # empty set
env_prog = {'green'}      # always eventually green
env_safe = {'((red && !green && !yellow) || (green && !red && !yellow) || (yellow && !red && !green))'}        # never green and red at the same time


# System specification
#
# The system specification is that the car should drive to the goal
# but only cross from cell 2 into cell 3 if the light is green or yellow
#     []<> goal && []((in X2 && red) -> stay in state X2)

# @specs_setup_section@
# Augment the system description to make it GR(1)
sys_vars = set()          # infer the rest from TS
sys_init = set()
sys_prog = {'goal'}       # []<>goal
sys_safe = {'((signal && red)->X(signal)) && (goal -> X(goal))'}


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
if not ctrl.save('simpletrafficlight.png'):
    print(ctrl)
# @plot_print_end@

# appended as in documentation chapter 6
dumpsmach.write_python_case("simpletrafficlight_fsm.py", ctrl, classname="ExampleFSM")
