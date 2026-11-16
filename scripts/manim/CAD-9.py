# CAD-9：拓撲邊界異常排解 —— 零厚度幾何（Non-Manifold）與虛擬交點（Virtual Sharp）
# 產生方式：manim -s -o CAD-9 CAD-9.py CAD9
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
FILL_OK = "#E7F5FF"
FILL_ERR = "#FFF5F5"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def C(s, size=16, color=INK, weight=NORMAL):
    return Text(s, font=MONO, font_size=size, color=color, weight=weight)


def SYM(s, size=24, color=INK):
    return Text(s, font="Segoe UI Symbol", font_size=size, color=color)


def filleted_corner_pts(origin, w, h, slope_dx, R, n_arc=24):
    """建立左上平、右側具拔模斜度並帶圓角 R 的剖面輪廓點（供虛擬交點比較）。
    右上角兩線交點（虛擬交點）位於 corner = (origin_x + w, origin_y + h)。
    """
    ox, oy = origin
    vx, vy = ox + w, oy + h
    # 上邊方向單位向量 u1 = (-1, 0)，右斜邊方向單位向量 u2 = (slope_dx, -h) 單位化
    u1 = np.array([-1.0, 0.0, 0.0])
    v_down = np.array([slope_dx, -h, 0.0])
    u2 = v_down / np.linalg.norm(v_down)
    # 角平分線與切點距離 d = R / tan(theta/2)
    cos_t = np.dot(u1, u2)
    theta = np.arccos(np.clip(cos_t, -1.0, 1.0))
    d = R / np.tan(theta / 2)
    corner = np.array([vx, vy, 0.0])
    t1 = corner + u1 * d  # 上邊切點
    t2 = corner + u2 * d  # 斜邊切點
    # 圓心在垂直於 u1 的內側距離 R
    center = t1 + np.array([0.0, -R, 0.0])
    a1 = np.arctan2(t1[1] - center[1], t1[0] - center[0])
    a2 = np.arctan2(t2[1] - center[1], t2[0] - center[0])
    if a2 > a1:
        a2 -= TAU
    arc_pts = [center + R * np.array([np.cos(a), np.sin(a), 0.0]) for a in np.linspace(a1, a2, n_arc)]
    pts = [
        np.array([ox, oy, 0.0]),
        np.array([ox, vy, 0.0]),
        *arc_pts,
        np.array([vx + slope_dx, oy, 0.0]),
    ]
    return pts, corner, t1


