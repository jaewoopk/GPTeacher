
const idCheck = document.getElementById("idcheck");   
const psCheck = document.getElementById("passwordcheck"); 
const joinClick = document.getElementById("submitclick");



function checkId(){
    alert("user id check!!");
};

idCheck.addEventListener("click",checkId);
  

function checkPs(){
    alert("user password check!!");
};

psCheck.addEventListener("click",checkPs);
  


function submitClick(){
    alert("submit complete!");
};

joinClick.addEventListener("click",submitClick);
  