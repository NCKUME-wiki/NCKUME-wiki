pagetime: 2025/02/01
title: 電腦輔助製造 (CAM) 核心原理與數控加工架構
author: NCKUME Wiki Team

【電腦輔助製造(Computer-Aided Manufacturing, CAM)】是指運用專用軟體系統，讀取 3D CAD 實體幾何資訊，依據選定之工具機運動學特性、切削刀具規格與工裝夾持條件，規劃刀具切削路徑（Toolpath Generation），並透過後處理器（Post-Processor）將軌跡資料轉換為數值控制（CNC）工具機能夠解譯執行的 NC 程式碼（G-Code / M-Code）。

---

## 1. 常見 CAM 軟體特性比較與生態定位 (Comparison of Major CAM Software)

在數控加工與機械製造領域中，CAM 軟體的選擇與上游 CAD 幾何系統架構高度相依。為確保設計模型至數控刀具路徑之連續性與一致性，CAM 系統主要分為兩大體系：
1. **主流 CAD 整合 / 原生型 CAM 系統**：順序嚴格對應 [CAD 軟體架構排行](file:///C:/projects/NCKUME-wiki/docs/computer-aided/CAD.md)，具備特徵關聯連動（Associative Toolpath）優勢。
2. **產業界獨立跨平台專用 CAM 系統**：廣泛佈署於加工廠現場，專注於極致多軸加工策略、多通道車銑複合與跨格式中性幾何（STEP / Parasolid）處理。

### A. 主流 CAD 整合型 CAM 系統 (與 CAD 體系呼應)

依據大專院校與產業界 [CAD 軟體排行](file:///C:/projects/NCKUME-wiki/docs/computer-aided/CAD.md)（SolidWorks $\to$ Siemens NX $\to$ PTC Creo $\to$ Autodesk $\to$ CATIA）對應排列：

| 排名與系統名稱 | 對應 CAD 生態 | 開發商 | 幾何核心 / 整合架構 | 核心製造領域與技術特點 |
| :--- | :--- | :--- | :--- | :--- |
| **1. SolidCAM / CAMWorks** | **SolidWorks** (第 1 位) | SolidCAM Ltd. / HCL | 深度嵌入 SolidWorks | 大專院校與一般機械加工廠最普及之嵌入式 CAM。專利 **iMachining** 技術依工件材料物理剪切強度與瞬時刀具包角，全自動動態調整進給與轉速，大幅延長刀具壽命並縮短粗銑週期。 |
| **2. Siemens NX CAM** | **Siemens NX** (第 2 位) | Siemens Digital Industries | 原生 Parasolid 完全整合 | 大專進階數控與高端工業標準。專攻航太發動機葉盤、機匣、汽車傳動大型模具；支援頂尖 5 軸聯動流線刀軸控制、車銑複合（Mill-Turn）及全工具機數位雙生（Digital Twin）模擬。 |
| **3. PTC Creo Manufacturing** | **PTC Creo** (第 3 位) | PTC | 原生 Granite 完全整合 | 傳統機構件、3C 模具與重工設備加工。設計幾何與加工工藝模型完全同步，支援特徵識別加工（Feature-Based Machining），設計變更時 NC 刀軌全自動無縫再生。 |
| **4. Autodesk Fusion 360 / Inventor CAM** | **Autodesk Inventor / Fusion 360** (第 4, 5 位) | Autodesk | 原生內建 HSMWorks 核心 | 大專專題實作、創客打樣與平價 3~5 軸機台普及率最高。內建專利**自適應清除 (Adaptive Clearing)**，雲端協同版本控管，跨平台授權靈活。 |
| **5. CATIA Machining (DELMIA)** | **CATIA** (第 6 位) | Dassault Systèmes | 原生 CGM 完全整合 | 民航客機結構件（機翼樑肋、發動機吊艙）與汽車車身覆蓋件沖壓模。專精數萬道刀軌之大型工藝流程管理與航太複材鋪層切削。 |

### B. 產業界獨立跨平台專用 CAM 系統 (Dedicated Multi-CAD Suites)

專注於車間多品牌 CAD 格式讀取（透過 STEP AP242 或 Parasolid 原生檔）、特定工藝（極致高速銑、深孔窄槽五軸、車銑複合走心機）：

| 軟體名稱 | 開發商 | 平台架構 | 工業地位與核心技術優勢 |
| :--- | :--- | :--- | :--- |
| **Mastercam** | CNC Software | 獨立平台 (亦支援嵌入 SW) | **機械加工廠普及度第一**。技職與大專機工實習採用率最高；具備全球最大之後處理器（Post-Processor）庫、成熟 2D/3D 銑削、四軸/五軸、車削及專利**動態運動 (Dynamic Motion)** 軌跡技術。 |
| **Autodesk PowerMill** | Autodesk | 獨立平台 (原 Delcam) | **模具與高速銑削 (HSM) 工業標準**。專精於淬硬鋼大型模具、汽車沖模與葉片表面加工；具備極致之流線多軸精加工演算法與嚴密的刀具/夾頭/機台動態防碰撞避讓運算。 |
| **OPEN MIND HyperMILL** | OPEN MIND Technologies | 獨立平台 / 支援外掛 | **頂級 5 軸專用加工標竿**。專精航太整體葉輪（Impeller/Blisk）與渦輪機械；具備專利錐度螺旋銑削、自適應深槽粗銑與無接縫曲面過渡演算法。 |
| **Hexagon ESPRIT / GibbsCAM** | Hexagon / Cambrio | 獨立平台 | **多通道車銑複合與走心機 (Swiss-Type) 專精**。支援多主軸、多刀塔同動切削同期化同步控制（Synchronization），廣泛應用於醫療微型植入物與精密鐘錶軸件車銑。 |

---

## 2. 坐標系設定與加工工藝準備 (Setup & Coordinate Systems)

CAM 程式規劃的第一步是定義幾何邊界與運動參考系。

### 工件坐標系 (Work Coordinate System, WCS)
* **定義**：建立工具機加工的原點（即 CNC 程式中的 `G54` ~ `G59` 零點）。
* **設定原則**：
  * **原點選擇**：應與零件圖面的主要定位基準（Datum A, B, C）對齊，或設定在毛坯的幾何中心點、加工頂面或分度旋轉中心。
  * **對刀可達性**：原點應配置於操作者容易使用尋邊器（Edge Finder）、光學探針（Touch Probe）或對刀儀精確接觸測量之位置。

### 毛坯定義 (Stock Definition)
* 毛坯為材料切削前的初始體積。CAM 軟體依據毛坯與目標零件實體比對，計算「材料移除體積（Material to be removed）」。
* **形態**：
  * 矩形包絡塊（Bounding Box）：常用於板件、塊狀件切削。
  * 圓柱體（Cylinder）：常用於旋轉對稱車削件。
  * 3D 前道工序殘料模型（In-Process Stock, IPW）：讀取上一道加工或鑄造、鍛造之實體模型，避免空刀（Air Cut）。

### 安全幾何高度 (Clearance & Retract Planes)
* **安全平面 (Clearance Plane)**：刀具快速移動（`G00`）時的安全高度，必須高於工件最高點與所有夾具（如虎鉗爪、壓板壓塊）。
* **退刀平面 (Retract Plane)**：各切削切面之間的短距離快速抬刀高度。
* **進刀平面 (Feed Height)**：刀具自快速定位速度（`G00`）切換為切削進給速度（`G01`）之臨界高度（通常為零件表面上方 $1 \sim 3\text{ mm}$）。

---

## 3. 切削物理參數與數學公式 (Machining Physics & Formulas)

數控切削之材料移除率、刀具壽命與工件表面粗糙度受切削三要素決定：

### A. 切削速度與主軸轉速
切削速度 $V_c$（線速度）指刀具切削刃相對於工件表面切削點的瞬時速度：

$$
V_c = \frac{\pi \cdot D \cdot N}{1000} \quad [\text{m/min}]
$$

相應的主軸轉速 $N$ 計算公式為：

$$
N = \frac{1000 \cdot V_c}{\pi \cdot D} \quad [\text{rpm}]
$$

其中：
* $D$ 為刀具公稱直徑 $[\text{mm}]$。
* $V_c$ 依工件材料與刀具塗層查表選定（如鋁合金切削碳化鎢刀具 $V_c \approx 300 \sim 800\text{ m/min}$；不鏽鋼 $V_c \approx 80 \sim 150\text{ m/min}$）。

### B. 進給率與每刃進給量
工作台直線進給速度 $F$ 定義為：

$$
F = N \cdot z \cdot f_z \quad [\text{mm/min}]
$$

其中：
* $z$ 為刀具切削有效刃數（Flutes）。
* $f_z$ 為每刃進給量（Feed per tooth / Chipload）$[\text{mm/tooth}]$。

### C. 切削截面與材料移除率 (MRR)
材料移除率（Material Removal Rate, MRR）表示單位時間內切除之金屬體積：

$$
\text{MRR} = a_p \cdot a_e \cdot F \times 10^{-3} \quad [\text{cm}^3\text{/min}]
$$

其中：
* $a_p$ 為軸向切深（Axial Depth of Cut）$[\text{mm}]$。
* $a_e$ 為徑向切寬 / 步距（Radial Depth of Cut / Stepover）$[\text{mm}]$。

### D. 表面殘留高度 (Scallop Height) 與粗糙度
球刀（Ball End Mill）於曲面精加工時，兩相鄰切削軌跡步距 $s$ 會在工件表面留下圓弧殘脊。殘留高度 $h$ 與步距 $s$ 及球刀半徑 $R$ 之幾何關係為：

$$
h = R - \sqrt{R^2 - \left(\frac{s}{2}\right)^2} \approx \frac{s^2}{8R} \quad [\text{mm}]
$$

理論表面粗糙度 $Ra$ 約為 $h / 4$。此式證明：縮小步距 $s$ 或增大刀具半徑 $R$ 能顯著降低表面粗糙度。

---

## 4. 切削加工策略 (Machining Strategies)

### A. 粗加工策略 (Roughing)
* **傳統等高粗銑 (Cavity / Z-Level Milling)**：於固定 Z 高度平面內依輪廓偏移切削。缺點在於遇到轉角死角時，刀具包角（Engagement Angle）會從設定值驟增至 $180^\circ$，切削阻力暴增易引發崩刃。
* **擺線切削與自適應清除 (Trochoidal Milling / Adaptive Clearing)**：
  * 演算法透過動態曲線運動，恆定控制刀具包角於安全範圍（通常為 $30^\circ \sim 50^\circ$）。
  * 容許使用刀具全刃長進行大軸向切深（$a_p = 1.5 \sim 2.0 D$）、小徑向切寬（$a_e = 0.05 \sim 0.15 D$）高速加工，刀具磨損均勻且切削效率提升 2~4 倍。

### B. 殘料清除策略 (Rest Machining)
* 大直徑粗銑刀無法切入之角落區域，CAM 系統透過動態殘料模型（IPW）自動識別殘留材料，僅指派較小直徑刀具針對未切除區域進行局部切削，避免小刀切入大體積實體產生滿刀負荷。

### C. 精加工策略 (Finishing)
* **分區切削原則（Steep and Shallow）**：
  * **陡峭區域（坡度角 $\ge 45^\circ$）**：採用**等高切削（Contour / Z-Level）**，刀具沿水平等高線環切，法向切深均勻。
  * **淺平區域（坡度角 $< 45^\circ$）**：若採用等高切削會產生過大步距殘脊，應切換為**平行往復切削（Raster）**或 **3D 等距環繞切削（Constant Scallop）**。
* **順銑 vs. 逆銑 (Climb vs. Conventional Milling)**：
  * **順銑（Climb）**：切削厚度由厚至薄，切削力向下壓向工作台，工件震動小且表面硬化現象低，為 CNC 加工之絕對優先標準。
  * **逆銑（Conventional）**：切削厚度由零遞增至厚，刀刃在初期滑移摩擦，加速刀具後刀面磨損，僅在工件表面存在硬化鑄皮/氧化層時特殊採用。

---

## 5. 多軸數控加工技術 (Multi-Axis Machining)

| 加工型態 | 自由度配置 | 刀軸控制特點 | 典型適用工件 |
| :--- | :--- | :--- | :--- |
| **3 軸加工** | X, Y, Z 線性軸 | 刀軸固定垂直於工作台 ($+Z$) | 簡易板類、箱體頂面特徵、無倒勾特徵件。 |
| **3+2 定位加工** (Positional 5-Axis) | 3 線性軸 + 2 旋轉軸傾斜定位 | 旋轉軸傾斜固定角度後鎖定，以 3 軸方式切削 | 多面體箱體、具傾角之斜孔/斜槽、深腔避空。 |
| **5 軸連續聯動** (Simultaneous 5-Axis) | 5 軸即時同步插補 | 刀軸方向於切削過程中動態連續變更 | 航太閉式葉輪（Impeller）、渦輪葉片、底切曲面。 |

### 3+2 定位加工的工程優勢
* 透過擺角使切削表面正對主軸，允許使用短刃高剛性刀具切削深型腔，大幅降低長懸臂銑削之震顫，其加工效率與表面精度往往高於連續五軸聯動。

### 5 軸聯動切削點規避（避開零切速點）
* 球刀（Ball Mill）頂端旋轉中心之線速度為零（$V_c = 0$）。若採 3 軸垂直切削平坦表面，球刀中心僅以摩擦擠壓材料而非切削，表面粗糙度極差。
* 5 軸聯動可設定**前傾角（Lead Angle, $10^\circ \sim 15^\circ$）**與**側傾角（Tilt Angle）**，使切削接觸點偏移至球刃切速正常之有效半徑區域，大幅提升表面加工光潔度。

### 旋轉刀具中心點控制 (RTCP / Tool Center Point Control)
* 在多軸機台中，旋轉軸擺動會導致刀尖空間座標產生幾何偏移。
* 傳統機台需將擺長與中心偏置寫入後處理；現代控制器（如 Fanuc `G43.4`、Heidenhain `M128`、Siemens `TRAORI`）具備 RTCP 功能，即時補償旋轉軸幾何非線性偏移，確保編程之刀尖空間位置與進給向量恆定。

---

## 6. 後處理與 G 代碼系統 (Post-Processing & NC Code)

後處理器（Post-Processor）是連結 CAM 幾何軟體與工具機硬體的編譯器。

```
[CAD 3D 實體模型]
       ↓
[CAM 軟體計算刀具路徑] → 內部路徑中繼檔 (CLDATA / APT: 記錄純幾何座標 X, Y, Z, I, J, K)
       ↓
[專用機台後處理器]       → 依據機台運動學、控制器代碼語法與加減速限制轉譯
       ↓
[NC 程式碼 (G-Code)]    → 傳輸至工具機控制器 (Fanuc, Heidenhain, Siemens, Haas)
```

### 常用標準數控指令速查

| 代碼 | 功能定義 | 說明與注意事項 |
| :--- | :--- | :--- |
| `G00` | 快速點定位 (Rapid Traverse) | 非切削進給，各軸以機台最大速率移動，禁止用於接觸工件。 |
| `G01` | 直線插補 (Linear Interpolation) | 依設定進給率 $F$ 進行直線切削移動。 |
| `G02` / `G03` | 圓弧插補 (順時針 / 逆時針) | 以半徑 $R$ 或圓心增量向量 $I, J, K$ 定義圓弧路徑。 |
| `G17` / `G18` / `G19` | 工作平面選擇 (XY / ZX / YZ) | 指定圓弧插補與刀具半徑補正之基準平面。 |
| `G40` / `G41` / `G42` | 刀具半徑補正 (取消 / 左偏 / 右偏) | 補償刀具實體直徑與磨損，路徑以工件實際輪廓編程。 |
| `G43` / `G49` | 刀具長度補正 (啟用 / 取消) | 讀取刀長補正暫存器（`H` 代碼），將刀尖對齊工件座標系。 |
| `G54` ~ `G59` | 工件座標系選擇 1 ~ 6 | 呼叫機台內部設定之工件基準原點。 |
| `M03` / `M04` / `M05` | 主軸運轉 (順時針轉 / 逆時針轉 / 停止) | 搭配 `S` 參數指定轉速（如 `M03 S3000`）。 |
| `M06` | 自動換刀 (Automatic Tool Change) | 搭配 `T` 參數呼叫刀套（如 `T02 M06`）。 |
| `M08` / `M09` | 切削液冷卻 (開啟 / 關閉) | 啟用主軸外噴或高壓主軸中心出水（CTS）。 |
| `M30` | 程式結束並重置回起點 | 停止主軸、關閉冷卻液並準備進行下一循環。 |

---

## 7. 模擬驗證與防碰撞分析 (Simulation & Verification)

在實際將 NC 程式傳送至實體機台切削前，必須執行嚴密之模擬流程以防範撞機與零件報廢：

1. **軌跡路徑驗證 (Toolpath Simulation)**：檢視刀尖與切削線框軌跡是否平滑，確認進退刀（Lead-in / Lead-out）向量無突異轉折。
2. **體素材料切除模擬 (Material Removal Simulation)**：比對切削後實體與原始 CAD 模型之幾何公差差值，以彩色雲圖檢驗「過切（Gouge）」與「欠切/殘料（Excess/Under-cut）」。
3. **全工具機動態防碰撞模擬 (Machine Simulation / Digital Twin)**：
   * 載入工具機床身、主軸頭、工作台與治具實體幾何。
   * 檢測項目：
     * 主軸外殼、刀桿夾頭（Tool Holder）與虎鉗/夾具之空間碰撞。
     * 旋轉軸與線性軸之行程極限超程（Soft Limit Over-travel）。
     * 5 軸運動學奇異點（Singularity）：當刀軸與旋轉軸平行時，旋轉軸角度瞬時劇烈旋轉引發過切。

---

## 8. 延伸閱讀與跨領域對接

* [電腦輔助設計 (CAD) 核心原理](file:///C:/projects/NCKUME-wiki/docs/computer-aided/CAD.md)：標準機械實體參數化建模、主模型架構與大型裝配體管理。
* [3D 建模幾何典範與專用軟體架構](file:///C:/projects/NCKUME-wiki/docs/computer-aided/modeling.md)：實體 B-Rep、NURBS 自由曲面與多邊形網格（SubD）幾何典範比較。
* [為製造而設計 (DFM)](file:///C:/projects/NCKUME-wiki/docs/design/dfm.md)：機械切削、注塑成型與鈑金加工之尺寸與幾何設計限制。
