from manim import *

class Images(Scene):

    notifier = Dot(color=LIGHTER_GRAY, radius=0.05)
    notifier.move_to(7 * RIGHT + 3.9 * DOWN)

    def noticewait(self):
        self.add(self.notifier)
        self.wait()
        self.remove(self.notifier)

    def construct(self):
        self.camera.background_color = WHITE

        self.wait()
        
        img1 = ImageMobject("media_to_save/1_ruler.jpg")
        img1.height = 8

        self.play(FadeIn(img1))
        self.noticewait()

        img2 = ImageMobject("media_to_save/2_bear.jpg")
        img2.height = 8

        self.play(
            FadeOut(img1),
            FadeIn(img2)
        )
        self.noticewait()
        
        img3 = ImageMobject("media_to_save/3_fishing.jpg")
        img3.height = 8

        self.play(
            FadeOut(img2), 
            FadeIn(img3)
        )
        self.noticewait()

        self.wait()
