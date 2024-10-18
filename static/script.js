console.log("JS")



// ダーツボードの各セクションを選択し、クリックイベントを設定
document.querySelectorAll('.darts-board div').forEach(section => {
    section.addEventListener('click', function () {
        // クリックされたセクションのスコアを取得
        const score = this.getAttribute('data-score');
        console.log(`Clicked section with score: ${score}`); // デバッグ用のログ

        // スコアをhiddenフィールドにセット
        document.getElementById('score-input').value = score;

        // フォームを送信してスコアをPOSTリクエストでサーバーに送信
        document.getElementById('dart-form').submit();
    });
});