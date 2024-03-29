class ExampleFSM(object):
    """Mealy transducer.

    Internal states are integers, the current state
    is stored in the attribute "state".
    To take a transition, call method "move".

    The names of input variables are stored in the
    attribute "input_vars".

    Automatically generated by tulip.dumpsmach on 2019-08-06 19:37:37 UTC
    To learn more about TuLiP, visit http://tulip-control.org
    """
    def __init__(self):
        self.state = 15
        self.input_vars = ['red', 'yellow', 'green']

    def move(self, red, yellow, green):
        """Given inputs, take move and return outputs.

        @rtype: dict
        @return: dictionary with keys of the output variable names:
            ['goal', 'signal', 'loc']
        """
        output = dict()
        if self.state == 0:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 3

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 4

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 5

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            else:
                self._error(red, yellow, green)
        elif self.state == 1:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 3

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 4

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 5

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            else:
                self._error(red, yellow, green)
        elif self.state == 2:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 3

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 4

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 5

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X1'
            else:
                self._error(red, yellow, green)
        elif self.state == 3:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 6

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 7

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 8

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            else:
                self._error(red, yellow, green)
        elif self.state == 4:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 6

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 7

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 8

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            else:
                self._error(red, yellow, green)
        elif self.state == 5:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 6

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 7

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 8

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            else:
                self._error(red, yellow, green)
        elif self.state == 6:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 6

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 7

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 8

                output["goal"] = False
                output["signal"] = True
                output["loc"] = 'X2'
            else:
                self._error(red, yellow, green)
        elif self.state == 7:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 9

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 10

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 11

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            else:
                self._error(red, yellow, green)
        elif self.state == 8:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 9

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 10

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 11

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X3'
            else:
                self._error(red, yellow, green)
        elif self.state == 9:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 10:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 11:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 12:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 13:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 14:
            if (green == False) and (red == True) and (yellow == False):
                self.state = 12

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == True) and (red == False) and (yellow == False):
                self.state = 13

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 14

                output["goal"] = True
                output["signal"] = False
                output["loc"] = 'X4'
            else:
                self._error(red, yellow, green)
        elif self.state == 15:
            if (green == True) and (red == False) and (yellow == False):
                self.state = 0

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X0'
            elif (green == False) and (red == False) and (yellow == True):
                self.state = 1

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X0'
            elif (green == False) and (red == True) and (yellow == False):
                self.state = 2

                output["goal"] = False
                output["signal"] = False
                output["loc"] = 'X0'
            else:
                self._error(red, yellow, green)
        else:
            raise Exception("Unrecognized internal state: " + str(self.state))
        return output

    def _error(self, red, yellow, green):
        raise ValueError("Unrecognized input: " + (
            "red = {red}; "
            "yellow = {yellow}; "
            "green = {green}; ").format(
                red=red,
                yellow=yellow,
                green=green))
