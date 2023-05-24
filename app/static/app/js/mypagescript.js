 
const privateName = document.getElementById("myId");    //유저 네임이나 아이디
const privateScore = document.getElementById("myScore");    //유저 점수


const privatInfo = [
    {   
        userName: user,
        userScore: "20500",
    }
];

function updateInfo(){

    privateName.innerHTML = privatInfo[0].userName;
    privateScore.innerHTML = " Your Score : " + privatInfo[0].userScore;
  
};
  
updateInfo();
  

