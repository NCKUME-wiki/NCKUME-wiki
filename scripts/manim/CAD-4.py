# CAD-4：曲面（曲線）連續性 G0~G3 —— 曲率梳與曲率分佈 κ(s)
# 產生方式：manim -s -o CAD-4 CAD-4.py CAD4
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
COMB = "#ADB5BD"


def T(s, size=24, color=INK, weight=NORMAL):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight)


def M(s, size=26, color=INK):
    return Text(s, font="Cambria Math", font_size=size, color=color, slant=ITALIC)


L = 1.6  # 每段曲線弧長
N = 400


def build_curve(kappa_left, kappa_right, corner=0.0):
    """以曲率函數 κ(s) 積分出平面曲線；corner 為接縫處的切線折角（G0 用）。"""
    s_left = np.linspace(-L, 0, N)
    s_right = np.linspace(0, L, N)
    k_l = kappa_left(s_left)
    k_r = kappa_right(s_right)

    def integrate(s, k, theta0, p0, backward=False):
        ds = np.diff(s)
        theta = np.zeros_like(s)
        pts = np.zeros((len(s), 2))
        if backward:  # 從 s=0 向左積分
            theta[-1] = theta0
            pts[-1] = p0
            for i in range(len(s) - 2, -1, -1):
                theta[i] = theta[i + 1] - 0.5 * (k[i] + k[i + 1]) * ds[i]
                tm = 0.5 * (theta[i] + theta[i + 1])
                pts[i] = pts[i + 1] - ds[i] * np.array([np.cos(tm), np.sin(tm)])
        else:
            theta[0] = theta0
            pts[0] = p0
            for i in range(1, len(s)):
                theta[i] = theta[i - 1] + 0.5 * (k[i] + k[i - 1]) * ds[i - 1]
                tm = 0.5 * (theta[i] + theta[i - 1])
                pts[i] = pts[i - 1] + ds[i - 1] * np.array([np.cos(tm), np.sin(tm)])
        return pts, theta

    pl, tl = integrate(s_left, k_l, 0.0, np.zeros(2), backward=True)
    pr, tr = integrate(s_right, k_r, corner, np.zeros(2))
    return (s_left, k_l, pl, tl), (s_right, k_r, pr, tr)


CASES = [
    dict(
        name="G0", title="位置連續",
        kl=lambda s: 0.25 + 0 * s, kr=lambda s: 0.25 + 0 * s, corner=np.deg2rad(40),
        note="切線折角：曲率梳在接縫處斷開",
        cond="P₁ = P₂",
    ),
    dict(
        name="G1", title="正切連續",
        kl=lambda s: 0 * s, kr=lambda s: 1.0 + 0 * s, corner=0.0,
        note="相切但曲率階躍（0 → 1/R）",
        cond="N₁ = N₂",
    ),
    dict(
        name="G2", title="曲率連續",
        kl=lambda s: 0 * s, kr=lambda s: 0.9 * s, corner=0.0,
        note="曲率連續，但 dκ/ds 跳變（折點）",
        cond="κ₁ = κ₂",
    ),
    dict(
        name="G3", title="曲率變化率連續",
        kl=lambda s: 0 * s, kr=lambda s: 0.75 * s**2, corner=0.0,
        note="κ 與 dκ/ds 皆連續，梳形包絡平順",
        cond="dκ₁/ds = dκ₂/ds",
    ),
]


