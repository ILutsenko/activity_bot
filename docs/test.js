let tg = window.Telegram.WebApp;

tg.expand();
tg.MainButton.show()
const url = "http://80.78.248.142:80"

let task_button = document.getElementById("task_button");

task_button.addEventListener('click', function(){
    tg.MainButton.setText(`Кнопка нажата юзером ${tg.initDataUnsafe.user.id}`)
    alert([tg.initDataUnsafe.user.last_name, tg.initDataUnsafe.user.id])
});



// function myFunction() {
//     let user_id = tg.initDataUnsafe.user.id
//     let x = new XMLHttpRequest();
//       x.open("GET", "http://80.78.248.142:80", true);
//       x.onload = function (){
//           alert( x.responseText);
//       }
//       x.send(null);
// }


const get = async (url, params) => {
    const response = await fetch(url + '?' + new URLSearchParams(params))
    const data = await response.json()

    return data
}

// Call it with async:
(async () => {
    const data = await get(url, {
        user_id: tg.initDataUnsafe.user.id,
    })

    console.log(data)
})()

// Calling it with then:
get(url, {
    user_id: tg.initDataUnsafe.user.id,
}).then(data => alert.log(data))
