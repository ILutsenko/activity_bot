let tg = window.Telegram.WebApp;
const url = "http://80.78.248.142:80"
let task_button = document.getElementById("task_button");
let show_button = document.getElementById("show_button");

function make_request(url, method, request_params) {
    let compiled_url = url + '?' + new URLSearchParams(request_params)
    let params = {
        method: method,
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
    }
    return fetch(compiled_url, params).then((response) => {
        if (response.headers.get("content-type") !== "application/json") {
            throw new TypeError();
        }
        const json_data = response.json();
        return json_data;
  });
}

task_button.addEventListener('click', function(){
    const params = {user_id: tg.initDataUnsafe.user.id, task_name: task_name}
    const form = document.getElementById('form');
    const formData = new FormData(form);
    let task_name = formData.get('text1')
    make_request(`${url}/task`, 'POST', params)
    alert(`Задача успешно создана: ${task_name}`)
    createDetailsTag(params.task_name)
    let container = document.getElementById("task_list_id");
    let content = container.innerHTML;
    container.innerHTML= content;
    document.location.reload()
});

show_button.addEventListener('click', function(){
    let user_id
    if (tg.initDataUnsafe.user && tg.initDataUnsafe.user.id){
        user_id = tg.initDataUnsafe.user.id
    } else {user_id = 492323696}
    make_request(url, 'GET', {user_id: user_id}).then(
        data => alert(Object.values(data.message)[0].task_name)
    )
    // createDetailsTag()
});

function addButtons(element){
    const get_task = document.createElement('button');
    get_task.textContent = 'Взять задачу'
    element.appendChild(get_task);
}

function createDetailsTag(){
    // {user_id: tg.initDataUnsafe.user.id}
    make_request(url, 'GET', {user_id: tg.initDataUnsafe.user.id}).then(tasks_group => {
        if (!tasks_group){
            alert("У вас нет открытых задач")
        }
        let ul = document.getElementById('ul')
        console.log(tasks_group)
        for (const [key, value] of Object.entries(tasks_group.message)) {
            let li = document.createElement('li')
            li.innerText = value.task_name
            ul.append(li)
            // const details = document.createElement('details');
            // let par = document.createElement('p')
            // let summary = document.createElement('summary');
            // summary.textContent = value.task_name
            // par.textContent = `Статус задачи: ${value.status}`
            // details.appendChild(summary);
            // details.appendChild(par);
            // addButtons(details)
            // document.getElementById("task_list_id").appendChild(details);
        }
    })
}
// createDetailsTag()
