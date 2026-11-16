# CAD-3：單變數驅動架構 —— 以 Nominal_OD 連動法蘭全部尺寸（含 ±20% 彈性測試）
# 產生方式：manim -s -o CAD-3 CAD-3.py CAD3
from manim import *
import math

config.background_color = WHITE
config.pixel_width = 1920
config.pixel_height = 1080

FONT = "Noto Sans TC"
MONO = "Consolas"
INK = "#212529"
MUTED = "#868E96"
BLUE_ = "#1C7ED6"
ORANGE_ = "#E8590C"
RED_ = "#E03131"
GREEN_ = "#2F9E44"
FILL = "#E7F0FA"

HOLE_D = 9.0       # 螺栓孔徑（固定，M8 通孔）
RIM = 12.0         # 孔中心到法蘭外緣的邊距
SCALE = 0.0275      # 圖面單位 / mm（三個狀態共用同一比例）


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def C(s, size=20, color=INK, weight=NORMAL):
    return Text(s, font=MONO, font_size=size, color=color, weight=weight)


def params(od):
    wall = od * 0.08
    pcd = od + 25
    holes = math.floor(pcd / 30 + 0.5)  # round()：四捨五入
    return wall, pcd, holes


def flange(od, center):
    wall, pcd, n = params(od)
    s = SCALE
    g = VGroup()
    outer = Circle(radius=(pcd / 2 + RIM) * s, stroke_color=INK, stroke_width=3,
                   fill_color=FILL, fill_opacity=1)
    boss = Circle(radius=od / 2 * s, stroke_color=BLUE_, stroke_width=4)
    bore = Circle(radius=(od / 2 - wall) * s, stroke_color=INK, stroke_width=3,
                  fill_color=WHITE, fill_opacity=1)
    pcd_c = DashedVMobject(Circle(radius=pcd / 2 * s, stroke_color=ORANGE_, stroke_width=2.5),
                           num_dashes=48)
    g.add(outer, boss, bore, pcd_c)
    for k in range(n):
        a = PI / 2 + k * TAU / n
        p = pcd / 2 * s * np.array([math.cos(a), math.sin(a), 0])
        g.add(Circle(radius=HOLE_D / 2 * s, stroke_color=INK, stroke_width=2.5,
                     fill_color=WHITE, fill_opacity=1).move_to(p))
    r = (pcd / 2 + RIM) * s + 0.12
    g.add(DashedLine(LEFT * r, RIGHT * r, color=MUTED, stroke_width=1.2, dash_length=0.08))
    g.add(DashedLine(DOWN * r, UP * r, color=MUTED, stroke_width=1.2, dash_length=0.08))
    g.move_to(center)
    return g


def box(name, formula, driver=False, width=3.3, cjk=False):
    head = C(name, 22, WHITE if driver else INK, BOLD)
    sub = (T if cjk else C)(formula, 17, WHITE if driver else MUTED)
    txt = VGroup(head, sub).arrange(DOWN, buff=0.1)
    rect = RoundedRectangle(corner_radius=0.12, width=width, height=txt.height + 0.3,
                            stroke_color=BLUE_ if driver else INK, stroke_width=2.5,
                            fill_color=BLUE_ if driver else WHITE, fill_opacity=1)
    return VGroup(rect, txt.move_to(rect))


class CAD3(Scene):
    def construct(self):
        title = T("單變數驅動架構（Single-Driver）：修改 Nominal_OD，其餘尺寸依方程式級聯重建", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        # ---------- 相依關係圖 ----------
        b_od = box("Nominal_OD", "主驅動變數（唯一輸入）", driver=True, width=2.9, cjk=True).move_to([-4.6, 2.05, 0])
        b_wall = box("Wall_Thick", '= "Nominal_OD" * 0.08').move_to([-0.6, 2.6, 0])
        b_pcd = box("PCD", '= "Nominal_OD" + 25 mm').move_to([-0.6, 1.5, 0])
        b_n = box("Hole_Count", '= round("PCD" / 30)').move_to([3.9, 1.5, 0])

        def arrow(a, b):
            return Arrow(a, b, buff=0.08, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.12)

        arrows = VGroup(
            arrow(b_od.get_right(), b_wall.get_left()),
            arrow(b_od.get_right(), b_pcd.get_left()),
            arrow(b_pcd.get_right(), b_n.get_left()),
        )
        self.add(arrows, b_od, b_wall, b_pcd, b_n)

        # ---------- 三種狀態的法蘭 ----------
        states = [(40, "−20%"), (50, "基準值"), (60, "+20%")]
        xs = [-4.6, 0.0, 4.6]
        cy = -0.68
        base_n = params(50)[2]
        for (od, tag), x in zip(states, xs):
            wall, pcd, n = params(od)
            self.add(flange(od, [x, cy, 0]))

            head = VGroup(C(f"Nominal_OD = {od}", 21, BLUE_, BOLD), T(f"mm（{tag}）", 19, INK)).arrange(
                RIGHT, buff=0.08)
            head.move_to([x, -2.55, 0])
            n_color = ORANGE_ if n != base_n else INK
            row1 = VGroup(
                C(f"Wall_Thick {wall:.1f}", 17, INK), C("·", 17, MUTED), C(f"PCD {pcd:.0f}", 17, INK),
            ).arrange(RIGHT, buff=0.12)
            row2 = C(f"Hole_Count {n}", 17, n_color, BOLD if n != base_n else NORMAL)
            detail = VGroup(row1, row2).arrange(DOWN, buff=0.1).next_to(head, DOWN, buff=0.12)
            self.add(head, detail)
            if n != base_n:
                warn = T("孔數跳變 → 須確認陣列與下游特徵仍能重建", 16, ORANGE_)
                warn.next_to(detail, DOWN, buff=0.1)
                self.add(warn)

        # 圖例
        legend = VGroup(
            VGroup(Circle(radius=0.12, stroke_color=BLUE_, stroke_width=4), T("Nominal_OD（管座外徑）", 16, MUTED)),
            VGroup(DashedVMobject(Circle(radius=0.12, stroke_color=ORANGE_, stroke_width=2.5), num_dashes=8),
                   T("PCD 螺栓分度圓", 16, MUTED)),
            VGroup(Circle(radius=0.12, stroke_color=INK, stroke_width=2.5, fill_color=WHITE, fill_opacity=1),
                   T("螺栓孔 Ø9（固定）", 16, MUTED)),
        )
        for g in legend:
            g.arrange(RIGHT, buff=0.12)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        legend.move_to([2.55, 3.0, 0], aligned_edge=UL)
        self.add(legend)
