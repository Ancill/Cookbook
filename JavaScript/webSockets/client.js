const connection = new WebSocket('ws://localhost:8080');
const button = document.querySelector('#send');

// -----------------------------------------------------------------------------
// There a few events that using WebSocket
// *WebSocket.onopen -- called when the connection is opened
// *WebSocket.onclose => called when the connection is closed
// *WebSocket.onerror => called when an error occurs
// * WebSocket.onmessage => called when a message is received from the server
// -----------------------------------------------------------------------------

connection.onopen = event => {
  console.log('Websocket is open now');
};
connection.onclose = event => {
  console.log('Websocket is close now');
};
connection.onerror = event => {
  console.log('Websocket error observed', event);
};
connection.onmessage = event => {
  // append received message from the server
  const chat = document.querySelector('#chat');
  chat.innerHTML += event.data;
};

button.addEventListener('click', () => {
  const name = document.querySelector('#name');
  const message = document.querySelector('#message');
  const data = `<p>${name.value}: ${message.value}</p>`;

  //send message to the server
  connection.send(data);

  //clear input fields
  name.value = '';
  message.value = '';
});
