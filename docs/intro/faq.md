本頁面主要解答一些常見的問題。

## 我想問點與這個 Wiki 相關的問題

Q：你們是為什麼想要做這個 Wiki 的呢？

A：不知道你在學 **OI** 的時候，面對龐大的知識體系，有沒有感到過迷茫無助的時候？**NCKUME wiki** 想要做的事情可能類似於「讓更多競賽資源不充裕的同學能方便地接觸到訓練資源」。當然這麼表述也不完全，做 Wiki 的動機可能也很純粹，只是簡單地想要對 **OI** 的發展做出一點點微小的貢獻吧。XD

***

Q：我很感興趣，怎麼參與？

A：**NCKUME wiki** 現在託管在 GitHub 上，你可以直接訪問這個 [repo](https://github.com/NCKUME-wiki/NCKUME-wiki) 來查看最新進展。參與的途徑包括在 GitHub 上面開 [Issue](https://github.com/NCKUME-wiki/NCKUME-wiki/issues)、[Pull Request](https://github.com/NCKUME-wiki/NCKUME-wiki/pulls)，或者在交流群中分享你的想法、直接向管理員投稿。目前，我們使用的框架是用 Python 開發的 [MkDocs](https://mkdocs.readthedocs.io)，支援 Markdown 格式（也支援插入數學公式）。

***

Q：可是我比較弱……不知道我能做點什麼。

A：一切源於熱愛。你可以協助其他人審核修改稿件，幫助我們宣傳 **NCKUME wiki**，為社區營造良好學習交流氛圍！

***

Q：現在主要是誰在做這件事啊？感覺這是個大坑，真的能做好嗎？

A：最開始主要是一些退役老年選手在做這件事，後來遇到了很多志同道合的小夥伴：有現役選手，退役玩家，也有從未參加過 **OI** 的朋友。目前，這個專案主要是由 **NCKUME wiki** 專案組來維護（下面是一張合影）。

<a href="https://github.com/NCKUME-wiki/NCKUME-wiki/graphs/contributors"><img src="https://opencollective.com/NCKUME-wiki/contributors.svg?width=890&button=false"/></a>

當然，這個項目只靠我們的力量是很難做得十全十美的，我們誠摯地邀請你一起來完善 **NCKUME wiki**。

***

Q：你們怎麼保證我們添加的內容不會突然消失？

A：我們把內容託管在 [GitHub](https://github.com/NCKUME-wiki/NCKUME-wiki) 上面，即使我們的伺服器翻車了，內容也不會丟失。另外，我們也會定期備份大家的心血，即使有一天 GitHub 倒閉了（？），我們的內容也不會丟失。

***

Q：**NCKUME wiki** 好像有空的頁面啊！

A：是的。受限於項目組成員的水準和時間，我們暫時無法完成這些空頁面。所以我們在這裡進行徵稿和招募，希望可以遇到有同樣想法的朋友，我們一起把 **NCKUME wiki** 完善起來。

***

Q：為什麼不直接去寫 [中文維琪百科](https://zh.wikipedia.org/) 呢？

A：因為我們希望可以真正幫到更多的選手或者對這些內容感興趣的人。而且由於眾所周知的原因，中文維琪上的內容並不是無門檻就可以獲取到的。

## 我想參與進來！

Q：我要怎麼與專案組交流？

A：可以通過 [關於本專案裡的交流方式](./about.md#交流方式) 聯繫我們。

***

Q：我要怎麼貢獻代碼或者內容？

請參考 [如何參與](./htc.md) 頁面。

***

Q：目錄在哪？

A：目錄在專案根目錄下的 [mkdocs.yml](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/mkdocs.yml#L17) 文件中。

***

Q：如何修改一個 topic 的內容？

A：在對應頁面右上方有一個編輯按鈕<i class="md-icon">edit</i>，點擊並確認閱讀了 [如何貢獻](./htc.md) 之後會跳轉到 GitHub 上對應檔的位置。

或者也可以自行閱讀目錄 [(mkdocs.yml)](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/mkdocs.yml) 查找檔位置。

***

Q：如何添加一個 topic？

A：有兩種選擇：

-   可以開一個 Issue，注明希望能添加的內容。
-   可以開一個 Pull Request，在目錄 [(mkdocs.yml)](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/mkdocs.yml) 中加上新的 topic，並在 [docs](https://github.com/NCKUME-wiki/NCKUME-wiki/tree/master/docs) 資料夾下對應位置創建一個空的 `.md` 文件。文檔的格式細節請參考 [格式手冊](./format.md#貢獻文檔要求)。

***

Q：我嘗試訪問 GitHub 的時候遇到了困難。

A：推薦在 hosts 文件中加入如下幾行[^ref1]：

```text
# GitHub Start
140.82.114.25                 alive.github.com
140.82.113.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
140.82.112.3                  gist.github.com
52.216.163.147                github-cloud.s3.amazonaws.com
52.217.124.1                  github-com.s3.amazonaws.com
52.216.144.83                 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.121.249                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.206.57                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.4                  github.com
140.82.113.18                 github.community
185.199.110.154               github.githubassets.com
151.101.1.194                 github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.111.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.112.25                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com
# GitHub End
```

可以在 [GitHub520](https://gitee.com/klmahuaw/GitHub520) 上瞭解到最新內容和更多資訊。

Linux 和 macOS 用戶可以嘗試使用 [依雲](https://github.com/lilydjwg/) 的 [gh-check 腳本](https://gist.github.com/lilydjwg/93d33ed04547e1b9f7a86b64ef2ed058) 獲取訪問最快的 IP，使用 `--hosts` 參數可以直接更新 hosts 檔。使用 `--help` 參數可以獲取使用幫助。使用先需要安裝 Python3 和 aiohttp（`pip install aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple/`）。依雲博客的介紹：[尋找最快的 GitHub IP](https://blog.lilydjwg.me/2019/8/16/gh-check.214730.html)。

同時，您可以使用 [Gitclone](https://www.gitclone.com/) 服務加速 Clone，可以閱讀其首頁上的說明。

如果您僅僅是想 Clone **NCKUME wiki** 的倉庫，那麼：

```bash
git clone https://gitclone.com/github.com/NCKUME-wiki/NCKUME-wiki
```

如果您需要向 **NCKUME wiki** 貢獻，那麼首先 fork **NCKUME wiki** 的倉庫，然後（將 `username` 替換為您的用戶名），需要注意的是提供的示例將使您使用 SSH 連接到 GitHub[^only-ssh-connect]：

```bash
git clone https://gitclone.com/github.com/username/NCKUME-wiki
git remote set-url origin git@github.com:username/NCKUME-wiki.git
```

***

Q：我這裡 pip 也太慢了！

A：可以選擇更換國內源[^ref2]，或者：

```bash
pip install -U -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

***

Q：我在用戶端 clone 了這個專案，速度太慢。

A：如果有安裝 `git bash`，可以加幾個限制來減少下載量。[^ref3]

```bash
git clone https://github.com/NCKUME-wiki/NCKUME-wiki.git --depth=1 -b master
```

***

Q：我沒裝過 Python 3。

A：可以訪問 [Python 官網](https://www.python.org/downloads/) 瞭解更多資訊。

***

Q：好像提示我 pip 版本過低。

A：進入 cmd/shell 之後，執行以下命令：

```bash
python -m pip install --upgrade pip
```

***

Q：我安裝依賴失敗了。

A：檢查一下：網路？許可權？查看錯誤資訊？

***

Q：我已經 clone 下來了，為什麼部署不了？

A：檢查一下是否安裝好了依賴？

***

Q：我 clone 了很久之前的 repo，怎麼更新到新版本呢？

A：請參考 GitHub 官方的説明頁面 [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)。

***

Q：如果是裝了之前的依賴怎麼更新？

A：請輸入以下命令：

```bash
pip install -U -r requirements.txt
```

***

Q：為什麼我的 markdown 格式亂了？

A：可以查閱 [cyent 的筆記](https://cyent.github.io/markdown-with-mkdocs-material/)，或者 [MkDocs 使用說明](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)。

我們目前使用 [remark-lint](https://github.com/remarkjs/remark-lint) 來自動化修正格式，可能還有一些 [配置](https://github.com/NCKUME-wiki/NCKUME-wiki/blob/master/.remarkrc) 不夠好的地方，歡迎指出。

***

Q：GitHub 是不是不顯示我的數學公式？

A：是的，GitHub 的預覽不顯示數學公式。但是請放心，MkDocs 是支援數學公式的，可以正常使用，只要是 MathJax 支援的句式都可以使用。

***

Q：我的數學公式怎麼亂碼了？

A：如果是行間公式（用的 `$$`），目前已知的問題是需要在 `$$` 兩側留有空行，且 `$$` 要 **單獨** 放在一行裡（且不要在前加空格）。格式如下：

```text
// 空行
$$
a_i
$$
// 空行
```

***

Q：我的公式為什麼在目錄裡沒有正常顯示？好像雙倍了。

A：是的，這個是 python-markdown 的一個 bug，可能近期會修復。

如果想要避免目錄中出現雙倍公式，可以參考 [string 分類下 SAM 的目錄寫法](https://github.com/NCKUME-wiki/NCKUME-wiki/blame/master/docs/string/sam.md#L73)。

```text
結束位置 <script type="math/tex">endpos</script>
```

在目錄中會變成

```text
結束位置 endpos
```

注：現在請儘量避免在目錄中引入 MathJax 公式。

***

Q：如何給一個頁面單獨聲明版權資訊？

A：在頁面開頭加一行即可。[^ref4]

比如：

```text
copyright: SATA
```

注：默認的是 CC BY-SA 4.0 和 SATA。

***

Q：為什麼作者資訊統計處沒有我的名字？

A：如果你發現自己寫過一個頁面中的部分內容，但是你沒有被記錄進作者清單，可以把自己的 GitHub ID 加入到檔頭的 [author 欄位](./htc.md#author-欄位)。

***

感謝你看到了最後，我們現在亟需的，就是你的幫助。

**NCKUME wiki** 項目組

2018.8

## 參考資料與注釋

[^ref1]: [GitHub520](https://gitee.com/klmahuaw/GitHub520)

[^ref2]: [更改 pip 源至國內鏡像 - L 瑜 - CSDN 博客](https://blog.csdn.net/lambert310/article/details/52412059)

[^ref3]: [GIT--- 看我一步步入門（Windows Git Bash）](https://blog.csdn.net/FreeApe/article/details/46845555)

[^ref4]: [Metadata - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/extensions/metadata/#usage)

[^only-ssh-connect]: GitHub 棄用了基於密碼身份驗證的 HTTPS 協定，連接必須使用 SSH 或者 Personal Access Token，參見 [我應使用哪個遠端 URL？](https://docs.github.com/cn/github/using-git/which-remote-url-should-i-use)，[創建個人訪問權杖](https://docs.github.com/cn/github/authenticating-to-github/creating-a-personal-access-token) 和 [使用 SSH 連接到 GitHub](https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh)。


