# CAD-2：基準坐標系與參考幾何配置 —— 基準面依附原則與中間面對稱拉伸
# 產生方式：manim -s -o CAD-2 CAD-2.py CAD2
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
FILL_BODY = "#E9ECEF"
FILL_GOOD = "#E7F5FF"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def C(s, size=16, color=INK, weight=NORMAL):
    return Text(s, font=MONO, font_size=size, color=color, weight=weight)


def SYM(s, size=24, color=INK):
    return Text(s, font="Segoe UI Symbol", font_size=size, color=color)


def stepped_block(cx, y_base, chamfered=False, fill=FILL_BODY):
    """側視階梯塊體：底部寬 2.0、右側高台寬 0.9。chamfered=True 表示上游特徵將頂面切斜。"""
    x0 = cx - 1.0
    if not chamfered:
        pts = [
            [x0, y_base, 0], [x0 + 2.0, y_base, 0], [x0 + 2.0, y_base + 1.15, 0],
            [x0 + 1.05, y_base + 1.15, 0], [x0 + 1.05, y_base + 0.65, 0], [x0, y_base + 0.65, 0],
        ]
    else:
        pts = [
            [x0, y_base, 0], [x0 + 2.0, y_base, 0], [x0 + 2.0, y_base + 0.8, 0],
            [x0 + 1.05, y_base + 1.15, 0], [x0 + 1.05, y_base + 0.65, 0], [x0, y_base + 0.65, 0],
        ]
    return Polygon(*pts, stroke_color=INK, stroke_width=2.5, fill_color=fill, fill_opacity=1)


