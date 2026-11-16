# CAD-5：斑馬線反射分析（Zebra Stripes）—— G0~G3 接縫的條紋表現
# 產生方式：manim -s -o CAD-5 CAD-5.py CAD5
#
# 模型：曲面 z = f(x) + y²/2，接縫位於 x = 0（左側 f = 0）。
# 以「環境貼圖」近似，反射條紋相位 p = y + A·f'(x)，因此條紋等值線為 y = c − A·f'(x)：
#   G0：f' 跳躍 → 條紋錯位斷裂；G1：f'' 跳躍 → 條紋折角；
#   G2：f''' 跳躍 → 條紋平滑但彎曲率突變；G3：更高階連續 → 條紋流動平順。
from manim import *
import numpy as np

config.background_color = WHITE
config.pixel_width = 1920
config.pixel_height = 1080

FONT = "Noto Sans TC"
INK = "#212529"
MUTED = "#868E96"
BLUE_ = "#1C7ED6"
ORANGE_ = "#E8590C"
RED_ = "#E03131"
GREEN_ = "#2F9E44"

PERIOD = 0.25  # 條紋週期


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


CASES = [
    dict(name="G0", title="位置連續", fp=lambda x: np.where(x > 0, PERIOD / 2, 0.0),
         note="條紋在交界處完全斷裂、錯位", good=False),
    dict(name="G1", title="正切連續", fp=lambda x: np.where(x > 0, 0.45 * x, 0.0),
         note="條紋相接，但產生銳角折轉", good=False),
    dict(name="G2", title="曲率連續", fp=lambda x: np.where(x > 0, 0.6 * x**2, 0.0),
         note="條紋平滑連續、無折角", good=True),
    dict(name="G3", title="曲率變化率連續", fp=lambda x: np.where(x > 0, 0.7 * x**3, 0.0),
         note="條紋切線方向亦連續流動", good=True),
]


def zebra_image(fp, px=420, ss=3):
    n = px * ss
    x = np.linspace(-1, 1, n)
    y = np.linspace(1, -1, n)
    X, Y = np.meshgrid(x, y)
    phase = (Y + fp(X)) / PERIOD
    v = 0.5 + 0.5 * np.tanh(6.0 * np.sin(2 * np.pi * phase))
    # 輕微明暗（模擬曲面受光），增加立體感
    shade = 0.92 + 0.08 * (1 - 0.5 * (X**2 + Y**2))
    dark = np.array([33, 37, 41], dtype=float)
    light = np.array([248, 249, 250], dtype=float)
    img = (dark[None, None, :] * (1 - v[..., None]) + light[None, None, :] * v[..., None]) * shade[..., None]
    img = img.reshape(px, ss, px, ss, 3).mean(axis=(1, 3))
    return np.clip(img, 0, 255).astype(np.uint8)


class CAD5(Scene):
    def construct(self):
        title = T("斑馬線反射分析（Zebra Stripes）：由條紋形態判讀接縫連續性", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        side = 3.0
        gap = 0.45
        xs = [(i - 1.5) * (side + gap) for i in range(4)]
        cy = 0.05

        for cx, c in zip(xs, CASES):
            img = ImageMobject(zebra_image(c["fp"]))
            img.height = side
            img.move_to([cx, cy, 0])
            border = Square(side, stroke_color=INK, stroke_width=2).move_to(img)

            seam = DashedLine([cx, cy - side / 2 - 0.12, 0], [cx, cy + side / 2 + 0.12, 0],
                              color=RED_, stroke_width=3, dash_length=0.1)

            # 以橘線描出其中一條條紋邊界，凸顯其形狀
            c0 = 0.25 * PERIOD
            xx = np.linspace(-1, 0.999, 300)
            yy = c0 - c["fp"](xx)
            pts = [np.array([cx + u * side / 2, cy + v * side / 2, 0]) for u, v in zip(xx, yy)]
            trace = VGroup()
            if c["name"] == "G0":
                left = [p for p, u in zip(pts, xx) if u <= 0]
                right = [p for p, u in zip(pts, xx) if u > 0]
                for seg in (left, right):
                    m = VMobject(stroke_color=ORANGE_, stroke_width=5)
                    m.set_points_as_corners(seg)
                    trace.add(m)

            else:
                m = VMobject(stroke_color=ORANGE_, stroke_width=5)
                m.set_points_as_corners(pts)
                trace.add(m)

            lab_a = T("曲面 A", 16, MUTED).next_to(border, UP, buff=0.15).shift(LEFT * side / 4)
            lab_b = T("曲面 B", 16, MUTED).next_to(border, UP, buff=0.15).shift(RIGHT * side / 4)

            head = VGroup(T(c["name"], 30, BLUE_, BOLD), T(c["title"], 20, INK, BOLD)).arrange(
                RIGHT, buff=0.15, aligned_edge=DOWN).next_to(border, DOWN, buff=0.3)
            mark = Text("✔" if c["good"] else "✘", font="Segoe UI Symbol", font_size=22,
                        color=GREEN_ if c["good"] else RED_)
            note = VGroup(mark, T(c["note"], 17, INK)).arrange(RIGHT, buff=0.1).next_to(head, DOWN, buff=0.18)

            self.add(img, border, trace, seam, lab_a, lab_b, head, note)

        foot = VGroup(
            VGroup(DashedLine(ORIGIN, RIGHT * 0.45, color=RED_, stroke_width=3, dash_length=0.1),
                   T("曲面接縫", 16, MUTED)).arrange(RIGHT, buff=0.12),
            VGroup(Line(ORIGIN, RIGHT * 0.45, color=ORANGE_, stroke_width=4),
                   T("描出單一條紋邊界以觀察其走向", 16, MUTED)).arrange(RIGHT, buff=0.12),
            T("外觀件（Class-A）一般要求至少 G2", 16, MUTED),
        ).arrange(RIGHT, buff=0.7).to_edge(DOWN, buff=0.25)
        self.add(foot)