class CAD9(Scene):
    def construct(self):
        title = T("拓撲邊界異常排解：零厚度非流形幾何與虛擬交點標註規範", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        LX, RX = -3.55, 3.55
        pw, y_top, y_bot = 6.7, 3.05, -3.65
        for cx in (LX, RX):
            self.add(RoundedRectangle(width=pw, height=y_top - y_bot, corner_radius=0.15,
                                      stroke_color=CARD, stroke_width=2).move_to([cx, (y_top + y_bot) / 2, 0]))

        # ================= 左欄：零厚度幾何 =================
        head_l = T("零厚度幾何（Zero-Thickness / Non-Manifold）", 21, INK, BOLD).move_to([LX, 2.65, 0])
        self.add(head_l)

        # ---- 上半部（✘ 相切零厚度）----
        y_err = 1.2
        sub_l1 = VGroup(SYM("✘", 20, RED_), T("兩圓柱相切執行布林合併 → 幾何核心報錯", 16, RED_, BOLD)).arrange(
            RIGHT, buff=0.1).move_to([LX, 2.1, 0])
        r_c = 0.72
        c_left = Circle(radius=r_c, stroke_color=INK, stroke_width=2.5,
                        fill_color=FILL_ERR, fill_opacity=1).move_to([LX - 1.15 - r_c, y_err, 0])
        c_right = Circle(radius=r_c, stroke_color=INK, stroke_width=2.5,
                         fill_color=FILL_ERR, fill_opacity=1).move_to([LX - 1.15 + r_c, y_err, 0])
        pt_tan = np.array([LX - 1.15, y_err, 0.0])
        tan_ring = Circle(radius=0.18, stroke_color=RED_, stroke_width=2.5).move_to(pt_tan)
        tan_dot = Dot(pt_tan, radius=0.055, color=RED_)

        # 右側局部放大鏡
        z_center = np.array([LX + 1.55, y_err + 0.05, 0.0])
        z_r = 0.72
        zoom_box = Circle(radius=z_r, stroke_color=RED_, stroke_width=2.5, fill_color=WHITE, fill_opacity=1).move_to(z_center)
        # 在放大框中畫兩條相切的圓弧
        arc_l = Arc(radius=2.2, start_angle=-0.31, angle=0.62, stroke_color=INK, stroke_width=3).shift(
            z_center - np.array([2.2, 0, 0]))
        arc_r = Arc(radius=2.2, start_angle=PI - 0.31, angle=0.62, stroke_color=INK, stroke_width=3).shift(
            z_center + np.array([2.2, 0, 0]))
        z_dot = Dot(z_center, radius=0.07, color=RED_)
        z_lbl = T("厚度 = 0\n非流形邊", 14, RED_, BOLD).next_to(zoom_box, RIGHT, buff=0.15)
        callout = VGroup(
            DashedLine(tan_ring.get_top(), zoom_box.get_top(), color=RED_, stroke_width=1.5, dash_length=0.06),
            DashedLine(tan_ring.get_bottom(), zoom_box.get_bottom(), color=RED_, stroke_width=1.5, dash_length=0.06),
        )
        err_msg = T("B-Rep 無法定義單一接觸線之內外側 → 布林運算失敗", 14, RED_).move_to([LX, 0.15, 0])
        self.add(sub_l1, c_left, c_right, tan_ring, tan_dot, callout, zoom_box, arc_l, arc_r, z_dot, z_lbl, err_msg)

        self.add(Line([LX - 2.9, -0.22, 0], [LX + 2.9, -0.22, 0], color=CARD, stroke_width=1.5))

        # ---- 下半部（✔ 主動微量重疊）----
        y_ok = -1.65
        sub_l2 = VGroup(SYM("✔", 20, GREEN_), T("排解：主動微量重疊 0.05~0.1 mm 或合併草圖", 16, GREEN_, BOLD)).arrange(
            RIGHT, buff=0.1).move_to([LX, -0.62, 0])
        ov = 0.14  # 圖示誇大重疊量
        u_l = Circle(radius=r_c).move_to([LX - 1.15 - r_c + ov / 2, y_ok, 0])
        u_r = Circle(radius=r_c).move_to([LX - 1.15 + r_c - ov / 2, y_ok, 0])
        merged = Union(u_l, u_r).set_fill(FILL_OK, opacity=1).set_stroke(GREEN_, width=3)
        # 標出重疊區域輪廓（虛線）
        g_l = DashedVMobject(u_l.copy().set_stroke(MUTED, 1.4), num_dashes=28)
        g_r = DashedVMobject(u_r.copy().set_stroke(MUTED, 1.4), num_dashes=28)
        ov_ring = Circle(radius=0.22, stroke_color=GREEN_, stroke_width=2.5).move_to([LX - 1.15, y_ok, 0])

        z2_center = np.array([LX + 1.55, y_ok + 0.05, 0.0])
        zoom2 = Circle(radius=z_r, stroke_color=GREEN_, stroke_width=2.5, fill_color=WHITE, fill_opacity=1).move_to(z2_center)
        zu_l = Circle(radius=1.25).move_to(z2_center + LEFT * 1.12)
        zu_r = Circle(radius=1.25).move_to(z2_center + RIGHT * 1.12)
        neck = Intersection(zoom2.copy(), Union(zu_l, zu_r)).set_fill(FILL_OK, opacity=1).set_stroke(GREEN_, width=3)
        z2_arr = DoubleArrow(z2_center + LEFT * 0.16, z2_center + RIGHT * 0.16, buff=0,
                             color=BLUE_, stroke_width=2.5, tip_length=0.08, max_tip_length_to_length_ratio=0.35)
        z2_val = C("0.05~0.1mm", 12, BLUE_, BOLD).next_to(z2_arr, UP, buff=0.05)
        z2_lbl = T("有限壁厚\n封閉流形", 14, GREEN_, BOLD).next_to(zoom2, RIGHT, buff=0.15)
        callout2 = VGroup(
            DashedLine(ov_ring.get_top(), zoom2.get_top(), color=GREEN_, stroke_width=1.5, dash_length=0.06),
            DashedLine(ov_ring.get_bottom(), zoom2.get_bottom(), color=GREEN_, stroke_width=1.5, dash_length=0.06),
        )
        ok_msg = T("形成明確實體內外側（Manifold），特徵重建穩定", 14, GREEN_, BOLD).move_to([LX, -3.05, 0])
        self.add(sub_l2, g_l, g_r, merged, ov_ring, callout2, zoom2, neck, z2_arr, z2_val, z2_lbl, ok_msg)

        # ================= 右欄：虛擬交點 =================
        head_r = T("虛擬交點（Virtual Sharp）尺寸標註", 21, INK, BOLD).move_to([RX, 2.65, 0])
        self.add(head_r)

        # ---- 上半部（✘ 直接標註圓角切點）----
        sub_r1 = VGroup(SYM("✘", 20, RED_), T("直接點選圓弧切點 → 圓角改變時尺寸漂移", 16, RED_, BOLD)).arrange(
            RIGHT, buff=0.1).move_to([RX, 2.1, 0])

        orig1 = (RX - 1.75, 0.25)
        pts_r5, _, t1_r5 = filleted_corner_pts(orig1, 2.55, 1.15, 0.42, R=0.16)
        pts_r15, _, t1_r15 = filleted_corner_pts(orig1, 2.55, 1.15, 0.42, R=0.52)

        poly_r5 = Polygon(*pts_r5, stroke_color=INK, stroke_width=2.5, fill_color=FILL_ERR, fill_opacity=0.8)
        poly_r15 = DashedVMobject(Polygon(*pts_r15, stroke_color=ORANGE_, stroke_width=2.5), num_dashes=42)
        dot_t5 = Dot(t1_r5, radius=0.055, color=INK)
        dot_t15 = Dot(t1_r15, radius=0.055, color=ORANGE_)

        # 兩個漂移的尺寸標註
        x0_1 = orig1[0]
        y_dim1, y_dim2 = 1.62, 1.84
        ext_0 = Line([x0_1, orig1[1] + 1.15, 0], [x0_1, y_dim2 + 0.06, 0], color=MUTED, stroke_width=1.3)
        ext_t5 = Line(t1_r5, [t1_r5[0], y_dim1 + 0.06, 0], color=INK, stroke_width=1.3)
        ext_t15 = Line(t1_r15, [t1_r15[0], y_dim2 + 0.06, 0], color=ORANGE_, stroke_width=1.3)
        arr_t5 = DoubleArrow([x0_1, y_dim1, 0], [t1_r5[0], y_dim1, 0], buff=0, color=INK, stroke_width=2,
                             tip_length=0.09, max_tip_length_to_length_ratio=0.15)
        arr_t15 = DoubleArrow([x0_1, y_dim2, 0], [t1_r15[0], y_dim2, 0], buff=0, color=ORANGE_, stroke_width=2,
                              tip_length=0.09, max_tip_length_to_length_ratio=0.15)
        lbl_t5 = C("L1 (R5)", 13, INK, BOLD).next_to(arr_t5, RIGHT, buff=0.08)
        lbl_t15 = C("L2 (R15)", 13, ORANGE_, BOLD).next_to(arr_t15, RIGHT, buff=0.08)
        drift_note = T("切點隨 R 移動 → 公差基準不穩定", 14, RED_).move_to([RX, 0.02, 0])
        self.add(sub_r1, poly_r5, poly_r15, dot_t5, dot_t15, ext_0, ext_t5, ext_t15,
                 arr_t5, arr_t15, lbl_t5, lbl_t15, drift_note)

        self.add(Line([RX - 2.9, -0.22, 0], [RX + 2.9, -0.22, 0], color=CARD, stroke_width=1.5))

        # ---- 下半部（✔ 定錨於虛擬交點）----
        sub_r2 = VGroup(SYM("✔", 20, GREEN_), T("以構造線延伸求取虛擬交點 → 基準恆定", 16, GREEN_, BOLD)).arrange(
            RIGHT, buff=0.1).move_to([RX, -0.62, 0])

        orig2 = (RX - 1.75, -2.55)
        pts2_r5, corner2, _ = filleted_corner_pts(orig2, 2.55, 1.15, 0.42, R=0.16)
        pts2_r15, _, _ = filleted_corner_pts(orig2, 2.55, 1.15, 0.42, R=0.52)

        poly2_r5 = Polygon(*pts2_r5, stroke_color=INK, stroke_width=2.5, fill_color=FILL_OK, fill_opacity=0.8)
        poly2_r15 = DashedVMobject(Polygon(*pts2_r15, stroke_color=BLUE_, stroke_width=2.2), num_dashes=42)

        # 兩條延長構造線相交於 corner2（虛擬交點）
        ext_h = DashedLine([orig2[0] + 1.5, corner2[1], 0], corner2 + RIGHT * 0.28,
                           color=GREEN_, stroke_width=2.2, dash_length=0.07)
        s_dir = np.array([-0.42, 1.15, 0.0])
        s_dir = s_dir / np.linalg.norm(s_dir)
        ext_s = DashedLine(corner2 - s_dir * 0.72, corner2 + s_dir * 0.28,
                           color=GREEN_, stroke_width=2.2, dash_length=0.07)
        # 虛擬交點十字星號記號
        vs_mark = VGroup(
            Dot(corner2, radius=0.065, color=GREEN_),
            Circle(radius=0.14, stroke_color=GREEN_, stroke_width=2).move_to(corner2),
        )
        vs_lbl = T("虛擬交點\nVirtual Sharp", 13, GREEN_, BOLD).next_to(vs_mark, RIGHT, buff=0.14).shift(DOWN * 0.18)

        # 恆定尺寸標註
        x0_2 = orig2[0]
        y_dim_ok = corner2[1] + 0.34
        ext2_0 = Line([x0_2, corner2[1], 0], [x0_2, y_dim_ok + 0.08, 0], color=GREEN_, stroke_width=1.4)
        ext2_v = Line(corner2, [corner2[0], y_dim_ok + 0.08, 0], color=GREEN_, stroke_width=1.4)
        arr_ok = DoubleArrow([x0_2, y_dim_ok, 0], [corner2[0], y_dim_ok, 0], buff=0,
                             color=GREEN_, stroke_width=2.5, tip_length=0.1, max_tip_length_to_length_ratio=0.15)
        bg_ok = BackgroundRectangle(C("L = 定值", 14, GREEN_, BOLD), color=WHITE, fill_opacity=0.95, buff=0.04)
        lbl_ok = T("L = 定值（不受 R 影響）", 14, GREEN_, BOLD).next_to(arr_ok, UP, buff=0.06)

        ok_msg2 = T("確保鑄造/沖壓件拔模稜邊之工程公差基點唯一", 14, GREEN_, BOLD).move_to([RX, -3.05, 0])
        self.add(sub_r2, poly2_r5, poly2_r15, ext_h, ext_s, vs_mark, vs_lbl,
                 ext2_0, ext2_v, arr_ok, lbl_ok, ok_msg2)
