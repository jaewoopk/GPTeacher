
  

const rankPacks = document.querySelector("ol"); 
const rankNames = rankPacks.querySelectorAll("mark");    //유저 네임이나 아이디
const rankScores = rankPacks.querySelectorAll("small");    //유저 점수

let userCount = 0 ;

// 유저정보
const userInfo = [
    {   
        userName: "jenny",
        userScore: "32000",
    },
    {   
        userName: "sunnny",
        userScore: "28500",

    },
    {   
        userName: "chris",
        userScore: "26600",

    },
    {   
        userName: "sam",
        userScore: "24800",

    },
    {   
        userName: "mink",
        userScore: "21000",

    },
    {   
        userName: "lee",
        userScore: "20700",

    },
    {   
        userName: "jaewoopk",
        userScore: "20500",

    },
    {   
        userName: "kim",
        userScore: "19800",

    },
    {   
        userName: "joe",
        userScore: "18700",

    },
    {   
        userName: "jessica",
        userScore: "18650",

    }
];
  

function updateRank(){

    for(let i = 0; i<10; i++){
        rankNames[i].textContent = userInfo[userCount].userName;
        rankScores[i].textContent = userInfo[userCount].userScore;
        userCount++;  
    }
  
};

updateRank();
  



