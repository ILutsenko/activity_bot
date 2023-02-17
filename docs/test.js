let tg = window.Telegram.WebApp;
const url = "http://80.78.248.142:80"
alert(`user_id: ${tg.initDataUnsafe.user.id}`)
let task_button = document.getElementById("task_button");


task_button.addEventListener('click', function(){
    alert(tg.initDataUnsafe.user.id)
    // const form = document.getElementById('form');
    // const formData = new FormData(form);
    // let task_name = formData.get('text1')
    // post(`${url}/task`, {user_id: tg.initDataUnsafe.user.id, task_name: task_name})
});

const post = async (url, params) => {
    console.log(JSON.stringify(params))
    let post_url = url + '?' + new URLSearchParams(params)
    fetch(post_url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // body: JSON.stringify(params)
    }).then(response => response).then(
        response => console.log(response)
    )
    createDetailsTag(params.task_name)
    // tg.reload()
    var container = document.getElementById("task_list_id");
    var content = container.innerHTML;
    container.innerHTML= content;
    document.location.reload()
    alert('Задача успешно создана')
}

const get = async (url, params) => {
    const response = await fetch(url + '?' + new URLSearchParams(params))
    const data = await response.json()
    return data
}
function get_tasks() {
    return get(url, {user_id: tg.initDataUnsafe.user.id}).then(
        data => {return data.message}
    )
}

function addButtons(element){
    const get_task = document.createElement('button');
    get_task.textContent = 'Взять задачу'
    element.appendChild(get_task);
}

function createDetailsTag(element = NaN){
    alert(`user_id: ${tg.initDataUnsafe.user.id}`)
    get_tasks(url, {user_id: tg.initDataUnsafe.user.id}).then(tasks_group => {
        if (!tasks_group){
            alert("У вас нет открытых задач")
        }
        else if (element){
            tasks_group = {1: element}
        }
        for (const [key, value] of Object.entries(tasks_group)) {
            console.log(value)
            const details = document.createElement('details');
            let par = document.createElement('p')
            let summary = document.createElement('summary');
            summary.textContent = value.task_name
            par.textContent = `Статус задачи: ${value.status}`
            details.appendChild(summary);
            details.appendChild(par);
            addButtons(details)
            document.getElementById("task_list_id").appendChild(details);
        }
    })
}
// createDetailsTag()
