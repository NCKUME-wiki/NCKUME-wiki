# CAD-6：主模型技術（Master Model Technique）—— 多本體分割、衍生零件與工程圖連動
# 產生方式：manim -s -o CAD-6 CAD-6.py CAD6
#
# 示意幾何：手持裝置外殼側視剖面（圓角薄殼 + 分模面 + 公母止口 + 螺絲柱）。
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

TOP_C = BLUE_   # 上蓋
BOT_C = GREEN_  # 下蓋


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


# ---------------- 外殼剖面幾何 ----------------
W, H, R, TH = 2.3, 1.1, 0.32, 0.16   # 外寬、外高、外圓角、壁厚
LW, LH = 0.08, 0.11                  # 止口寬、高
BW = 0.3                             # 螺絲柱外徑
BOSS_X = 0.45                        # 螺絲柱位置


def rect(x0, x1, y0, y1):
    return Rectangle(width=x1 - x0, height=y1 - y0).move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0])


def housing():
    """回傳 (上蓋, 下蓋) 兩個剖面 VMobject，分模面位於 y = 0。"""
    outer = RoundedRectangle(width=W, height=H, corner_radius=R)
    inner = RoundedRectangle(width=W - 2 * TH, height=H - 2 * TH, corner_radius=R - TH)
    shell = Difference(outer, inner)
    upper = rect(-W, W, 0, H)
    lower = rect(-W, W, -H, 0)
    # 公止口：位於下蓋壁厚內側一半，向上凸出
    lips = [rect(-W / 2 + TH - LW, -W / 2 + TH, -0.01, LH),
            rect(W / 2 - TH, W / 2 - TH + LW, -0.01, LH)]
    boss_b = rect(BOSS_X - BW / 2, BOSS_X + BW / 2, -H / 2 + TH / 2, 0)
    boss_t = rect(BOSS_X - BW / 2, BOSS_X + BW / 2, 0, H / 2 - TH / 2)
    hole_b = rect(BOSS_X - 0.055, BOSS_X + 0.055, -H, 0.02)
    hole_t = rect(BOSS_X - 0.04, BOSS_X + 0.04, -0.02, 0.28)

    bottom = Union(Intersection(shell, lower), *lips, boss_b)
    bottom = Difference(bottom, hole_b)
    top = Union(Intersection(shell, upper), boss_t)
    top = Difference(top, Union(*[l.copy() for l in lips]))   # 母止口（溝槽）
    top = Difference(top, hole_t)
    for m, c in ((top, TOP_C), (bottom, BOT_C)):
        m.set_fill(c, opacity=0.3).set_stroke(c, width=2.5)
    return top, bottom


def file_icon(color, h=0.34):
    w = h * 0.78
    f = h * 0.3
    body = Polygon([0, 0, 0], [w, 0, 0], [w, h - f, 0], [w - f, h, 0], [0, h, 0],
                   stroke_color=color, stroke_width=2, fill_color=WHITE, fill_opacity=1)
    fold = VMobject(stroke_color=color, stroke_width=2).set_points_as_corners(
        [[w - f, h, 0], [w - f, h - f, 0], [w, h - f, 0]])
    return VGroup(body, fold)


def tip(point, direction, color, size=0.16):
    d = np.array(direction, dtype=float)
    d /= np.linalg.norm(d)
    n = np.array([-d[1], d[0], 0])
    p = np.array(point)
    return Polygon(p, p - d * size + n * size * 0.55, p - d * size - n * size * 0.55,
                   stroke_width=0, fill_color=color, fill_opacity=1)


