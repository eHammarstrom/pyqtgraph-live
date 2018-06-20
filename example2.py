import lib as pg_live
import numpy as np
import time
import pyqtgraph as pg

live_graph = pg_live.LivePlot( size=(600, 400)
                             , window_title='Test')

live_graph.show()

xy2 = [ ( 1.0, 0.1 * i ) for i in range(10) ]

live_graph.set_axis((0, 2), (0, 1))

for point in xy2:
    live_graph.clear()
    live_graph.add_points('test2', point, color='r')
    live_graph.update()
    time.sleep(1)


input("")
