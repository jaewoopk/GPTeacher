 
const privateName = document.getElementById("myId");    //유저 네임이나 아이디
const privateScore = document.getElementById("myScore");    //유저 점수


const privatInfo = [
    {   
        userName: "jenny",
        userScore: "300",
    }
];


function updateInfo(){

    privateName.innerHTML = " ID : " + privatInfo[0].userName;
    privateScore.innerHTML = " SCORE : " + privatInfo[0].userScore;
  
};
  
updateInfo();
  

