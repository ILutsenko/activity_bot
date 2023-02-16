function myFunction(message) {
    let user_id = getUserId(message)
    console.log(user_id)
    let x = new XMLHttpRequest();
      x.open("GET", "http://127.0.0.1:80", true);
      x.onload = function (){
          console.log( x.responseText);
      }
      x.send(null);
}

const getUserId = (message) => {
  if (message.reply_to_message) {
    return message.reply_to_message.from.id;
  }
  return message.from.id;
};
