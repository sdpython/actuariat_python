# -*- coding: utf-8 -*-
"""

.. _l-example-one:

Quelques examples simples
=========================

.. contents::
    :local:

Case 1
++++++

Que calcule le programme suivant ?

"""
res = [[1]]
for i in range(1, 10):
    row = [1]
    for j in range(1, i):
        n = sum(res[-1][j - 1: j + 1])
        row.append(n)
    row.append(1)
    res.append(row)


print(res)

################################
# Un autre affichage peut peut-être aider.


import pprint
pprint.pprint(res)


########################################
# Case 2
# ++++++
import cProfile


nombres = [9, 7, 5, 4, 6, 7, 3, 1, 7, 8]


def moyenne(ens):
    return sum(ens) / len(ens)


def ecarttype(ens):
    var = [(n - moyenne(ens)) ** 2 for n in ens]
    return (sum(var) / len(var)) ** 0.5


print(moyenne(nombres))
print(ecarttype(nombres))

with cProfile.Profile() as pr:
    for n in range(100000):
        ecarttype(nombres)

pr.print_stats()


#########################################
# Case 3
# ++++++

def bizarre(ensemble):
    # premier zero
    ensemble.append(0)
    for i in range(len(ensemble)):
        if ensemble[i] == 0:
            return i


res = [1, 4, 5]
print("bizarre=", bizarre(res))
print("res=", res)
