from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from pandas import read_csv


class PlotGraph:
    def __init__(self, df, plotname):
        self.name = plotname
        self.p = figure(x_axis_type="datetime", height=100, width=500,
                        sizing_mode="scale_width", title="Motion graph")
        self.p.yaxis.minor_tick_line_color = None
        self.p.ygrid[0].ticker.desired_num_ticks = 1
        df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
        df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

        hover = HoverTool(tooltips=[("Start", "@Start_string"),
                                    ("End", "@End_string")])
        self.p.add_tools(hover)

        self.p.quad(source=ColumnDataSource(df), left="Start",
                    right="End", bottom=0, top=1, color="red")

        output_file(self.name + ".html")

    def show(self):
        show(self.p)


if __name__ == '__main__':
    data = read_csv("sample_times.csv", parse_dates=["Start", "End"])
    sample_graph = PlotGraph(data, "sample_graph")
    sample_graph.show()
