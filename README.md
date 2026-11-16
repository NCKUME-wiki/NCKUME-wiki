# NCKUME Wiki

[![Build and Test](https://github.com/NCKUME-wiki/NCKUME-wiki/actions/workflows/test.yml/badge.svg)](https://github.com/NCKUME-wiki/NCKUME-wiki/actions)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

> **NCKUME Wiki** 致力於成為一個開放、嚴謹且持續更新的 **機械工程（Mechanical Engineering）** 知識整合平台。

網站注重核心觀念與實際工程問題的連結，梳理涵蓋**四大力學、工程數學、熱流科學、機電整合、控制工程、機械設計與製造**等領域的知識體系，協助學習者快速建立全貌並深入掌握工程專業。

---

## 本地端開發與預覽

本專案使用基於 Python 的 [MkDocs](https://www.mkdocs.org/) 與 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主題建置靜態網站。

### 環境需求

- Python 3.10 或更高版本
- Node.js (用於部分腳本檢查與格式化工具)
- Yarn 或 npm

### 快速開始

1. **複製儲存庫：**
   ```bash
   git clone https://github.com/NCKUME-wiki/NCKUME-wiki.git
   cd NCKUME-wiki
   ```

2. **建立並啟用 Python 虛擬環境：**
   * Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **安裝依賴套件：**
   ```bash
   pip install -r requirements.txt
   # 若使用 Pipenv:
   # pipenv install
   ```

4. **啟動本機即時預覽伺服器：**
   ```bash
   mkdocs serve
   ```
   啟動後於瀏覽器開啟 `http://127.0.0.1:8000` 即可預覽網站。

5. **建置靜態網站檔案：**
   ```bash
   mkdocs build
   ```
   建置後的靜態網站檔案將輸出於 `site/` 目錄。

---

## 目錄結構說明

```text
NCKUME-wiki/
├── mkdocs.yml              # 網站全域設定檔（導航目錄、外掛程式、主題設定）
├── hooks/                  # MkDocs 建置掛鉤（客製化數學巨集與專有名詞轉換）
├── docs/                   # Markdown 內容檔案
│   ├── index.md            # 首頁
│   ├── intro/              # 專案方針、貢獻手冊、格式規範、FAQ
│   ├── eng-math/           # 工程數學（微積分、線代、ODE、PDE、複分析等）
│   ├── mechanics/          # 工程力學（靜力學、動力學、材力、彈性、塑性）
│   ├── thermo-fluid/       # 熱流科學（熱力學、熱傳學、流體力學、燃燒學）
│   ├── material/           # 材料科學（金屬、陶瓷、聚合物、複合材料等）
│   ├── control/            # 控制理論與機器人學
│   ├── general/            # 總論（工程圖、機動學、振動學、量測）
│   ├── design/             # 機械設計
│   ├── manufacture/        # 機械製造
│   ├── computer-aided/     # 電腦輔助工程 (CAD/CAM/CAE/PLM)
│   ├── oem/                # 光電磁學（光學、電子、電工、機電系統）
│   ├── misc/               # 品質工程、可靠度、SPC、數值方法
│   └── _static/            # 前端 CSS 與 JavaScript 腳本
└── scripts/                # 自動化檢查與 CI 輔助腳本
```

---

## 如何參與貢獻

我們歡迎所有熱愛機械工程與開源協作的朋友一同參與！

* 閱讀 [專案方針與簡介](https://nckume-wiki.org/intro/about/)
* 查閱 [如何參與指南](https://nckume-wiki.org/intro/htc/)
* 遵循 [格式規範手冊](https://nckume-wiki.org/intro/format/)

在撰寫內容前，建議先在 [Issues](https://github.com/NCKUME-wiki/NCKUME-wiki/issues) 開立討論，避免多人重複編輯同一主題。

---

## 授權條款

本專案內容以 [創用 CC 姓名標示-相同方式分享 4.0 國際授權條款 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.zh_TW) 釋出。
程式碼部分遵循相應開源條款。
