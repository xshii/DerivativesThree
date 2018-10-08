class Equation:
    _variableList = []
    _outputList = []
    _diffPoint = []
    _equationList = []
    _dx = []
    _dy = []
    method = ""

    def __repr__(self):
        beginStr = "Get derivatives of "
        dxStr = self._dx.__repr__()
        midStr = " with respect to "
        dyStr = self._dy.__repr__()
        endStr = " at point " + self._diffPoint.__repr__()
        return "\n".join([beginStr, dxStr,midStr,dyStr,endStr])

    def getVariableList(self):
        return self._variableList
    def getOutputList(self):
        return self._outputList
    def getDiffPoint(self):
        return self._diffPoint
    def getEquationList(self):
        return self._equationList

    def addVariable(self, name=""):
        self._variableList.append(name)

    def addOutput(self, name=""):
        self._outputList.append(name)

    def addEquation(self,equation=""):
        self._equationList.append(equation)

    def addDiffPoint(self, point=[]):
        assert point.__len__() == self._variableList.__len__()
        self._diffPoint = point

    def dYdX(self, X = [], Y = []):
        self._dx = X
        self._dy = Y
        pass



