from manim import *

class Snell(Scene):
    notifier = Dot(color=LIGHTER_GRAY, radius=0.05)
    notifier.move_to(7 * RIGHT + 3.9 * DOWN)

    def noticewait(self):
        self.add(self.notifier)
        self.wait()
        self.remove(self.notifier)

    def construct(self):
        self.camera.background_color = WHITE

        self.wait()
        self.noticewait()

        p = Dot([-1.5 - 4.5, 3, 0], color=BLACK, z_index=1)
        q = Dot([1.5 - 4.5, -3, 0], color=BLACK, z_index=1)
        interface = Line(
            [-2.51 - 4.5 - 0.5,0,0],
            [2.01 - 4.5,0,0],
            stroke_width=2,
            color=BLUE
        )

        water = Rectangle(BLUE_B, height=4, width=4.5 + 0.5, z_index = -1)
        water.set_fill(BLUE_B, opacity=1)
        water.align_to(interface, UP).shift((0.25 + 4.75)*LEFT)

        self.play(FadeIn(water), Create(interface))
        self.play(Create(p), Create(q))
        self.noticewait()

        x = ValueTracker(1 - 4.5)

        contact = Dot([x.get_value(),0,0], color=YELLOW, radius=0.01)
        ray1 = Line(p.get_center(), [x.get_value(),0,0], color=YELLOW)
        ray2 = Line([x.get_value(),0,0], q.get_center(), color=YELLOW)

        contact.add_updater(
            lambda s : s.move_to([x.get_value(),0,0])
        )
        ray1.add_updater(
            lambda s : s.put_start_and_end_on(
                p.get_center(),
                [x.get_value(),0,0]
            )
        )
        ray2.add_updater(
            lambda s : s.put_start_and_end_on(
                [x.get_value(),0,0],
                q.get_center()
            )
        )

        self.play(
            Create(ray1),
            run_time=0.5,
            rate_func=rate_functions.rush_into
        )
        self.add(contact)
        self.play(
            Create(ray2),
            run_time=0.5,
            rate_func=rate_functions.rush_from
        )
        self.noticewait()

        self.play(x.animate.set_value(1 - 4.5))
        self.play(x.animate.set_value(-1.9 - 4.5))
        self.play(x.animate.set_value(1.5 - 4.5))
        self.play(x.animate.set_value(1 - 4.5))
        self.noticewait()

        fermat = Tex(
            "\\textbf{Fermat's Principle}: \
                    light travels along the path \
                    which takes the least time.",
            color=BLACK,
            font_size=38
        )
        fermat.move_to(3.5*UP)

        self.play(Write(fermat))
        self.noticewait()

        brace_x = BraceBetweenPoints(
            [-1.5 - 4.5,0,0],
            [x.get_value(),0,0],
            color=BLACK
        )
        label_x = MathTex("x", color=BLACK)
        brace_x.put_at_tip(label_x)

        self.play(
            FadeIn(brace_x, shift=UP),
            FadeIn(label_x, shift=UP)
        )

        brace_x.add_updater(
            lambda s : s.become(
                BraceBetweenPoints(
                    [-1.5 - 4.5,0,0],
                    [x.get_value(),0,0],
                    color=BLACK
                )
            ).put_at_tip(label_x)
        )

        self.noticewait()

        x_axis_label = MathTex("x", color=GRAY)
        y_axis_label = MathTex("t", color=GRAY)
        x_conf = { "color" : GRAY }
        y_conf = { "color" : GRAY }
        ax = Axes(
            x_range = [-0.25, 1.75, 0.25],
            y_range = [12.365, 13.865, 0.125],
            x_axis_config = x_conf,
            y_axis_config = y_conf,
            tips = False,
            x_length = 4,
            y_length = 6
        )
        ax.move_to(0.5*DOWN)
        x_axis_label.move_to(1.75 * RIGHT + 3.75 * DOWN)
        y_axis_label.move_to(1.75 * LEFT + 2.35 * UP)

        self.play(
            Create(ax),
            Write(x_axis_label),
            Write(y_axis_label)
        )
        self.noticewait()

        graph = ax.plot(
            lambda x : np.sqrt(9 + (x+0.25)**2) + 3 * np.sqrt(9 + (1.75-x)**2),
            x_range=[-0.25, 1.75],
            color=BLACK
        )

        self.play(x.animate.set_value(-2 - 4.5))
        self.play(
            x.animate.set_value(2 - 4.5),
            Create(graph),
            run_time=5,
            rate_func=rate_functions.linear
        )
        self.play(x.animate.set_value(1 - 4.5))
        self.noticewait()

        brace_ha = BraceBetweenPoints([-1.5 - 4.5,3,0], [-1.5 - 4.5,0,0], color=BLACK)
        brace_hw = BraceBetweenPoints([-1.5 - 4.5,0,0], [-1.5 - 4.5,-3,0], color=BLACK)
        brace_d = BraceBetweenPoints([-1.5 - 4.5,-3,0], [1.5 - 4.5,-3,0], color=BLACK)
        label_ha = MathTex("h_a", color=BLACK, font_size=36)
        label_hw = MathTex("h_w", color=BLACK, font_size=36)
        label_d = MathTex("d", color=BLACK, font_size=36)
        brace_ha.put_at_tip(label_ha)
        brace_hw.put_at_tip(label_hw)
        brace_d.put_at_tip(label_d)
        label_ha.shift(0.15 * RIGHT)
        label_hw.shift(0.15 * RIGHT)
        label_d.shift(0.15 * UP)

        self.play(
            FadeIn(brace_ha, shift=RIGHT),
            FadeIn(label_ha, shift=RIGHT),
            FadeIn(brace_hw, shift=RIGHT),
            FadeIn(label_hw, shift=RIGHT),
            FadeIn(brace_d, shift=UP),
            FadeIn(label_d, shift=UP)
        )
        self.noticewait()

        label_va = MathTex("v_a", color=BLACK, font_size=40)
        label_vw = MathTex("v_w", color=BLACK, font_size=40)
        label_va.move_to((2.25+4.5) * LEFT + 0.25 * UP)
        label_vw.move_to((2.25+4.5) * LEFT + 0.25 * DOWN)
        
        self.play(
            Write(label_va),
            Write(label_vw)
        )
        self.noticewait()

        formula_t = MathTex(
            r't='
            r'{'
            r'\sqrt{x^2 + h_a^2}'
            r'\over '
            r'v_a'
            r'}'
            r'+'
            r'{'
            r'\sqrt{(d-x)^2 + h_w^2}'
            r'\over '
            r'v_w'
            r'}',
            color=BLACK,
            font_size=40
        )
        formula_t.move_to(3 * RIGHT + 2.5 * UP)

        self.play(Write(formula_t))
        self.noticewait()

        formula_dt = MathTex(
            r'\frac{dt}{dx} ='
            r'{'
            r'x'
            r'\over '
            r'v_a'
            r'\sqrt{x^2 + h_a^2}'
            r'}'
            r'-'
            r'{'
            r'd-x'
            r'\over '
            r'v_w'
            r'\sqrt{(d-x)^2 + h_w^2}'
            r'}',
            color=BLACK,
            font_size=40
        )
        formula_dt.move_to(3.25 * RIGHT + 1 * UP)

        self.play(FadeIn(formula_dt, shift=DOWN))
        self.noticewait()

        formula_crit = MathTex(
            r'{'
            r'{{x\hskip0pt}}'
            r'\over '
            r'v_a'
            r'{{\sqrt{x^2+h_a^2}}}'
            r'}'
            r'='
            r'{'
            r'{{d\hskip0pt-x}}'
            r'\over '
            r'v_w'
            r'{{\sqrt{(d-x)^2+h_w^2}}}'
            r'}',
            color=BLACK,
            font_size=40
        )
        formula_crit.move_to(3.75 * RIGHT + 0.5 * DOWN)
        
        self.play(FadeIn(formula_crit, shift=DOWN))
        self.noticewait()

        line_x = Line(p.get_center(), [x.get_value()+0.01, 3, 0], color=PURE_RED)
        line_dx = Line(q.get_center(), [x.get_value()-0.01, -3, 0], color=PURE_BLUE)
        line_hypa = Line(p.get_center(), [x.get_value(), 0, 0], color=ORANGE)
        line_hypw = Line(q.get_center(), [x.get_value(), 0, 0], color=PURE_GREEN)

        self.play(
            formula_crit.animate.set_color_by_tex(r'x\hskip0pt', PURE_RED),
            Create(line_x)
        )
        self.noticewait()

        self.play(
            formula_crit.animate.set_color_by_tex(r'd\hskip0pt-x', PURE_BLUE),
            Create(line_dx)
        )
        self.noticewait()

        self.play(
            formula_crit.animate.set_color_by_tex(r'h_a', ORANGE),
            Create(line_hypa)
        )
        self.noticewait()

        self.play(
            formula_crit.animate.set_color_by_tex(r'h_w', PURE_GREEN),
            Create(line_hypw)
        )
        self.noticewait()

        normal = Line(
            [x.get_value(), 3.01, 0],
            [x.get_value(), -3.01, 0],
            color=DARK_GRAY,
            z_index=-0.5
        )
        self.play(Create(normal))
        self.noticewait()

        theta_a = Angle(
            ray1,
            normal,
            other_angle=True,
            quadrant=(-1,-1),
            color=LIGHT_GRAY,
            radius=1,
            z_index=-1
        )
        theta_w = Angle(
            normal,
            ray2,
            color=LIGHT_GRAY,
            radius=2,
            z_index=-1
        )
        label_theta_a = MathTex(r'\theta_a', color=BLACK, font_size=30)
        label_theta_w = MathTex(r'\theta_w', color=BLACK, font_size=30)
        label_theta_a.next_to(theta_a, UP).shift(0.2 * LEFT + 0.1 * DOWN)
        label_theta_w.next_to(theta_w, DOWN).shift(0.05 * RIGHT + 0.1 * DOWN)

        self.play(
            Create(theta_a),
            Create(theta_w),
            Write(label_theta_a),
            Write(label_theta_w)
        )
        self.noticewait()

        slaw_1 = MathTex(
            r"{ \sin \theta_a \over {{v_a}} } = ",
            r"{ {{\sin \theta_w}} \over v_w }",
            color=BLACK
        )
        slaw_1.move_to(4.5 * RIGHT + 2 * DOWN)
        self.play(FadeIn(slaw_1, scale=1.5))
        self.noticewait()

        slaw_2 = MathTex(
            r"{ \sin \theta_a \over {{\sin \theta_w}} } = ",
            r"{ {{v_a}} \over v_w }",
            color=BLACK
        )
        slaw_2.move_to(4.5 * RIGHT + 2 * DOWN)
        self.play(TransformMatchingTex(slaw_1, slaw_2))
        self.noticewait()

        brace_x.clear_updaters()

        new_normal = Line(
            [x.get_value(), 3, 0],
            [x.get_value(), -4, 0],
            stroke_width = 3,
            color = GRAY,
            z_index = -0.5
        )

        self.play(
            FadeOut(brace_x),
            FadeOut(brace_d),
            FadeOut(brace_ha),
            FadeOut(brace_hw),
            FadeOut(label_x),
            FadeOut(label_d),
            FadeOut(label_ha),
            FadeOut(label_hw),
            FadeOut(line_x),
            FadeOut(line_dx),
            FadeOut(line_hypa),
            FadeOut(line_hypw),
            Transform(normal, new_normal)
        )
        self.noticewait()

        snell = Tex(r"\textbf{Snell's Law}", color=BLACK)
        snell.move_to(4.5 * RIGHT + 3.25 * DOWN)

        snell_box = Rectangle(
            width = 3.125,
            height = 2.375,
            color = BLACK,
            stroke_width = 2
        ).move_to(4.5 * RIGHT + 2.5 * DOWN)

        self.play(Write(snell))
        self.play(Create(snell_box))
        self.noticewait()
        
        self.play(ApplyWave(fermat))
        self.noticewait()
        self.wait()
