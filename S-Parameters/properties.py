from manim import *

class GraphAreaPlot(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=6,
            x_labeled_nums=[0,2,3],
            **kwargs)

    def construct(self):
        self.setup_axes()
        curve1 = self.get_graph(lambda x: 4 * x - x ** 2, x_min=0, x_max=4)
        curve2 = self.get_graph(lambda x: 0.8 * x ** 2 - 3 * x + 4, x_min=0, x_max=4)
        line1 = self.get_vertical_line_to_graph(2, curve1, DashedLine, color=YELLOW)
        line2 = self.get_vertical_line_to_graph(3, curve1, DashedLine, color=YELLOW)
        area1 = self.get_area(curve1, 0.3, 0.6, dx_scaling=10, area_color=BLUE)
        area2 = self.get_area(curve2, 2, 3, bounded=curve1)
        self.play(FadeIn(curve1), FadeIn(curve2), FadeIn(line1), FadeIn(line2), FadeIn(area1), FadeIn(area2))