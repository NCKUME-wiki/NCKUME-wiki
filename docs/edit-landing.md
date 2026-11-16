disqus:

## 編輯前須知

首先，感謝您願意為 **NCKUME Wiki** 做出貢獻！

在開始編輯之前，建議您先閱讀並熟知 [如何參與](./intro/htc.md) 與 [格式手冊](./intro/format.md) 裡的規範，以確保內容品質並使審核合併過程更加順暢。

閱讀完畢後，請點擊下方按鈕開始進行編輯。

???+ note "敬請留意"
    - 請記得在 Markdown 文件頭部的 `author` 欄位後方，依照格式填入您的 GitHub ID；
    - 根據專案規範，合併時可能會視 Commit 內容品質採用 Rebase 或 Squash 方式，敬請留意。

<a id="btn-startedit" style="padding: 0.75em 1.25em; display: inline-block; line-height: 1; text-decoration: none; white-space: nowrap; cursor: pointer; border: 1px solid #6190e8; border-radius: 5px; background-color: #6190e8; color: #fff; outline: none; font-size: 0.75em;">開始編輯</a>

<script>
	function getQueryVariable(name, dft)
	{
		var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
		var r = window.location.search.substr(1).match(reg);
		if (r != null)
		{
			return unescape(r[2]);
		}
		return dft;
	}
	document.getElementById("btn-startedit").href = "https://github.com/NCKUME-wiki/NCKUME-wiki/edit/main/docs" + getQueryVariable("ref", "");
</script>
