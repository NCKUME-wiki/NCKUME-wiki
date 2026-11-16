# CAD-8：裝配配合（Mates）的自由度收斂 —— 三個基準面重合依序消除 6 個自由度
# 產生方式：manim -s -o CAD-8 CAD-8.py CAD8
#
# 以等角投影繪製長方塊：X 軸往右下、Y 軸往左下、Z 軸朝上。
# 基準面 1（z = 0）消除 Tz、Rx、Ry；基準面 2（y = 0）消除 Ty、Rz；基準面 3（x = 0）消除 Tx。
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
GHOST = "#CED4DA"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def M(s, size=26, color=INK):
    return Text(s, font="Cambria Math", font_size=size, color=color, slant=ITALIC)


def Sub(base, sub, size=24, color=INK):
    """以 Text 組出下標符號，例如 T_x。"""
    b = M(base, size, color)
    s = M(sub, size * 0.7, color)
    s.next_to(b, RIGHT, buff=0.02).align_to(b, DOWN).shift(DOWN * 0.05)
    return VGroup(b, s)


# ---------- 等角投影 ----------
SC = 0.84
C30 = np.cos(np.pi / 6)
A, B, C = 1.3, 1.0, 0.72  # 方塊尺寸（x, y, z）
ARW = 0.82  # 平移箭頭長度


def iso(o, x, y, z):
    return o + SC * np.array([(x - y) * C30, -(x + y) * 0.5 + z, 0.0])


def poly(o, pts, fill, opacity=1.0, stroke=INK, sw=2.5):
    return Polygon(*[iso(o, *p) for p in pts], fill_color=fill, fill_opacity=opacity,
                   stroke_color=stroke, stroke_width=sw)


AXES = {
    "x": (np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])),
    "y": (np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([1, 0, 0])),
    "z": (np.array([0, 0, 1]), np.array([1, 0, 0]), np.array([0, 1, 0])),
}
STARTS = {
    "x": np.array([A, B / 2, C / 2]),
    "y": np.array([A / 2, B, C / 2]),
    "z": np.array([A / 2, B / 2, C]),
}

STAGES = [
    dict(head="① 自由剛體", sub="尚未施加任何配合", planes=0, removed=set(), new=set()),
    dict(head="② 第 1 個基準面重合", sub="底面 ↔ 基準面 1：消除 Tz、Rx、Ry", planes=1,
         removed={"Tz", "Rx", "Ry"}, new={"Tz", "Rx", "Ry"}),
    dict(head="③ 第 2 個基準面重合", sub="背面 ↔ 基準面 2：消除 Ty、Rz", planes=2,
         removed={"Tz", "Rx", "Ry", "Ty", "Rz"}, new={"Ty", "Rz"}),
    dict(head="④ 第 3 個基準面重合", sub="側面 ↔ 基準面 3：消除 Tx", planes=3,
         removed={"Tz", "Rx", "Ry", "Ty", "Rz", "Tx"}, new={"Tx"}),
]


def cross_mark(p, size=0.11):
    return VGroup(
        Line(p + np.array([-size, -size, 0]), p + np.array([size, size, 0]), color=RED_, stroke_width=4),
        Line(p + np.array([-size, size, 0]), p + np.array([size, -size, 0]), color=RED_, stroke_width=4),
    )


