from manim import *
import numpy as np
import sympy 


def f(x):
     return x**3

class Integral(Scene):
   def construct(self):
      ax = Axes (
          x_range=[-0.1, 2.1], y_range=[-0.1, 8.4], tips= True,
          axis_config = {
              "include_numbers": True,
              "color": WHITE
          },
      )
      labels = ax.get_axis_labels(x_label="x", y_label="y=x^3")
      # self.play(Create(ax), Create(labels))
      self.add(ax, labels)

      graph = ax.plot(lambda x: x**3, x_range=[0, 2])
      self.play(Create(graph))


      riemann_areas = [ax.get_riemann_rectangles(graph, x_range=[0, 2], input_sample_type="center", color=(TEAL_C, YELLOW_B), dx=2/i, fill_opacity=0.8) for i in range(2, 100, 1)] 
      tex = [Tex(f"$n={i}$").to_corner(RIGHT+UP) for i in range(2, 100, 1)]
      tex_last = Tex(r"$n \to \infty$")

      x = sympy.Symbol("x")
      real_area = sympy.integrate(f(x), (x, 0,2))
      

      current_area = [Tex(r'$\sigma = $'+ "{0:.6f}".format((sum([f((2*i/n+2*(i-1)/n)/2) * 2/n for i in range(n+1)])))).to_edge(UP) for n in range(2, 100, 1)]
      current_R_n = [Tex(r'$Current R_n = $'+ "{0:.6f}".format((real_area - sum([f((2*i/n+2*(i-1)/n)/2) * 2/n for i in range(n+1)])))).next_to(current_area[n-2], DOWN) for n in range(2, 100, 1)]
      theory_R_n = [Tex(r'$Theory R_n = $'+ "{0:.6f}".format(4/n**2)).next_to(current_R_n[n-2], DOWN) for n in range(2, 100, 1)]


      self.play(Create(riemann_areas[0]))
      self.add(tex[0])
      self.add(current_area[0])
      self.add(current_R_n[0])
      self.add(theory_R_n[0])

      self.wait(0.8)
      
      for i in range(3, len(riemann_areas), 5):
        self.play(Transform(riemann_areas[0], riemann_areas[i]), Transform(tex[0], tex[i]), Transform(current_area[0], current_area[i]), Transform(current_R_n[0], current_R_n[i]), Transform(theory_R_n[0], theory_R_n[i]), run_time=0.2)
        self.wait(0.8)

      area = ax.get_area(graph, x_range=[0, 2], opacity=1, color=(TEAL_C, YELLOW_B))
      self.remove(current_R_n[0], theory_R_n[0])
      self.play(Transform(riemann_areas[0], area), Transform(tex[0], tex_last), Transform(current_area[0], Tex(r'$\int\limits_0^2 x^3\, dx = $'+str(real_area)).to_edge(UP)))
      self.wait(2)