class CAD2(Scene):
    def construct(self):
        title = T("基準坐標系與參考幾何配置：基準面依附原則與中間面對稱拉伸", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        LX, RX = -3.55, 3.55
        pw, y_top, y_bot = 6.7, 3.05, -3.65
        for cx in (LX, RX):
            self.add(RoundedRectangle(width=pw, height=y_top - y_bot, corner_radius=0.15,
                                      stroke_color=CARD, stroke_width=2).move_to([cx, (y_top + y_bot) / 2, 0]))

        # ================= 左欄：錯誤示範 =================
        head_l = VGroup(SYM("✘", 24, RED_), T("實體表面依附 & 單向拉伸", 22, RED_, BOLD)).arrange(RIGHT, buff=0.12)
        head_l.move_to([LX, 2.65, 0])
        self.add(head_l)

        # 上半部：實體表面依附造成懸空參照
        sec_l1 = T("1. 草圖直接依附實體表面（Face-Based）", 16, INK, BOLD).move_to([LX, 2.2, 0])
        self.add(sec_l1)

        x_l1, x_l2 = LX - 1.65, LX + 1.55
        yb = 0.02
        blk_l1 = stepped_block(x_l1, yb, False, FILL_BODY)
        # 被依附的實體頂面（橘紅加粗）
        face_ref = Line([x_l1 + 0.05, yb + 1.15, 0], [x_l1 + 1.0, yb + 1.15, 0], color=ORANGE_, stroke_width=5)
        boss_l1 = Rectangle(width=0.45, height=0.42, stroke_color=BLUE_, stroke_width=2.5,
                            fill_color=BLUE_, fill_opacity=0.25).move_to([x_l1 + 0.525, yb + 1.36, 0])
        lbl_face = T("依附實體頂面", 13, ORANGE_, BOLD).next_to(face_ref, LEFT, buff=0.14).shift(UP * 0.05)
        lbl_boss = T("下游凸台", 13, BLUE_, BOLD).next_to(boss_l1, UP, buff=0.05)
        self.add(blk_l1, face_ref, boss_l1, lbl_face, lbl_boss)

        arr_mid_l = Arrow([x_l1 + 1.12, yb + 0.72, 0], [x_l2 - 1.12, yb + 0.72, 0], buff=0,
                          color=RED_, stroke_width=3.5, max_tip_length_to_length_ratio=0.28)
        arr_mid_lbl = T("上游斜切", 13, RED_, BOLD).next_to(arr_mid_l, UP, buff=0.08)
        self.add(arr_mid_l, arr_mid_lbl)

        blk_l2 = stepped_block(x_l2, yb, True, FILL_BODY)
        cut_face = Line([x_l2 + 0.05, yb + 1.15, 0], [x_l2 + 1.0, yb + 0.8, 0], color=RED_, stroke_width=4)
        ghost_boss = DashedVMobject(
            Rectangle(width=0.45, height=0.42, stroke_color=RED_, stroke_width=2.5),
            num_dashes=16,
        ).move_to([x_l2 + 0.525, yb + 1.36, 0])
        err_x = SYM("✘", 22, RED_).move_to(ghost_boss)
        err_tag = T("懸空參照！", 14, RED_, BOLD).next_to(ghost_boss, UP, buff=0.05)
        err_sub = T("原頂面 ID 消失 → 重建失敗", 13, RED_).next_to(blk_l2, DOWN, buff=0.1)
        self.add(blk_l2, cut_face, ghost_boss, err_x, err_tag, err_sub)

        # 左側水平分隔線
        self.add(Line([LX - 2.9, -0.42, 0], [LX + 2.9, -0.42, 0], color=CARD, stroke_width=1.5))

        # 下半部：單向拉伸導致基準偏離中心
        sec_l2 = T("2. 單向拉伸（Blind Extrude）", 16, INK, BOLD).move_to([LX, -0.78, 0])
        self.add(sec_l2)

        y_ex_l = -1.98
        ext_l = Rectangle(width=2.8, height=0.95, stroke_color=INK, stroke_width=2.5,
                          fill_color=FILL_BODY, fill_opacity=1).move_to([LX + 0.25, y_ex_l, 0])
        datum_l = Line([ext_l.get_left()[0], y_ex_l - 0.72, 0],
                       [ext_l.get_left()[0], y_ex_l + 0.72, 0], color=ORANGE_, stroke_width=3.5)
        datum_l_lbl = T("基準面", 13, ORANGE_, BOLD).next_to(datum_l, UP, buff=0.05)
        cl_l = DashedLine([ext_l.get_center()[0], y_ex_l - 0.65, 0],
                          [ext_l.get_center()[0], y_ex_l + 0.65, 0], color=MUTED, stroke_width=1.8)
        cl_l_lbl = T("幾何中心", 13, MUTED).next_to(cl_l, UP, buff=0.05)
        blind_arr = Arrow([ext_l.get_left()[0] + 0.15, y_ex_l, 0],
                          [ext_l.get_right()[0] - 0.15, y_ex_l, 0], buff=0,
                          color=ORANGE_, stroke_width=3.5, max_tip_length_to_length_ratio=0.12)
        blind_lbl = C("+L", 15, ORANGE_, BOLD).next_to(blind_arr, UP, buff=0.04)
        off_note = T("基準面偏離零件中心，鏡射與定位皆須額外建立輔助面", 14, RED_, BOLD).move_to([LX, -3.22, 0])
        self.add(ext_l, datum_l, datum_l_lbl, cl_l, cl_l_lbl, blind_arr, blind_lbl, off_note)

        # ================= 右欄：正確做法 =================
        head_r = VGroup(SYM("✔", 24, GREEN_), T("基準面依附 & 中間面對稱拉伸", 22, GREEN_, BOLD)).arrange(RIGHT, buff=0.12)
        head_r.move_to([RX, 2.65, 0])
        self.add(head_r)

        # 上半部：基準面依附原則
        sec_r1 = T("1. 草圖依附於獨立偏移基準面（Plane-Based）", 16, INK, BOLD).move_to([RX, 2.2, 0])
        self.add(sec_r1)

        x_r1, x_r2 = RX - 1.7, RX + 1.55
        for xx, ch in ((x_r1, False), (x_r2, True)):
            blk = stepped_block(xx, yb, ch, FILL_GOOD)
            # 基準底面（上基準面 Top Plane）
            base_pl = Line([xx - 1.28, yb, 0], [xx + 1.22, yb, 0], color=BLUE_, stroke_width=2.5)
            # 偏移基準面（Datum Plane 1，位於 y = yb + 1.15）
            off_pl = DashedLine([xx - 1.25, yb + 1.15, 0], [xx + 1.2, yb + 1.15, 0],
                                color=BLUE_, stroke_width=3, dash_length=0.09)
            # 高度 H 標註（錨定於上基準面）
            h_arr = DoubleArrow([xx - 1.18, yb, 0], [xx - 1.18, yb + 1.15, 0], buff=0,
                                color=BLUE_, stroke_width=2, tip_length=0.09, max_tip_length_to_length_ratio=0.18)
            h_lbl = C("H", 13, BLUE_, BOLD).next_to(h_arr, LEFT, buff=0.04)
            boss = Rectangle(width=0.45, height=0.42, stroke_color=GREEN_, stroke_width=2.5,
                             fill_color=GREEN_, fill_opacity=0.3).move_to([xx + 0.525, yb + 1.36, 0])
            self.add(blk, base_pl, off_pl, h_arr, h_lbl, boss)
            if not ch:
                self.add(T("偏移基準面", 13, BLUE_, BOLD).next_to(off_pl, UP, buff=0.05).shift(LEFT * 0.45))
            else:
                self.add(VGroup(SYM("✔", 16, GREEN_), T("穩固重建", 13, GREEN_, BOLD))
                         .arrange(RIGHT, buff=0.05).next_to(boss, UP, buff=0.05))
                self.add(T("基準面 Entity ID 恆定不受影響", 13, GREEN_).next_to(blk, DOWN, buff=0.1))

        arr_mid_r = Arrow([x_r1 + 1.18, yb + 0.72, 0], [x_r2 - 1.18, yb + 0.72, 0], buff=0,
                          color=GREEN_, stroke_width=3.5, max_tip_length_to_length_ratio=0.28)
        arr_mid_r_lbl = T("上游斜切", 13, GREEN_, BOLD).next_to(arr_mid_r, UP, buff=0.08)
        self.add(arr_mid_r, arr_mid_r_lbl)

        # 右側水平分隔線
        self.add(Line([RX - 2.9, -0.42, 0], [RX + 2.9, -0.42, 0], color=CARD, stroke_width=1.5))

        # 下半部：中間面對稱拉伸 + 原點 3-2-1 基準
        sec_r2 = T("2. 中間面對稱拉伸（Midplane）& 3-2-1 原點整合", 16, INK, BOLD).move_to([RX, -0.78, 0])
        self.add(sec_r2)

        y_ex_r = -1.98
        ext_r = Rectangle(width=2.8, height=1.04, stroke_color=INK, stroke_width=2.5,
                          fill_color=FILL_GOOD, fill_opacity=1).move_to([RX, y_ex_r, 0])
        # 中央基準面與原點 (0,0,0)
        datum_r = Line([RX, y_ex_r - 0.72, 0], [RX, y_ex_r + 0.72, 0], color=BLUE_, stroke_width=3.5)
        datum_r_lbl = T("前基準面（對稱中心）", 13, BLUE_, BOLD).next_to(datum_r, UP, buff=0.05)
        base_datum = Line([RX - 1.75, y_ex_r - 0.52, 0], [RX + 1.75, y_ex_r - 0.52, 0],
                          color=GREEN_, stroke_width=2.5)
        origin_dot = Dot([RX, y_ex_r - 0.52, 0], radius=0.075, color=RED_)
        origin_lbl = T("原點 (0,0,0) / Datum A·B·C / G54", 13, RED_, BOLD).next_to(origin_dot, DOWN, buff=0.14)

        # 雙向對稱拉伸箭頭
        a_left = Arrow([RX - 0.08, y_ex_r + 0.18, 0], [RX - 1.3, y_ex_r + 0.18, 0], buff=0,
                       color=BLUE_, stroke_width=3, max_tip_length_to_length_ratio=0.18)
        a_right = Arrow([RX + 0.08, y_ex_r + 0.18, 0], [RX + 1.3, y_ex_r + 0.18, 0], buff=0,
                        color=BLUE_, stroke_width=3, max_tip_length_to_length_ratio=0.18)
        self.add(C("-L/2", 14, BLUE_, BOLD).next_to(a_left, UP, buff=0.04))
        self.add(C("+L/2", 14, BLUE_, BOLD).next_to(a_right, UP, buff=0.04))

        # 鏡射孔示範（箭頭放在方塊內部上方，完全避開底部原點）
        hole_l = Rectangle(width=0.22, height=0.26, stroke_color=GREEN_, stroke_width=2,
                           fill_color=WHITE, fill_opacity=1).move_to([RX - 0.92, y_ex_r - 0.24, 0])
        hole_r = hole_l.copy().move_to([RX + 0.92, y_ex_r - 0.24, 0])
        mir_arc = CurvedArrow(hole_l.get_top() + RIGHT * 0.05 + UP * 0.02,
                              hole_r.get_top() + LEFT * 0.05 + UP * 0.02,
                              angle=-0.22, color=GREEN_, stroke_width=2, tip_length=0.1)
        mir_lbl = T("Mirror 鏡射", 11, GREEN_, BOLD).move_to([RX + 0.42, y_ex_r - 0.24, 0])

        ok_note = T("直接共用中心基準面執行鏡射，並對齊 GD&T 與 CNC 加工座標", 14, GREEN_, BOLD).move_to([RX, -3.22, 0])
        self.add(ext_r, datum_r, datum_r_lbl, base_datum, origin_dot, origin_lbl,
                 a_left, a_right, hole_l, hole_r, mir_arc, mir_lbl, ok_note)
