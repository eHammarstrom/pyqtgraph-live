import lib as pg_live
import numpy as np
import time
import pyqtgraph as pg

live_graph = pg_live.LivePlot( size=(600, 400)
                             , window_title='Test')

live_graph.show()

xs = np.linspace(0, 1, 10).tolist()
ys = np.linspace(0, 1, 10).tolist()

xy = list(zip(xs, ys))

xy2 = [ ( 1.0, 0.1 * i ) for i in range(10) ]

pen = pg.mkPen('b')
brush = pg.mkBrush('g')
data_item = pg.PlotDataItem(pen=pen, brush=brush)

live_graph.add_points( 'test'
                     , xy
                     , plot_data_item=data_item)

live_graph.update()

for point in xy2:
    live_graph.add_points('test2', point, color='r')
    live_graph.update()
    time.sleep(1)


input("")
