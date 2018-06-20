from PyQt5 import QtGui, QtCore
import pyqtgraph as pg

class LivePlot:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', (800, 600))
        self.window_title = kwargs.get('window_title', 'LivePlot')

        self.app = QtGui.QApplication([])
        self.plot_widget = pg.PlotWidget(background='w')
        self.plot_item = self.plot_widget.getPlotItem()


        '''
        plots =
            {
                name: {
                    color: C,
                    points: [(x, y)]
                }
            }
        '''
        self.plots = {}

    def show(self):
        self.plot_widget.show()

    def clear(self, name=None):
        """
        Removes a scatter group with the specified name.
        Removes all if no name is specified.

        Parameters
        ----------
        name : key
            Name of plot group
        """
        if name:
            self.plots.pop(name)
        else:
            self.plots = {}

        self.plot_item.clear()

    def set_axis(self, x=(-5, 5), y=(-2, 10)):
        self.plot_item.setRange(xRange=x, yRange=y)

    def update(self):
        """
        Re-draw plot groups.
        """
        for k, v in self.plots.items():
            color = v['color']
            points = v['points']
            plot_data_item = v['plot_data_item']

            if not points:
                continue

            xs, ys = [], []
            for x, y in points:
                xs.append(x)
                ys.append(y)

            if plot_data_item:
                data_item = plot_data_item

                if isinstance(data_item, pg.PlotDataItem):
                    data_item.setData(xs, ys)
                else:
                    data_item.addPoints(xs, ys)
            else:
                data_item = self.plot_data_item(xs, ys, size=10, pen=pg.mkPen(None))

                if color != None:
                    data_item.setBrush(pg.mkBrush(color))
                else:
                    data_item.setBrush(
                            QtGui.QBrush(
                                QtGui.QColor(
                                    QtCore.qrand() % 256,
                                    QtCore.qrand() % 256,
                                    QtCore.qrand() % 256)))

            self.plot_item.addItem(data_item)

        pg.QtGui.QApplication.processEvents()

    def add_points( self , name, data
                  , color=None
                  , plot_data_item=None):
        """
        Adds points of data to plot group _name_.

        Parameters
        ----------
        name : string
            Name of point group
        data : (x, y) or [(x, y)]
            Tuple of list or scalar x, y coordinates
        """
        if not isinstance(data, tuple) and not isinstance(data, list):
            raise TypeError('Expected a tuple of x, y or list of tuples.')

        if name in self.plots:

            if isinstance(data, list):
                self.plots[name]['points'].extend(data)
            else:
                self.plots[name]['points'].append(data)

        else:
            if isinstance(data, list):
                self.plots[name] = { 'color': color, 'points': data }
            else:
                self.plots[name] = { 'color': color, 'points': [data] }

            self.plots[name]['plot_data_item'] = plot_data_item






