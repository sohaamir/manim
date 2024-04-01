from manim import *

class AamirSohailAnimation(Scene):
    def construct(self):
        name = Tex(r"\textbf{Aamir Sohail}").scale(1.5)
        box = Rectangle(width=name.width + 0.5, height=name.height + 0.5, color=YELLOW).move_to(name.get_center())
        phd_text = Text("PhD student in Psychology", font_size=36).next_to(box, DOWN)
        university_text = Text("University of Birmingham", font_size=36).next_to(phd_text, DOWN)
        name_group = VGroup(box, name, phd_text, university_text).shift(DOWN)

        self.play(Create(box), Write(name))
        self.play(Write(phd_text))
        self.play(Write(university_text))

        image_files = ["axial.png", "sagittal.png", "coronal.png"]
        image_mobjects = [ImageMobject(image_file).set_height(2 * 1.8) for image_file in image_files]
        image_group = Group(*image_mobjects).arrange(RIGHT, buff=0.5).to_edge(UP)

        self.play(FadeIn(image_group))
        self.wait(2)

        self.play(
            FadeOut(name_group),
            FadeOut(image_group),
            run_time=2,
        )


    def loop_animation(self):
        while True:
            self.construct()

if __name__ == "__main__":
    scene = AamirSohailAnimation()
    scene.loop_animation()