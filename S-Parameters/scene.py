### time python3 -m manim scene.py -r 256,144 --fps 60 -f intro
### time python3 -m manim scene.py -qm -f scene3
### Manim version: v0.12.0
### tex_mobject.py had to be modified to use BLUE instead of WHITE by default (for scene_efield_thru)

from manim import *
import math
from manim.utils.rate_functions import ease_in_out_sine
import numpy as np
from colour import Color
#config["tex_template"].add_to_preamble("\\usepackage{circuitikz}")
#config["tex_template"].add_to_preamble("\\documentclass[preview,dvisvgm]{standalone} ")

class TikzMobject(Text):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }


class logo(MovingCameraScene):
    def construct(self):
        circle_bg = Circle(radius=3.2, color=BLACK, fill_opacity=1).set_z_index(10)
        line_r = Line(start=LEFT*3,end=RIGHT*3).set_color(RED).set_z_index(12)
        arc_1 = Arc(radius=3, angle=-PI/2).rotate(-PI/2).shift(UP*3).set_color(RED).set_z_index(12)
        arc_2 = Arc(radius=3, angle=PI/2).rotate(PI/2).shift(DOWN*3).set_color(RED).set_z_index(12)
        circle_1 = Circle(radius=3*1.0).set_color(BLUE).set_z_index(13)
        #circle_15 = Circle(radius=3*0.75).shift(RIGHT*0.75)
        circle_2 = Circle(radius=3*0.5).shift(RIGHT*3*0.5).set_color(BLUE).set_z_index(13).rotate(PI)
        circle_3 = Circle(radius=3*0.25).shift(RIGHT*3*0.75).set_color(BLUE).set_z_index(13)
        self.play(Create(circle_bg))
        self.play(Create(circle_1),Create(circle_2),Create(circle_3),rate_func=smooth)
        #self.play(Create(circle_15))
        #self.play(Create(circle_2))
        #self.play(Create(circle_3))
        self.play(Create(line_r),rate_func=smooth)
        self.play(Create(arc_1),Create(arc_2),rate_func=smooth)
        a = Dot(RIGHT * 2).set_color(YELLOW).set_z_index(15).shift(LEFT*3+UP*2)
        #b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        #self.play(GrowFromCenter(a), FadeIn(b),run_time=0.5)
        self.wait(0.1)
        self.play(a.animate(path_arc=PI * 0.5).shift(RIGHT*2.7 +  DOWN*1),run_time=1.5,rate_func=smooth)
        #b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        #self.wait(0.2)
        self.play(a.animate(path_arc=PI * 1.6).shift(LEFT*0.7 + DOWN*1.5),run_time=1.6,rate_func=smooth)
        #b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        #self.wait(0.2)
        self.play(a.animate(path_arc=-PI * 0.5).move_to(RIGHT*3 + DOWN*0),run_time=1,rate_func=smooth)
        self.wait(7)
        self.play((self.camera.frame.animate).set_width(6.5),run_time=1.5,rate_func=smooth)
        self.wait(5)








class intro(MovingCameraScene):
    def construct(self):
        axes = Axes(
            x_range=[-8, 8, 0.1],
            y_range=[-2.9, 2.9, 0.1],
            x_length=20,
            tips=False,
        ).shift(UP*20)
        wavelet = axes.get_graph(lambda x: np.cos(15*x)*np.exp(-x**2), color=BLUE).shift(DOWN*21.8).set_z_index(20)

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[european,straightvoltages,straightlabels]{circuitikz}")

        circ="""\\begin{circuitikz}[american, line width=1pt]
                    \\draw[ultra thin](-4,0) to [R] (0,0) to [cute inductor] (3.5,-0) to[vC] (4.5,-0) to[diode] (10,-0);
                    \\draw[short, *-] (5.5,-0) to (5.49,0.01) to (5.51,-0.01) to (5.51,0.01) to (5.51,-0.01) to (5.49,-0.01) to (5.5,0.0) to [short, *-] (5.5,-2.5) to (5.49,-2.49) to (5.51,-2.51) to (5.51,-2.49) to (5.51,-2.51) to (5.49,-2.51) to (5.5,-2.5) ;
                    \\draw[ultra thin](0,0) to [capacitor,l^] (0,-1) to (0,-0.8) node[ground]{};;
                    \\draw[ultra thin](-4,-2.5) to [diode] (-2,-2.5) to [cute inductor] (1,-2.5) to[C] (3.5,-2.5) to[vC] (10,-2.5);
                    \\draw[ultra thin, short, *-] (5.5,-2.5) to [short, *-] (5.5,-2.5) to [short, -] (5.5,-2.5);
                    \\draw[ultra thin](4,-2.5) to [R] (4,-4.2) to (4,-4) node[ground]{};;
                    \\end{circuitikz}"""
        circuit1=Tex(circ,tex_template=myTemplate,stroke_width=2,fill_opacity=0).scale(0.5) #.shift(LEFT*-8.84)

        circuit_group1=VGroup(*[circuit1.copy() for s in range(30)]).set_x(0).arrange_in_grid(rows=6, buff=(0, 0.8)).scale(0.6).rotate(PI/22).set_color(DARK_GRAY)

        rectangle_efield = Rectangle(height=3.5, width=11, stroke_width=3, color=YELLOW_D, fill_color=GRAY, fill_opacity=0.2).shift(UP*1.5)
        rectangle_title = Text('How do we characterize\n         RF Networks?', gradient=(GREEN, YELLOW_D)).scale(1.4).shift(UP*1.5)
        rectangle_title_2 = Text('A Visual Introduction to\n  Scattering Parameters', gradient=(ORANGE, YELLOW)).scale(1.4).shift(UP*1.5)

        #rectangle_title.shift(UP*3.35).shift(LEFT*0.7)
        rectangle_subtitle = Text('Animation by Apostolos Spanakis-Misirlis', color=YELLOW).scale(0.8)
        rectangle_subtitle.shift(DOWN*3.4)

        self.wait(3)
        self.play(
            Write(circuit_group1)
        )
        self.wait(3)
        self.play(
            GrowFromCenter(rectangle_efield),
            Write(rectangle_title),
        )
        self.wait(3)
        self.play(ReplacementTransform(rectangle_title,rectangle_title_2))
        self.wait(3)
        self.play(Write(wavelet),run_time=7)
        self.wait(3)
        self.play(Write(rectangle_subtitle))
        self.wait(3)

class open_engineering(MovingCameraScene):
    def construct(self):
        circle_bg = Circle(radius=3.2, color=BLACK, fill_opacity=1).set_z_index(10)
        line_r = Line(start=LEFT*3,end=RIGHT*3).set_color(RED).set_z_index(12)
        arc_1 = Arc(radius=3, angle=-PI/2).rotate(-PI/2).shift(UP*3).set_color(RED).set_z_index(12)
        arc_2 = Arc(radius=3, angle=PI/2).rotate(PI/2).shift(DOWN*3).set_color(RED).set_z_index(12)
        circle_1 = Circle(radius=3*1.0).set_color(BLUE).set_z_index(13)
        #circle_15 = Circle(radius=3*0.75).shift(RIGHT*0.75)
        circle_2 = Circle(radius=3*0.5).shift(RIGHT*3*0.5).set_color(BLUE).set_z_index(13).rotate(PI)
        circle_3 = Circle(radius=3*0.25).shift(RIGHT*3*0.75).set_color(BLUE).set_z_index(13)
        self.play(Create(circle_bg))
        self.play(Create(circle_1),Create(circle_2),Create(circle_3),rate_func=smooth)
        #self.play(Create(circle_15))
        #self.play(Create(circle_2))
        #self.play(Create(circle_3))
        self.play(Create(line_r),rate_func=smooth)
        self.play(Create(arc_1),Create(arc_2),rate_func=smooth)
        a = Dot(RIGHT * 2).set_color(YELLOW).set_z_index(15).shift(LEFT*3+UP*2)
        b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        self.play(GrowFromCenter(a), FadeIn(b),run_time=0.5)
        self.wait(0.1)
        self.play(a.animate(path_arc=PI * 0.5).shift(RIGHT*2.7 +  DOWN*1),run_time=1.5,rate_func=smooth)
        b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        #self.wait(0.2)
        self.play(a.animate(path_arc=PI * 1.6).shift(LEFT*0.7 + DOWN*1.5),run_time=1.6,rate_func=smooth)
        b = TracedPath(a.get_center, dissipating_time=0.24, stroke_opacity=[1, 0]).set_z_index(15)
        #self.wait(0.2)
        self.play(a.animate(path_arc=-PI * 0.5).move_to(RIGHT*3 + DOWN*0),run_time=1,rate_func=smooth)
        self.play((self.camera.frame.animate).set_width(12).move_to(RIGHT*4+UP*0.6),run_time=1.5,rate_func=smooth)
        rectangle_title = Text('Open', gradient=(YELLOW, YELLOW_E)).scale(4.2).shift(RIGHT*5.6+UP*1.6)
        rectangle_title_2 = Text('Engineering', gradient=(YELLOW_D, ORANGE)).scale(2).shift(RIGHT*6.5+DOWN*0.165)
        rectangle_box = Rectangle(height=0.8, width=8, stroke_width=2, color=MAROON, fill_opacity=0).shift(RIGHT*6.3+DOWN*1.86)
        rectangle_box_2 = Rectangle(height=0.8, width=8, stroke_width=2, color=MAROON, fill_opacity=0).shift(RIGHT*6.3+DOWN*1.86).rotate(PI)
        rectangle_title_3 = Text('Introduction to S-Parameters', color="#A7C957").scale(0.7).shift(RIGHT*6.37+DOWN*1.85)

        #self.wait(3)
        self.play(
            AnimationGroup(
            Write(rectangle_title),
            Write(rectangle_title_2),
            run_time=2.3,
            lag_ratio=0.4,
            rate_func=smooth)
        )
        self.wait(0.5)
        self.play(AnimationGroup(FadeIn(rectangle_title_3), run_time=1.5),AnimationGroup(Create(rectangle_box),run_time=3,rate_func=smooth),AnimationGroup(Create(rectangle_box_2),run_time=3,rate_func=smooth))
        self.wait()