class CAD6(Scene):
    def construct(self):
        title = T("主模型技術（Master Model Technique）：單一主模型 → 分割本體 → 衍生零件 → 工程圖", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        card_w, gap = 2.75, 0.75
        xs = [(i - 1.5) * (card_w + gap) for i in range(4)]
        y_top, y_bot = 3.1, -2.2
        cy = (y_top + y_bot) / 2
        geo_y = 0.55

        heads = [
            ("主模型", "Master.sldprt"),
            ("分割本體", "Split Bodies"),
            ("衍生零件", "Derive / Insert into New Part"),
            ("工程圖", "Drawings"),
        ]
        bullets = [
            ["單一零件檔、多本體建模", "外觀、分模面、止口、", "螺絲柱一併建立"],
            ["以分模面執行 Split", "切成上蓋 / 下蓋兩實體", "仍位於同一主模型檔內"],
            ["各實體輸出為獨立零件檔", "外部參照連結回主模型"],
            ["由衍生零件出圖", "視圖與尺寸隨模型更新"],
        ]

        for i, (x, (h1, h2)) in enumerate(zip(xs, heads)):
            card = RoundedRectangle(width=card_w, height=y_top - y_bot, corner_radius=0.15,
                                    stroke_color=CARD, stroke_width=2).move_to([x, cy, 0])
            num = VGroup(Circle(0.19, fill_color=BLUE_, fill_opacity=1, stroke_width=0),
                         T(str(i + 1), 18, WHITE, BOLD))
            num[1].move_to(num[0])
            hd = VGroup(num, T(h1, 21, INK, BOLD)).arrange(RIGHT, buff=0.15)
            sub = T(h2, 15, MUTED)
            if sub.width > card_w - 0.2:
                sub.scale_to_fit_width(card_w - 0.2)
            header = VGroup(hd, sub).arrange(DOWN, buff=0.12).move_to([x, 2.55, 0])
            bl = VGroup(*[T(s, 15, INK) for s in bullets[i]]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            bl.move_to([x, -1.45, 0])
            self.add(card, header, bl)

        # ---------- 1. 主模型 ----------
        x = xs[0]
        top, bot = housing()
        master = VGroup(top, bot).move_to([x, geo_y, 0])
        pl = DashedLine([x - W / 2 - 0.12, geo_y, 0], [x + W / 2 + 0.12, geo_y, 0],
                        color=RED_, stroke_width=3, dash_length=0.08)
        pl_lab = T("分模面", 15, RED_).next_to(master, UP, buff=0.12).shift(LEFT * 0.6)
        pl_ptr = Line(pl_lab.get_bottom() + DOWN * 0.03, [x - 0.75, geo_y + 0.02, 0], color=RED_, stroke_width=1.5)
        lip_pt = np.array([x - W / 2 + TH - LW / 2, geo_y + LH / 2, 0])
        lip_lab = T("止口", 15, INK).move_to([x - 0.8, geo_y - H / 2 - 0.35, 0])
        lip_ptr = Line(lip_lab.get_top() + UP * 0.03, lip_pt, color=MUTED, stroke_width=1.5)
        boss_pt = np.array([x + BOSS_X + BW / 2, geo_y - 0.2, 0])
        boss_lab = T("螺絲柱", 15, INK).move_to([x + 0.85, geo_y - H / 2 - 0.35, 0])
        boss_ptr = Line(boss_lab.get_top() + UP * 0.03, boss_pt, color=MUTED, stroke_width=1.5)
        self.add(master, pl, pl_lab, pl_ptr, lip_ptr, lip_lab, boss_ptr, boss_lab,
                 Dot(lip_pt, 0.035, color=INK), Dot(boss_pt, 0.035, color=INK))

        # ---------- 2. 分割本體 ----------
        x = xs[1]
        top, bot = housing()
        VGroup(top, bot).move_to([x, geo_y, 0])
        top.shift(UP * 0.3)
        bot.shift(DOWN * 0.3)
        sp = DashedLine([x - W / 2 - 0.12, geo_y, 0], [x + W / 2 + 0.12, geo_y, 0],
                        color=RED_, stroke_width=2, dash_length=0.08, stroke_opacity=0.6)
        t_lab = T("上蓋本體", 16, TOP_C, BOLD).next_to(top, UP, buff=0.12)
        b_lab = T("下蓋本體", 16, BOT_C, BOLD).next_to(bot, DOWN, buff=0.12)
        self.add(sp, top, bot, t_lab, b_lab)

        # ---------- 3. 衍生零件 ----------
        x = xs[2]
        for k, (name, col, dy) in enumerate((("Top_Cover.sldprt", TOP_C, 1.18), ("Bottom_Cover.sldprt", BOT_C, -0.12))):
            top, bot = housing()
            part = (top if k == 0 else bot)
            part.scale(0.68)
            ic = file_icon(col)
            nm = T(name, 15, col, BOLD)
            lab = VGroup(ic, nm).arrange(RIGHT, buff=0.1)
            grp = VGroup(lab, part).arrange(DOWN, buff=0.12).move_to([x, geo_y + dy - 0.55, 0])
            self.add(grp)

        # ---------- 4. 工程圖 ----------
        x = xs[3]
        sw, sh = 2.35, 1.75
        sheet = Rectangle(width=sw, height=sh, stroke_color=INK, stroke_width=2).move_to([x, geo_y + 0.05, 0])
        border = Rectangle(width=sw - 0.14, height=sh - 0.14, stroke_color=INK, stroke_width=1).move_to(sheet)
        tb = Rectangle(width=0.8, height=0.3, stroke_color=INK, stroke_width=1)
        tb.align_to(border, DR)
        tb_lines = VGroup(Line(tb.get_left(), tb.get_right(), stroke_width=0.8, color=INK),
                          Line(tb.get_top(), tb.get_bottom(), stroke_width=0.8, color=INK).shift(LEFT * 0.15))
        top, bot = housing()
        views = VGroup()
        for m in (top, bot):
            v = m.copy().set_fill(opacity=0).set_stroke(INK, width=1.6).scale(0.62)
            views.add(v)
        views.arrange(DOWN, buff=0.28).move_to(sheet).shift(UP * 0.12 + LEFT * 0.08)
        # 螺絲柱位置尺寸（下蓋視圖）
        bv = views[1]
        y_d = bv.get_bottom()[1] - 0.12
        x_l = bv.get_left()[0]
        x_b = bv.get_center()[0] + BOSS_X * 0.62
        dim = DoubleArrow([x_l, y_d, 0], [x_b, y_d, 0], buff=0, color=ORANGE_, stroke_width=2,
                          tip_length=0.09, max_tip_length_to_length_ratio=0.2)
        ext = VGroup(Line([x_l, bv.get_bottom()[1], 0], [x_l, y_d - 0.05, 0], stroke_width=1, color=ORANGE_),
                     Line([x_b, bv.get_bottom()[1] + 0.05, 0], [x_b, y_d - 0.05, 0], stroke_width=1, color=ORANGE_))
        dval = T("自動更新", 11, ORANGE_).next_to(dim, DOWN, buff=0.04)
        self.add(sheet, border, tb, tb_lines, views, dim, ext, dval)

        # ---------- 卡片間流程箭頭 ----------
        flow = [("分割", "Split"), ("衍生", "Derive"), ("出圖", "Detail")]
        for i, (a, b) in enumerate(flow):
            x0 = xs[i] + card_w / 2 + 0.06
            x1 = xs[i + 1] - card_w / 2 - 0.06
            arr = Arrow([x0, geo_y, 0], [x1, geo_y, 0], buff=0, color=BLUE_, stroke_width=5,
                        max_tip_length_to_length_ratio=0.35)
            la = T(a, 16, BLUE_, BOLD).next_to(arr, UP, buff=0.1)
            lb = T(b, 13, MUTED).next_to(arr, DOWN, buff=0.1)
            self.add(arr, la, lb)

        # ---------- 修改傳遞（回饋）----------
        y_line = -2.62
        path = VMobject().set_points_as_corners([[xs[0], y_bot - 0.02, 0], [xs[0], y_line, 0], [xs[3], y_line, 0]])
        dashed = DashedVMobject(path, num_dashes=70).set_stroke(ORANGE_, width=3)
        self.add(dashed)
        for x in xs[1:]:
            self.add(DashedLine([x, y_line, 0], [x, y_bot - 0.14, 0], color=ORANGE_, stroke_width=3, dash_length=0.06),
                     tip([x, y_bot - 0.02, 0], UP, ORANGE_))
        edit = T("修改", 15, ORANGE_, BOLD).next_to([xs[0], y_bot - 0.2, 0], LEFT, buff=0.1)
        self.add(edit)
        msg = T("修改主模型 → 全部分件與工程圖自動同步", 20, ORANGE_, BOLD)
        msg2 = T("外輪廓、螺絲柱位置變更時只需編輯 Master.sldprt，上下蓋永遠由同一組幾何切出，杜絕組裝錯位與干涉", 15, MUTED)
        VGroup(msg, msg2).arrange(DOWN, buff=0.1).move_to([0, -3.3, 0])
        self.add(msg, msg2)
