const quizType = document.querySelector(".quiz_type");
var quizNumber = document.querySelector(".quiz_question .number");
var quizAsk = document.querySelector(".quiz_question .ask");
const quizconfirm = document.querySelector(".quiz_try .confirm");
var quizResult = document.querySelector(".quiz_try .result");

var quizExplanation = document.querySelector(".user .explanation")
var idx_update  = document.querySelector(".menuex .testidx")
var quizSelects = document.querySelector(".quiz_selects");
var quizChoice = quizSelects.querySelectorAll(".choice");
var quizSelect = quizSelects.querySelectorAll(".select");

var quizInfo = [];

const quizNext = document.getElementById("next-btn");
const quizBefore = document.getElementById("before-btn");

var idx = localStorage.getItem('quizIndex') ? parseInt(localStorage.getItem('quizIndex')) : 0;

var xhr = new XMLHttpRequest();
xhr.overrideMimeType("application/json");
xhr.open("GET", "../../../static/app/js/sentenceData.json", true);
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    var json = JSON.parse(xhr.responseText);
    initializeQuizInfo(json); // JSON 데이터를 전달하여 quizInfo를 초기화합니다.
  }
};
xhr.send();

function initializeQuizInfo(data) {
  idx = test-1;
  quizInfo = data;
  updateQuiz(idx); // 초기화 후 문제를 업데이트합니다.
}

function updateQuiz(index) {
  quizNumber.textContent = quizInfo[index].idsentenceData + ". ";
  quizAsk.textContent = quizInfo[index].sentenceData_contents;
  quizResult.textContent = "";
  document.getElementById('idx_update').value = index+1;
  quizChoice[0].textContent = quizInfo[index].sentenceData_word1;
  quizChoice[1].textContent = quizInfo[index].sentenceData_word2;
  quizChoice[2].textContent = quizInfo[index].sentenceData_word3;
  quizChoice[3].textContent = quizInfo[index].sentenceData_word4;

  for(let i = 0; i < quizSelect.length; i++) {
    quizSelect[i].checked = false; // 선택 해제
  }
}
//quizInfo[index].Explanation
function answerQuiz() {
  var selectedValue;
  var answerValue;
  for(let i = 0; i < quizSelect.length; i++) {
    if (quizSelect[i].checked) {
      selectedValue = quizChoice[i].textContent;
      break;
    }
  }

  switch (quizInfo[idx].sentenceData_answerword) {
    case ("A") :
      answerValue = quizInfo[idx].sentenceData_word1;
      break ;
    case ("B") :
      answerValue = quizInfo[idx].sentenceData_word2;
      break ;
    case ("C") :
      answerValue = quizInfo[idx].sentenceData_word3;
      break ;
    case ("D") :
      answerValue = quizInfo[idx].sentenceData_word4;
      break ;
  }
  if (selectedValue === answerValue) {
    quizResult.textContent = "Correct";
  } else {
    quizResult.textContent = "Wrong";
  }
  Show_Explanation();
}
function Show_Explanation(){
    quizExplanation.textContent = quizInfo[idx].Explanation;
}
quizconfirm.addEventListener("click", answerQuiz);

function nextQuiz() {
  if (idx < quizInfo.length - 1) {
    alert("Next quiz move!!");
    idx += 1;
    localStorage.setItem('quizIndex', idx);  // idx 값을 로컬 저장소에 저장
    updateQuiz(idx);

    quizExplanation.removeChild();
  } else {
    alert("No more quizzes");
  }
}

quizNext.addEventListener("click", nextQuiz);

function beforeQuiz() {
  if (idx > 0) {
    alert("Before quiz move!!");
    localStorage.setItem('quizIndex', idx);  // idx 값을 로컬 저장소에 저장
    idx -= 1;
    updateQuiz(idx);

    quizExplanation.removeChild();
  } else {
    alert("This is the first quiz");
  }
}

quizBefore.addEventListener("click", beforeQuiz);
