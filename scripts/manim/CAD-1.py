# CAD-1：設計意圖（Design Intent）—— 靜態建模 vs. 參數化建模在尺寸變更時的差異
# 產生方式：manim -s -o CAD-1 CAD-1.py CAD1
from manim import *
import numpy as np

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
CARD = "#DEE2E6"
FILL_STATIC = "#F1F3F5"
FILL_PARAM = "#E7F5FF"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def C(s, size=18, color=INK, weight=NORMAL):
    return Text(s, font=MONO, font_size=size, color=color, weight=weight)


def SYM(s, size=24, color=INK):
    return Text(s, font="Segoe UI Symbol", font_size=size, color=color)


def dim_h(x0, x1, y, label_mob, color=MUTED, ext_from_y=None):
    """繪製水平尺寸標註線與延伸線。"""
    g = VGroup()
    if ext_from_y is not None:
        dy = -0.08 if y < ext_from_y else 0.08
        g.add(
            Line([x0, ext_from_y, 0], [x0, y + dy, 0], color=color, stroke_width=1.4),
            Line([x1, ext_from_y, 0], [x1, y + dy, 0], color=color, stroke_width=1.4),
        )
    arr = DoubleArrow([x0, y, 0], [x1, y, 0], buff=0, color=color, stroke_width=2.2,
                      tip_length=0.11, max_tip_length_to_length_ratio=0.15)
    bg = BackgroundRectangle(label_mob, color=WHITE, fill_opacity=0.95, buff=0.04)
    label_mob.move_to([(x0 + x1) / 2, y, 0])
    bg.move_to(label_mob)
    g.add(arr, bg, label_mob)
    return g


def draw_bracket(x_left, y_c, W_mm, hole_xs_mm, scale, fill_col, stroke_col=INK,
                 cl_col=MUTED, extra_zone_from=None):
    """繪製安裝座正視圖：總寬 W_mm、兩個螺孔與一個中心軸承孔。"""
    w = W_mm * scale
    h = 0.96
    cx = x_left + w / 2
    plate = RoundedRectangle(width=w, height=h, corner_radius=0.08,
                             stroke_color=stroke_col, stroke_width=2.5,
                             fill_color=fill_col, fill_opacity=1).move_to([cx, y_c, 0])
    g = VGroup(plate)
    if extra_zone_from is not None:
        ew = (W_mm - extra_zone_from) * scale
        ex = x_left + extra_zone_from * scale + ew / 2
        zone = Rectangle(width=ew, height=h - 0.04, stroke_width=0,
                         fill_color=ORANGE_, fill_opacity=0.16).move_to([ex, y_c, 0])
        g.add(zone)
        g.add(DashedLine([x_left + extra_zone_from * scale, y_c - h / 2, 0],
                         [x_left + extra_zone_from * scale, y_c + h / 2, 0],
                         color=ORANGE_, stroke_width=1.8, dash_length=0.06))

    # 板件幾何中心線 CL
    g.add(DashedLine([cx, y_c - h / 2 - 0.14, 0], [cx, y_c + h / 2 + 0.14, 0],
                     color=cl_col, stroke_width=2, dash_length=0.07))

    # 三個孔：左螺孔、中心軸承孔、右螺孔
    radii = (0.09, 0.24, 0.09)
    for hx_mm, r in zip(hole_xs_mm, radii):
        hx = x_left + hx_mm * scale
        hole = Circle(radius=r, stroke_color=INK, stroke_width=2.5,
                      fill_color=WHITE, fill_opacity=1).move_to([hx, y_c, 0])
        g.add(hole)
        if r > 0.15:
            g.add(
                DashedLine([hx - r - 0.08, y_c, 0], [hx + r + 0.08, y_c, 0],
                           color=MUTED, stroke_width=1.2, dash_length=0.05),
                DashedLine([hx, y_c - r - 0.08, 0], [hx, y_c + r + 0.08, 0],
                           color=MUTED, stroke_width=1.2, dash_length=0.05),
            )
    return g


