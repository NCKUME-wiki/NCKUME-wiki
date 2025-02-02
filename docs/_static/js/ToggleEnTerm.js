function toggleAllTranslations() {
  var translations = document.querySelectorAll('.translation');
  var showCount = 0;
  // 計算目前顯示的翻譯數量
  for (var i = 0; i < translations.length; i++) {
    if (translations[i].style.display !== "none") {
      showCount++;
    }
  }
  // 顯示數量超過一半則全部隱藏，否則全部顯示
  var action = (showCount > translations.length / 2) ? "none" : "inline";

  for (var i = 0; i < translations.length; i++) {
    translations[i].style.display = action;
  }
}
var terms = document.querySelectorAll('.term');
for (var i = 0; i < terms.length; i++) {
  terms[i].addEventListener('click', function () {
    var translation = this.nextElementSibling;
    translation.style.display = (translation.style.display === "none") ? "inline" : "none";
  });
}
