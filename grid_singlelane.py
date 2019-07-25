from __future__ import print_function

import sys
import tulip.gridworld as gw
from tulip import synth

with open("singlelane.txt", "r") as f:
    lane = gw.GridWorld(f.read(), prefix="Y")

print(lane)


spc = lane.spec()
spc.moore = False
spc.qinit = r'\A \E'
if not synth.is_realizable(spc, solver='omega'):
    print("Not realizable.")
else:
    ctrl = synth.synthesize(spc, solver='omega')
    if not ctrl.save('ctrl-singlelane.png'):
        print(ctrl)