class CAD1(Scene):
    def construct(self):
        title = T("設計意圖（Design Intent）：靜態建模 vs. 參數化建模在尺寸變更時的差異", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        LX, RX = -3.55, 3.55
        pw, y_top, y_bot = 6.7, 3.05, -3.65
        for cx in (LX, RX):
            self.add(RoundedRectangle(width=pw, height=y_top - y_bot, corner_radius=0.15,
                                      stroke_color=CARD, stroke_width=2).move_to([cx, (y_top + y_bot) / 2, 0]))

        SC = 0.031
        y_init, y_after = 1.05, -1.62

        # ================= 左欄：靜態建模 =================
        head_l = VGroup(SYM("✘", 24, RED_), T("靜態建模（缺乏設計意圖）", 22, RED_, BOLD)).arrange(RIGHT, buff=0.12)
        head_l.move_to([LX, 2.68, 0])
        self.add(head_l)

        xl_base = LX - 140 * SC / 2  # 左邊界固定對齊，右端隨 W 伸長
        # 初始狀態 W = 100
        tag_l1 = VGroup(T("初始狀態：", 15, MUTED), C("W = 100 mm", 16, BLUE_, BOLD)).arrange(RIGHT, buff=0.08)
        tag_l1.move_to([LX, 2.22, 0])
        br_l1 = draw_bracket(xl_base, y_init, 100, (20, 50, 80), SC, FILL_STATIC)
        d_l1_w = dim_h(xl_base, xl_base + 100 * SC, y_init + 0.76, C("W = 100", 14, BLUE_, BOLD),
                       BLUE_, ext_from_y=y_init + 0.48)
        # 左基準絕對尺寸 20, 50, 80
        d_l1_20 = dim_h(xl_base, xl_base + 20 * SC, y_init - 0.66, C("20", 13, MUTED),
                        MUTED, ext_from_y=y_init)
        d_l1_50 = dim_h(xl_base, xl_base + 50 * SC, y_init - 0.96, C("50", 13, MUTED),
                        MUTED, ext_from_y=y_init - 0.24)
        d_l1_80 = dim_h(xl_base, xl_base + 80 * SC, y_init - 1.26, C("80", 13, MUTED),
                        MUTED, ext_from_y=y_init)
        self.add(tag_l1, br_l1, d_l1_w, d_l1_20, d_l1_50, d_l1_80)

        # 中間轉變箭頭
        arr_l = Arrow([LX, -0.26, 0], [LX, -0.74, 0], buff=0, color=ORANGE_, stroke_width=4,
                      max_tip_length_to_length_ratio=0.32)
        arr_l_lbl = VGroup(T("總寬變更：", 15, ORANGE_, BOLD), C("W = 140 mm", 16, ORANGE_, BOLD)).arrange(
            RIGHT, buff=0.08).next_to(arr_l, RIGHT, buff=0.14)
        self.add(arr_l, arr_l_lbl)

        # 變更後狀態 W = 140（絕對位置 20, 50, 80 未動）
        br_l2 = draw_bracket(xl_base, y_after, 140, (20, 50, 80), SC, FILL_STATIC,
                             cl_col=RED_, extra_zone_from=100)
        d_l2_w = dim_h(xl_base, xl_base + 140 * SC, y_after + 0.78, C("W = 140", 14, ORANGE_, BOLD),
                       ORANGE_, ext_from_y=y_after + 0.48)
        # 標註偏心問題
        cx_new = xl_base + 70 * SC
        cx_bore = xl_base + 50 * SC
        cl_lbl = C("CL", 13, RED_, BOLD).move_to([cx_new + 0.16, y_after + 0.56, 0])
        # 以文字移動標出偏心間隙
        ecc_arr = DoubleArrow([cx_bore, y_after - 0.68, 0], [cx_new, y_after - 0.68, 0], buff=0,
                              color=RED_, stroke_width=2.5, tip_length=0.1, max_tip_length_to_length_ratio=0.25)
        ecc_ext = VGroup(
            Line([cx_bore, y_after - 0.24, 0], [cx_bore, y_after - 0.74, 0], color=RED_, stroke_width=1.4),
            Line([cx_new, y_after - 0.48, 0], [cx_new, y_after - 0.74, 0], color=RED_, stroke_width=1.4),
        )
        ecc_lbl = T("孔位偏心 20 mm！", 14, RED_, BOLD).next_to(ecc_arr, DOWN, buff=0.08)
        right_gap = dim_h(xl_base + 80 * SC, xl_base + 140 * SC, y_after - 0.68,
                          C("60 (≠20)", 13, RED_, BOLD), RED_, ext_from_y=y_after)
        self.add(br_l2, d_l2_w, cl_lbl, ecc_ext, ecc_arr, ecc_lbl, right_gap)

        cap_l = T("絕對尺寸鎖死 → 寬度變更後孔位偏離中心、失去對稱功能", 15, RED_, BOLD).move_to([LX, -3.26, 0])
        self.add(cap_l)

        # ================= 右欄：參數化建模 =================
        head_r = VGroup(SYM("✔", 24, GREEN_), T("參數化建模（落實設計意圖）", 22, GREEN_, BOLD)).arrange(RIGHT, buff=0.12)
        head_r.move_to([RX, 2.68, 0])
        self.add(head_r)

        # 初始狀態 W = 100（對稱中心線 CL 位於 RX）
        tag_r1 = VGroup(T("初始狀態：", 15, MUTED), C("W = 100 mm", 16, BLUE_, BOLD)).arrange(RIGHT, buff=0.08)
        tag_r1.move_to([RX, 2.22, 0])
        xr_1 = RX - 100 * SC / 2
        br_r1 = draw_bracket(xr_1, y_init, 100, (20, 50, 80), SC, FILL_PARAM,
                             stroke_col=INK, cl_col=BLUE_)
        d_r1_w = dim_h(xr_1, xr_1 + 100 * SC, y_init + 0.76, C("W = 100", 14, BLUE_, BOLD),
                       BLUE_, ext_from_y=y_init + 0.48)
        cl_r1 = C("CL", 13, BLUE_, BOLD).move_to([RX + 0.16, y_init + 0.56, 0])
        # 邊距 20 + 對稱符號 + 中心重合標註
        d_r1_edge = dim_h(xr_1, xr_1 + 20 * SC, y_init - 0.66, C("20", 13, GREEN_, BOLD),
                          GREEN_, ext_from_y=y_init)
        d_r1_edge2 = dim_h(xr_1 + 80 * SC, xr_1 + 100 * SC, y_init - 0.66, C("= 20", 13, GREEN_, BOLD),
                           GREEN_, ext_from_y=y_init)
        sym_lbl = T("中心孔重合 CL · 兩側螺孔對稱約束", 14, GREEN_, BOLD).move_to([RX, y_init - 1.08, 0])
        self.add(tag_r1, br_r1, d_r1_w, cl_r1, d_r1_edge, d_r1_edge2, sym_lbl)

        # 中間轉變箭頭
        arr_r = Arrow([RX, -0.26, 0], [RX, -0.74, 0], buff=0, color=GREEN_, stroke_width=4,
                      max_tip_length_to_length_ratio=0.32)
        arr_r_lbl = VGroup(T("總寬變更：", 15, GREEN_, BOLD), C("W = 140 mm", 16, GREEN_, BOLD)).arrange(
            RIGHT, buff=0.08).next_to(arr_r, RIGHT, buff=0.14)
        self.add(arr_r, arr_r_lbl)

        # 變更後狀態 W = 140（中心孔保持於 CL，兩側螺孔自動移至 20 與 120）
        xr_2 = RX - 140 * SC / 2
        br_r2 = draw_bracket(xr_2, y_after, 140, (20, 70, 120), SC, FILL_PARAM,
                             stroke_col=INK, cl_col=BLUE_)
        d_r2_w = dim_h(xr_2, xr_2 + 140 * SC, y_after + 0.78, C("W = 140", 14, GREEN_, BOLD),
                       GREEN_, ext_from_y=y_after + 0.48)
        cl_r2 = C("CL", 13, BLUE_, BOLD).move_to([RX + 0.16, y_after + 0.56, 0])
        d_r2_edge1 = dim_h(xr_2, xr_2 + 20 * SC, y_after - 0.66, C("20", 13, GREEN_, BOLD),
                           GREEN_, ext_from_y=y_after)
        d_r2_edge2 = dim_h(xr_2 + 120 * SC, xr_2 + 140 * SC, y_after - 0.66, C("20", 13, GREEN_, BOLD),
                           GREEN_, ext_from_y=y_after)
        d_r2_span = dim_h(xr_2 + 20 * SC, xr_2 + 120 * SC, y_after - 1.04,
                          C("PCD = W - 40 = 100", 13, BLUE_, BOLD), BLUE_, ext_from_y=y_after - 0.66)
        self.add(br_r2, d_r2_w, cl_r2, d_r2_edge1, d_r2_edge2, d_r2_span)

        cap_r = T("幾何約束 + 方程式連動 → 尺寸變更後自動維持對稱（Clean Rebuild）", 15, GREEN_, BOLD).move_to([RX, -3.26, 0])
        self.add(cap_r)
