let tg = window.Telegram.WebApp;

tg.expand(); //расширяем на все окно

let task_button = document.getElementById("task_button");

task_button.addEventListener('click', function(){
	myFunction()
});



function myFunction() {
    let user_id = tg.initDataUnsafe.user.id
    alert(user_id)
    let x = new XMLHttpRequest();
      x.open("GET", "http://127.0.0.1:80", true);
      x.onload = function (){
          console.log( x.responseText);
      }
      x.send(null);
}
