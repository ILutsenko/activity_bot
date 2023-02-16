let tg = window.Telegram.WebApp;

tg.expand();

let task_button = document.getElementById("task_button");
alert(task_button)


let usercard = document.getElementById("usercard")
let p = document.createElement("p")

tg.initDataUnsafe.full_name
p.innerText = '${tg.initDataUnsafe.user.full_name} and ${tg.initDataUnsafe.user.id}'

usercard.appendChild(p)

task_button.addEventListener('click', function(){
    alert([tg.initDataUnsafe.user.full_name, tg.initDataUnsafe.user.id])
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
