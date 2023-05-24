const quizType = document.querySelector(".quiz_type");
var quizNumber = document.querySelector(".quiz_question .number");
var quizAsk = document.querySelector(".quiz_question .ask");
const quizconfirm = document.querySelector(".quiz_try .confirm");
var quizResult = document.querySelector(".quiz_try .result");
var quizSelects = document.querySelector(".quiz_selects");
var quizChoice = quizSelects.querySelectorAll(".choice");
var quizSelect = quizSelects.querySelectorAll(".select");
var quizExplanation = document.querySelector(".user .explanation")
const quizView = document.querySelector(".user");             
var quizSelects = document.querySelector(".quiz_selects");
var quizChoice = quizSelects.querySelectorAll(".choice");
var quizSelect = quizSelects.querySelectorAll(".select");

var quizInfo = [];
var quiz_select_store = []; //  0-> 초기입력 줄바꿈 제거   1~4 -> 0 : none  1 : 입력

const quizNext = document.getElementById("next-btn");

var mylist = JSON.parse(test)


var idx = localStorage.getItem('quizIndex') ? parseInt(localStorage.getItem('quizIndex')) : 0;
var number;
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
  idx = 0;
  quizInfo = data;

  updateQuiz(idx); // 초기화 후 문제를 업데이트합니다.
};

function updateQuiz(index) {
  index = mylist[idx]
  quizNumber.textContent = quizInfo[index].idsentencedata + ". ";
  quizAsk.textContent = quizInfo[index].sentenceData_contents;
  quizResult.textContent = "";
  quizChoice[0].textContent = quizInfo[index].sentenceData_word1;
  quizChoice[1].textContent = quizInfo[index].sentenceData_word2;
  quizChoice[2].textContent = quizInfo[index].sentenceData_word3;
  quizChoice[3].textContent = quizInfo[index].sentenceData_word4;
  quiz_select_init();
  for(let i = 0; i < quizSelect.length; i++) {
    quizSelect[i].checked = false; // 선택 해제
  }
};

function quiz_select_init()
{
    for(i=0;i<5;i++){
    quiz_select_store[i]  = 0;
    }
}

function nextQuiz() {
  if (idx < 10) {
    localStorage.setItem('quizIndex', idx);  // idx 값을 로컬 저장소에 저장
    idx += 1;
    updateQuiz(idx);
  } else {
    alert("No more quizzes");
  }

};

quizNext.addEventListener("click", nextQuiz);

function answerQuiz() {
  var selectedValue;
  var answerValue;

  for(let i = 0; i < quizSelect.length; i++) {
    if (quizSelect[i].checked) {
      selectedValue = quizChoice[i].textContent;
      number = i+1;
      break;
    }
  }

  switch (quizInfo[idx].sentenCeDAtA_AnswerworD) {
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
    quizView.classList.remove("negative");
    quizView.classList.add("positive");

    document.getElementById("user_gpt_id").style.display ='block';
    document.getElementById("user_gpt_id_text").style.display ='block';
    document.getElementById("ask_gpt").style.display ='block';
    document.getElementById("user_answer_to_view").value = quizInfo[idx].sentenceData_contents + " blank is " + answerValue;

  } else {
    quizView.classList.remove("positive");
    quizView.classList.add("negative");
  }
};

quizconfirm.addEventListener("click", answerQuiz);