# -*- coding: utf-8 -*-
array = []
for i in xrange(6):
    entrada = float(raw_input())
    if entrada > 0:
        array.append(entrada)
print "%d valores positivos" % len(array)
print "%.1f" % (sum(array)/float(len(array)))
