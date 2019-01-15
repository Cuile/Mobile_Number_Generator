# -*- coding: utf-8 -*-
import time

start = startTime = end = endTime = bar = None


def timing_starts():
    global start, startTime
    start = time.clock()
    startTime = time.time()


def timing_ends():
    global end, endTime
    end = time.clock()
    endTime = time.time()
    print("-------------------------------------------------------------------------")
    print("CPU Running time: {fs:.2f}s".format(fs=(end - start)))
    print("Script Running time: {fs:.2f}s".format(fs=(endTime - startTime)))
    print("-------------------------------------------------------------------------")
