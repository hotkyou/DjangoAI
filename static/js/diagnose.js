document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelector(".custom-button")
    .addEventListener("click", function () {
      let currentQuestion = 0;
      const questions = document.querySelectorAll(".question-list > div");
			const sentButton = document.getElementById("sent-button");
      const sendButton = document.getElementById("send-button");
      const nextButton = document.getElementById("next-button");
      const prevButton = document.getElementById("prev-button");

      document.querySelector(".container").style.display = "none";
      document.querySelector(".question-list").style.display = "block";
      nextButton.style.display = "block";

			

      // 最初にすべての質問と「前へ」ボタンを非表示にする
      questions.forEach(function (question) {
        question.style.display = "none";
      });
      prevButton.style.display = "none";

      // 最初の質問を表示する
      if (questions[currentQuestion]) {
        questions[currentQuestion].style.display = "block";
      }

      nextButton.addEventListener("click", function () {
				if (!isRadioButtonSelected(questions[currentQuestion])) {
					showAlert();
					return;
				}
        if (currentQuestion < questions.length - 1) {
          questions[currentQuestion].style.display = "none"; // 現在の質問を非表示にする
          currentQuestion++; // インデックスを増やす
          questions[currentQuestion].style.display = "block"; // 次の質問を表示する

          prevButton.style.display = "block"; // 「前へ」ボタンを表示

          // 最後の質問の場合、「次へ」ボタンのテキストを「送信」に変更
          if (currentQuestion === questions.length - 1) {
            sendButton.style.display = "block";
            nextButton.style.display = "none";
          }
        }
      });

      prevButton.addEventListener("click", function () {
        if (currentQuestion > 0) {
          questions[currentQuestion].style.display = "none"; // 現在の質問を非表示にする
          currentQuestion--; // インデックスを減らす
          questions[currentQuestion].style.display = "block"; // 前の質問を表示する

          // 最初の質問の場合、「前へ」ボタンを非表示
          if (currentQuestion === 0) {
            prevButton.style.display = "none";
          }

          // 「次へ」ボタンのテキストを元に戻す
          sendButton.style.display = "none";
          nextButton.style.display = "block";
        }
      });

			sendButton.addEventListener("click", function () {
				if (!isRadioButtonSelected(questions[currentQuestion])) {
					showAlert();
					return;
				}
				sentButton.click();
			});
    });
});

function isRadioButtonSelected(question) {
	const radioButtons = question.querySelectorAll('input[type="radio"]');
	for (let i = 0; i < radioButtons.length; i++) {
			if (radioButtons[i].checked) {
					return true;
			}
	}
	return false;
}

function showAlert() {
	const alertElement = document.getElementById('customAlert');
	alertElement.style.right = '20px';

	// アラートを5秒後に非表示にする
	setTimeout(() => {
			alertElement.style.right = '-300px';
	}, 3000);
}
