from mdentropy.entropy import ncmi
from numpy import mean
from itertools import combinations_with_replacement as combinations


class TransferEntropy(object):
    def __call__(self, i):
        return mean([ncmi(self.n,
                          self.cD[d[1]][i[1]],
                          self.pD[d[0]][i[0]],
                          self.pD[d[1]][i[1]],
                          method=self.method)
                     if i[0] in self.cD[d[0]].columns and
                     i[1] in self.cD[d[1]].columns
                     else 0.0
                     for d in combinations(range(len(self.cD)), 2)])

    def __init__(self, cD, pD, nbins=24, method='chaowangjost'):
        self.cD = cD
        self.pD = pD
        self.n = nbins
        self.method = method
