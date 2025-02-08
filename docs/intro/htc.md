在文章開始之前，**NCKUME wiki** 專案組全體成員十分歡迎您為本專案貢獻頁面。正因為有了上百位像您一樣的人，才有了 **NCKUME wiki** 的今天！

這篇文章將主要敘述參與 **NCKUME wiki** 編寫的寫作過程。請您在撰稿或者修正 Wiki 頁面以前，仔細閱讀以下內容，以説明您完成更高品質的內容。

## 貢獻指南

請您在編輯前查看 [NCKUME wiki 貢獻指南](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/.github/CONTRIBUTING.md) 和 [專案方針](./about.md#項目方針)，以更好地和社區貢獻者進行合作、交流。

## 參與協作

???+ warning
    在開始編寫一段內容之前，請查閱 [Issues](https://github.com/NCKUME-wiki/NCKUME-wiki/issues)，確認沒有別人在做相同的工作之後，開個 [新 issue](https://github.com/NCKUME-wiki/NCKUME-wiki/issues/new) 記錄待編寫的內容。

???+ tip
    在 Issues 中也有很多待修復/解決的問題，尤其是我們的反覆運算計畫（Iteration Plan）。從這裡獲取任務是一個很好的開始！

為了保證條目內容的專業性和準確性，我們建議您在編輯前先考慮以下幾點：

1.  **選擇您熟悉的領域**：請優先編輯那些與您的專業知識、學習背景或興趣愛好相關的條目。這有助於您創作出高品質的內容。
2.  **謹慎對待新領域**：如果您對某個主題還處於初學階段或不太瞭解，建議您先通過閱讀、學習加深理解，待有一定把握後再動手編輯。
3.  **查閱相關資料**：為條目添加內容或進行修訂時，建議您先查閱權威文獻和資料，確保資訊準確無誤。也歡迎您在頁面評論區或我們的社區提出問題，與其他編者交流討論。

我們珍惜每位貢獻者的熱情和付出，也理解大家的專業水準不盡相同。讓我們攜手合作，共同呵護這個知識的樂園，用準確、專業的內容去説明更多讀者。期待您的貢獻！在這裡引用維基百科的一句話：

> 不要害怕編輯，勇於更新頁面！[^ref1]

### 在 GitHub 上編輯

參與 **NCKUME wiki** 的編寫 **需要** 一個 GitHub 帳號（可以前往 [GitHub 的帳號註冊頁面](https://github.com/signup) 頁面註冊），但 **不需要** 高超的 GitHub 技巧，即使你是一名新手，只要按照下面所述的步驟操作，也能夠 **非常出色** 地完成編輯。

???+ tip
    在你的更改被合併到 **NCKUME wiki** 的主倉庫之前，你對 **NCKUME wiki** 的內容所作出的修改均不會出現在 **NCKUME wiki** 的主站上，所以無需擔心你的修改會破壞 **NCKUME wiki** 上正在顯示的內容。
    
    如果還是不放心，可以查看 [GitHub 的官方教程](https://skills.github.com/)。

#### 編輯單個頁面內的內容

1.  在 **NCKUME wiki** 上找到對應頁面；
2.  點擊正文右上方（目錄左側）的 **「編輯此頁」**（<i class="md-icon">edit</i>）按鈕，在確認您已經閱讀了本頁面和 [格式手冊](./format.md) 後點擊按鈕根據提示跳轉到 GitHub 進行編輯；
3.  在編輯方塊內編寫你想修改的內容。請注意，在修改和接下來的提交過程中，請 **關閉您的自動翻譯軟體**，因為它可能產生不必要的麻煩（例如您修改的檔有時會被其錯誤改名，從而影響目錄結構）；
4.  編寫完成後滾動到頁面下方，按照本文中 [commit 資訊格式規範](#commit-資訊格式規範) 填寫 commit 資訊，之後點擊 **Propose changes** 按鈕提交修改。點擊按鈕後，GitHub 會自動幫你創建一份 **NCKUME wiki** 倉庫的分支，並將你的提交添加到這個分支倉庫。
5.  GitHub 會自動跳轉到你的分支倉庫的頁面，此時頁面上方會顯示一個綠色的 **Create pull request** 按鈕，點擊後 GitHub 會跳轉到一個創建 Pull Request 頁面。向下滾動檢查自己所作出的修改沒有錯誤後，按照本文中 [Pull Request 資訊格式規範](#pull-request-資訊格式規範) 一節中的規範書寫 Pull Request 資訊，然後點擊頁面上的綠色的 **Create pull request** 按鈕創建 Pull Request。
6.  不出意外的話，你的 Pull Request 就順利提交到倉庫，等待管理員審核併合並到主倉庫中即可。

在等待合併的時間裡，你可以給他人的 Pull Request 提意見、點贊或者點踩。如果有新消息，會在網頁右上角出現提示，並附有郵件提醒（取決於個人設置中配置的通知方式）。

#### 編輯多個頁面內的內容

如果你需要同時編輯互相無關聯的多個頁面的內容，請按照上方的 [編輯單個頁面內的內容](#編輯單個頁面內的內容) 一節一次修改所有頁面。

1.  打開 [NCKUME-wiki/NCKUME-wiki](https://github.com/NCKUME-wiki/NCKUME-wiki) 倉庫，點擊鍵盤上的<kbd>.</kbd>按鈕（或者將 URL 中的 `github.com` 更改為 `github.dev`）[^ref2]，進入 GitHub 的網頁版 VS Code 編輯器；
2.  在編輯器中作出對頁面原始檔案的更改，可以使用頁面右上方的預覽按鈕（或按下<kbd>Ctrl+K</kbd><kbd>V</kbd>快速鍵）在右側打開預覽介面；
3.  修改完成後使用左側的 Source Control 選項卡，並按照本文中 [commit 資訊格式規範](#commit-資訊格式規範) 填寫 commit 資訊並提交，提交時會提示是否創建此倉庫的分支，點擊綠色的 **Fork Repository** 按鈕即可。
4.  提交後會在網頁上方的中央彈出一個提示框，在第一次的提示框內填寫標題，第二次的提示框內填寫此提交要提交到的倉庫內分支名稱，之後右下角會彈出一個提示框，內容類別似於 `Created Pull Request #1 for NCKUME-wiki/NCKUME-wiki.`，點擊藍字連結即可查看該 Pull Request。

#### 向 Pull Request 追加更改

1.  打開 [NCKUME-wiki 的 Pull Request 列表](https://github.com/NCKUME-wiki/NCKUME-wiki/pulls)，找到您提交的 Pull Request 並點擊。
2.  Pull Request 頁面的標題下方將會有一段例如 `<您的ID> wants to merge x commits into NCKUME-wiki:master from <您的ID>:patch-1` 的文字，點擊 `<您的ID>:patch-1` 部分。
3.  您應該會被重定向到您的分支倉庫中，而且檔清單左上角的分支名稱是你提交 Pull Request 的分支名稱（在本示例中應為 `patch-1`）。
4.  進行您需要的更改。
    -   如果您需要編輯單個檔或多個互相無關聯的頁面的內容，請直接找到你要的檔並進行更改，更改完成後滾動到頁面下方，按照本文中 [commit 資訊格式規範](#commit-資訊格式規範) 填寫 commit 資訊，之後點擊 **Commit changes** 按鈕提交修改。
    -   如果您需要編輯多個檔，點擊鍵盤上的<kbd>.</kbd>按鈕（或者將 URL 中的 `github.com` 更改為 `github.dev`）[^ref2]，進入 GitHub 的網頁版 VS Code 編輯器並作出更改。然後使用左側的 Source Control 選項卡，並按照本文中 [commit 資訊格式規範](#commit-資訊格式規範) 填寫 commit 資訊並提交修改。
5.  這時你的更改會被自動追加在您的 Pull Request 中。

### 使用 Git 在本地進行編輯

???+ warning
    對於一般用戶，我們更推薦使用上方所述的 GitHub 的 Web 編輯器進行編輯。

雖然大多數情況下您可以直接在 GitHub 上進行編輯，但對於一些較為特殊的情況（如需要使用 GPG 簽名），我們更推薦使用 Git 在本地進行編輯。

大致流程如下：

1.  將主倉庫 Fork 到自己的倉庫中；
2.  將 Fork 後的分支倉庫克隆（clone）到本地；
3.  在本地進行修改後提交（commit）這些更改；
4.  將這些更改推送（push）到你克隆的分支倉庫；
5.  提交 Pull Request 至主倉庫。

詳細的操作方式可以參考 [Git](../tools/git.md) 頁面。

#### 向 Pull Request 追加更改

在 clone 下來的本地分支倉庫中繼續進行修改，並提交（commit）以及推送（push）這些更改即可。你的更改會被自動追加在 Pull Request 中。

### 在構建的網頁中預覽變更

在 Pull Request 頁面下方可以找到測試頁面，點擊 netlify/NCKUME-wiki/deploy-preview 一項的 Details 連結（如下圖），可以進入自動構建的，由您變更後的頁面供您預覽。

![deploy\_preview](./images/deploy_preview.png)

### 對於目錄和引用的變更

通常情況下，如果您需要添加一個新頁面，或者修改已有頁面在目錄中的連結，您就需要對 [`mkdocs.yml`](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/mkdocs.yml) 檔作出改動。

添加新頁面可以參考既有的格式。但除非是進行重構或修正名詞，否則 **我們不建議對既有頁面的引用連結進行修改**，Pull Requests 中不必要的修改也將被駁回。

如果您堅持要修改連結，請注意更新 author 欄位和重定向檔。

### author 欄位

GitHub API 在檔目錄變更後不能跟蹤統計，所以我們在檔頭手動維護了一個作者列表來解決這個問題。author 欄位位於整個 Markdown 文件的開頭，形如 `author: Ir1d, cjsoft`，相鄰兩個 ID 之間用逗號加空格隔開。這裡的 ID 是 GitHub 的用戶名，即 GitHub profile 的地址（例如 <https://github.com/Ir1d> 中的 `Ir1d`）。

修改連結時，需要將當前頁面中的 contributors 逐一填入 author 欄位。

### 重定向文件

在修改連結時，為了避免在站外引用時出現死鏈，需要修改重定向檔。

[`_redirects`](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/docs/_redirects) 檔用於生成 [netlify 的配置](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file) 和 [用於跳轉的文件](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/scripts/gen_redirect.py)。

每一行表示一個重定向規則，分別寫跳轉的起點和終點的 url（不包含功能變數名稱）：

```text
/path/to/src /path/to/desc
```

注：所有跳轉均為 301 跳轉，只有在修改目錄中 url 造成死鏈的時候需要修改。

### Commit 資訊格式規範

對於提交時需要填寫的 commit 資訊，請遵守以下幾點基本要求：

1.  commit 摘要請簡要描述這一次 commit 改動的內容。注意 commit 摘要的長度不要超過 50 字元，超出的部分會自動置於正文中。
2.  如果需要進一步描述本次 commit 內容，請在正文中詳細說明。

對於 commit 摘要，推薦按照如下格式書寫：

```text
<修改類型>(<檔案名>): <修改的內容>
```

修改類型分為如下幾類：

-   `feat`：用於添加內容的情況。
-   `fix`：用於修正現有內容錯誤的情況。
-   `refactor`：用於對一個頁面進行重構（較大規模的更改）的情況。
-   `revert`：用於回退之前更改的情況。

### Pull Request 資訊格式規範

對於 Pull Request，請遵守以下幾點要求：

1.  標題請寫明本次 PR 的目的（做了 **什麼** 工作，修復了 **什麼** 問題）。
2.  內容請簡要敘述修改的內容。如果修復了一個 issue 的問題，請在內容中添加 `fix #xxxx` 欄位，其中 `xxxx` 代表 issue 的編號。
3.  請您仔細閱讀 [貢獻指南](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/.github/CONTRIBUTING.md) 和 [社區公約](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/CODE_OF_CONDUCT.md)，並在同意後勾選 PR 範本中的框，表示您同意了以上指南和公約。

對於 Pull Request 的標題，推薦使用如下格式書寫：

```plain
<修改類型>(<檔案名>): <修改的內容> (<對應 issue 的編號>)
```

修改類型分為如下幾類：

-   `feat`：用於添加內容的情況。
-   `fix`：用於修正現有內容錯誤的情況。
-   `refactor`：用於對一個頁面進行重構（較大規模的更改）的情況。
-   `revert`：用於回退之前更改的情況。

示例：

-   `fix(ds/persistent-seg): 修改代碼注釋使描述更清晰`
-   `fix: tools/judger/index 不在目錄中 (#3709)`
-   `feat(math/poly/fft): better proof`
-   `refactor(ds/stack): 整理頁面內容`

### 協作流程

1.  在收到一個新的 Pull Request 之後，GitHub 會給 reviewer 發送郵件；
2.  與此同時，在 [GitHub Actions](https://github.com/NCKUME-wiki/NCKUME-wiki/actions) 和 [Netlify](https://app.netlify.com/sites/NCKUME-wiki) 上會運行兩組測試，它們會把進度同步在 PR 頁面的下方。GitHub Actions 主要用來確認 PR 中內容的修改不會影響到網站構建的進程；Netlify 用來把 PR 中的更新構建出來，方便 reviewer 審核（在測試完成後點擊 Details 可以瞭解更多）；
3.  reviewer 可能會發現問題，並提出 `review` 或 `suggested changes`（建議更改，顯示為灰色圖示）/`requested changes`（強制更改，顯示為紅色圖示，只會在 reviewer 擁有 repo 寫許可權時出現）。一般來說，reviewer 也會附上建議和需要進行的更改，在這時，您將會需要繼續向 Pull Request 追加其他更改。更改的方法可以參考 `在 GitHub 上編輯` 或者 `使用 Git 在本地進行編輯` 部分的 `向 Pull Request 追加更改` 部分。
4.  在足夠多 reviewer 投票通過一個 PR 之後，這個 PR 才可以合併到 master 分支中；
5.  在合併到 master 分支之後，GitHub Actions 會重新構建一遍網站內容，並更新到 gh-pages 分支；
6.  這時伺服器才會拉取 gh-pages 分支的更新，並重新部署最新版本的內容。

## 參考資料與注釋

[^ref1]: [維基百科：新手入門/編輯](https://zh.wikipedia.org/wiki/Wikipedia:%E6%96%B0%E6%89%8B%E5%85%A5%E9%96%80/%E7%B7%A8%E8%BC%AF)

[^ref2]: [Web-based editor - GitHub Codespaces - GitHub Docs](https://docs.github.com/en/codespaces/developing-in-codespaces/web-based-editor)


