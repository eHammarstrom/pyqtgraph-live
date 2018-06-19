from PyQt5 import QtGui
import pyqtgraph as pg

class LiveGraph:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', (800, 600))
        self.window_title = kwargs.get('window_title', 'LiveGraph')
        self.app = QtGui.QApplication([])

        self.plot_widget = pg.PlotWidget(background='w')
        self.plot_item = self.plot_widget.getPlotItem()


        '''
        plots =
            {
                name: {
                    color: C,
                    points: [x, y]
                }
            }
        '''
        self.plots = {}

    def show(self):
        self.plot_widget.show()

    def update(self):


    def add_points(self, name, data, color='r')
        """
        Adds points of data to plot group _name_.

        Parameters
        ----------
        name : string
            Name of point group
        data : (x, y) or ([x], [y])
            Tuple of list or scalar x, y coordinates
        """
        if name in self.plots:
            plot = self.plots[name]

            plot['color'] = color

            if isinstance(data, list):
                plot['points'].extend(data)
            else:
                plot['points'].append(data)

        else:
            if isinstance(data, list):
                plot = { 'color': color, 'points': data }
            else:
                plot = { 'color': color, 'points': [data] }






