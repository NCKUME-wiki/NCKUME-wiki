pagetime: 2025/02/01
title: 工程公式自訂命令 (newcommand)
author: NCKUME wiki Team

在工程領域中，數理公式通常結構明確、重複性高且每個符號都有特定的物理意義，但各家教科書採用的符號與記號習慣往往有所不同，導致學習與交流時需反覆轉換。

為提升編輯速度、維持符號一致性與跨篇章可讀性，我們建議在公式中適度使用 `\newcommand` 巨集。

例如，使用 `\pdev{f}{x}` 取代繁瑣的 `\frac{\partial f}{\partial x}`，能大幅簡化 Markdown 原始碼並減少打字失誤。

## newcommand 語法說明

在 LaTeX / MathJax 中，定義自訂命令的基本語法為：

```latex
\newcommand{\命令名稱}[參數個數]{命令定義}
```

例如偏微分算子：
```latex
\newcommand{\pdev}[2]{\frac{\partial #1}{\partial #2}}
```
使用時只需寫 `\pdev{u}{t}`，即可渲染為 $\frac{\partial u}{\partial t}$。

## 預定義 newcommand 列表

為方便全站通用，NCKUME Wiki 透過建置掛鉤（Hook）支援引用通用工程巨集。在頁面開頭加入：

```markdown
#include<newcommand_math>
```

即可啟用以下預定義巨集：

| 巨集命令 | 渲染效果 | 物理/工程意義 |
| :--- | :--- | :--- |
| `\pdev{f}{x}` | $\frac{\partial f}{\partial x}$ | 偏微分（Partial Derivative） |
| `\youngs` | $E$ | 楊氏模數 / 彈性模數（Young's Modulus） |
| `\secondmomentum` / `\ndM` | $I$ | 截面二次軸矩 / 慣性矩（Area Moment of Inertia） |
| `\deflection` | $\delta$ | 樑變形量 / 撓度（Deflection） |
| `\traction` | $P$ | 集中力 / 負載（Point Load / Traction） |
| `\heatflux` | $q$ | 熱通量（Heat Flux） |
| `\heatrate` | $\dot{q}$ | 熱傳率 / 單位時間熱通量（Heat Rate） |

## 即時預覽編輯方式

由於數學公式是由前端 MathJax 進行渲染，且部分全域自訂命令在 MkDocs 轉換階段動態注入，在一般的純文字編輯器或 GitHub 網頁原生預覽中可能無法即時呈現最終排版。

建議使用本地建置預覽（`mkdocs serve`），或參考專案根目錄下的 [tex 目錄](https://github.com/NCKUME-wiki/NCKUME-wiki/tree/main/tex)，上傳至 [Overleaf](https://www.overleaf.com/) 等專業 LaTeX 編輯器輔助排版與檢視。

## 參考資料與注釋

* 數學公式排版細節請參閱 [格式手冊](./format.md#對數學公式的附加格式要求)。
