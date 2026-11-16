# CAD-7：骨架模型（Skeleton Model）單向樹狀數據流 vs. 循環參照（Cyclic Reference）
# 產生方式：manim -s -o CAD-7 CAD-7.py CAD7
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
CARD = "#DEE2E6"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def SYM(s, size=24, color=INK):
    return Text(s, font="Segoe UI Symbol", font_size=size, color=color)


def box(label, w, h, color, sub=None, size=18):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.1, stroke_color=color, stroke_width=2.5,
                         fill_color=color, fill_opacity=0.08)
    t = T(label, size, INK, BOLD)
    if sub:
        t = VGroup(t, T(sub, 13, MUTED)).arrange(DOWN, buff=0.06)
    t.move_to(r)
    return VGroup(r, t)


def skeleton_icons():
    """骨架內容小圖示：基準平面、運動線、包絡框、硬點。"""
    s = 0.55
    plane = Polygon([-s * 0.55, -s * 0.3, 0], [s * 0.25, -s * 0.3, 0], [s * 0.55, s * 0.3, 0], [-s * 0.25, s * 0.3, 0],
                    stroke_color=BLUE_, stroke_width=2, fill_color=BLUE_, fill_opacity=0.15)
    motion = VGroup(
        Line([-s * 0.5, -s * 0.3, 0], [0, s * 0.25, 0], color=ORANGE_, stroke_width=3),
        Line([0, s * 0.25, 0], [s * 0.5, -s * 0.1, 0], color=ORANGE_, stroke_width=3),
        Dot([-s * 0.5, -s * 0.3, 0], 0.045, color=ORANGE_), Dot([0, s * 0.25, 0], 0.045, color=ORANGE_),
        Dot([s * 0.5, -s * 0.1, 0], 0.045, color=ORANGE_),
    )
    bbox = DashedVMobject(Rectangle(width=s * 1.1, height=s * 0.7), num_dashes=16).set_stroke(MUTED, 2)
    hard = VGroup(*[VGroup(Line([px - 0.07, py, 0], [px + 0.07, py, 0], color=RED_, stroke_width=2.5),
                           Line([px, py - 0.07, 0], [px, py + 0.07, 0], color=RED_, stroke_width=2.5))
                    for px, py in ((-0.17, -0.1), (0.15, 0.12), (0.05, -0.15))])
    names = ["基準平面", "運動線", "包絡框", "硬點"]
    items = VGroup()
    for icon, n in zip((plane, motion, bbox, hard), names):
        holder = Rectangle(width=0.8, height=0.45, stroke_width=0)
        icon.move_to(holder)
        items.add(VGroup(VGroup(holder, icon), T(n, 14, INK)).arrange(DOWN, buff=0.08))
    return items.arrange(RIGHT, buff=0.3)


def arrow(a, b, color, sw=4):
    return Arrow(a, b, buff=0, color=color, stroke_width=sw, max_tip_length_to_length_ratio=0.22,
                 tip_length=0.18)


