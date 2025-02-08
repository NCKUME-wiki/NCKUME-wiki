title: 
author: NCKUME wiki Team

在工程上的公式通常結構簡單、重複性高且每一個符號都有特定物理意義，問題是**形式相當自由**。各品牌的教科書使用的符號或多或少有所不同，進一步導致更換學習資源或交換知識的成本提高。

為提升編輯速度與交換性，我們建議使用`\newcommand`來為符號取名。

雖然此種方法違背了Markdown簡潔易讀的初衷，但團隊相信使用`\pdev{f}{x}`取代`\frac{\partial{}f}{\partial{}x}`是值得的。

## 



## newcommand語法




## 預定義newcommand列表

### 使用方式



## 即時預覽編輯方式

由於數學公式是在前端渲染，加之預定義檔案在其他資料夾，github或markdown編輯器無法直接轉換。我們推薦[Overleaf](https://www.overleaf.com/)等互動式Latex[^note1]編輯器，將[tex文件夾](https://github.com/NCKUME-wiki/NCKUME-wiki/tree/main/tex)作為project file上傳即可視覺化編輯。




[^note1]: 數學公式是用Mathjax不是純Latex，見 [格式手冊](../format/#對數學公式的附加格式要求)