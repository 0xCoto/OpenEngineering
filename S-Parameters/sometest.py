class matrix_example(Scene):
    def construct(self):
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

        g_3port = VGroup(m1_3port, m2_3port, eq_3port).scale(2).shift(RIGHT*3.7+UP*0)

        self.play(Write(g_3port))