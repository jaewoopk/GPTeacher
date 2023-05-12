


const quizType = document.querySelector(".quiz_type");                     // 퀴즈 종류
const quizNumber = document.querySelector(".quiz_question .number");       // 퀴즈 번호
const quizAsk = document.querySelector(".quiz_question .ask");             // 퀴즈 질문
const quizconfirm = document.querySelector(".quiz_try .confirm");       // 정답 확인 버튼
const quizResult = document.querySelector(".quiz_try .result");         // 정답 결과

const quizSelects = document.querySelector(".quiz_selects");                //객관식 보기
const quizChoice = quizSelects.querySelectorAll(".choice");                    //객관식 보기  
const quizSelect = quizSelects.querySelectorAll(".select");                    //객관식 보기


const quizNext = document.getElementById("next-btn");   //다음 퀴즈로
const quizBefore = document.getElementById("before-btn"); //이전 퀴즈로





// 문제정보
const quizInfo = [
  {   
      answerNum: "1",
      answerAsk: "Henry will make a _______ on the new manufacturing process",
      answerChoice: ["(a) present", "(b) presentation", "(c) presents", "(d) present"],
      answerResult: "2"
  }
];


//문제출력 함수
function updateQuiz(){

  quizNumber.textContent = quizInfo[0].answerNum + ". ";
  quizAsk.textContent = quizInfo[0].answerAsk;
  quizResult.textContent = quizInfo[0].answerEx;


  for(let i = 0; i<quizSelect.length; i++){
      quizChoice[i].textContent = quizInfo[0].answerChoice[i];
  }

};

updateQuiz();

// 정답확인

function answerQuiz(){

  // 유저가 선택한 정답(클릭한 input값 --> checked라는 속성 생김) vs 정답
  for(let i = 0; i<quizSelect.length; i++){
      if(quizSelect[i].checked == true){          //보기에 체크가 된 상태
          //체크 번호 vs 문제번호
          if(quizSelect[i].value == quizInfo[0].answerResult){
              document.getElementById("change").innerHTML="correct";
             
          } else{
              document.getElementById("change").innerHTML="wrong"; 
          } 
      }
  }
};

quizconfirm.addEventListener("click",answerQuiz);




/*
var ansbtn = document.getElementById("ans-btn");
    
ansbtn.addEventListener("click",  function() {
  if(select.userAns[1].checked == true) 
    document.getElementById("change").innerHTML="correct";
  else 
    document.getElementById("change").innerHTML="wrong";
})
  

*/


function nextQuiz(){
  alert("Next quiz move!!");
}

quizNext.addEventListener("click",nextQuiz);


function beforeQuiz(){
  alert("Before quiz move!!");
}

quizBefore.addEventListener("click",beforeQuiz);




