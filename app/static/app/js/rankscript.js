
  

const rankPacks = document.querySelector("ol"); 
const rankNames = rankPacks.querySelectorAll("mark");    //유저 네임이나 아이디
const rankScores = rankPacks.querySelectorAll("small");    //유저 점수

let userCount = 0 ;

// 유저정보
const userInfo = [
    {   
        userName: "jenny",
        userScore: "300",
    },
    {   
        userName: "sunnny",
        userScore: "350",

    },
    {   
        userName: "chris",
        userScore: "450",

    },
    {   
        userName: "sam",
        userScore: "540",

    },
    {   
        userName: "mink",
        userScore: "653",

    },
    {   
        userName: "lee",
        userScore: "659",

    },
    {   
        userName: "park",
        userScore: "700",

    },
    {   
        userName: "kim",
        userScore: "850",

    },
    {   
        userName: "joe",
        userScore: "900",

    },
    {   
        userName: "jessica",
        userScore: "930",

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
  



