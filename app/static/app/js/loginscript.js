var regiforname;
var regiforpass;
var regiforrepass;
var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

$(function() {

    $(".input input").focus(function() {
 
       $(this).parent(".input").each(function() {
          $("label", this).css({
             "line-height": "18px",
             "font-size": "18px",
             "font-weight": "100",
             "top": "0px"
          })
          $(".spin", this).css({
             "width": "100%"
          })
       });
    }).blur(function() {
       $(".spin").css({
          "width": "0px"
       })
       if ($(this).val() == "") {
          $(this).parent(".input").each(function() {
             $("label", this).css({
                "line-height": "60px",
                "font-size": "24px",
                "font-weight": "300",
                "top": "10px"
             })
          });
 
       }
    });
 
    $(".button").click(function(e) {
       var pX = e.pageX,
          pY = e.pageY,
          oX = parseInt($(this).offset().left),
          oY = parseInt($(this).offset().top);
          console.log("qddda");
          
          regiforname = document.getElementById('regname').value;
          regiforpass = document.getElementById('regpass').value;
          regiforrepass= document.getElementById('reregpass').value;
          console.log(regiforname);
          console.log(regiforpass);
          console.log(regiforrepass);

          var formLayout = document.createElement("form"); 
    	 	 formLayout.setAttribute("charset", "UTF-8");
    		 formLayout.setAttribute("method", "POST"); 
    		 formLayout.setAttribute("action", "/app/english/join/");

    		 var emailLayout = document.createElement("input"); 
    		 emailLayout.setAttribute("type", "text");
    		 emailLayout.setAttribute("name", "email");
    		 emailLayout.setAttribute("value", regiforname);
    		 formLayout.appendChild(emailLayout); 

    		 var passLayout = document.createElement("input"); 
    		 passLayout.setAttribute("type", "text");
    		 passLayout.setAttribute("name", "password");
    		 passLayout.setAttribute("value", regiforpass);
    		 formLayout.appendChild(passLayout); 

          var repassLayout = document.createElement("input");
          repassLayout.setAttribute("type", "text");
          repassLayout.setAttribute("name", "repassword");
          repassLayout.setAttribute("value", regiforpass);
    		 formLayout.appendChild(repassLayout); 

          var csrftoken = document.createElement("input");
          csrftoken.setAttribute("type", "hidden");
          csrftoken.setAttribute("name", 'csrfmiddlewaretoken');
          csrftoken.setAttribute("value", csrfToken);
          formLayout.appendChild(csrftoken); 

    		 document.body.appendChild(formLayout); 
    		 formLayout.submit(); 
    		 document.body.removeChild(formLayout);  

          console.log("emd");

       $(this).append('<span class="click-efect x-' + oX + ' y-' + oY + '" style="margin-left:' + (pX - oX) + 'px;margin-top:' + (pY - oY) + 'px;"></span>')
       $('.x-' + oX + '.y-' + oY + '').animate({
          "width": "500px",
          "height": "500px",
          "top": "250px",
          "left": "-250px",
 
       }, 600);
       $("button", this).addClass('active');
    })
 
    $(".alt-2").click(function() {
       if (!$(this).hasClass('material-button')) {
          $(".shape").css({
             "width": "100%",
             "height": "100%",
             "transform": "rotate(0deg)"
          })
 
          setTimeout(function() {
             $(".overbox").css({
                "overflow": "initial"
             })
          }, 600)
 
          $(this).animate({
             "width": "86.4px",
             "height": "54px"
          }, 500, function() {
             $(".box").removeClass("back");
 
             $(this).removeClass('active')
          });
 
          $(".overbox .title").fadeOut(300);
          $(".overbox .input").fadeOut(300);
          $(".overbox .button").fadeOut(300);
 
          $(".alt-2").addClass('material-buton');
       }
 
    })
 
    $(".material-button").click(function() {
 
       if ($(this).hasClass('material-button')) {
          setTimeout(function() {
             $(".overbox").css({
                "overflow": "hidden"
             })
             $(".box").addClass("back");
          }, 200)
          $(this).addClass('active').animate({
             "width": "700px",
             "height": "700px"
          });
 
          setTimeout(function() {
             $(".shape").css({
                "width": "50%",
                "height": "50%",
                "transform": "rotate(45deg)"
             })
 
             $(".overbox .title").fadeIn(300);
             $(".overbox .input").fadeIn(300);
             $(".overbox .button").fadeIn(300);
          }, 700)
 
          $(this).removeClass('material-button');
 
       }
 
       if ($(".alt-2").hasClass('material-buton')) {
          $(".alt-2").removeClass('material-buton');
          $(".alt-2").addClass('material-button');
       }
 
    });
 
 });