class CAD4(Scene):
    def construct(self):
        title = T("曲線/曲面連續性分級 G0 ~ G3：曲率梳（Curvature Comb）與曲率分佈 κ(s)", 26, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.add(title)

        col_w = 3.4
        xs = [-1.5 * col_w, -0.5 * col_w, 0.5 * col_w, 1.5 * col_w]
        geo_scale = 0.8
        comb_gain = 0.42

        for cx, c in zip(xs, CASES):
            (sl, kl, pl, tl), (sr, kr, pr, tr) = build_curve(c["kl"], c["kr"], c["corner"])

            # ---------- 標題 ----------
            head = VGroup(
                T(c["name"], 30, BLUE_, BOLD),
                T(c["title"], 20, INK, BOLD),
            ).arrange(RIGHT, buff=0.18, aligned_edge=DOWN)
            cond = M(c["cond"], 22, MUTED)
            header = VGroup(head, cond).arrange(DOWN, buff=0.12).move_to([cx, 2.75, 0])

            # ---------- 幾何曲線 + 曲率梳 ----------
            all_pts = np.vstack([pl, pr])
            center = (all_pts.max(axis=0) + all_pts.min(axis=0)) / 2

            def to3(p):
                q = (p - center) * geo_scale
                return np.array([cx + q[0], 1.05 + q[1], 0.0])

            curve_grp = VGroup()
            comb_grp = VGroup()
            env_grp = VGroup()
            for (s, k, p, th), col in (((sl, kl, pl, tl), INK), ((sr, kr, pr, tr), BLUE_)):
                curve = VMobject(stroke_color=col, stroke_width=5)
                curve.set_points_smoothly([to3(q) for q in p[::8]] + [to3(p[-1])])
                curve_grp.add(curve)
                # 梳齒畫在曲率中心的反側（凸側）
                tips = []
                for i in range(0, len(s), 16):
                    nrm = np.array([-np.sin(th[i]), np.cos(th[i])])
                    tip = p[i] - nrm * k[i] * comb_gain / geo_scale * 0.9
                    tips.append(tip)
                    if abs(k[i]) > 1e-6:
                        comb_grp.add(Line(to3(p[i]), to3(tip), stroke_color=COMB, stroke_width=1.6))
                nrm = np.array([-np.sin(th[-1]), np.cos(th[-1])])
                tips.append(p[-1] - nrm * k[-1] * comb_gain / geo_scale * 0.9)
                if np.max(np.abs(k)) > 1e-6:
                    env = VMobject(stroke_color=ORANGE_, stroke_width=2.5)
                    env.set_points_as_corners([to3(q) for q in tips])
                    env_grp.add(env)
            # 若左段曲率為 0，包絡線就是曲線本身；G1 時要畫出包絡的「垂直跳躍」
            if c["name"] == "G1":
                p0 = pr[0]
                th0 = tr[0]
                nrm = np.array([-np.sin(th0), np.cos(th0)])
                tip = p0 - nrm * kr[0] * comb_gain / geo_scale * 0.9
                env_grp.add(Line(to3(p0), to3(tip), stroke_color=RED_, stroke_width=3.5))
            if c["name"] == "G0":
                # 兩段在接縫處切線方向不同
                p0 = to3(np.zeros(2))
                t_l = to3(np.array([np.cos(tl[-1]), np.sin(tl[-1])]) * 0.55) - p0
                t_r = to3(np.array([np.cos(tr[0]), np.sin(tr[0])]) * 0.55) - p0
                env_grp.add(Arrow(p0, p0 + t_l * 1.4, buff=0, stroke_width=3, color=RED_,
                                  max_tip_length_to_length_ratio=0.18))
                env_grp.add(Arrow(p0, p0 + t_r * 1.4, buff=0, stroke_width=3, color=RED_,
                                  max_tip_length_to_length_ratio=0.18))
                arc = Angle(Line(p0, p0 + t_l), Line(p0, p0 + t_r), radius=0.45, color=RED_)
                env_grp.add(arc)

            joint = Dot(to3(np.zeros(2)), radius=0.06, color=RED_)

            # ---------- κ(s) 圖 ----------
            ax = Axes(
                x_range=[-L, L, L], y_range=[0, 2.1, 0.7],
                x_length=2.9, y_length=1.55,
                axis_config=dict(color=MUTED, stroke_width=2, include_ticks=False,
                                 tip_width=0.14, tip_height=0.14),
            ).move_to([cx, -1.6, 0])
            xl = M("s", 26, MUTED).next_to(ax.x_axis.get_end(), DOWN, buff=0.08)
            yl = M("κ", 28, MUTED).next_to(ax.y_axis.get_end(), LEFT, buff=0.08)
            seam = DashedLine(ax.c2p(0, 0), ax.c2p(0, 2.0), color=MUTED, stroke_width=1.5, dash_length=0.06)

            g_l = ax.plot(lambda s: float(c["kl"](np.array(s))), x_range=[-L, 0], color=INK, stroke_width=4)
            g_r = ax.plot(lambda s: float(c["kr"](np.array(s))), x_range=[0, L * 0.999],
                          color=BLUE_, stroke_width=4)
            extras = VGroup()
            if c["name"] == "G0":
                extras.add(Arrow(ax.c2p(0, 0.25), ax.c2p(0, 2.0), buff=0, color=RED_, stroke_width=4,
                                 max_tip_length_to_length_ratio=0.15))
                extras.add(M("δ", 28, RED_).next_to(ax.c2p(0, 1.5), RIGHT, buff=0.08))
            elif c["name"] == "G1":
                extras.add(Line(ax.c2p(0, 0), ax.c2p(0, 1.0), color=RED_, stroke_width=4))
                extras.add(Dot(ax.c2p(0, 0), radius=0.05, color=RED_), Dot(ax.c2p(0, 1.0), radius=0.05, color=RED_))
            elif c["name"] == "G2":
                extras.add(Dot(ax.c2p(0, 0), radius=0.07, color=RED_))
            else:
                extras.add(Dot(ax.c2p(0, 0), radius=0.07, color=GREEN_))

            note = T(c["note"], 17, INK).next_to(ax, DOWN, buff=0.28)
            if note.width > col_w - 0.2:
                note.scale_to_fit_width(col_w - 0.2)

            self.add(header, comb_grp, curve_grp, env_grp, joint, ax, xl, yl, seam, g_l, g_r, extras, note)

        # 欄位分隔線
        for x in (-col_w, 0, col_w):
            self.add(Line([x, 2.95, 0], [x, -3.45, 0], color="#DEE2E6", stroke_width=1.5))

        items = [
            (Line(ORIGIN, RIGHT * 0.45, color=COMB, stroke_width=3), "梳齒（長度 ∝ 曲率 1/R）"),
            (Line(ORIGIN, RIGHT * 0.45, color=ORANGE_, stroke_width=3), "梳形包絡線"),
            (Dot(radius=0.07, color=RED_), "接縫處不連續"),
            (Dot(radius=0.07, color=GREEN_), "接縫處連續"),
        ]
        legend = VGroup(*[VGroup(icon, T(lbl, 16, MUTED)).arrange(RIGHT, buff=0.12) for icon, lbl in items])
        legend.arrange(RIGHT, buff=0.6).to_edge(DOWN, buff=0.2)
        self.add(legend)