class CAD7(Scene):
    def construct(self):
        title = T("骨架模型（Skeleton Model）：嚴格單向的由上而下數據流，嚴禁循環參照", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        LX, RX = -3.55, 3.55
        pw, y_top, y_bot = 6.7, 3.1, -3.55
        for cx, col in ((LX, GREEN_), (RX, RED_)):
            self.add(RoundedRectangle(width=pw, height=y_top - y_bot, corner_radius=0.15, stroke_color=CARD,
                                      stroke_width=2).move_to([cx, (y_top + y_bot) / 2, 0]))

        # ================= 左：單向樹狀數據流 =================
        head_l = VGroup(SYM("✔", 24, GREEN_), T("單向樹狀數據流", 22, GREEN_, BOLD)).arrange(RIGHT, buff=0.12)
        head_l.move_to([LX, 2.7, 0])
        self.add(head_l)

        icons = skeleton_icons()
        sk_title = VGroup(T("骨架模型", 19, INK, BOLD), T("Skeleton（不含實體特徵）", 14, MUTED)).arrange(RIGHT, buff=0.15,
                                                                                                aligned_edge=DOWN)
        sk_content = VGroup(sk_title, icons).arrange(DOWN, buff=0.15)
        sk_rect = RoundedRectangle(width=sk_content.width + 0.5, height=sk_content.height + 0.3, corner_radius=0.12,
                                   stroke_color=BLUE_, stroke_width=3, fill_color=BLUE_, fill_opacity=0.06)
        sk = VGroup(sk_rect, sk_content.move_to(sk_rect)).move_to([LX, 1.45, 0])
        self.add(sk)

        y_sub, y_part = -0.55, -2.05
        sub_xs = [LX - 1.45, LX + 1.45]
        subs = [box("次組裝 A", 2.0, 0.62, GREEN_).move_to([sub_xs[0], y_sub, 0]),
                box("次組裝 B", 2.0, 0.62, GREEN_).move_to([sub_xs[1], y_sub, 0])]
        part_xs = [LX - 2.2, LX - 0.7, LX + 0.7, LX + 2.2]
        names = ["零件 A1", "零件 A2", "零件 B1", "零件 B2"]
        parts = [box(n, 1.2, 0.55, GREEN_, size=16).move_to([px, y_part, 0]) for n, px in zip(names, part_xs)]
        self.add(*subs, *parts)

        y_from = sk_rect.get_bottom()[1]
        for sx, s in zip(sub_xs, subs):
            self.add(arrow([LX + (sx - LX) * 0.35, y_from, 0], s.get_top(), GREEN_))
        pub = VGroup(T("發布幾何", 15, GREEN_, BOLD), T("Publish Geometry", 13, MUTED)).arrange(DOWN, buff=0.04)
        pub.move_to([LX, (y_from + subs[0].get_top()[1]) / 2, 0])
        self.add(pub)
        for k, p in enumerate(parts):
            s = subs[k // 2]
            self.add(arrow(s.get_bottom() + RIGHT * (p.get_x() - s.get_x()) * 0.35, p.get_top(), GREEN_, 3.5))

        cap_l = T("骨架 → 次組裝 → 零件：只向下參照，不跨層、不回頭", 15, MUTED).move_to([LX, -3.05, 0])
        self.add(cap_l)

        # ================= 右：循環參照 =================
        head_r = VGroup(SYM("✘", 24, RED_), T("循環參照（Cyclic Reference）", 22, RED_, BOLD)).arrange(RIGHT, buff=0.12)
        head_r.move_to([RX, 2.7, 0])
        self.add(head_r)

        y_ab = 0.95
        pa = box("零件 A", 1.7, 0.9, RED_, size=20).move_to([RX - 1.75, y_ab, 0])
        pb = box("零件 B", 1.7, 0.9, RED_, size=20).move_to([RX + 1.75, y_ab, 0])
        top_arc = CurvedArrow(pa.get_top() + RIGHT * 0.3, pb.get_top() + LEFT * 0.3, angle=-TAU / 6,
                              color=RED_, stroke_width=4, tip_length=0.2)
        bot_arc = CurvedArrow(pb.get_bottom() + LEFT * 0.3, pa.get_bottom() + RIGHT * 0.3, angle=-TAU / 6,
                              color=RED_, stroke_width=4, tip_length=0.2)
        lab_t = T("A 參照 B 的特徵", 15, INK).next_to(top_arc, UP, buff=0.08)
        lab_b = T("B 又反向參照 A 的特徵", 15, INK).next_to(bot_arc, DOWN, buff=0.08)
        loop = SYM("⟳", 40, RED_).move_to([RX, y_ab, 0])
        self.add(pa, pb, top_arc, bot_arc, lab_t, lab_b, loop)

        chain = T("A 更新 → B 重算 → A 再更新 → B 再重算 → …", 15, MUTED).move_to([RX, -1.0, 0])
        warn_t = VGroup(SYM("⚠", 24, RED_), T("求解無窮迭代、模型損毀", 20, RED_, BOLD)).arrange(RIGHT, buff=0.12)
        warn_r = RoundedRectangle(width=warn_t.width + 0.6, height=warn_t.height + 0.35, corner_radius=0.1,
                                  stroke_color=RED_, stroke_width=2.5, fill_color=RED_, fill_opacity=0.08)
        warn = VGroup(warn_r, warn_t.move_to(warn_r)).move_to([RX, -2.0, 0])
        self.add(chain, warn)

        cap_r = T("修正：A、B 皆改為參照骨架的發布幾何，切斷彼此間的參照", 15, MUTED).move_to([RX, -3.05, 0])
        self.add(cap_r)
