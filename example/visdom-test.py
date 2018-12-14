import visdom
import numpy as np
import matplotlib.pyplot as plt
import time

#vis = visdom.Visdom(server='http://visdom')
vis = visdom.Visdom()

x = np.linspace(-3,3,200)
y = np.sin(x)

vis.text('Hello Spark, world!')
vis.line(X=x, Y=y, win='spark test')