class scene1(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[european,straightvoltages,straightlabels]{circuitikz}")
        # Create RF networok
        self.wait(3)
        rf_network = Rectangle(height=2.75, width=4.5).set_fill(ORANGE, opacity=0.6)
        rf_network.set_stroke(color=WHITE, width=3)

        # Show RF network
        self.play(FadeIn(rf_network))
        self.wait(3)

        # Create ports
        # Port 1
        port1 = Rectangle(height=0.7, width=0.3).set_fill(MAROON, opacity=0.6)
        port1.set_stroke(color=WHITE, width=2)
        port1.move_to(LEFT * 2.41)

        # Numbering
        port1_num=MathTex("1")
        port1_num.move_to(LEFT * 2.42)
        port1_num.shift(UP * 0.57)
        port1_num.scale(0.8)

        # Port 2
        port2 = Rectangle(height=0.7, width=0.3).set_fill(MAROON, opacity=0.6)
        port2.set_stroke(color=WHITE, width=2)
        port2.move_to(RIGHT * 2.41)

        self.play(FadeIn(port1), FadeIn(port2))
        self.wait(3)

        # Numbering
        port2_num=MathTex("2")
        port2_num.move_to(RIGHT * 2.42)
        port2_num.shift(UP * 0.57)
        port2_num.scale(0.8)

        self.play(Write(port1_num),Write(port2_num))

        # Change color
        self.wait(3)
        self.play(ApplyMethod(rf_network.set_fill, DARK_GREY, opacity=0.3))

        # Circuit content
        circuit="""\\begin{circuitikz}[american]
                    \\draw[ultra thin](-2.64,0) to [R] (0,0) to [cute inductor] (2.64,-0);
                    \\draw[ultra thin](0,0) to [capacitor,l^] (0,-1) to (0,-0.8) node[ground]{};;
                    \\end{circuitikz}"""

        circuit=Tex(circuit,tex_template=myTemplate,stroke_width=2,fill_opacity=0)
        circuit.shift(DOWN * 0.5)
        circuit.scale(0.6)

        self.wait(3)
        self.play(Write(circuit), run_time=3)
        self.wait(3)
        self.play(FadeOut(circuit))
        self.wait(3)
        self.play(ApplyMethod(rf_network.set_fill, RED, opacity=0.3))
        self.wait(3)

        # Questionmark
        questionmark=MathTex("?")
        questionmark.scale(3)

        self.play(Write(questionmark))
        self.wait(3)
        self.play(FadeOut(questionmark))
        self.wait(3)

        # Title
        title = Text("Introduction to Scattering Parameters", color=YELLOW)
        title.scale_in_place(0.75)
        title.to_edge(UP)
        title_new = Text("Introduction to S-Parameters", color=YELLOW)
        title_new.scale_in_place(0.75)
        title_new.to_edge(UP)

        # Title underline
        underline = Line(LEFT, RIGHT, color=YELLOW)
        underline.set_width(1.1*title.get_width())
        underline.next_to(title, DOWN)
        underline.shift(UP * 0.1)
        underline_new = Line(LEFT, RIGHT, color=YELLOW)
        underline_new.set_width(1.1*title_new.get_width())
        underline_new.next_to(title_new, DOWN)

        #self.play(Write(title), Create(underline))
        #self.wait(3)
        #self.play(ReplacementTransform(title,title_new),ReplacementTransform(underline,underline_new))
        self.wait(3)

        # a1
        a1_arr = Arrow(LEFT * 2,RIGHT).set_color(BLUE)
        a1_arr.scale(0.8)
        a1_arr.next_to(port1,LEFT)
        a1_arr.shift(RIGHT * 0.15)
        a1_arr.shift(UP * 0.2)

        a1_lab=MathTex("a_1").set_color(BLUE)
        a1_lab.move_to(LEFT * 3.6)
        a1_lab.shift(UP * 0.42)
        a1_lab.scale(0.8)

        # b1
        b1_arr = Arrow(RIGHT * 1.5,LEFT*1.5).set_color(RED)
        b1_arr.scale(0.8)
        b1_arr.next_to(port1,LEFT)
        b1_arr.shift(RIGHT * 0.15)
        b1_arr.shift(DOWN * 0.2)

        b1_lab=MathTex("b_1").set_color(RED)
        b1_lab.move_to(LEFT * 3.6)
        b1_lab.shift(DOWN * 0.46)
        b1_lab.scale(0.8)

        # S11
        s11_arr = CurvedArrow(UP*0.5,DOWN*0.5,angle=-PI/1.1,color=WHITE)
        s11_arr.scale(0.51)
        s11_arr.next_to(a1_arr,RIGHT*2.1)
        s11_arr.shift(DOWN*0.24)
        s11_arr.rotate(-7*DEGREES)

        s11_lab=MathTex("\mathrm{S}_{11}").set_color(WHITE)
        s11_lab.move_to(LEFT * 1.54)
        s11_lab.scale(0.6)

        # a2
        a2_arr = Arrow(RIGHT * 2,LEFT).set_color(BLUE)
        a2_arr.scale(0.8)
        a2_arr.next_to(port2,RIGHT)
        a2_arr.shift(LEFT * 0.15)
        a2_arr.shift(DOWN * 0.2)

        a2_lab=MathTex("a_2").set_color(BLUE)
        a2_lab.move_to(RIGHT * 3.6)
        a2_lab.shift(DOWN * 0.42)
        a2_lab.scale(0.8)

        # b2
        b2_arr = Arrow(LEFT * 1.5,RIGHT*1.5).set_color(RED)
        b2_arr.scale(0.8)
        b2_arr.next_to(port2,RIGHT)
        b2_arr.shift(LEFT * 0.15)
        b2_arr.shift(UP * 0.2)

        b2_lab=MathTex("b_2").set_color(RED)
        b2_lab.move_to(RIGHT * 3.6)
        b2_lab.shift(UP * 0.46)
        b2_lab.scale(0.8)

        # S22
        s22_arr = CurvedArrow(DOWN*0.5,UP*0.5,angle=-PI/1.1,color=WHITE)
        s22_arr.scale(0.51)
        s22_arr.next_to(a2_arr,LEFT*2.1)
        s22_arr.shift(UP*0.24)
        s22_arr.rotate(-7*DEGREES)

        s22_lab=MathTex("\mathrm{S}_{22}").set_color(WHITE)
        s22_lab.move_to(RIGHT * 1.54)
        s22_lab.scale(0.6)

        # S21
        s21_arr = Arrow(LEFT*2.1,RIGHT*2.1,max_stroke_width_to_length_ratio=1,max_tip_length_to_length_ratio=0.05).set_color(WHITE)

        s21_arr.shift(UP * 0.25)

        s21_lab=MathTex("\mathrm{S}_{21}").set_color(WHITE)
        s21_lab.shift(UP * 0.48)
        s21_lab.scale(0.6)


        # S12
        s12_arr = Arrow(RIGHT*2.1,LEFT*2.1,max_stroke_width_to_length_ratio=1,max_tip_length_to_length_ratio=0.05).set_color(WHITE)

        s12_arr.shift(DOWN * 0.25)

        s12_lab=MathTex("\mathrm{S}_{12}").set_color(WHITE)
        s12_lab.shift(DOWN * 0.48)
        s12_lab.scale(0.6)

        self.play(Write(a1_arr))
        self.play(Write(a1_lab))
        self.wait(3)
        self.play(Write(b2_arr))
        self.play(Write(b2_lab))
        self.wait(3)
        self.play(Write(s21_arr))
        self.wait(3)
        self.play(Write(b1_arr))
        self.play(Write(b1_lab))
        self.wait(3)
        self.play(Write(s11_arr))
        self.wait(3)
        self.play(Write(a2_arr))
        self.play(Write(a2_lab))
        self.wait(3)
        self.play(
            Write(s12_arr),
            Write(s22_arr)
        )
        self.wait(3)
        self.play(Write(s11_lab))
        self.play(Write(s21_lab))
        self.play(Write(s12_lab))
        self.play(Write(s22_lab))
        self.wait(3)

        # S_ij indices clarification
        dark_foreground = Rectangle(height=30, width=30, stroke_width=2.5, fill_color=BLACK, fill_opacity=0.8)
        sij_indices = MathTex("\mathrm{S}_{ij}").set_color(YELLOW).scale(2.5)
        self.play(FadeIn(dark_foreground))
        self.wait(3)
        self.play(Write(sij_indices))
        self.wait(3)
        i_arrow = Arrow(LEFT*1.7+RIGHT).set_color(WHITE).rotate(PI/2).shift(LEFT*0.05+DOWN*1.2)
        j_arrow = Arrow(LEFT*1.7+RIGHT).set_color(WHITE).rotate(-PI/2).shift(RIGHT*0.45+UP*0.9)
        self.play(Write(i_arrow))
        self.wait(3)
        
        # i index
        output_port_label = Tex("Output", " Port").scale(1.2).shift(LEFT*0.25+DOWN*2.2)
        output_port_label.set_color_by_tex_to_color_map({
        "Output": RED,
        "port": WHITE
        })

        # j index
        input_port_label = Tex("Input", " Port").scale(1.2).shift(RIGHT*0.47+UP*1.85)
        input_port_label.set_color_by_tex_to_color_map({
        "Input": BLUE,
        "port": WHITE
        })
        self.play(Write(output_port_label))
        self.wait(3)
        self.play(Write(j_arrow))
        self.wait(3)
        self.play(Write(input_port_label))
        self.wait(3)
        self.play(
            Unwrite(input_port_label),
            Unwrite(output_port_label),
            Uncreate(i_arrow),
            Uncreate(j_arrow),
            Unwrite(sij_indices),
        )
        self.wait(3)
        self.play(FadeOut(dark_foreground))
        self.wait(3)


        # Move camera
        self.play((self.camera.frame.animate).move_to(DOWN*2))
        self.wait(3)

        # ai
        ai_eq=MathTex("a_{i}", #0
        "={\\frac {1}{2}}", #1
        "k_{i}", #2
        "(", #3
        "V_{i}", #4
        "+", #5
        "Z_{i}", #6
        "I_{i}", #7
        ")") #8
        ai_eq.set_color_by_tex_to_color_map({
        "a_{i}": BLUE,
        "k_{i}": YELLOW,
        "V_{i}": GREEN,
        "Z_{i}": ORANGE,
        "I_{i}": PURPLE
        })
        ai_eq.move_to(DOWN * 3)
        ai_eq.shift(LEFT * 4)
        self.play(Write(ai_eq))
        self.wait(3)

        # Vi
        brace_vi = Brace(ai_eq[4], DOWN, buff=SMALL_BUFF)
        text_vi = brace_vi.get_text("Complex ","Voltage"," amplitude at port ","$\\boldsymbol{i}$")
        text_vi.scale(0.6)
        text_vi.shift(UP*0.2)
        text_vi.shift(RIGHT*0.65)
        text_vi.set_color_by_tex_to_color_map({
        "Voltage": GREEN,
        "$\\boldsymbol{i}$": YELLOW
        })

        # Ii
        brace_ii = Brace(ai_eq[7], DOWN, buff=SMALL_BUFF)
        text_ii = brace_vi.get_text("Complex ","Current"," amplitude at port ","$\\boldsymbol{i}$")
        text_ii.scale(0.6)
        text_ii.shift(UP*0.2)
        text_ii.shift(RIGHT*0.65)
        text_ii.set_color_by_tex_to_color_map({
        "Current": PURPLE,
        "$\\boldsymbol{i}$": YELLOW
        })

        # Zi
        brace_zi = Brace(ai_eq[6], DOWN, buff=SMALL_BUFF)
        text_zi = brace_vi.get_text("Complex ","Impedance"," of port ","$\\boldsymbol{i}$")
        text_zi.scale(0.6)
        text_zi.shift(UP*0.2)
        text_zi.shift(RIGHT*1)
        text_zi.set_color_by_tex_to_color_map({
        "Impedance": ORANGE,
        "$\\boldsymbol{i}$": YELLOW
        })

        self.play(
            GrowFromCenter(brace_vi),
            FadeIn(text_vi)
        )
        self.wait(3)
        self.play(
            ReplacementTransform(brace_vi,brace_ii),
            ReplacementTransform(text_vi,text_ii)
        )
        self.wait(3)
        self.play(
            ReplacementTransform(brace_ii,brace_zi),
            ReplacementTransform(text_ii,text_zi)
        )
        self.wait(3)
        self.play(FadeOut(brace_zi),FadeOut(text_zi))

        #bi
        bi_eq=MathTex("b_{i}", #0
        "={\\frac {1}{2}}", #1
        "k_{i}", #2
        "(", #3
        "V_{i}", #4
        "-", #5
        "Z_{i}^{*}", #6
        "I_{i}", #7
        ")") #8
        bi_eq.set_color_by_tex_to_color_map({
        "b_{i}": RED,
        "k_{i}": YELLOW,
        "V_{i}": GREEN,
        "Z_{i}^{*}": ORANGE,
        "I_{i}": PURPLE
        })
        bi_eq.move_to(DOWN * 5)
        bi_eq.shift(LEFT * 4)
        self.wait(3)
        self.play(Write(bi_eq))

        # Zi*
        brace_zis = Brace(bi_eq[6], UP, buff=SMALL_BUFF)
        text_zis = brace_vi.get_text("Complex conjugate"," of ","$\\boldsymbol{Z_{i}}$")
        text_zis.scale(0.6)
        text_zis.shift(DOWN*0.1)
        #text_zis.shift(RIGHT*0.65)
        text_zis.set_color_by_tex_to_color_map({
        "Z_{i}": ORANGE
        })

        self.wait(3)
        self.play(
            GrowFromCenter(brace_zis),
            FadeIn(text_zis)
        )
        self.wait(3)
        self.play(FadeOut(brace_zis),FadeOut(text_zis))

        framebox_ki1 = SurroundingRectangle(ai_eq[2], buff = .05)
        framebox_ki2 = SurroundingRectangle(bi_eq[2], buff = .05)
        self.wait(3)
        self.play(
            Create(framebox_ki1),
            Create(framebox_ki2)
        )
        self.wait(3)

        ki_eq=MathTex("k_{i}", #0
        "=\\bigg({\sqrt {\\big| ", #1
        "\mathfrak{R} \{", #2
        "Z_{i}", #3
        "\}", #4
        "\\big|}}", #5
        "\\bigg)^{-1}") #6
        ki_eq.set_color_by_tex_to_color_map({
        "k_{i}": YELLOW,
        "Z_{i}": ORANGE
        })
        ki_eq.move_to(DOWN * 4)
        ki_eq.shift(RIGHT * 4)

        framebox_ki3 = SurroundingRectangle(ki_eq, buff = .1)
        self.play(
            Write(ki_eq),
            ReplacementTransform(framebox_ki1,framebox_ki3),
            ReplacementTransform(framebox_ki2,framebox_ki3),
            run_time=2
        )
        self.wait(3)

        ki_eq_new=MathTex("k_{i}", #0
        "=\\bigg({\sqrt {\\big| ", #1
        "\mathfrak{R} \{", #2
        "Z_{0}", #3
        "\}", #4
        "\\big|}}", #5
        "\\bigg)^{-1}") #6
        ki_eq_new.set_color_by_tex_to_color_map({
        "k_{i}": YELLOW,
        "Z_{0}": ORANGE
        })
        ki_eq_new.move_to(DOWN * 4)
        ki_eq_new.shift(RIGHT * 4)


        self.play(
            ReplacementTransform(ki_eq,ki_eq_new)
        )
        self.wait(3)

        ### ki_eq_new2
        ki_eq_new2=MathTex("k_{i}", #0
        "=\\bigg({\sqrt {\\big| ", #1
        "\mathfrak{R} \{", #2
        "Z_{0}", #3
        "\}", #4
        "\\big|}}", #5
        "\\bigg)^{-1}") #6
        ki_eq_new2.set_color_by_tex_to_color_map({
        "k_{i}": YELLOW,
        "Z_{0}": ORANGE
        })
        ki_eq_new2.move_to(DOWN * 4)
        ki_eq_new2.shift(RIGHT * 4)

        self.play(
            FadeOut(framebox_ki3)
        )
        self.wait(3)

        self.add(ki_eq_new)







        #obj_list = []
        #for mob in self.mobjects:
        #    obj_list.append(mob)
        #objects_before = VGroup(obj_list)
        #self.play(
        #    FadeOut(objects_before)
        #)
        before_out = [FadeOut(mob) for mob in self.mobjects]
        before_in = [FadeIn(mob) for mob in self.mobjects]
        self.wait(3)
        self.play(
            *before_out
        )
        self.wait(3)

        self.play((self.camera.frame.animate).move_to(UP*0))
        self.wait(3)

        # Origin point dot
        dot = Dot(ORIGIN).set_z_index(10)
        dot.plot_depth = 1 # Bring forward

        # R
        resistance_arrow = Arrow(ORIGIN, [2.5, 0, 0], buff=0).set_color(RED_D)
        tip_text_resistance = Tex('$R$').next_to(resistance_arrow.get_end(), DOWN)
        tip_text_resistance.set_color_by_tex_to_color_map({"R": RED_D})
        #tip_text_resistance.shift(DOWN*0.1)

        # X
        reactance_arrow = Arrow(ORIGIN, [0, 1.5, 0], buff=0).set_color(GREEN_D)
        tip_text_reactance = MathTex('X').next_to(reactance_arrow.get_end(), LEFT)
        #tip_text_reactance[0].set_color(LIGHT_GRAY)
        tip_text_reactance[0].set_color(GREEN_D)
        #tip_text_reactance.set_color_by_tex_to_color_map({"j": PURPLE_A, "X": GREEN_D})
        #tip_text_reactance.shift(RIGHT*0.1)

        # Z
        impedance_arrow = Arrow(ORIGIN, [2.5, 1.5, 0], buff=0).set_color(ORANGE)
        tip_text_impedance = Tex('$Z$').next_to(impedance_arrow.get_end(), RIGHT)
        tip_text_impedance.set_color_by_tex_to_color_map({"Z": ORANGE})
        tip_text_impedance.shift(LEFT*0.1)

        # Axes properties
        numberplane = NumberPlane(
        axis_config={
            "unit_size": 1
            #"x_unit_size": 2,
            #"y_unit_size": 2
            }
        )
        numberplane.set_opacity(0.5).set_z_index(-2)
        rectangle_Zplot = Rectangle(height=50, width=10, stroke_width=0, fill_color=BLACK, fill_opacity=0.6, z_index=-1).shift(LEFT*5.01)
        #origin_text = Text('(0, 0)').next_to(dot, DOWN)

        self.add(numberplane)
        self.play(Create(numberplane, run_time=2, lag_ratio=0.1))
        self.wait(3)

        # Title
        title_impedance = Text("Complex Impedance", color=YELLOW)
        title_impedance.scale_in_place(0.55)
        title_impedance.to_edge(UP).shift(LEFT*5+UP*0.2)

        # Title underline
        underline_impedance = Line(LEFT, RIGHT, color=YELLOW)
        underline_impedance.set_width(1.1*title_impedance.get_width())
        underline_impedance.next_to(title_impedance, DOWN)
        underline_impedance.shift(UP * 0.1)

        self.play(FadeIn(title_impedance, shift=LEFT), GrowFromCenter(underline_impedance))
        self.wait(3)

        # Axis labels
        right_arrow = Arrow(ORIGIN, [7.1, 0, 0], buff=0, stroke_width=0.8).set_color(WHITE)
        right_arrow_label=Text('Resistance').scale(0.5).next_to(right_arrow).shift(LEFT*2.15+DOWN*0.25).set_color(RED_E)
        up_arrow = Arrow(ORIGIN, [0, 4, 0], buff=0, stroke_width=0.8).set_color(WHITE)
        up_arrow_label=Text('Inductive\nReactance').scale(0.5).rotate(PI/2).next_to(up_arrow).shift(LEFT*1.15+UP*0.8).set_color(GREEN_E)
        down_arrow = Arrow(ORIGIN, [0, -4, 0], buff=0, stroke_width=0.8).set_color(WHITE)
        down_arrow_label=Text('Capacitive\nReactance').scale(0.5).rotate(PI/2).next_to(down_arrow).shift(LEFT*1.15+DOWN*0.76).set_color(GREEN_E)

        # Re
        re_label=Tex('$\mathfrak{R}$').scale(0.8).next_to(right_arrow).shift(LEFT*0.75+UP*0.45)

        # Im
        im_label=Tex('$\mathfrak{I}$').scale(0.8).next_to(up_arrow).shift(LEFT*0.11+UP*1.65)

        # Axes
        self.play(
            GrowArrow(right_arrow, run_time=2),
            GrowArrow(up_arrow, run_time=2),
            GrowArrow(down_arrow, run_time=2)
        )
        self.wait(3)
        self.play(
            Write(right_arrow_label)
        )
        self.wait(3)
        self.play(
            Write(re_label)
        )
        self.wait(3)
        self.play(
            Write(up_arrow_label),
            Write(down_arrow_label)
        )
        self.wait(3)
        self.play(
            Write(im_label)
        )
        self.wait(3)
        self.play(FadeIn(rectangle_Zplot), run_time=2.5)
        self.wait(3)
        self.play(
            GrowArrow(resistance_arrow, run_time=1.5),
            Write(tip_text_resistance),
            GrowArrow(reactance_arrow, run_time=1.5),
            Write(tip_text_reactance),
            GrowFromCenter(dot)
        )
        #Z_dot = Dot(impedance_arrow.get_end()).set_color(ORANGE).set_z_index(10)
        #Z_dot.plot_depth = 1 # Bring forward
        self.wait(3)
        #####################
        self.play(
            Write(impedance_arrow, run_time=1.5),
            Write(tip_text_impedance),
        )
        self.wait(3)
        
        # Dashed lines
        R_line = Line(resistance_arrow.get_end(), impedance_arrow.get_end()).set_color(ORANGE)
        R_dashed_line=DashedVMobject(R_line)
        X_line = Line(reactance_arrow.get_end(), impedance_arrow.get_end()).set_color(ORANGE)
        X_dashed_line=DashedVMobject(X_line)

        self.play(
            Create(R_dashed_line),
            Create(X_dashed_line)
        )
        self.wait(3)

        tip_text_impedance_mag = MathTex(
      '|Z|','=',r'\sqrt', '{','R^2 + X^2','}',
      tex_to_color_map={"Z":ORANGE, "R":RED_D, "X":GREEN_D}
    ).next_to(impedance_arrow.get_end(), RIGHT)
        #tip_text_impedance_mag.shift(RIGHT*0.0)
        self.play(
            ReplacementTransform(tip_text_impedance,tip_text_impedance_mag)
        )
        self.wait(3)

        # Angle
        arc = Arc(radius=1.1, start_angle=0.025, angle=PI/6.3, stroke_width=3, color=YELLOW)
 
        theta = MathTex('\\phi')
        theta.scale(0.8).set_color(YELLOW)
        theta.next_to(arc, 0.5 * RIGHT).shift(0.07 * UP)
 
        self.play(Create(arc))
        self.wait(3)
        self.play(Write(theta))
        self.wait(3)

        # Angle label
        theta_label = MathTex(r'\phi','=',r'\arctan',r'{\left(',r'{{X}','\over','{R}',r'}\right)}')
        theta_label[0].set_color(YELLOW)
        theta_label[4].set_color(GREEN_D)
        theta_label[6].set_color(RED_D)
        theta_label.scale_in_place(0.7)
        theta_label.shift(RIGHT*5 + DOWN*3)
        rectangle_theta = Rectangle(height=1.2, width=3, stroke_width=2.5, color=YELLOW_D, fill_color=DARKER_GRAY, fill_opacity=0.7)
        rectangle_theta.next_to(theta_label).shift(LEFT*3)
        rectangle_title = Text('Phase Angle', color=YELLOW_D).scale(0.6)
        rectangle_title.next_to(rectangle_theta).shift(LEFT*2.745+UP*0.852)

        self.play(GrowFromCenter(rectangle_theta), Write(rectangle_title))
        self.wait(3)
        self.play(Write(theta_label))
        self.wait(3)
        self.play(
            FadeOut(dot),
            FadeOut(resistance_arrow),
            FadeOut(tip_text_resistance),
            FadeOut(reactance_arrow),
            FadeOut(tip_text_reactance),
            FadeOut(impedance_arrow),
            FadeOut(tip_text_impedance),
            FadeOut(numberplane),
            FadeOut(title_impedance),
            FadeOut(underline_impedance),
            FadeOut(right_arrow),
            FadeOut(right_arrow_label),
            FadeOut(up_arrow),
            FadeOut(up_arrow_label),
            FadeOut(down_arrow),
            FadeOut(down_arrow_label),
            FadeOut(re_label),
            FadeOut(im_label),
            FadeOut(R_line),
            FadeOut(R_dashed_line),
            FadeOut(X_line),
            FadeOut(X_dashed_line),
            FadeOut(tip_text_impedance_mag),
            FadeOut(arc),
            FadeOut(theta),
            FadeOut(theta_label),
            FadeOut(rectangle_theta),
            FadeOut(rectangle_title)
        )
        self.wait(3)
        self.play((self.camera.frame.animate).move_to(DOWN*2))
        self.wait(3)
        self.play(
            *before_in
        )
        self.wait(3)


        brace_z0 = Brace(ki_eq_new2[2:5], DOWN, buff=SMALL_BUFF)
        text_z0 = brace_z0.get_text("$R_{0}$")
        text_z0.scale(0.8)
        text_z0.shift(UP*0.1)
        #text_z0.shift(UP*0.2)
        #text_z0.shift(RIGHT*1)
        text_z0.set_color_by_tex_to_color_map({
        "$R_{0}$": MAROON_B
        })

        self.play(
            GrowFromCenter(brace_z0),
            FadeIn(text_z0)
        )

        self.wait(3)
        self.play(
            FadeOut(brace_z0),
            FadeOut(text_z0)
        )
        self.wait(3)

        # ai_new
        ai_eq_new=MathTex("a_{i}", #0
        "= { { 1 }\over{ 2 } } ", #1
        " { { ( ",
        "V_{i}",
        "+",
        "Z_{0}",
        "I_{i}",
        ")}",
        "\over{\sqrt{|",
        "\mathfrak{R}",
        "\{",
        " { Z_{0 } } ",
        "\} | } } }")
        ai_eq_new.set_color_by_tex_to_color_map({
        "a_{i}": BLUE,
        "V_{i}": GREEN,
        "Z_{0}": ORANGE,
        "I_{i}": PURPLE,
        " { Z_{0 } } ": ORANGE,
        })
        ai_eq_new.move_to(DOWN * 3)
        ai_eq_new.shift(LEFT * 4)

        # ai_new
        bi_eq_new=MathTex("b_{i}", #0
        "= { { 1 }\\over{2 } } ", #1
        " { { ( ",
        "V_{i}",
        "-",
        "Z_{0}^{*}",
        "I_{i}",
        " ) } ",
        "\\over{\sqrt{|",
        "\mathfrak{R}",
        "\{",
        " { Z_{0} } ",
        "\} | } } } ")
        bi_eq_new.set_color_by_tex_to_color_map({
        "b_{i}": RED,
        "V_{i}": GREEN,
        "Z_{0}": ORANGE,
        "I_{i}": PURPLE,
        "{Z_{0}}": ORANGE,
        })
        bi_eq_new.move_to(DOWN * 5)
        bi_eq_new.shift(LEFT * 4)

        self.play(
            ReplacementTransform(ai_eq,ai_eq_new),
            ReplacementTransform(bi_eq,bi_eq_new),
            ReplacementTransform(ki_eq_new,ai_eq_new),
            ReplacementTransform(ki_eq_new2,bi_eq_new)
        )
        self.wait(3)

        #### relation_eq (b = Sa)

        relation_eq=MathTex("b", #0
        "=", #1
        "\mathrm{S}", #2
        "a") #3
        relation_eq[0].set_color(RED)
        relation_eq[2].set_color(YELLOW)
        relation_eq[3].set_color(BLUE)

        relation_eq.move_to(DOWN * 4)
        relation_eq.shift(RIGHT * 4)

        self.wait(3)

        framebox_relation_eq = SurroundingRectangle(relation_eq, buff = .1)

        self.play(
            Create(framebox_relation_eq),
            Write(relation_eq)
        )
        self.wait(3)

        #relation_matrix=MathTex()
        m1 = Matrix([[r"b_1"], [r"\vdots"], [r"b_n"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        eq = MathTex("=")
        m2 = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{1n}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{n1}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m3 = Matrix([[r"a_1"], [r"\vdots"], [r"a_n"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1.shift(LEFT*2)
        eq.next_to(m1)
        m2.next_to(eq)
        m3.next_to(m2)
        m1[0][0].set_color(RED)
        m1[0][2].set_color(RED)
        m2[0][0].set_color(YELLOW)
        m2[0][2].set_color(YELLOW)
        m2[0][6].set_color(YELLOW)
        m2[0][8].set_color(YELLOW)
        m3[0][0].set_color(BLUE)
        m3[0][2].set_color(BLUE)
        g = VGroup(m1, m2, m3, eq)

        g.move_to(DOWN * 4)
        g.shift(RIGHT * 2.8)
        self.play(
            FadeOut(framebox_relation_eq),
            ReplacementTransform(relation_eq, g)
        )
        self.wait(3)

        ### n-port n^2 clarification
        brace_n = Brace(m2[0][0:3], UP, buff=SMALL_BUFF)
        brace_n.shift(UP*0.2)
        text_n = brace_n.get_text("$n^2$", " elements")
        text_n.scale(0.8)
        text_n.shift(DOWN*0.1)
        #text_z0.shift(UP*0.2)
        #text_z0.shift(RIGHT*1)
        text_n.set_color_by_tex_to_color_map({
        "$n^2$": YELLOW
        })

        self.play(
            GrowFromCenter(brace_n),
            FadeIn(text_n)
        )
        self.wait(3)
        #self.play(
        #    FadeOut(brace_n),
        #    FadeOut(text_n)
        #)

        # 2-port example
        m1_2port = Matrix([[r"b_1"], [r"b_2"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        eq_2port = MathTex("=")
        m2_2port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
                           [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m3_2port = Matrix([[r"a_1"], [r"a_2"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_2port.shift(LEFT*2)
        eq_2port.next_to(m1_2port)
        m2_2port.next_to(eq_2port)
        m3_2port.next_to(m2_2port)
        m1_2port[0][0].set_color(RED)
        m1_2port[0][1].set_color(RED)
        m2_2port[0][0].set_color(YELLOW)
        m2_2port[0][1].set_color(YELLOW)
        m2_2port[0][2].set_color(YELLOW)
        m2_2port[0][3].set_color(YELLOW)
        m3_2port[0][0].set_color(BLUE)
        m3_2port[0][1].set_color(BLUE)
        g_2port = VGroup(m1_2port, m2_2port, m3_2port, eq_2port)

        g_2port.move_to(DOWN * 4)
        g_2port.shift(RIGHT * 2.8)

        # Brace for 2x2 matrix
        brace_2 = Brace(m2_2port[0][0:2], UP, buff=SMALL_BUFF)
        brace_2.shift(UP*0.2)

        text_2 = brace_2.get_text("$2^2$", " elements")
        text_2.scale(0.8)
        text_2.shift(DOWN*0.1)
        #text_z0.shift(UP*0.2)
        #text_z0.shift(RIGHT*1)
        text_2.set_color_by_tex_to_color_map({
        "$2^2$": YELLOW
        })
        self.play(
            ReplacementTransform(g, g_2port),
            ReplacementTransform(brace_n, brace_2),
            ReplacementTransform(text_n, text_2)
        )
        self.wait(3)
        text_4 = brace_2.get_text("$4$", " elements")
        text_4.scale(0.8)
        text_4.shift(DOWN*0.1)
        #text_z0.shift(UP*0.2)
        #text_z0.shift(RIGHT*1)
        text_4.set_color_by_tex_to_color_map({
        "$4$": YELLOW
        })
        self.play(
            ReplacementTransform(text_2, text_4)
        )
        self.wait(3)



        # Voltages
        # a1
        voltage_a1=MathTex("a_1", #0
        "=", #1
        "V_{1}^{+}" #2
        )
        voltage_a1[0].set_color(BLUE)
        voltage_a1[2].set_color(GREEN)
        voltage_a1.move_to(DOWN * 2.5)
        voltage_a1.shift(LEFT * 4)

        # a2
        voltage_a2=MathTex("a_2", #0
        "=", #1
        "V_{2}^{+}" #2
        )
        voltage_a2[0].set_color(BLUE)
        voltage_a2[2].set_color(GREEN)
        voltage_a2.move_to(DOWN * 3.3)
        voltage_a2.shift(LEFT * 4)

        # b1
        voltage_b1=MathTex("b_1", #0
        "=", #1
        "V_{1}^{-}" #2
        )
        voltage_b1[0].set_color(RED)
        voltage_b1[2].set_color(GREEN)
        voltage_b1.move_to(DOWN * 4.6)
        voltage_b1.shift(LEFT * 4)

        # b2
        voltage_b2=MathTex("b_2", #0
        "=", #1
        "V_{2}^{-}" #2
        )
        voltage_b2[0].set_color(RED)
        voltage_b2[2].set_color(GREEN)
        voltage_b2.move_to(DOWN * 5.4)
        voltage_b2.shift(LEFT * 4)
        
        self.play(
            FadeOut(g_2port),
            FadeOut(ai_eq_new),
            FadeOut(bi_eq_new),
            FadeOut(brace_2),
            FadeOut(text_4)
        )
        self.wait(3)
        self.play(Write(voltage_a1))
        self.wait(3)
        self.play(Write(voltage_a2))
        self.wait(3)
        self.play(Write(voltage_b1))
        self.wait(3)
        self.play(Write(voltage_b2))

        # ai voltage
        eq_group_ai=VGroup(voltage_a1,voltage_a2)
        brace_ai=Brace(eq_group_ai,RIGHT)
        eq_text_ai = brace_ai.get_text('$a_i $ ',' $ = $ ',' $ V_{i}^{+}$')

        eq_text_ai.set_color_by_tex_to_color_map({
        "$a_i $ ": BLUE,
        "V_{i}^{+}": GREEN
        })

        # bi voltage
        eq_group_bi=VGroup(voltage_b1,voltage_b2)
        brace_bi=Brace(eq_group_bi,RIGHT)
        eq_text_bi = brace_bi.get_text('$b_i $ ',' $ = $ ',' $ V_{i}^{-}$')

        eq_text_bi.set_color_by_tex_to_color_map({
        "$b_i $ ": RED,
        "V_{i}^{-}": GREEN
        })

        self.wait(3)
        self.play(
            GrowFromCenter(brace_ai),
            GrowFromCenter(brace_bi)
        )
        self.wait(3)
        self.play(
            Write(eq_text_ai),
            Write(eq_text_bi)
        )
        self.wait(3)

        long_right_arrow=Tex('$\Longrightarrow$').scale(1).next_to(eq_text_bi).shift(UP*1+RIGHT*0.1)

        self.play(
            FadeIn(long_right_arrow, shift=RIGHT)
        )
        self.wait(3)

        # S-parameters
        # s11
        s11=MathTex("\mathrm{S}_{11}", #0
        "=", #1
        "{b_1", #2
        "\over", #3
        "a_1}", #4
        "=", #5
        "{V_{1}^{-}", #6
        "\over", #7
        "V_{1}^{+}}" #8
        )

        s11[0].set_color(YELLOW)
        s11[2].set_color(RED)
        s11[4].set_color(BLUE)
        s11[6].set_color(GREEN)
        s11[8].set_color(GREEN)
        s11.move_to(DOWN * 4.05)
        s11.shift(RIGHT * 2.7)
        self.play(Write(s11))
        self.wait(3)

        # s21
        s21=MathTex("\mathrm{S}_{21}", #0
        "=", #1
        "{b_2", #2
        "\over", #3
        "a_1}", #4
        "=", #5
        "{V_{2}^{-}", #6
        "\over", #7
        "V_{1}^{+}}" #8
        )

        s21[0].set_color(YELLOW)
        s21[2].set_color(RED)
        s21[4].set_color(BLUE)
        s21[6].set_color(GREEN)
        s21[8].set_color(GREEN)
        s21.move_to(DOWN * 4.05)
        s21.shift(RIGHT * 2.7)
        self.play(ReplacementTransform(s11,s21))

        self.wait(3)

        # s12
        s12=MathTex("\mathrm{S}_{12}", #0
        "=", #1
        "{b_1", #2
        "\over", #3
        "a_2}", #4
        "=", #5
        "{V_{1}^{-}", #6
        "\over", #7
        "V_{2}^{+}}" #8
        )

        s12[0].set_color(YELLOW)
        s12[2].set_color(RED)
        s12[4].set_color(BLUE)
        s12[6].set_color(GREEN)
        s12[8].set_color(GREEN)
        s12.move_to(DOWN * 4.05)
        s12.shift(RIGHT * 2.7)
        self.play(ReplacementTransform(s21,s12))
        self.wait(3)

        # s22
        s22=MathTex("\mathrm{S}_{22}", #0
        "=", #1
        "{b_2", #2
        "\over", #3
        "a_2}", #4
        "=", #5
        "{V_{2}^{-}", #6
        "\over", #7
        "V_{2}^{+}}" #8
        )

        s22[0].set_color(YELLOW)
        s22[2].set_color(RED)
        s22[4].set_color(BLUE)
        s22[6].set_color(GREEN)
        s22[8].set_color(GREEN)
        s22.move_to(DOWN * 4.05)
        s22.shift(RIGHT * 2.7)
        self.play(ReplacementTransform(s12,s22))

        self.wait(3)

        # sij
        sij=MathTex("\mathrm{S}_{ij}", #0
        "=", #1
        "{b_i", #2
        "\over", #3
        "a_j}", #4
        "=", #5
        "{V_{i}^{-}", #6
        "\over", #7
        "V_{j}^{+}}" #8
        )

        sij[0].set_color(YELLOW)
        sij[2].set_color(RED)
        sij[4].set_color(BLUE)
        sij[6].set_color(GREEN)
        sij[8].set_color(GREEN)
        sij.move_to(DOWN * 4.05)
        sij.shift(RIGHT * 2.7)

        self.play(
            FadeOut(long_right_arrow),
            FadeOut(eq_text_ai, shift=LEFT),
            FadeOut(eq_text_bi, shift=LEFT),
            FadeOut(brace_ai, shift=LEFT),
            FadeOut(brace_bi, shift=LEFT),
            FadeOut(voltage_a1, shift=LEFT),
            FadeOut(voltage_a2, shift=LEFT),
            FadeOut(voltage_b1, shift=LEFT),
            FadeOut(voltage_b2, shift=LEFT)
        )
        self.wait(3)

        #self.play(ReplacementTransform(s22,sij))
        sij.generate_target()
        sij.target.shift(2.7*LEFT)
        self.play(ReplacementTransform(s22,sij))
        self.play(MoveToTarget(sij))
        framebox_sij = SurroundingRectangle(sij, buff = .15)
        self.play(Create(framebox_sij))
        self.wait(3)

class scene2(MovingCameraScene):
    def construct(self):
        image = ImageMobject("/Users/Coto/Documents/edu/first_frame.png").scale(0.78 ).shift(LEFT*0.3+DOWN*1.4)

        # Title
        title_wave = Text("Reflection & Transmission Coefficients", color=YELLOW)
        title_wave.scale_in_place(0.8)
        title_wave.to_edge(UP)#.shift(LEFT*5+UP*0.2)

        # Title underline
        underline_wave = Line(LEFT, RIGHT, color=YELLOW)
        underline_wave.set_width(1.1*title_wave.get_width())
        underline_wave.next_to(title_wave, DOWN)
        underline_wave.shift(UP * 0.1)

        self.play(FadeIn(image), Write(title_wave, shift=DOWN), GrowFromCenter(underline_wave))
        self.wait(3)

        # Name ports
        # Port 1
        port1_num_wave=MathTex("1").set_color(YELLOW)
        port1_num_wave.move_to(LEFT * 6.1)
        port1_num_wave.shift(DOWN * 1.2)
        port1_num_wave.scale(1)

        # Port 2
        port2_num_wave=MathTex("2").set_color(YELLOW)
        port2_num_wave.move_to(RIGHT * 6.1)
        port2_num_wave.shift(DOWN * 1.2)
        port2_num_wave.scale(1)

        self.play(Write(port1_num_wave),Write(port2_num_wave))


        s11_wave=MathTex(
        "|", #0
        "\mathrm{S}_{11}", #1
        "|", #2
        "=", #3
        "0", #4
        ).move_to(UP*1.3).scale(1.2)

        s11_wave[1].set_color(YELLOW)
        s11_wave[3].set_color(WHITE)
        s11_wave[4].set_color(GREEN)

        s21_wave=MathTex("|", #0
        "\mathrm{S}_{21}", #1
        "|", #2
        "=", #3
        "1", #4
        ).move_to(UP*1.3).scale(1.2)

        s21_wave[1].set_color(YELLOW)
        s21_wave[3].set_color(WHITE)
        s21_wave[4].set_color(GREEN)


        s21_wave_db=MathTex(
        "|", #0
        "\mathrm{S}_{21}", #1
        "|", #2
        "=", #3
        "0 \mathrm{ \ dB}", #4
        ).move_to(UP*1.3).scale(1.2)

        s21_wave_db[1].set_color(YELLOW)
        s21_wave_db[3].set_color(WHITE)
        s21_wave_db[4].set_color(GREEN)

        framebox_s21_wave_db = SurroundingRectangle(s21_wave_db, buff = .15).set_color(GOLD)
        self.wait(3)
        self.play(Write(s11_wave))
        self.wait(3)
        self.play(ReplacementTransform(s11_wave, s21_wave))
        self.wait(3)
        self.play(ReplacementTransform(s21_wave, s21_wave_db))
        self.play(Write(framebox_s21_wave_db))
        self.wait(3)
        self.play(FadeOut(s21_wave_db), FadeOut(framebox_s21_wave_db))



        self.wait(3)
        self.wait(3)



        z1_wave = MathTex("Z_{1}").set_color(ORANGE).shift(RIGHT*0.55).shift(UP*1.5).scale(1)
        z2_wave = MathTex("Z_{2}").set_color(ORANGE).shift(RIGHT*1.65).shift(UP*1.5).scale(1)
        self.play(Write(z1_wave), Write(z2_wave))
        self.wait(3)

        neq_wave = MathTex("\\neq").set_color(ORANGE).shift(RIGHT*(1.65+0.55)/float(2)).shift(UP*1.5).scale(1)
        z2_star_wave = MathTex("Z_{2}^{*}").set_color(ORANGE).shift(RIGHT*1.65).shift(UP*1.5).scale(1)
        self.play(Write(neq_wave),ReplacementTransform(z2_wave,z2_star_wave))
        self.wait(3)

        objects_wave = VGroup(z1_wave, neq_wave, z2_star_wave)

        text_wave = Text("Discontinuity", color=RED).scale(0.7).shift(UP*1.9).shift(RIGHT*1.1).shift(DOWN*0.05)
        brace_wave = Brace(text_wave).shift(UP*0.1).scale(1.05)
        self.play(FadeOut(objects_wave), GrowFromCenter(brace_wave))
        self.play(Write(text_wave))
        self.wait(3)
        self.play(FadeOut(text_wave), FadeOut(brace_wave))
        self.wait(3)

        # b2 < a1
        b2_a1=MathTex("b_2", #0
        "<", #1
        "a_1" #2
        ).move_to(UP*2+LEFT*1.9).scale(1.2)

        b2_a1[0].set_color(RED)
        b2_a1[1].set_color(WHITE)
        b2_a1[2].set_color(BLUE)
        
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(1.2).next_to(b2_a1).shift(RIGHT*0.2)

        self.play(Write(b2_a1))
        self.wait(3)
        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # s11 > 0
        s11_0=MathTex(
        "|", #0
        "\mathrm{S}_{11}", #1
        "|", #2
        ">", #3
        "0" #4
        ).move_to(UP*2+RIGHT*1.8).scale(1.2)

        s11_0[1].set_color(YELLOW)
        s11_0[3].set_color(WHITE)
        s11_0[4].set_color(GREEN)

        self.wait(3)
        self.play(Write(s11_0))

        # s21 < 1
        s21_0=MathTex(
        "|", #0
        "\mathrm{S}_{21}", #1
        "|", #2
        "<", #3
        "1" #4
        ).move_to(UP*2+RIGHT*1.8).scale(1.2)

        s21_0[1].set_color(YELLOW)
        s21_0[3].set_color(WHITE)
        s21_0[4].set_color(GREEN)

        self.wait(3)
        self.play(ReplacementTransform(s11_0, s21_0))

        # s21 < 0 db
        s21_0_db=MathTex(
        "|", #0
        "\mathrm{S}_{21}", #1
        "|", #2
        "<", #3
        "0 \mathrm{ \ dB}" #4
        ).move_to(UP*2+RIGHT*2.28).scale(1.2)

        s21_0_db[1].set_color(YELLOW)
        s21_0_db[3].set_color(WHITE)
        s21_0_db[4].set_color(GREEN)

        self.wait(3)
        self.play(ReplacementTransform(s21_0, s21_0_db))
        self.wait(3)
        framebox_s21_0_db = SurroundingRectangle(s21_0_db, buff = .15).set_color(GOLD)

        self.play(Write(framebox_s21_0_db))
        self.wait(3)
        self.play(
            FadeOut(framebox_s21_0_db),
            FadeOut(s21_0_db),
            FadeOut(long_right_arrow_wave),
            FadeOut(b2_a1)
        )
        #image_end = ImageMobject("/Users/Coto/Documents/last_freeze_frame.png").scale(0.78 ).shift(LEFT*0.3+DOWN*1.4)
        #self.play(FadeOut(image))
        #self.add(image_end)

        start_amplitude_arrow = Arrow(LEFT * 2,RIGHT).set_color(BLUE_B)
        start_amplitude_arrow.scale(0.4)
        start_amplitude_arrow.move_to(LEFT*2.07+DOWN*2.15)
        start_amplitude_arrow.rotate(PI/2)

        end_amplitude_arrow = Arrow(LEFT * 2,RIGHT).set_color(BLUE_B)
        end_amplitude_arrow.scale(0.4)
        end_amplitude_arrow.move_to(RIGHT*2.68+DOWN*0.1)
        end_amplitude_arrow.rotate(-PI/2)
        self.play(Write(start_amplitude_arrow),
        Write(end_amplitude_arrow))
        self.wait(3)

class scene3(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[-0.06, 5.001, 1],
            y_range=[-30.01, 0.5, 5],
            x_length=11,
            y_length=5.7,
            x_axis_config={"numbers_to_include": np.arange(0, 5.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-30.01, 0.5, 5)},
            tips=False,
        )
        ax_highfreq = Axes(
            x_range=[13, 18.001, 1],
            y_range=[-30.01, 0.5, 5],
            x_length=10.9,
            y_length=5.7,
            x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-30.01, 0.5, 5)},
            tips=False,
        )
        ax_highfreq.shift(DOWN*5.9+RIGHT*2.45).scale(1.25)
        ax_amp = Axes(
            x_range=[13, 18.001, 1],
            y_range=[-40.01, 20.5, 10],
            x_length=10.9,
            y_length=6.7,
            x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-40.01, 20.5, 10)},
            tips=False,
        )
        ax_amp.shift(DOWN*5.9+RIGHT*2.45).scale(1.25)
        self.play(
            self.camera.frame.animate.set_width(26).move_to(2.2*LEFT+8*DOWN)
        )
        # Title
        title_properties = Text("Example Networks", color=YELLOW)
        title_properties.scale_in_place(1.2)
        title_properties.to_edge(UP).shift(LEFT*11+DOWN*5)

        # Title underline
        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)

        self.play(FadeIn(title_properties, shift=LEFT), GrowFromCenter(underline_properties))
        self.wait(3)

        x = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators", "Amplifiers") #, height=5, width=5, dot_scale_factor=3.5)
        for network in x:
            dot = MathTex("\\cdot").scale(3)
            dot.next_to(network[0], LEFT*0.4, buff=0.4)
            network.add_to_back(dot)
        x.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        #x.set_color_by_tex("Antennas", WHITE)

        x.scale_in_place(1.45)
        x.shift(LEFT*11.4+DOWN*6.1)
        x.set_opacity(0.5)
        self.play(Write(x))
        self.play(x.submobjects[0].animate.set_opacity(1))

        # PLOT
        ax.shift(DOWN*5.9+RIGHT*2.3).scale(1.25)

        curve1 = ax.get_graph(lambda x: 27*(-2.71828183** (-((x-2)**2)/(2*(0.2**2))) ) - 0.1, x_range=[0, 5], color=BLUE)

        line1 = ax.get_vertical_line(
            ax.i2gp(2, curve1), line_func=DashedLine, stroke_width=8, color=BLUE_E
        )
        dc_label = MathTex("\mathrm{DC}").next_to(ax).scale(0.9).shift(LEFT*14.29, UP*3.68).set_color(WHITE)
        frequency_label = MathTex("\mathrm{Frequency \ (GHz)}").next_to(ax).scale(1.1).shift(LEFT*9, UP*4.4).set_color(WHITE)
        magnitude_label = MathTex("\mathrm{Magnitude \ (dB)}").next_to(ax).scale(1.1).shift(LEFT*17.2+DOWN*0.3).set_color(WHITE).rotate(PI/2)

        self.play(
            Write(ax),
            Write(dc_label),
            Write(frequency_label),
            Write(magnitude_label),
            run_time=4, lag_ratio=0.2
        )

        ### Antennas
        ant_symbol = ImageMobject('/Users/Coto/Documents/edu/antenna.png').shift(DOWN*12.5+LEFT*10.5).scale(0.7)

        # Port 1 ANT
        port1_num_ant=MathTex("1").set_color(YELLOW)
        port1_num_ant.shift(DOWN * 13.7)
        port1_num_ant.shift(LEFT * 9.8)
        port1_num_ant.scale(1.8)

        self.play(FadeIn(ant_symbol, shift=UP))
        self.play(Write(port1_num_ant))

        # Right arrow
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*3).set_color(WHITE)

        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # n^2 = 1
        nsquared=MathTex("n^2", #0
        "=", #1
        "1", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared[0].set_color(YELLOW)
        nsquared[1].set_color(WHITE)
        nsquared[2].set_color(YELLOW)
        self.play(Write(nsquared))

        # 1-port matrix
        matrix_1=MathTex("\mathrm{S}", #0
        "=", #1
        r"\big(", #2
        "\mathrm{S}_{11}", #3
        r"\big)" #4
        ).next_to(long_right_arrow_wave).scale(2.2).shift(RIGHT*4+UP*0)

        matrix_1[0].set_color(YELLOW)
        matrix_1[1].set_color(WHITE)
        matrix_1[2].set_color(WHITE)
        matrix_1[3].set_color(BLUE)
        matrix_1[4].set_color(WHITE)
        self.play(Write(matrix_1))
        self.wait(3)

        # s11 magnitude
        s11_mag=MathTex("|", #0
        "\mathrm{S}_{11}", #1
        "(", #2
        "f", #3
        ")", #4
        "|" #5
        ).next_to(long_right_arrow_wave).scale(2.2).shift(RIGHT*4+UP*0)

        s11_mag[0].set_color(WHITE)
        s11_mag[1].set_color(BLUE)
        s11_mag[2].set_color(WHITE)
        s11_mag[3].set_color(MAROON)
        s11_mag[4].set_color(WHITE)
        s11_mag[5].set_color(WHITE)
        self.play(ReplacementTransform(matrix_1, s11_mag))


        self.play(Write(curve1), run_time=3)
        
        self.wait(3)
        self.play(Write(line1), run_time=1)


        
        # Delete plot antenna curve
        self.wait(3)

        ### Dummy Loads
        self.play(
        FadeOut(ant_symbol, shift=DOWN),
        FadeOut(port1_num_ant, shift=DOWN),
        Uncreate(line1), Uncreate(curve1), run_time=3, lag_ratio=0.2)
        self.play(
            x.submobjects[0].animate.set_opacity(0.5),
            x.submobjects[1].animate.set_opacity(1)
        )

        # Display circuit
        circuit_dummy = ImageMobject("/Users/Coto/Documents/edu/dummy_load.png").scale(0.65).shift(LEFT*10.5+DOWN*12.6)

        self.play(FadeIn(circuit_dummy, shift=RIGHT), run_time=1)

        # Show source framebox
        framebox_source = DashedVMobject(Rectangle(height=4.4, width=3.5).set_color(YELLOW).next_to(circuit_dummy).shift(LEFT*6.7), num_dashes=30, positive_space_ratio=0.6)
        self.play(Write(framebox_source), run_time=1.5)
        # Source label
        label_source = Text("Source").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_source.next_to(framebox_source, direction=UP)
        self.play(Write(label_source))
        self.wait(3)

        # Show load framebox
        framebox_load = DashedVMobject(Rectangle(height=4.4, width=2.7).set_color(YELLOW).next_to(circuit_dummy).shift(LEFT*2.7), num_dashes=27, positive_space_ratio=0.6)
        # Load label
        label_load = Text("Load").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_load.next_to(framebox_load, direction=UP)
        self.play(ReplacementTransform(framebox_source, framebox_load),
        ReplacementTransform(label_source, label_load),
        run_time=1.5)
        self.wait(3)

        # Hide framebox & label
        self.play(Uncreate(framebox_load), Unwrite(label_load))
        self.wait(3)

        # R_source label
        R_source=MathTex("R_{S}").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*4.24)
        R_source[0].set_color(WHITE)

        # R_load label
        R_load=MathTex("R_{L}").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*0.35)
        R_load[0].set_color(WHITE)

        self.play(Write(R_source))
        self.wait(3)
        self.play(Write(R_load))
        self.wait(3)

        # R_source 50ohm label
        R_source_50=MathTex("50 \ \Omega").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*4.4)
        R_source_50[0].set_color(WHITE)

        # R_load 50ohm label
        R_load_50=MathTex("50 \ \Omega").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*0.45)
        R_load_50[0].set_color(WHITE)

        self.play(ReplacementTransform(R_source, R_source_50), ReplacementTransform(R_load, R_load_50))

        # Display dummy load curve
        curve_load = ax.get_graph(lambda x: -30, x_range=[0, 5], color=BLUE)

        line1 = ax.get_vertical_line(
            ax.i2gp(2, curve1), line_func=DashedLine, stroke_width=8, color=YELLOW_E
        )

        self.play(Write(curve_load), run_time=3)
        self.wait(3)
        #self.play(Uncreate(curve_load), run_time=3)
        self.wait(3)

        # Hide dummy load section
        self.play(
        FadeOut(circuit_dummy, shift=DOWN),
        FadeOut(R_source_50, shift=DOWN),
        FadeOut(R_load_50, shift=DOWN),
        Uncreate(curve_load),
        FadeOut(long_right_arrow_wave, shift=RIGHT),
        Unwrite(s11_mag),
        Unwrite(nsquared), run_time=2)
        self.wait(3)
        self.play(
            x.submobjects[1].animate.set_opacity(0.5),
            x.submobjects[2].animate.set_opacity(1)
        )





        ### Filters
        ##### equation (desmos): f\left(x\right)=\frac{1}{\sqrt{1+\left(x-1.4\right)^{\left(2\cdot2\right)}}}

        # Display lowpass circuit
        circuit_lowpass = ImageMobject("/Users/Coto/Documents/edu/lowpass.png").scale(0.65).shift(LEFT*9.7+DOWN*12.6)

        self.play(FadeIn(circuit_lowpass, shift=RIGHT), run_time=1)

        # Show LC framebox
        framebox_LC = DashedVMobject(Rectangle(height=4.4, width=3.8).set_color(YELLOW).next_to(circuit_lowpass).shift(LEFT*6.3), num_dashes=30, positive_space_ratio=0.6)
        self.play(Write(framebox_LC), run_time=1.5)

        # Source label
        label_LC = Text("LC Filter").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_LC.next_to(framebox_LC, direction=UP)
        self.play(Write(label_LC))
        self.wait(3)

        # Hide framebox & label
        self.play(Uncreate(framebox_LC), Unwrite(label_LC))
        self.wait(3)

        # R_source label
        R_source=MathTex("R_{S}").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*5.2)
        R_source[0].set_color(WHITE)

        # R_load label
        R_load=MathTex("R_{L}").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*2.95)
        R_load[0].set_color(WHITE)

        self.play(Write(R_source), Write(R_load))
        self.wait(3)

        # R_source 50ohm label
        R_source_50=MathTex("50 \ \Omega").next_to(label_source).scale(1.3).shift(DOWN*0.32+LEFT*5.3)
        R_source_50[0].set_color(WHITE)

        # R_load 50ohm label
        R_load_50=MathTex("50 \ \Omega").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*3)
        R_load_50[0].set_color(WHITE)

        self.play(ReplacementTransform(R_source, R_source_50), ReplacementTransform(R_load, R_load_50))
        self.wait(3)

        # L_1 label
        L_1=MathTex("L_{1}").next_to(R_source_50).scale(1.3).shift(RIGHT*1.55)
        L_1[0].set_color(WHITE)

        # C_1 label
        C_1=MathTex("C_{1}").next_to(R_load_50).scale(1.3).shift(LEFT*3.8)
        C_1[0].set_color(WHITE)
        self.play(Write(L_1))
        self.play(Write(C_1))

        self.wait(3)

        # Right arrow
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*5.9).set_color(WHITE)

        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # n^2 = 4
        nsquared=MathTex("n^2", #0
        "=", #1
        "4", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared[0].set_color(YELLOW)
        nsquared[1].set_color(WHITE)
        nsquared[2].set_color(YELLOW)
        self.play(Write(nsquared))

        # 2-port matrix
        m1_2port = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_2port = MathTex("=")
        m2_2port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
                           [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_2port.shift(LEFT*2)
        eq_2port.next_to(m1_2port)
        m2_2port.next_to(eq_2port)
        m2_2port[0][0].set_color(BLUE)
        m2_2port[0][1].set_color(GREEN)
        m2_2port[0][2].set_color(RED)
        m2_2port[0][3].set_color(PURPLE)
        
        g_2port = VGroup(m1_2port, m2_2port, eq_2port).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*2.5+UP*0)

        self.play(Write(g_2port))
        self.wait(3)

        # Framebox S21

        framebox_s21 = SurroundingRectangle(m2_2port[0][2], buff = .2)
        self.play(Create(framebox_s21))
        self.wait(3)

        # Display S21 curve
        lowpass_s21 = ax.get_graph(lambda x: 10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))), x_range=[2.186, 5], color=RED)
        lowpass_s21_flat = ax.get_graph(lambda x: 0, x_range=[0, 2.186], color=RED)

        line1 = ax.get_vertical_line(
            ax.i2gp(3.5, lowpass_s21), line_func=DashedLine, stroke_width=8, color=ORANGE
        )

        cutoff_label=MathTex("-3 \mathrm{ \ dB}").next_to(R_source_50).scale(1.1).shift(RIGHT*15.8+UP*6.5)
        
        self.play(
            AnimationGroup(
                Write(lowpass_s21_flat),
                Write(lowpass_s21),
                run_time=3,
                lag_ratio=0.5
                )
        )
        self.wait(3)
        self.play(Write(line1),Write(cutoff_label))

        self.wait(3)

        framebox_s12 = SurroundingRectangle(m2_2port[0][1], buff = .2)

        # Display S12 curve
        lowpass_s12 = ax.get_graph(lambda x: 10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))), x_range=[2.186, 5], color=GREEN)
        lowpass_s12_flat = ax.get_graph(lambda x: 0, x_range=[0, 2.186], color=GREEN)

        self.play(
            AnimationGroup(
                ReplacementTransform(framebox_s21, framebox_s12),
                Write(lowpass_s12_flat),
                Write(lowpass_s12),
                run_time=3,
                lag_ratio=0.5
                ),
            #AnimationGroup(
            #    Uncreate(lowpass_s21),
            #    Uncreate(lowpass_s21_flat),
            #    run_time=3,
            #    lag_ratio=0.5
            #)
        )
        
        self.wait(3)

        # Hide S21 and S12 curves

        self.play(
        #    AnimationGroup(
        #        Uncreate(lowpass_s12),
        #        Uncreate(lowpass_s12_flat),
        #        run_time=3,
        #        lag_ratio=0.5
        #    ),
            Uncreate(line1),
            FadeOut(cutoff_label)
        )
        
        self.wait(3)

        # Display s11 curve
        lowpass_s11 = ax.get_graph(lambda x: 10*np.log10(1-10**((10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))))/10)), x_range=[2.3976, 5], color=BLUE)
        lowpass_s11_flat = ax.get_graph(lambda x: -30, x_range=[0, 2.3976], color=BLUE)

        framebox_s11 = SurroundingRectangle(m2_2port[0][0], buff = .2)
        self.play(
            ReplacementTransform(framebox_s12, framebox_s11),
            AnimationGroup(
                Write(lowpass_s11_flat),
                Write(lowpass_s11),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.wait(3)

        framebox_s22 = SurroundingRectangle(m2_2port[0][3], buff = .2)

        # Display S22 curve
        lowpass_s22 = ax.get_graph(lambda x: 10*np.log10(1-10**((10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))))/10)), x_range=[2.3976, 5], color=PURPLE)
        lowpass_s22_flat = ax.get_graph(lambda x: -30, x_range=[0, 2.3976], color=PURPLE)

        self.play(
            AnimationGroup(
                ReplacementTransform(framebox_s11, framebox_s22),
                Write(lowpass_s22_flat),
                Write(lowpass_s22),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.wait(3)

        # Hide curves section
        self.play(
            Uncreate(framebox_s22),
            AnimationGroup(
                Uncreate(lowpass_s11),
                Uncreate(lowpass_s22),
                Uncreate(lowpass_s21),
                Uncreate(lowpass_s12)
            ),
            run_time=1.5,
            lag_ratio=0.5
        )
        self.play(
            AnimationGroup(
                Uncreate(lowpass_s11_flat),
                Uncreate(lowpass_s22_flat),
                Uncreate(lowpass_s21_flat),
                Uncreate(lowpass_s12_flat)
            ),
            run_time=1.5,
            lag_ratio=0.5
        )


        #FadeOutAndShift(circuit_lowpass, direction=DOWN),
        #FadeOutAndShift(R_source_50, direction=DOWN),
        #FadeOutAndShift(R_load_50, direction=DOWN),
        
        #FadeOutAndShift(long_right_arrow_wave, direction=RIGHT),
        #Uncreate(s11_mag),
        #Uncreate(nsquared)
        #run_time=2)
        self.wait(3)






        ### Attenuator

        self.play(
            x.submobjects[2].animate.set_opacity(0.5),
            x.submobjects[3].animate.set_opacity(1)
        )

        # Display attenuator circuit
        circuit_attenuator = ImageMobject("/Users/Coto/Documents/edu/attenuator.png").scale(0.65).shift(LEFT*9.7+DOWN*12.6)

        self.play(
            FadeOut(L_1),
            FadeOut(C_1),
            ReplacementTransform(circuit_lowpass, circuit_attenuator)
        )

        # Show attenuator framebox
        framebox_attenuator = DashedVMobject(Rectangle(height=4.4, width=3.8).set_color(YELLOW).next_to(circuit_lowpass).shift(LEFT*6.4), num_dashes=30, positive_space_ratio=0.6)
        self.play(Write(framebox_attenuator), run_time=1.5)

        # Pi-pad attenuator label
        label_attenuator = Tex(r"$\Pi$-Pad Attenuator").set_color(YELLOW).scale(1).shift(DOWN*0.2)
        label_attenuator.next_to(framebox_attenuator, direction=UP)
        self.play(Write(label_attenuator))
        self.wait(3)

        # Hide framebox & label
        self.play(Unwrite(framebox_attenuator), Unwrite(label_attenuator))
        self.wait(3)

        # R_1 label
        R_1=MathTex("R_{1}").next_to(R_load_50).scale(1.3).shift(LEFT*6.6)
        R_1[0].set_color(WHITE)
        self.play(Write(R_1))

        # R_2 label
        R_2=MathTex("R_{2}").next_to(R_load_50).scale(1.3).shift(LEFT*6).shift(UP*1.8)
        R_2[0].set_color(WHITE)
        self.play(Write(R_2))

        # R_3 label
        R_3=MathTex("R_{3}").next_to(R_load_50).scale(1.3).shift(LEFT*3.92)
        R_3[0].set_color(WHITE)
        self.play(Write(R_3))

        # Framebox S21

        framebox_s21 = SurroundingRectangle(m2_2port[0][2], buff = .2)
        self.play(Create(framebox_s21))
        self.wait(3)

        # Display S21 curve
        attenuator_s21 = ax.get_graph(lambda x: - (-0.3)/( 0.4 ** (  (0.5*x - ((x)**(x-(9*(x**2)))))   )  ) - 1.8*x - 14.675 - 0.445, x_range=[0, 5], color=RED)
        line1 = ax.get_vertical_line(
            ax.i2gp(4, attenuator_s21), line_func=DashedLine, stroke_width=8, color=ORANGE
        )
        cutoff_label=MathTex("-20 \mathrm{ \ dB}").next_to(R_source_50).scale(1.1).shift(RIGHT*16.9+UP*2.6)
        
        self.play(
            AnimationGroup(
                #Write(attenuator_s21_flat),
                Write(attenuator_s21),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.play(Write(line1),Write(cutoff_label))

        attenuator_s12 = ax.get_graph(lambda x: - (-0.3)/( 0.4 ** (  (0.5*x - ((x)**(x-(9*(x**2)))))   )  ) - 1.8*x - 14.675 - 0.445, x_range=[0, 5], color=GREEN)

        framebox_s12 = SurroundingRectangle(m2_2port[0][1], buff = .2)

        self.play(
            AnimationGroup(
                ReplacementTransform(framebox_s21, framebox_s12),
                #Write(attenuator_s21_flat),
                Write(attenuator_s12),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.wait(3)
        self.play(
            Uncreate(line1),
            FadeOut(cutoff_label)
        )

        attenuator_s11 = ax.get_graph(lambda x: (0.2*(np.log(x+0.06)/np.log(1.1))) - 23, x_range=[0, 5], color=BLUE)
        # \left(0.2\log_{1.1}\left(x+0.06\right)\right)-23
        
        framebox_s11 = SurroundingRectangle(m2_2port[0][0], buff = .2)

        self.play(
            AnimationGroup(
                ReplacementTransform(framebox_s12, framebox_s11),
                #Write(attenuator_s21_flat),
                Write(attenuator_s11),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.wait(3)

        attenuator_s22 = ax.get_graph(lambda x: (0.2*(np.log(x+0.06)/np.log(1.1))) - 23, x_range=[0, 5], color=PURPLE)
        
        framebox_s22 = SurroundingRectangle(m2_2port[0][3], buff = .2)

        self.play(
            AnimationGroup(
                ReplacementTransform(framebox_s11, framebox_s22),
                Write(attenuator_s22),
                run_time=3,
                lag_ratio=0.5
                )
        )

        self.wait(3)





        ### Circulator

        self.play(
            x.submobjects[3].animate.set_opacity(0.5),
            x.submobjects[4].animate.set_opacity(1)
        )

        # Display circulator circuit
        circuit_circulator = ImageMobject("/Users/Coto/Documents/edu/circulator.png").scale(0.9).shift(LEFT*10.4+DOWN*12.9)

        self.play(
            Uncreate(attenuator_s11),
            Uncreate(attenuator_s12),
            Uncreate(attenuator_s21),
            Uncreate(attenuator_s22),
            Uncreate(framebox_s22),
            FadeOut(R_1),
            FadeOut(R_2),
            FadeOut(R_3),
            FadeOut(R_source_50),
            FadeOut(R_load_50),
            Unwrite(g_2port),
            Unwrite(nsquared),
            FadeOut(long_right_arrow_wave, shift=RIGHT),
            FadeOut(circuit_attenuator, shift=DOWN),
            FadeIn(circuit_circulator, shift=RIGHT)
        )

        # Port 1 Circulator
        port1_num_circ=MathTex("1").set_color(YELLOW)
        port1_num_circ.shift(DOWN * 11.4)
        port1_num_circ.shift(LEFT * 12.75)
        port1_num_circ.scale(1.8)
        # Port 2 Circulator
        port2_num_circ=MathTex("2").set_color(YELLOW)
        port2_num_circ.shift(DOWN * 11.4)
        port2_num_circ.shift(LEFT * 8.1)
        port2_num_circ.scale(1.8)
        # Port 3 Circulator
        port3_num_circ=MathTex("3").set_color(YELLOW)
        port3_num_circ.shift(DOWN * 14.1)
        port3_num_circ.shift(LEFT * 10.02)
        port3_num_circ.scale(1.8)
        # R_load label
        R_load=MathTex("R_{L}").scale(1.3).shift(DOWN * 13.65).shift(LEFT * 9.7)
        R_load[0].set_color(WHITE)

        self.play(
            Write(port1_num_circ)
        )
        self.play(
            Write(port2_num_circ)
        )
        self.play(
            Write(port3_num_circ)
        )

        # Right arrow
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*2.6).set_color(WHITE)

        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # n^2 = 9
        nsquared=MathTex("n^2", #0
        "=", #1
        "9", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared[0].set_color(YELLOW)
        nsquared[1].set_color(WHITE)
        nsquared[2].set_color(YELLOW)
        self.play(Write(nsquared))

        # 3-port matrix
        m1_3port = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_3port = MathTex("=")
        m2_3port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}", r"\mathrm{S}_{13}"],
                           [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}", r"\mathrm{S}_{23}"],
                           [r"\mathrm{S}_{31}", r"\mathrm{S}_{32}", r"\mathrm{S}_{33}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_2port.shift(LEFT*2)
        eq_3port.next_to(m1_3port)
        m2_3port.next_to(eq_3port)
        m2_3port[0][0].set_color(BLUE)
        m2_3port[0][1].set_color(GREEN)
        m2_3port[0][2].set_color(TEAL)
        m2_3port[0][3].set_color(RED)
        m2_3port[0][4].set_color(ORANGE)
        m2_3port[0][5].set_color(GOLD_A)
        m2_3port[0][6].set_color(PURPLE)
        m2_3port[0][7].set_color(MAROON_D)
        m2_3port[0][8].set_color(LIGHT_PINK)

        g_3port = VGroup(m1_3port, m2_3port, eq_3port).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*3.7+UP*0)

        self.play(Write(g_3port))

        self.wait(3)

        def create_csv(s):
            fin = open("manim_gif_data/circulator_data/"+s+".txt", "rt")
            fout = open("manim_gif_data/circulator_data/"+s+".csv", "wt")

            for line in fin:
	            fout.write(' '.join(line.split()).replace(' 1', '1').replace(' ', ',')+'\n')

            fin.close()
            fout.close()

        ### Set x-axis limits to 13-18 GHz
        self.play(
            Unwrite(dc_label),
            ReplacementTransform(ax, ax_highfreq)
        )
        #x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
        create_csv('s11')
        create_csv('s12')
        create_csv('s13')
        create_csv('s21')
        create_csv('s22')
        create_csv('s23')
        create_csv('s31')
        create_csv('s32')
        create_csv('s33')
        s11_circ = np.loadtxt(open("manim_gif_data/circulator_data/s11.csv", "rb"), delimiter=",", skiprows=2)
        s12_circ = np.loadtxt(open("manim_gif_data/circulator_data/s12.csv", "rb"), delimiter=",", skiprows=2)
        s13_circ = np.loadtxt(open("manim_gif_data/circulator_data/s13.csv", "rb"), delimiter=",", skiprows=2)
        s21_circ = np.loadtxt(open("manim_gif_data/circulator_data/s21.csv", "rb"), delimiter=",", skiprows=2)
        s22_circ = np.loadtxt(open("manim_gif_data/circulator_data/s22.csv", "rb"), delimiter=",", skiprows=2)
        s23_circ = np.loadtxt(open("manim_gif_data/circulator_data/s23.csv", "rb"), delimiter=",", skiprows=2)
        s31_circ = np.loadtxt(open("manim_gif_data/circulator_data/s31.csv", "rb"), delimiter=",", skiprows=2)
        s32_circ = np.loadtxt(open("manim_gif_data/circulator_data/s32.csv", "rb"), delimiter=",", skiprows=2)
        s33_circ = np.loadtxt(open("manim_gif_data/circulator_data/s33.csv", "rb"), delimiter=",", skiprows=2)

        circulator_s11 = ax_highfreq.get_line_graph(s11_circ[:,0], s11_circ[:,1], add_vertex_dots=False, line_color=BLUE)
        circulator_s12 = ax_highfreq.get_line_graph(s12_circ[:,0], s12_circ[:,1], add_vertex_dots=False, line_color=TEAL)
        circulator_s13 = ax_highfreq.get_line_graph(s13_circ[:,0], s13_circ[:,1], add_vertex_dots=False, line_color=GREEN)
        circulator_s21 = ax_highfreq.get_line_graph(s21_circ[:,0], s21_circ[:,1], add_vertex_dots=False, line_color=PURPLE)
        circulator_s22 = ax_highfreq.get_line_graph(s22_circ[:,0], s22_circ[:,1], add_vertex_dots=False, line_color=LIGHT_PINK)
        circulator_s23 = ax_highfreq.get_line_graph(s23_circ[:,0], s23_circ[:,1], add_vertex_dots=False, line_color=MAROON_D)
        circulator_s31 = ax_highfreq.get_line_graph(s31_circ[:,0], s31_circ[:,1], add_vertex_dots=False, line_color=RED)
        circulator_s32 = ax_highfreq.get_line_graph(s32_circ[:,0], s32_circ[:,1], add_vertex_dots=False, line_color=GOLD_A)
        circulator_s33 = ax_highfreq.get_line_graph(s33_circ[:,0], s33_circ[:,1], add_vertex_dots=False, line_color=ORANGE)

        # \left(0.2\log_{1.1}\left(x+0.06\right)\right)-23

        framebox_s11 = SurroundingRectangle(m2_3port[0][0], buff = .2)
        framebox_s12 = SurroundingRectangle(m2_3port[0][1], buff = .2)
        framebox_s13 = SurroundingRectangle(m2_3port[0][2], buff = .2)
        framebox_s21 = SurroundingRectangle(m2_3port[0][3], buff = .2)
        framebox_s22 = SurroundingRectangle(m2_3port[0][4], buff = .2)
        framebox_s23 = SurroundingRectangle(m2_3port[0][5], buff = .2)
        framebox_s31 = SurroundingRectangle(m2_3port[0][6], buff = .2)
        framebox_s32 = SurroundingRectangle(m2_3port[0][7], buff = .2)
        framebox_s33 = SurroundingRectangle(m2_3port[0][8], buff = .2)

        self.play(AnimationGroup(Create(framebox_s11),Write(circulator_s11),run_time=3,lag_ratio=0.5))
        self.wait(3)
        self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(circulator_s13),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s13),Write(circulator_s12),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s13,framebox_s21),Write(circulator_s31),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(circulator_s33),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s22,framebox_s23),Write(circulator_s32),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s23,framebox_s31),Write(circulator_s21),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s31,framebox_s32),Write(circulator_s23),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s32,framebox_s33),Write(circulator_s22),run_time=3,lag_ratio=0.5))
        
        self.wait(3)

        ### Isolator

        # n^2 = 4
        nsquared_isol=MathTex("n^2", #0
        "=", #1
        "4", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared_isol[0].set_color(YELLOW)
        nsquared_isol[1].set_color(WHITE)
        nsquared_isol[2].set_color(YELLOW)

        # 2-port matrix
        m1_2port_isol = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_2port_isol = MathTex("=")
        m2_2port_isol = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
                           [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_2port_isol.shift(LEFT*2)
        eq_2port_isol.next_to(m1_2port_isol)
        m2_2port_isol.next_to(eq_2port_isol)
        m2_2port_isol[0][0].set_color(BLUE)
        m2_2port_isol[0][1].set_color(GREEN)
        m2_2port_isol[0][2].set_color(RED)
        m2_2port_isol[0][3].set_color(PURPLE)
        
        g_2port_isol = VGroup(m1_2port_isol, m2_2port_isol, eq_2port_isol).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*3.2+UP*0)


        self.play(
            x.submobjects[4].animate.set_opacity(0.5),
            x.submobjects[5].animate.set_opacity(1)
        )

        # Display isolator circuit
        circuit_isolator = ImageMobject("/Users/Coto/Documents/edu/isolator.png").scale(0.9).shift(LEFT*10.4+DOWN*12.9).set_z_index(-1)
        isolator_s11 = circulator_s11.copy()
        isolator_s13 = circulator_s13.copy()
        isolator_s31 = circulator_s31.copy()
        isolator_s33 = circulator_s33.copy().set_color(PURPLE)
        self.play(
            ReplacementTransform(port3_num_circ, R_load),
            Uncreate(circulator_s11),
            Uncreate(circulator_s12),
            Uncreate(circulator_s13),
            Uncreate(circulator_s21),
            Uncreate(circulator_s22),
            Uncreate(circulator_s23),
            Uncreate(circulator_s31),
            Uncreate(circulator_s32),
            Uncreate(circulator_s33),
            FadeOut(framebox_s33),
            ReplacementTransform(g_3port, g_2port_isol),
            ReplacementTransform(nsquared, nsquared_isol),
            ReplacementTransform(circuit_circulator, circuit_isolator)
        )
        brace_isol = Brace(R_load, RIGHT, buff=0.1)
        text_isol = brace_isol.get_text("Matched ","Load")
        text_isol.scale(1.1) #.shift(LEFT*0.01)
        self.wait(3)
        self.play(GrowFromCenter(brace_isol))
        self.play(Write(text_isol))
        self.wait(3)
        self.play(FadeOut(brace_isol),Unwrite(text_isol))
        self.wait(3)

        framebox_s11 = SurroundingRectangle(m2_2port_isol[0][0], buff = .2)
        framebox_s12 = SurroundingRectangle(m2_2port_isol[0][1], buff = .2)
        framebox_s21 = SurroundingRectangle(m2_2port_isol[0][2], buff = .2)
        framebox_s22 = SurroundingRectangle(m2_2port_isol[0][3], buff = .2)

        self.play(AnimationGroup(Create(framebox_s11),Write(isolator_s11),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(isolator_s13),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s21),Write(isolator_s31),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(isolator_s33),run_time=3,lag_ratio=0.5))

        self.wait(3)






        ### Amplifier

        # Display amplifier circuit
        circuit_amplifier = ImageMobject("/Users/Coto/Documents/edu/amplifier.png").scale(0.6).shift(LEFT*10.6+DOWN*12.5).set_z_index(-1)

        self.play(
            Uncreate(isolator_s11),
            Uncreate(isolator_s13),
            Uncreate(isolator_s31),
            Uncreate(isolator_s33),
            FadeOut(framebox_s22)
        )
        self.play(
            ReplacementTransform(ax_highfreq, ax_amp)
        )

        # Plus symbol next to battery (+)
        plus=MathTex("+").set_color(WHITE)
        plus.shift(DOWN * 10.5)
        plus.shift(LEFT * 10.1)
        plus.scale(0.9)
        # Minus symbol next to battery (-)
        minus=MathTex("-").set_color(WHITE)
        minus.shift(DOWN * 10.5)
        minus.shift(LEFT * 9.3)
        minus.scale(0.9)

        # +V
        plusV=MathTex("\mathrm{+V}").set_color(WHITE)
        plusV.shift(DOWN * 11.1)
        plusV.shift(LEFT * 11.04)
        plusV.scale(0.85)

        # -V
        minusV=MathTex("\mathrm{-V}").set_color(WHITE)
        minusV.shift(DOWN * 14.1)
        minusV.shift(LEFT * 11.04)
        minusV.scale(0.85)

        # Plus symbol next to battery (+)
        voltage_num=MathTex("+").set_color(WHITE)
        voltage_num.shift(DOWN * 10.5)
        voltage_num.shift(LEFT * 10.1)
        voltage_num.scale(0.9)

        self.play(
            Unwrite(R_load),
            FadeOut(circuit_isolator, shift=DOWN),
            FadeIn(circuit_amplifier, shift=RIGHT),
            port1_num_circ.animate.shift(DOWN*0.8+LEFT*0.5),
            port2_num_circ.animate.shift(DOWN*0.8+RIGHT*0.1),
            x.submobjects[5].animate.set_opacity(0.5),
            x.submobjects[6].animate.set_opacity(1)
        )
        self.wait(3)
        self.play(
            Write(plus),
            Write(minus),
            Write(plusV),
            Write(minusV)
        )

        s11_amp = np.loadtxt(open("manim_gif_data/amplifier/s11.csv", "rb"), delimiter=",")
        s12_amp = np.loadtxt(open("manim_gif_data/amplifier/s12.csv", "rb"), delimiter=",")
        s21_amp = np.loadtxt(open("manim_gif_data/amplifier/s21.csv", "rb"), delimiter=",")
        s22_amp = np.loadtxt(open("manim_gif_data/amplifier/s22.csv", "rb"), delimiter=",")
        s11_amp[:,0] /= 1e9
        s12_amp[:,0] /= 1e9
        s12_amp[:,1] += 10
        s21_amp[:,0] /= 1e9
        s21_amp[:,1] -= 10
        s22_amp[:,0] /= 1e9

        amplifier_s11 = ax_amp.get_line_graph(s11_amp[:,0], s11_amp[:,1], add_vertex_dots=False, line_color=BLUE)
        amplifier_s12 = ax_amp.get_line_graph(s12_amp[:,0], s12_amp[:,1], add_vertex_dots=False, line_color=GREEN)
        amplifier_s21 = ax_amp.get_line_graph(s21_amp[:,0], s21_amp[:,1], add_vertex_dots=False, line_color=RED)
        amplifier_s22 = ax_amp.get_line_graph(s22_amp[:,0], s22_amp[:,1], add_vertex_dots=False, line_color=PURPLE)

        framebox_s11 = SurroundingRectangle(m2_2port_isol[0][0], buff = .2)
        framebox_s12 = SurroundingRectangle(m2_2port_isol[0][1], buff = .2)
        framebox_s21 = SurroundingRectangle(m2_2port_isol[0][2], buff = .2)
        framebox_s22 = SurroundingRectangle(m2_2port_isol[0][3], buff = .2)

        self.play(AnimationGroup(Create(framebox_s11),Write(amplifier_s11),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(amplifier_s12),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s21),Write(amplifier_s21),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(amplifier_s22),run_time=3,lag_ratio=0.5))
        self.wait(3)
        self.play(Uncreate(framebox_s22))

        self.wait(3)

        # 4.75-5.25 V DC tracker (counter)

        start = 4.75
        x_var = Variable(start, '', num_decimal_places=2).move_to(plus).shift(UP*0.6+LEFT*0.7).scale(1.2).set_color(TEAL)
        vdc = Tex(".V DC").scale(1.2).set_color(TEAL)
        # Hide '=' and '.'
        rectangle_equals = Rectangle(height=0.4, width=0.5, stroke_width=0, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(x_var).shift(LEFT*0.62).set_z_index(10)
        rectangle_dot = Rectangle(height=0.1, width=0.18, stroke_width=0, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(x_var).shift(RIGHT*0.91+DOWN*0.16).set_z_index(10)
        vdc.add_updater(lambda x: x.next_to(x_var,RIGHT,buff=0.05))
        self.play(
            FadeIn(rectangle_equals),
            FadeIn(rectangle_dot)
        )

        self.play(
            Write(x_var),
            Write(vdc)
        )
        self.wait(3)
        x_var.tracker.set_value(4.75)
        self.play(
            amplifier_s11.animate.shift(DOWN*0.2),
            amplifier_s12.animate.shift(DOWN*0.1), #at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(DOWN*0.2),
            amplifier_s22.animate.shift(UP*0.1),
            x_var.tracker.animate.set_value(5.25), run_time=3, rate_func=smooth
        )
        self.play(
            amplifier_s11.animate.shift(UP*0.2),
            amplifier_s12.animate.shift(UP*0.1), #at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(UP*0.2),
            amplifier_s22.animate.shift(DOWN*0.1),
            x_var.tracker.animate.set_value(4.75), run_time=3, rate_func=smooth
        )
        self.play(
            amplifier_s11.animate.shift(DOWN*0.1),
            amplifier_s12.animate.shift(DOWN*0.05), #at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(DOWN*0.1),
            amplifier_s22.animate.shift(UP*0.05),
            x_var.tracker.animate.set_value(5), run_time=1.5, rate_func=smooth
        )
        self.wait(3)

        # -20,+85 C temperature tracker (counter)
        def interpolate_color(color1, color2, alpha):
            rgb = interpolate(color_to_rgb(color1), color_to_rgb(color2), alpha)
            return rgb_to_color(rgb)
        def color_to_rgb(color):
            if isinstance(color, str):
                return hex_to_rgb(color)
            elif isinstance(color, Color):
                return np.array(color.get_rgb())
            else:
                raise Exception("Invalid color type")
        def rgb_to_color(rgb):
            try:
                return Color(rgb=rgb)
            except ValueError:
                return Color(WHITE)
        def get_alpha(Min,Max,Val):
            return (Val - Min)/(Max-Min)

        temp = ValueTracker(25)
        celcius = always_redraw(lambda: Tex("°C").scale(1.3).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))) if (temp.get_value()<0) else Tex("°C").scale(1.3).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))))
        celcius.add_updater(lambda x: x.next_to(temp_value,RIGHT,buff=0.05))
        temp_text = always_redraw(lambda: Tex("$T=$").move_to(frequency_label).shift(RIGHT*3.9).scale(1.3).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))) if (temp.get_value()<0) else Tex("$T=$").move_to(frequency_label).shift(RIGHT*3.9).scale(1.3).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))))
        temp_value = always_redraw(lambda: DecimalNumber(num_decimal_places=0,include_sign=True).set_value(temp.get_value()).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))).scale(1.3).next_to(temp_text, RIGHT, buff=0.1).shift(RIGHT*0.1) if (temp.get_value()<0) else DecimalNumber(num_decimal_places=0,include_sign=True).set_value(temp.get_value()).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))).scale(1.3).next_to(temp_text, RIGHT, buff=0.1).shift(RIGHT*0.1))
        framebox_temp = Rectangle(height=0.82, width=3.5, color=YELLOW, fill_color=BLACK, fill_opacity=0.35, stroke_width=1.5).move_to(temp_text).shift(RIGHT*1)
        self.play(
            Create(framebox_temp),
            Write(temp_text),
            Write(temp_value),
            Write(celcius)
        )
        self.wait(3)

        self.play(
            amplifier_s11.animate.shift(DOWN*0.2),
            amplifier_s12.animate.shift(DOWN*0.1), # at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(DOWN*0.4),
            amplifier_s22.animate.shift(UP*0.2),
            temp.animate.set_value(85), run_time=4, rate_func=smooth
        )
        self.wait(3)
        self.play(
            amplifier_s11.animate.shift(UP*0.2),
            amplifier_s12.animate.shift(UP*0.1), #at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(UP*0.4),
            amplifier_s22.animate.shift(DOWN*0.2),
            temp.animate.set_value(-20), run_time=5, rate_func=smooth
        )
        self.wait(3)
        self.play(
            amplifier_s11.animate.shift(DOWN*0.1),
            amplifier_s12.animate.shift(DOWN*0.05), #at some frequencies it also goes up, barely varies
            amplifier_s21.animate.shift(DOWN*0.2),
            amplifier_s22.animate.shift(UP*0.1),
            temp.animate.set_value(25), run_time=1.5, rate_func=smooth
        )

        self.wait(3)

        # s11 magnitude
        s_func=MathTex("\mathrm{S}", #0
        "(", #1
        "f", #2
        ",", #3
        "V_s", #4
        ",", #5
        "T", #6
        ")", #7
        ).move_to(g_2port_isol).scale(2.2).shift(RIGHT*0.5)

        s_func[0].set_color(YELLOW) #S
        s_func[1].set_color(WHITE) #()
        s_func[2].set_color(MAROON) #f
        s_func[3].set_color(WHITE) #,
        s_func[4].set_color(TEAL) #Vs
        s_func[5].set_color(WHITE) #,
        s_func[6].set_color(GOLD_E) #T
        s_func[7].set_color(WHITE) #)

        self.play(
            ReplacementTransform(g_2port_isol, s_func)
        )
        self.wait(3)
        framebox_s = SurroundingRectangle(s_func, buff = .2)
        self.play(Create(framebox_s))
        self.wait(3)

        s_func_p=MathTex("\mathrm{S}", #0
        "(", #1
        "f", #2
        ",", #3
        "V_s", #4
        ",", #5
        "T", #6
        ",", #7
        "P_\mathrm{in}", #8
        ")", #9
        ).move_to(g_2port_isol).scale(2.2).shift(RIGHT*0.8)
        framebox_p = SurroundingRectangle(s_func_p, buff = .2)

        s_func_p[0].set_color(YELLOW) #S
        s_func_p[1].set_color(WHITE) #()
        s_func_p[2].set_color(MAROON) #f
        s_func_p[3].set_color(WHITE) #,
        s_func_p[4].set_color(TEAL) #Vs
        s_func_p[5].set_color(WHITE) #,
        s_func_p[6].set_color(GOLD_E) #T
        s_func_p[7].set_color(WHITE) #,
        s_func_p[8].set_color(GREEN_B) #P_in
        s_func_p[9].set_color(WHITE) #)

        self.play(ReplacementTransform(framebox_s, framebox_p), ReplacementTransform(s_func, s_func_p))
        self.wait(3)

        # Move camera
        self.play((self.camera.frame.animate).shift(DOWN*14),run_time=2, rate_func=smooth)
        self.wait(3)

