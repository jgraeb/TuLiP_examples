#
# TuLiP example of a car driving along a single lane
# -----------------------------------------
# |  init |       |       |       |  goal |
# -----------------------------------------
#

from __future__ import print_function

import logging

from tulip import transys, spec, synth


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
sys.atomic_propositions.add_from({'init', 'goal'})
sys.states.add('X0', ap={'init'})
sys.states.add('X4', ap={'goal'})


# @environ_section@
env_vars = set()               # empty set
env_init = set()               # empty set
env_prog = set()               # empty set
env_safe = set()               # empty set

# System specification
#
# The system specification is that the car should drive to the goal
#
#     []<> goal 

# @specs_setup_section@
# Augment the system description to make it GR(1)
sys_vars = set()        # infer the rest from TS
sys_init = set()          # initialized as true
sys_prog = {'goal'}             # []<>goal
sys_safe = {'goal -> X(goal)'}
#sys_prog |= {}#'X0reach'}

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
if not ctrl.save('singlelane.png'):
    print(ctrl)
# @plot_print_end@

