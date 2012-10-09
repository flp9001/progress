#!/usr/bin/env python

from __future__ import print_function

from random import randint,random
from time import sleep

from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, ShadyBar)
from progress.spinner import Spinner, PieSpinner, MoonSpinner, LineSpinner
from progress.counter import Counter, Countdown, Stack, Pie


for bar in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
    for i in bar(bar.__name__,suffix='%(percent).1f%% - %(td)s').iter(range(500)):
        sleep(0.01*random()+(500-i)*0.0001)
        #sleep(0.005)


for bar in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
    for i in bar(bar.__name__+' (period=0.5s)',period=0.5,suffix='%(percent).1f%% - %(eta)ds').iter(range(1000)):
        sleep(0.01*random())
        #sleep(0.005)
        


for bar in (IncrementalBar, ShadyBar):
    for i in bar(bar.__name__).iter(range(200)):
        sleep(0.02)

for spin in (Spinner, PieSpinner, MoonSpinner, LineSpinner):
    for i in spin(spin.__name__ + ' ').iter(range(30)):
        sleep(0.1)
    print()

for singleton in (Counter, Countdown, Stack, Pie):
    for i in singleton(singleton.__name__ + ' ').iter(range(100)):
        sleep(0.04)
    print()

bar = IncrementalBar('Random', backtrack=True, suffix='')
for i in range(100):
    bar.goto(randint(0, 100))
    sleep(0.1)
bar.finish()