class scene_efield_thru(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[european,straightvoltages,straightlabels]{circuitikz}")

        circ="""\\begin{circuitikz}[american, line width=1pt]
                    \\draw[ultra thin](-4,0) to [R] (0,0) to [cute inductor] (3.5,-0) to[vC] (4.5,-0) to[diode] (10,-0);
                    \\draw[short, *-] (5.5,-0) to (5.49,0.01) to (5.51,-0.01) to (5.51,0.01) to (5.51,-0.01) to (5.49,-0.01) to (5.5,0.0) to [short, *-] (5.5,-2.5) to (5.49,-2.49) to (5.51,-2.51) to (5.51,-2.49) to (5.51,-2.51) to (5.49,-2.51) to (5.5,-2.5) ;
                    \\draw[ultra thin](0,0) to [capacitor,l^] (0,-1) to (0,-0.8) node[ground]{};;
                    \\draw[ultra thin](-4,-2.5) to [diode] (-2,-2.5) to [cute inductor] (1,-2.5) to[C] (3.5,-2.5) to[vC] (10,-2.5);
                    \\draw[ultra thin, short, *-] (5.5,-2.5) to [short, *-] (5.5,-2.5) to [short, -] (5.5,-2.5);
                    \\draw[ultra thin](4,-2.5) to [R] (4,-4.2) to (4,-4) node[ground]{};;
                    \\end{circuitikz}"""
        circuit1=Tex(circ,tex_template=myTemplate,stroke_width=2,fill_opacity=0).scale(0.5) #.shift(LEFT*-8.84)

        circuit_group1=VGroup(*[circuit1.copy() for s in range(30)]).set_x(0).arrange_in_grid(rows=6, buff=(0, 0.8)).scale(0.6).rotate(PI/22).set_color(DARK_GRAY)

        rectangle_efield = Rectangle(height=6.1, width=12, stroke_width=3, color=YELLOW_D, fill_color=BLACK, fill_opacity=0).shift(DOWN*0.25)
        rectangle_title = MathTex(r'\mathop{\mbox{$E$$-$$\mathrm{Field \ Simulation \ | \ Phase}$:\ }}',r'\phi ',r'=', color=YELLOW_D).scale(1.2)
        rectangle_title.set_color_by_tex_to_color_map({
        r'\phi': BLUE,
        r'=': BLUE
        })

        rectangle_title.shift(UP*3.35).shift(LEFT*0.7)
        rectangle_subtitle = MathTex(r'\mathop{\mbox{\textbf{E$/$M Solver:} Finite Integration Technique (FIT)}}', color=RED_B).scale(0.8)
        rectangle_subtitle.shift(DOWN*3.68)

        # 0-360 deg loop tracker (counter)
        start = 0
        x_var = Variable(start, '', num_decimal_places=0).shift(UP*3.35+RIGHT*3.1).scale(1.2)
        x_var.set_color(BLUE)
        Deg = Tex("°").scale(1.2)
        Deg.set_color(BLUE)
        Deg.add_updater(lambda x: x.next_to(x_var,RIGHT,buff=0.05).shift(UP*0.1))

        #self.add(x_var)
        #self.add(Deg)

        self.wait(3)
        self.play(
            Write(circuit_group1)
        )
        self.wait(3)
        self.play(
            Create(rectangle_efield),
            Write(rectangle_title),
        )
        self.wait(3)
        self.play(
            rectangle_efield.animate.set_opacity(1),
            Write(x_var),
            Write(Deg)
        )
        self.wait(3)
        self.play(Write(rectangle_subtitle))
        self.wait(3)
        for i in range(1, 7):
            x_var.tracker.set_value(0)
            self.play(x_var.tracker.animate.set_value(360), run_time=2, rate_func=linear)

        self.wait(3)

class vswr(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[1.001, 100, 20],
            y_range=[-60, 0, 10],
            x_length=10.5,
            y_length=5,
            x_axis_config={"numbers_to_include": [1, 20, 40, 60, 80, 100], "label_direction": UP},
            y_axis_config={"numbers_to_include": [-60, -50, -40, -30, -20, -10]},
            tips=False,
        )
        ax.shift(DOWN*0.85+RIGHT*0.2)
        zero_label = MathTex("0").next_to(ax).scale(0.75).shift(LEFT*11.45, UP*2.25).set_color(WHITE)
        vswr_label = MathTex("\mathrm{Voltage \ Standing \ Wave \ Ratio \ (VSWR)}").next_to(ax).scale(0.9).shift(LEFT*10, UP*3.2).set_color(WHITE)
        s11_label = MathTex("|\mathrm{S}_{11}| \ \mathrm{(dB)}}").next_to(ax).scale(0.9).shift(LEFT*13.3+DOWN*0.2).set_color(WHITE).rotate(PI/2)

        # Title
        title_properties = Text("Reflection Coefficient and VSWR", color=YELLOW)
        title_properties.scale_in_place(0.7)
        title_properties.to_edge(UP).shift(LEFT*3.2+UP*0.1)

        # Title underline
        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)
        self.play(Write(title_properties), GrowFromCenter(underline_properties))
        self.wait(3)
        self.play(Write(ax), Write(zero_label), Write(vswr_label), Write(s11_label), run_time=2.8, rate_func=smooth)
        vswr_graph_x = [1.002,1.0021,1.2021,1.4021,1.6021,1.8021,2.0021,2.2021,2.4021,2.6021,2.8021,3.0021,3.2021,3.4021,3.6021,3.8021,4.0021,4.2021,4.4021,4.6021,4.8021,5.0021,5.2021,5.4021,5.6021,5.8021,6.0021,6.2021,6.4021,6.6021,6.8021,7.0021,7.2021,7.4021,7.6021,7.8021,8.0021,8.2021,8.4021,8.6021,8.8021,9.0021,9.2021,9.4021,9.6021,9.8021,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        vswr_graph_y = [-60.00868155,-59.58532942,-20.74541447,-15.5251402,-12.71310711,-10.86510228,-9.530281847,-8.509885869,-7.699361713,-7.037322899,-6.48489297,-6.016043409,-5.612586929,-5.261376414,-4.952641372,-4.678951391,-4.434544304,-4.214876116,-4.016310887,-3.835901831,-3.67123349,-3.520305815,-3.381447619,-3.253250991,-3.134520937,-3.024236254,-2.921518782,-2.825609016,-2.735846574,-2.651654424,-2.572526055,-2.49801495,-2.427725911,-2.361307853,-2.298447776,-2.238865718,-2.182310484,-2.128556026,-2.07739836,-2.028652929,-1.982152329,-1.937744359,-1.895290325,-1.854663568,-1.815748185,-1.778437904,-1.743003514,-1.583624921,-1.451013343,-1.338935793,-1.242958135,-1.15983894,-1.087153246,-1.023050449,-0.9660935915,-0.9151498112,-0.8693138756,-0.8278537032,-0.7901708257,-0.7557712178,-0.7242434531,-0.6952421252,-0.6684751097,-0.6436936674,-0.6206846748,-0.5992644675,-0.5792739187,-0.560574472,-0.5430449209,-0.5265787744,-0.5110820894,-0.4964716745,-0.4826735943,-0.469621917,-0.4572576592,-0.4455278942,-0.4343849939,-0.4237859814,-0.4136919772,-0.4040677218,-0.3948811639,-0.3861031039,-0.3777068832,-0.3696681139,-0.3619644419,-0.3545753392,-0.3474819214,-0.340666786,-0.3341138701,-0.3278083238,-0.3217363979,-0.3158853437,-0.3102433236,-0.3047993311,-0.2995431194,-0.2944651364,-0.2895564674,-0.2848087823,-0.2802142889,-0.2757656897,-0.2714561438,-0.2672792312,-0.2632289212,-0.2592995433,-0.2554857607,-0.2517825462,-0.2481851596,-0.2446891283,-0.241290228,-0.237984466,-0.2347680654,-0.231637451,-0.2285892356,-0.2256202082,-0.2227273224,-0.219907686,-0.2171585518,-0.2144773078,-0.2118614699,-0.2093086736,-0.2068166668,-0.2043833036,-0.2020065381,-0.1996844181,-0.1974150805,-0.1951967458,-0.1930277135,-0.1909063581,-0.1888311247,-0.1868005251,-0.1848131347,-0.1828675888,-0.1809625795,-0.1790968531,-0.1772692066,-0.1754784862,-0.1737235837]
        vswr_graph = ax.get_line_graph(vswr_graph_x, vswr_graph_y, add_vertex_dots=False).set_color(TEAL)
        
        # Equations
        gamma_eq = MathTex(r'\Gamma',r'=',r'{{Z_{L}',r'-',r'Z_{0}}','\over',r'{Z_{L}',r'+',r'Z_{0}',r'}} = ',r'{{\mathrm{VSWR}',r'-1}','\over',r'{\mathrm{VSWR}',r' + 1}',r'}').next_to(ax).scale(1).shift(LEFT*8.7, UP*0.8).set_color(WHITE)
        #gamma_eq = MathTex(r"\Gamma = \frac{Z_{L}-Z_{0}}{Z_{L}+Z_{0}} = \frac{\mathrm{VSWR}-1}{\mathrm{VSWR}+1}").next_to(ax).scale(1).shift(LEFT*8.7, UP*0.8).set_color(WHITE)
        gamma_eq.set_color_by_tex_to_color_map({
        r'\Gamma': GREEN_B,
        r'Z': ORANGE,
        r'VSWR': TEAL,
        })
        s11_vswr_eq = MathTex(r'\Longrightarrow |',r'\mathrm{S}_{11}',r'| = 20\log_{10}',r'{\left(',r'{{\mathrm{VSWR}',r'-1}','\over',r'{\mathrm{VSWR}',r'+1}',r'}\right)}').next_to(ax).scale(1).shift(LEFT*9.5, DOWN*1.4).set_color(WHITE)
        s11_vswr_eq.set_color_by_tex_to_color_map({
        r'\mathrm{S}_{11}': YELLOW,
        r'VSWR': TEAL
        })
        self.wait(3)
        self.play(Write(gamma_eq))
        self.wait(3)
        self.play(Write(s11_vswr_eq))
        self.wait(3)
        framebox_gamam_eq = SurroundingRectangle(gamma_eq, buff = .3).set_color(MAROON)
        framebox_s11_vswr_eq = SurroundingRectangle(s11_vswr_eq, buff = .3).set_color(MAROON)
        self.play(Create(framebox_gamam_eq))
        self.wait(3)
        self.play(
            ReplacementTransform(framebox_gamam_eq, framebox_s11_vswr_eq)
        )
        self.wait(3)
        self.play(Create(vswr_graph), run_time=2, rate_func=rush_into)
        self.wait(3)

class scene6(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        self.play(
            self.camera.frame.animate.set_width(26).move_to(2.2*LEFT+8*DOWN)
        )
        self.play((self.camera.frame.animate).shift(DOWN*5))

        # Title
        title_classifying = Text("Designating S-Parameters", color=YELLOW)
        title_classifying.scale_in_place(1.2)
        title_classifying.to_edge(UP).shift(LEFT*9.8+DOWN*9.9)

        # Title underline
        underline_classifying = Line(LEFT, RIGHT, color=YELLOW)
        underline_classifying.set_width(1.1*title_classifying.get_width())
        underline_classifying.next_to(title_classifying, DOWN)
        underline_classifying.shift(UP * 0.1)
        self.play(FadeIn(title_classifying, shift=LEFT), GrowFromCenter(underline_classifying))

        m1_map = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_map = MathTex("=").set_color(WHITE)
        m2_map = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{1n}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{n1}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_map.shift(DOWN*13.15) #RIGHT*1.2
        eq_map.next_to(m1_map)
        m2_map.next_to(eq_map)

        m2_map[0][0].set_color(BLUE)
        m2_map[0][1].set_color(RED)
        m2_map[0][2].set_color(RED)
        m2_map[0][3].set_color(RED)
        m2_map[0][4].set_color(BLUE)
        m2_map[0][5].set_color(RED)
        m2_map[0][6].set_color(RED)
        m2_map[0][7].set_color(RED)
        m2_map[0][8].set_color(BLUE)
        g_map = VGroup(m1_map, m2_map, eq_map).scale(2.2).shift(LEFT*5.5)
        m1_map_clear = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_map_clear = MathTex("=").set_color(WHITE)
        m2_map_clear = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{1n}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{n1}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_map_clear.shift(DOWN*13.15) #RIGHT*1.2
        eq_map_clear.next_to(m1_map_clear)
        m2_map_clear.next_to(eq_map_clear)
        m2_map_clear[0][0].set_color(YELLOW)
        m2_map_clear[0][1].set_color(WHITE)
        m2_map_clear[0][2].set_color(YELLOW)
        m2_map_clear[0][3].set_color(WHITE)
        m2_map_clear[0][4].set_color(WHITE)
        m2_map_clear[0][5].set_color(WHITE)
        m2_map_clear[0][6].set_color(YELLOW)
        m2_map_clear[0][7].set_color(WHITE)
        m2_map_clear[0][8].set_color(YELLOW)
        g_map_clear = VGroup(m1_map_clear, m2_map_clear, eq_map_clear).scale(2.2).shift(LEFT*5.5).shift(RIGHT*(5.5+1.2))
        m1_map_t = MathTex(r"\mathrm{S}^\mathrm{T}").set_color(YELLOW)
        eq_map_t = MathTex("=").set_color(WHITE)
        m2_map_t = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{n1}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{1n}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        m1_map_t.shift(DOWN*13.15) #RIGHT*1.2
        eq_map_t.next_to(m1_map_t)
        m2_map_t.next_to(eq_map_t)
        m2_map_t[0][0].set_color(YELLOW)
        m2_map_t[0][1].set_color(WHITE)
        m2_map_t[0][2].set_color(YELLOW)
        m2_map_t[0][3].set_color(WHITE)
        m2_map_t[0][4].set_color(WHITE)
        m2_map_t[0][5].set_color(WHITE)
        m2_map_t[0][6].set_color(YELLOW)
        m2_map_t[0][7].set_color(WHITE)
        m2_map_t[0][8].set_color(YELLOW)
        self.play(Write(g_map))
        self.wait(3)
        self.play(g_map.animate.shift(RIGHT*(5.5+1.2)))
        g_map_t = VGroup(m1_map_t, m2_map_t, eq_map_t).scale(2.2).shift(LEFT*5.5).shift(RIGHT*(5.5+1.2))

        # Title refl
        title_refl = Tex(r"Reflection Coefficients ",r"$(i = j)$", color=BLUE)
        title_refl.set_color_by_tex_to_color_map({
        "j": YELLOW_D
        })
        title_refl.scale_in_place(1.5)
        title_refl.to_edge(UP).shift(LEFT*9.09+DOWN*(13-0.5))
        # Title refl underline
        underline_refl = Line(LEFT, RIGHT, color=BLUE)
        underline_refl.set_width(1.1*title_refl.get_width())
        underline_refl.next_to(title_refl, DOWN)
        underline_refl.shift(UP * 0.1)

        s11_txt = Tex(r"$\cdot$ $\mathrm{S}_{11}$ | Input return loss, VSWR", color=BLUE_B)
        s11_txt.scale_in_place(1.4)
        s11_txt.to_edge(UP).shift(LEFT*9.05+DOWN*(14.3-0.5))
        s22_txt = Tex(r"$\cdot$ $\mathrm{S}_{22}$ | Output return loss, VSWR", color=BLUE_B)
        s22_txt.scale_in_place(1.4)
        s22_txt.to_edge(UP).shift(LEFT*8.75+DOWN*(15.3-0.5))

        # Title tran
        title_tran = Tex(r"Transmission Coefficients ",r"$(i \neq j)$", color=RED)
        title_tran.set_color_by_tex_to_color_map({
        "j": YELLOW_D
        })
        title_tran.scale_in_place(1.5)
        title_tran.to_edge(UP).shift(LEFT*8.5+DOWN*(12+6))
        # Title tran underline
        underline_tran = Line(LEFT, RIGHT, color=RED)
        underline_tran.set_width(1.1*title_tran.get_width())
        underline_tran.next_to(title_tran, DOWN)
        underline_tran.shift(UP * 0.1)

        s21_txt = Tex(r"$\cdot$ $\mathrm{S}_{21}$ | Gain ($>0 \mathrm{ \ dB}$), Loss ($\leq0 \mathrm{ \ dB}$)", color=RED_B)
        s21_txt.scale_in_place(1.4)
        s21_txt.to_edge(UP).shift(LEFT*8.35+DOWN*(13.3+6))
        s12_txt = Tex(r"$\cdot$ $\mathrm{S}_{12}$ | Reverse Isolation", color=RED_B)
        s12_txt.scale_in_place(1.4)
        s12_txt.to_edge(UP).shift(LEFT*10.3+DOWN*(14.3+6))

        self.play(FadeIn(title_refl, shift=LEFT), GrowFromCenter(underline_refl))
        self.play(Write(s11_txt))
        self.play(Write(s22_txt))
        self.wait(3)
        self.play(FadeIn(title_tran, shift=LEFT), GrowFromCenter(underline_tran))
        self.play(Write(s21_txt))
        self.play(Write(s12_txt))
        self.wait(3)

        # Reciprocity & Losslessness
        title_rec = Text("Reciprocity & Losslessness", color=YELLOW)
        title_rec.scale_in_place(1.2)
        title_rec.to_edge(UP).shift(LEFT*9.6+DOWN*9.9)
        # Title rec underline
        underline_rec = Line(LEFT, RIGHT, color=YELLOW)
        underline_rec.set_width(1.1*title_rec.get_width())
        underline_rec.next_to(title_rec, DOWN)
        underline_rec.shift(UP * 0.1)

        self.play(
            FadeOut(title_refl),
            FadeOut(title_tran),
            FadeOut(s11_txt),
            FadeOut(s22_txt),
            FadeOut(s21_txt),
            FadeOut(s12_txt),
            FadeOut(underline_refl),
            FadeOut(underline_tran),
            ReplacementTransform(title_classifying, title_rec),
            ReplacementTransform(underline_classifying, underline_rec),
            ReplacementTransform(g_map, g_map_clear)
        )
        self.wait(3)
        # Title recipr
        title_recipr = Tex(r"Reciprocal Networks", color=TEAL)
        title_recipr.scale_in_place(1.5)
        title_recipr.to_edge(UP).shift(LEFT*(9.09+1.7)+DOWN*(13-0.5)).shift(DOWN*0.2)
        # Title recipr underline
        underline_recipr = Line(LEFT, RIGHT, color=TEAL)
        underline_recipr.set_width(1.1*title_recipr.get_width())
        underline_recipr.next_to(title_recipr, DOWN)
        underline_recipr.shift(UP * 0.1)

        rec1_txt = Tex(r"$\cdot$ ",r"$\mathrm{S}_{ij}$",r"$\mathrm{}=\mathrm{}$",r"$\mathrm{S}_{ji}$",r"$, \mathrm{ \ } $",r"$i \neq j$", color=TEAL_B)
        rec1_txt.set_color_by_tex_to_color_map({
        r"ij": YELLOW,
        r"=": WHITE,
        r"ji": YELLOW,
        r",": WHITE,
        r"i \neq j": YELLOW_D
        })
        rec1_txt.scale_in_place(1.4)
        rec1_txt.to_edge(UP).shift(LEFT*(9.05+2.5)+DOWN*(15.3-0.45)).shift(DOWN*0.2)
        rec2_txt = Tex(r"$\cdot$ ",r"$\mathrm{S}$",r"$\mathrm{}=\mathrm{}$",r"$\mathrm{S}^{\mathrm{T}}$",r"$\mathrm{}\Leftrightarrow$", color=TEAL_B)
        rec2_txt.set_color_by_tex_to_color_map({
        r"S": YELLOW,
        r"=": WHITE,
        r"\Leftrightarrow": WHITE
        })
        rec2_txt.scale_in_place(1.4)
        rec2_txt.to_edge(UP).shift(LEFT*(8.3+4.1)+DOWN*(14.3-0.45)).shift(DOWN*0.2)
        self.play(FadeIn(title_recipr, shift=LEFT), GrowFromCenter(underline_recipr))
        self.play(Write(rec2_txt))
        self.play(g_map_clear.animate.shift(UP*3.5),
        TransformFromCopy(g_map_clear, g_map_t.shift(DOWN*3.5+LEFT*0.3))
        )
        self.play(Write(rec1_txt))

        self.wait(3)

        # Title loss
        title_loss = Tex(r"Lossless Networks", color=PURPLE)
        title_loss.scale_in_place(1.5)
        title_loss.to_edge(UP).shift(LEFT*(9.09+2.18)+DOWN*(19-0.5)).shift(UP*0.6)
        # Title loss underline
        underline_loss = Line(LEFT, RIGHT, color=PURPLE)
        underline_loss.set_width(1.1*title_loss.get_width())
        underline_loss.next_to(title_loss, DOWN)
        underline_loss.shift(UP * 0.1)

        loss1_txt = Tex(r"$\cdot$ ",r"$P$",r"$\mathrm{} \propto \mathrm{}$",r"$V^2$",r"$\mathrm{}\Longrightarrow$", color=PURPLE_B)
        loss1_txt.set_color_by_tex_to_color_map({
        r"P": MAROON,
        r"\propto": WHITE,
        r"V": GREEN,
        r"$\mathrm{}\Longrightarrow$": WHITE,
        })
        loss1_txt.scale_in_place(1.4)
        loss1_txt.to_edge(UP).shift(LEFT*(8.88+3.2)+DOWN*(20.3-0.6)).shift(UP*0.6)
        loss2_txt = Tex(r"$\cdot$ ",r"$\sum\limits_{i=1}^{n} |$",r"$\mathrm{S}_{ij}$",r"$|^2$",r"$\mathrm{}=\mathrm{}$",r"$1$",r"$, \forall $",r"$j\mathrm{\ }$",r"$ \in $",r"$\mathrm{\ }[1, n]\mathrm{\ }$",r"$ \cap $",r"$\mathrm{\ }\mathbb{Z}$", color=WHITE)
        loss2_txt.set_color_by_tex_to_color_map({
        r"$\cdot$ ": PURPLE_B,
        r"S": YELLOW,
        r"$\mathrm{}=\mathrm{}$ ": WHITE,
        r"$\mathrm{\ }[1, n]\mathrm{\ }$": PURPLE,
        r"$1$": YELLOW,
        r"$\mathrm{\ }\mathbb{Z}$": ORANGE,
        r"$j\mathrm{\ }$": GOLD
        })
        loss2_txt.scale_in_place(1.4)
        loss2_txt.to_edge(UP).shift(LEFT*(5.45+4.1)+DOWN*(21.3-0.6)).shift(UP*0.6)
        self.play(FadeIn(title_loss, shift=LEFT), GrowFromCenter(underline_loss))
        self.wait(3)
        framebox1_scene6 = Rectangle(height=5.2, width=2, stroke_width=3, color=PURPLE_A, fill_color=PURPLE, fill_opacity=0.25).move_to(g_map_clear).shift(DOWN*0+LEFT*1.75)
        self.play(Write(loss1_txt))
        self.wait(3)
        self.play(Create(framebox1_scene6))
        self.wait(3)
        self.play(framebox1_scene6.animate.shift(RIGHT*2.88))
        self.wait(3)
        self.play(framebox1_scene6.animate.shift(RIGHT*2.86))
        self.wait(3)
        self.play(Uncreate(framebox1_scene6))
        self.wait(3)
        self.play(Write(loss2_txt))
        self.wait(3)

class vswr_animation(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=5,
            #x_axis_config={"numbers_to_include": [1, 20, 40, 60, 80, 100], "label_direction": UP},
            #y_axis_config={"numbers_to_include": [-60, -50, -40, -30, -20, -10]},
            tips=False,
        )
        ax.shift(DOWN*0+LEFT*0.4)
        #zero_label = MathTex("0").next_to(ax).scale(0.75).shift(LEFT*11.45, UP*2.25).set_color(WHITE)
        #vswr_label = MathTex("\mathrm{Voltage \ Standing \ Wave \ Ratio \ (VSWR)}").next_to(ax).scale(0.9).shift(LEFT*10, UP*3.2).set_color(WHITE)
        #s11_label = MathTex("|\mathrm{S}_{11}| \ \mathrm{(dB)}}").next_to(ax).scale(0.9).shift(LEFT*13.3+DOWN*0.2).set_color(WHITE).rotate(PI/2)

        # Title
        title_properties = Text("Interpreting Standing Waves", color=YELLOW)
        title_properties.scale_in_place(0.7)
        title_properties.to_edge(UP).shift(LEFT*3.2+UP*0.1).shift(LEFT*0.5)

        # Title underline
        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)
        self.play(Write(title_properties), GrowFromCenter(underline_properties))
        self.wait(3)
        self.play(Write(ax),run_time=2)
        self.wait(3)
        #self.play(Write(ax), Write(vswr_label), Write(s11_label), run_time=2.8, rate_func=smooth)
        phi = 0
        b_inc = ax.get_graph(lambda x: np.sin(15*x+phi)).set_color(BLACK)
        b_ref = ax.get_graph(lambda x: -0.7*np.sin(15*x+20)).set_color(BLACK)
        b_sum = ax.get_graph(lambda x: np.sin(15*x+phi)-0.7*np.sin(15*x+20)).set_color(BLACK)
        point_v_max = ax.c2p(1.145, 1.7)
        point_v_min = ax.c2p(1.145, 0.305)
        for phi in range(0, 200*8): #200 -> 1000 for increased duration - adjust phi values below accordingly (multiply by 4)
            a_inc = b_inc
            b_inc = ax.get_graph(lambda x: np.sin((15*x)-((phi/10)+(1/10)))).set_color(BLUE) #divide /50 not /10
            self.remove(a_inc)
            self.add(b_inc)
            if phi >= 20*8:
                a_ref = b_ref
                b_ref = ax.get_graph(lambda x: -0.7*np.sin((15*x)+(((phi)/10)+(1/10)))).set_color(RED) #divide /50 not /10
                self.remove(a_ref)
                self.add(b_ref)
            if phi >= 40*8:
                a_sum = b_sum
                b_sum = ax.get_graph(lambda x: np.sin((15*x)-((phi/10)+(1/10)))-0.7*np.sin((15*x)+(((phi)/10)+(1/10)))).set_color(GREEN)
                self.remove(a_sum)
                self.add(b_sum)
            if phi == 90*8:
                V_max_line = ax.get_horizontal_line(point_v_max, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)
                self.add(V_max_line)
            if phi == 70*8:
                V_min_line = ax.get_horizontal_line(point_v_min, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)
                self.add(V_min_line)
            if phi == 110*8:
                V_max_label = MathTex(r'|',r'V_\mathrm{max}',r'|').next_to(V_max_line, direction=UP).shift(RIGHT*5.26+DOWN*0.12).scale(1).set_color(WHITE).shift(LEFT*0.2)
                V_max_label.set_color_by_tex_to_color_map({
                r'V_\mathrm{max}': YELLOW_D,
                }) 
                V_min_label = MathTex(r'|',r'V_\mathrm{min}',r'|').next_to(V_min_line, direction=UP).shift(RIGHT*5.26+DOWN*0.12).scale(1).set_color(WHITE).shift(LEFT*0.2)
                V_min_label.set_color_by_tex_to_color_map({
                r'V_\mathrm{min}': YELLOW_D,
                }) 
                vswr_V_eq_long = MathTex(r'\mathrm{Voltage \ Standing \ Wave \ Ratio}',r'=',r'{{|',r'V_\mathrm{max}',r'|}','\over',r'{|',r'V_\mathrm{min}',r'|}}').scale(1).shift(LEFT*0+DOWN*3.12).set_color(WHITE)
                vswr_V_eq_long.set_color_by_tex_to_color_map({
                r'V_\mathrm{max}': YELLOW_D,
                r'V_\mathrm{min}': YELLOW_D,
                r'\mathrm{Voltage \ Standing \ Wave \ Ratio}': TEAL,
                }) 
                vswr_V_eq = MathTex(r'\mathrm{VSWR}',r'=',r'{{|',r'V_\mathrm{max}',r'|}','\over',r'{|',r'V_\mathrm{min}',r'|}}').scale(1).shift(LEFT*0+DOWN*3.12).set_color(WHITE)
                vswr_V_eq.set_color_by_tex_to_color_map({
                r'V_\mathrm{max}': YELLOW_D,
                r'V_\mathrm{min}': YELLOW_D,
                r'VSWR': TEAL,
                }) 
                self.play(Write(V_min_label))
                self.wait(3)
                self.play(Write(V_max_label))
                self.wait(3)
                self.play(Write(vswr_V_eq_long))
                self.wait(3)
                self.play(ReplacementTransform(vswr_V_eq_long, vswr_V_eq))

            self.wait(0.08)
        self.wait(3)

class outro(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-15, 15, 1],
            y_range=[-2, 2, 1],
            x_length=20,
            tips=False,
        ).shift(UP*20)
        wavelet = axes.get_graph(lambda x: np.cos(2*np.pi*x-2*np.pi*5)*np.exp(-x**2), color=BLUE).shift(DOWN*20.3).set_z_index(20)

        rectangle_outro = Rectangle(height=50, width=20, stroke_width=0, fill_color=BLACK, fill_opacity=0.6, z_index=-1).set_z_index(10)
        self.play(FadeIn(rectangle_outro))
        # Title
        title = Text("Special Thanks", gradient=(ORANGE,RED_D)).set_z_index(20)
        title.scale_in_place(1.5)
        title.to_edge(UP)

        # Title underline
        underline = Line(LEFT, RIGHT).set_z_index(20)
        underline.set_color(color_gradient([RED_D,ORANGE],10))
        underline.set_width(1.1*title.get_width())
        underline.next_to(title, DOWN)
        underline.shift(UP * 0.1)

        # Names
        thanks1 = Text("Athanasios Kanatas", color=YELLOW_D).set_z_index(20).scale(0.8).shift(LEFT*3.5+UP*1.55)
        thanks2 = Text("Leonidas Marantis", color=YELLOW_D).set_z_index(20).scale(0.8).shift(LEFT*3.5+UP*0.45)
        thanks3 = Text("Dimitrios Rongas", color=YELLOW_D).set_z_index(20).scale(0.8).shift(RIGHT*3.5+UP*1.55)
        thanks4 = Text("Cameron Van Eck", color=YELLOW_D).set_z_index(20).scale(0.8).shift(RIGHT*3.5+UP*0.45)
        thanks_manim = Text("Manim Community & Developers", color=GOLD).set_z_index(20).scale(0.7).shift(LEFT*0.8+DOWN*2.1)
        thanks_3b1b = Text("Grant Sanderson (3Blue1Brown)", color=GOLD).set_z_index(20).scale(0.7).shift(LEFT*0.7+DOWN*3.2)

        # Manim Community
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#e7e0da"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN).set_z_index(20)
        logo.scale(0.2).shift(RIGHT*3.3+DOWN*2.1)

        #3b1b logo
        logo_3b1b = SVGMobject("/Users/Coto/Documents/edu/3b1b_logo.svg").set_z_index(20).scale(0.42).shift(DOWN*3.2+RIGHT*3.2)

        t = ValueTracker(0)

        def func1(x):
            w = lambda p: 0.35*np.array([p[1]*np.cos(x)-p[0]*np.sin(x),-p[1]*np.sin(x)-p[0]*np.cos(x),0])
            return w

        field1 = ArrowVectorField(func1(float(t.get_value()))).set_z_index(0)
        field1.set_color_by_gradient(BLUE_D, BLUE_E)
        field1.add_updater(lambda j: j.become(ArrowVectorField(func1(float(t.get_value())))))
        
        #Logo = Text("Special thanks...").scale(1).move_to([0,-0.2,0])
        #Logo2 = Text("EE", color = BLUE).scale(4).move_to([2,-1.5,0])
        self.add(field1)

        # 8-sec
        self.play(t.animate.set_value(0+8), run_time = 16, rate_func=linear)
        # title
        self.play(Write(title),GrowFromCenter(underline), t.animate.set_value(8+0.5), run_time = 1, rate_func=linear)
        # 1-sec
        self.play(t.animate.set_value(8.5+0.5), run_time = 1, rate_func=linear)
        # thanks 1-4
        self.play(AnimationGroup(Write(thanks1),Write(thanks2),Write(thanks3),Write(thanks4),lag_ratio=0.4),t.animate.set_value(9+0.5),run_time=1, rate_func=linear)
        # 1-sec
        self.play(t.animate.set_value(9.5+0.5), run_time = 1, rate_func=linear)
        # wavelet
        self.play(Write(wavelet),t.animate.set_value(10+2),run_time=4, rate_func=linear)
        # 0.5-sec
        self.play(t.animate.set_value(12+0.25), run_time = 0.5, rate_func=linear)
        # manim thanks
        self.play(GrowFromCenter(logo_3b1b),Write(thanks_manim),Write(thanks_3b1b),Create(logo),FadeIn(axes),t.animate.set_value(12.25+0.5),run_time=1, rate_func=linear)
        # 8-sec
        self.play(t.animate.set_value(12.75+4), run_time = 8, rate_func=linear)

        ###self.play(Rotate(field1.scale(2),PI),run_time = 6)
