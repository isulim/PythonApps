from bokeh.plotting import figure, show, output_file


class PlotGraph:
    def __init__(self, df, plotname):
        self.name = plotname
        self.p = figure(x_axis_type="datetime", height=100, width=500,
                        sizing_mode="scale_width", title="Motion graph")
        self.p.yaxis.minor_tick_line_color = None
        self.p.ygrid[0].ticker.desired_num_ticks = 1
        self.p.quad(left=df["Start"], right=df["End"],
                    bottom=0, top=1, color="red")

        output_file(self.name + ".html")

    def show(self):
        show(self.p)
