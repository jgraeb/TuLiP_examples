from __future__ import print_function

import sys
import tulip.gridworld as gw
from tulip import synth

# import specified gridworld from textfile - singlelane.txt
with open("singlelane.txt", "r") as f:
    lane = gw.GridWorld(f.read(), prefix="Y")
print(lane)

# adding environment - traffic light is red or not red
env_vars = {'red'}
env_init = set()                # empty set
env_prog = '!red'
env_safe = set()                # empty set
#lane[0,0] = 'init'
#lane[0,5] = 'goal'
lane.atomic_propositions.add_from({'signal', 'goal'})
#lane.states.add(lane[0,0], ap={'init'})
lane.states.add(lane[0,2], ap={'signal'})
lane.states.add(lane[0,5], ap={'goal'})

# specs
sys_vars = set()#'X0reach'}          # infer the rest from TS
sys_init = set()#{'X0reach'}
sys_prog = {'goal'}             # []<>Goal
sys_safe = {'((signal && red)->X(signal)) && (goal -> X(goal))'}
#sys_prog |= {'X0reach'}
# @specs_setup_section_end@

# synthesis and plot result
spc = lane.spec()
spc.moore = False
spc.qinit = r'\A \E'
if not synth.is_realizable(spc, solver='omega'):
    print("Not realizable.")
else:
    ctrl = synth.synthesize(spc, solver='omega')
    if not ctrl.save('ctrl-singlelane_signal.png'):
        print(ctrl)