def rot_arc(o, axis, color):
    u, e1, e2 = AXES[axis]
    center = STARTS[axis] + u * ARW * 0.5
    r = 0.24
    ts = np.linspace(0.25 * np.pi, 1.85 * np.pi, 60)
    pts = [iso(o, *(center + r * (np.cos(t) * e1 + np.sin(t) * e2))) for t in ts]
    arc = VMobject(stroke_color=color, stroke_width=3.5)
    arc.set_points_smoothly(pts)
    d = pts[-1] - pts[-3]
    d = d / np.linalg.norm(d)
    n = np.array([-d[1], d[0], 0])
    p = pts[-1]
    tip = Polygon(p + d * 0.13, p - n * 0.07, p + n * 0.07, fill_color=color, fill_opacity=1,
                  stroke_width=0)
    mid = pts[len(pts) // 2]
    return VGroup(arc, tip), mid, iso(o, *center)


class CAD8(Scene):
    def construct(self):
        title = T("裝配配合的自由度收斂：以基準面重合（Coincident）逐步消除剛體 6 個自由度", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        col_w = 3.5
        xs = [(i - 1.5) * col_w for i in range(4)]
        draw_y = 0.55

        for k, (cx, st) in enumerate(zip(xs, STAGES)):
            # ---------- 標題 ----------
            head = T(st["head"], 20, INK, BOLD)
            sub = T(st["sub"], 15, MUTED)
            header = VGroup(head, sub).arrange(DOWN, buff=0.12).move_to([cx, 2.85, 0])
            self.add(header)

            o = np.array([cx - (A - B) / 2 * C30 * SC - 0.05, draw_y - 0.15, 0])

            # ---------- 基準面 ----------
            planes = VGroup()
            plane_labels = VGroup()
            pe = 0.28  # 基準面外擴量
            defs = [
                ([(-pe, -pe, 0), (A + 0.45, -pe, 0), (A + 0.45, B + 0.45, 0), (-pe, B + 0.45, 0)],
                 "基準面 1", (A + 0.45, B + 0.45, 0), DOWN, ORIGIN),
                ([(-pe, 0, 0), (A + 0.35, 0, 0), (A + 0.35, 0, C + 0.35), (-pe, 0, C + 0.35)],
                 "基準面 2", (A * 0.65, 0, C + 0.35), UR, ORIGIN),
                ([(0, -pe, 0), (0, B + 0.35, 0), (0, B + 0.35, C + 0.35), (0, -pe, C + 0.35)],
                 "基準面 3", (0, B * 0.65, C + 0.35), UL, ORIGIN),
            ]
            for i in range(st["planes"]):
                pts, lbl, anchor, dirn, sh = defs[i]
                is_new = i == st["planes"] - 1
                col = ORANGE_ if is_new else MUTED
                planes.add(poly(o, pts, col, 0.16 if is_new else 0.08, stroke=col, sw=2 if is_new else 1.5))
                plane_labels.add(T(lbl, 13, col, BOLD if is_new else NORMAL)
                                 .next_to(iso(o, *anchor), dirn, buff=0.05).shift(sh))
            # 先畫平面 1 再畫牆面（牆面在方塊後方）
            self.add(*planes)

            # ---------- 方塊 ----------
            top = poly(o, [(0, 0, C), (A, 0, C), (A, B, C), (0, B, C)], "#F8F9FA")
            right = poly(o, [(A, 0, 0), (A, B, 0), (A, B, C), (A, 0, C)], "#DEE2E6")
            front = poly(o, [(0, B, 0), (A, B, 0), (A, B, C), (0, B, C)], "#E9ECEF")
            block = VGroup(top, right, front)
            self.add(block)

            # 接觸邊加粗（顯示重合面位置）
            contact = VGroup()
            if st["planes"] >= 1:
                c1 = ORANGE_ if st["planes"] == 1 else MUTED
                contact.add(Line(iso(o, 0, B, 0), iso(o, A, B, 0), color=c1, stroke_width=5),
                            Line(iso(o, A, B, 0), iso(o, A, 0, 0), color=c1, stroke_width=5))
            if st["planes"] >= 2:
                c2 = ORANGE_ if st["planes"] == 2 else MUTED
                contact.add(Line(iso(o, 0, 0, C), iso(o, A, 0, C), color=c2, stroke_width=5),
                            Line(iso(o, A, 0, C), iso(o, A, 0, 0), color=c2, stroke_width=5))
            if st["planes"] >= 3:
                contact.add(Line(iso(o, 0, 0, C), iso(o, 0, B, C), color=ORANGE_, stroke_width=5),
                            Line(iso(o, 0, B, C), iso(o, 0, B, 0), color=ORANGE_, stroke_width=5))
            self.add(contact, plane_labels)

            # ---------- 自由度箭頭 ----------
            dof = VGroup()
            marks = VGroup()
            for ax_name in ("x", "y", "z"):
                u = AXES[ax_name][0]
                s3 = STARTS[ax_name]
                p0, p1 = iso(o, *s3), iso(o, *(s3 + u * ARW))
                tname, rname = "T" + ax_name, "R" + ax_name
                t_off = tname in st["removed"]
                r_off = rname in st["removed"]
                tc = GHOST if t_off else BLUE_
                rc = GHOST if r_off else BLUE_
                arr = Arrow(p0, p1, buff=0, color=tc, stroke_width=5,
                            max_tip_length_to_length_ratio=0.25, max_stroke_width_to_length_ratio=10)
                arc, arc_mid, arc_c = rot_arc(o, ax_name, rc)
                sd = (p1 - p0) / np.linalg.norm(p1 - p0)
                tl = Sub("T", ax_name, 22, tc).move_to(p1 + sd * 0.25)
                # 旋轉標籤放在弧線外側
                rd = arc_mid - arc_c
                rd = rd / np.linalg.norm(rd)
                rl = Sub("R", ax_name, 22, rc).move_to(arc_mid + rd * 0.24)
                dof.add(arc, arr, tl, rl)
                if t_off:
                    marks.add(cross_mark(p0 + (p1 - p0) * 0.3, 0.09).set_color(RED_ if tname in st["new"] else MUTED))
                if r_off:
                    marks.add(cross_mark(arc_mid, 0.09).set_color(RED_ if rname in st["new"] else MUTED))
            self.add(dof, marks)

            # ---------- 自由度清單 ----------
            chips = VGroup()
            for nm in ("Tx", "Ty", "Tz", "Rx", "Ry", "Rz"):
                off = nm in st["removed"]
                col = GHOST if off else BLUE_
                lab = Sub(nm[0], nm[1], 17, MUTED if off else BLUE_)
                box = RoundedRectangle(corner_radius=0.07, width=0.42, height=0.35,
                                       stroke_color=col, stroke_width=2,
                                       fill_color=WHITE if off else "#E7F5FF", fill_opacity=1)
                lab.move_to(box)
                chip = VGroup(box, lab)
                if off:
                    chip.add(Line(box.get_corner(DL), box.get_corner(UR),
                                  color=RED_ if nm in st["new"] else MUTED, stroke_width=2.2))
                chips.add(chip)
            chips.arrange(RIGHT, buff=0.055).move_to([cx, -1.85, 0])
            self.add(chips)

            # ---------- 計數 ----------
            n = 6 - len(st["removed"])
            num_col = GREEN_ if n == 0 else BLUE_
            counter = VGroup(T("剩餘自由度", 18, INK), T(str(n), 40, num_col, BOLD)).arrange(
                RIGHT, buff=0.2, aligned_edge=DOWN)
            if n == 0:
                counter.add(T("完全定義", 18, GREEN_, BOLD))
                counter.arrange(RIGHT, buff=0.2, aligned_edge=DOWN)
            counter.move_to([cx, -2.6, 0])
            self.add(counter)

            if k < 3:
                self.add(Arrow([cx + col_w / 2 - 0.16, -1.85, 0], [cx + col_w / 2 + 0.16, -1.85, 0],
                               buff=0, color=MUTED, stroke_width=3.5, max_tip_length_to_length_ratio=0.45))

        for x in (-col_w, 0, col_w):
            self.add(Line([x, 3.15, 0], [x, -1.5, 0], color="#DEE2E6", stroke_width=1.5))

        foot = VGroup(
            VGroup(Line(ORIGIN, RIGHT * 0.45, color=BLUE_, stroke_width=5), T("剩餘自由度", 16, MUTED)).arrange(RIGHT, buff=0.12),
            VGroup(Line(ORIGIN, RIGHT * 0.45, color=GHOST, stroke_width=5), T("已消除", 16, MUTED)).arrange(RIGHT, buff=0.12),
            VGroup(Rectangle(width=0.45, height=0.25, fill_color=ORANGE_, fill_opacity=0.2, stroke_color=ORANGE_, stroke_width=2),
                   T("本步驟新增的重合基準面", 16, MUTED)).arrange(RIGHT, buff=0.12),
        ).arrange(RIGHT, buff=0.6)
        note = T("平面重合為線性約束、單次消除多個自由度；相切/曲面配合需數值迭代，成本較高", 17, INK)
        VGroup(foot, note).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.22)
        self.add(foot, note)
