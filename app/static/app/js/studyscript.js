const quizType = document.querySelector(".quiz_type");
var quizNumber = document.querySelector(".quiz_question .number");
var quizAsk = document.querySelector(".quiz_question .ask");
const quizconfirm = document.querySelector(".quiz_try .confirm");
var quizResult = document.querySelector(".quiz_try .result");
var gpt_message = document.querySelector(".user .gpt_respond_message");
var quizExplanation = document.querySelector(".user .explanation")
var idx_update  = document.querySelector(".menuex .testidx")
var idx_update2  = document.querySelector(".menuex2 .testidx2")
var quizSelects = document.querySelector(".quiz_selects");
var quizChoice = quizSelects.querySelectorAll(".choice");
var quizSelect = quizSelects.querySelectorAll(".select");

const quizView = document.querySelector(".user");             

var quizInfo = [];
var quiz_select_store = []; //  0-> 초기입력 줄바꿈 제거   1~4 -> 0 : none  1 : 입력

const quizNext = document.getElementById("next-btn");
const quizBefore = document.getElementById("before-btn");
const user_GPT_ask = document.getElementById("ask_gpt")

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
  idx = test-1;
  quizInfo = data;

  updateQuiz(idx); // 초기화 후 문제를 업데이트합니다.
};

function updateQuiz(index) {
  document.getElementById("user_gpt_id").style.display ='none';
  document.getElementById("user_gpt_id_text").style.display ='none';
  document.getElementById("ask_gpt").style.display ='none';
  quizNumber.textContent = quizInfo[index].idsentencedata + ". ";
  quizAsk.textContent = quizInfo[index].sentenceData_contents;
  quizResult.textContent = "";
  document.getElementById('idx_update').value = index+1;
  document.getElementById('idx_update2').value = index+1;
  //GPT.replace(/<[^>]*>?/g, '');
  quizExplanation.innerHTML = "";
  gpt_message.innerHTML = "";
  quizChoice[0].textContent = quizInfo[index].sentenceData_word1;
  quizChoice[1].textContent = quizInfo[index].sentenceData_word2;
  quizChoice[2].textContent = quizInfo[index].sentenceData_word3;
  quizChoice[3].textContent = quizInfo[index].sentenceData_word4;
  quiz_select_init();
  for(let i = 0; i < quizSelect.length; i++) {
    quizSelect[i].checked = false; // 선택 해제
  }
};

//quizInfo[index].Explanation
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
      document.getElementById("gpt_answer_to_view").value = quizInfo[idx].Exp_1;
      break ;
    case ("B") :
      answerValue = quizInfo[idx].sentenceData_word2;
      document.getElementById("gpt_answer_to_view").value = quizInfo[idx].Exp_2;
      break ;
    case ("C") :
      answerValue = quizInfo[idx].sentenceData_word3;
      document.getElementById("gpt_answer_to_view").value = quizInfo[idx].Exp_3;
      break ;
    case ("D") :
      answerValue = quizInfo[idx].sentenceData_word4;
      document.getElementById("gpt_answer_to_view").value = quizInfo[idx].Exp_4;
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
  Show_Explanation();
};

function Show_Explanation(){

    if (number == 1 && quiz_select_store[1] == 0){
    quizExplanation.innerHTML += quizInfo[idx].Exp_1;
    quiz_select_store[1] = 1;
    }
  else if (number == 2 && quiz_select_store[2] == 0){
    quizExplanation.innerHTML += quizInfo[idx].Exp_2;
    quiz_select_store[2] = 1;
    }
  else if (number == 3 && quiz_select_store[3] == 0){
    quizExplanation.innerHTML += quizInfo[idx].Exp_3;
    quiz_select_store[3] = 1;
    }
  else if (number == 4 && quiz_select_store[4] == 0){
    quizExplanation.innerHTML += quizInfo[idx].Exp_4;
    quiz_select_store[4] = 1;
    }
  if(quiz_select_store[0] == 0){quizExplanation.innerHTML += "<br><br>"}
};
function sendRequestToGPT()
{
    var gpt_message_send = document.getElementById("user_gpt_id").value;
    var httpRequest = new XMLHttpRequest();
    httpRequest.open("POST", "");
    httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    httpRequest.onreadystatechange =function() {

        if(httpRequest.readyState == 4 ){
            const {GPT_respond_ajax } = JSON.parse(httpRequest.response);
            gpt_message.innerHTML = GPT_respond_ajax;
        }

    };
    var sentence_answer = document.getElementById("user_answer_to_view").value;
    var explanation = document.getElementById("gpt_answer_to_view").value;
    httpRequest.send(JSON.stringify({user_ask: gpt_message_send,"sentence_answer":sentence_answer,"explanation":explanation}));

}

quizconfirm.addEventListener("click", answerQuiz);
function quiz_select_init()
{
    for(i=0;i<5;i++){
    quiz_select_store[i]  = 0;
    }
}
user_GPT_ask.addEventListener("click", sendRequestToGPT)
function nextQuiz() {
  quizView.classList.remove("positive", "negative");
  if (idx < quizInfo.length - 1) {

    idx += 1;
    localStorage.setItem('quizIndex', idx);  // idx 값을 로컬 저장소에 저장
    updateQuiz(idx);

    quizExplanation.removeChild();
  } else {
    alert("No more quizzes");
  }

};

quizNext.addEventListener("click", nextQuiz);

function beforeQuiz() {
  if (idx > 0) {

    localStorage.setItem('quizIndex', idx);  // idx 값을 로컬 저장소에 저장
    idx -= 1;
    updateQuiz(idx);

    quizExplanation.removeChild();
  } else {
    alert("This is the first quiz");
  }

};

quizBefore.addEventListener("click", beforeQuiz);
