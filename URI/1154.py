#!/usr/bin/env python2.7
# encoding : utf-8
array = []
while True:
	entrada = int(raw_input())
	if entrada < 0:
		break
	else:
		array.append(entrada)
print "%.2f" % (sum(array)/float(len(array)))
