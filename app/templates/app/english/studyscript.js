

var ansbtn = document.getElementById("ans-btn");
    
ansbtn.addEventListener("click",  function() {
  if(select.userAns[1].checked == true) 
    document.getElementById("change").innerHTML="correct";
  else 
    document.getElementById("change").innerHTML="wrong";
})
  



window.onload = function () {

  var nextbtn = document.getElementById("next-btn");
    
  nextbtn.addEventListener("click", function () {
    alert("Next quiz move!!");
  })



  var beforebtn = document.getElementById("before-btn");
    
  beforebtn.addEventListener("click", function () {
      alert("Before quiz move!!");
  })


}