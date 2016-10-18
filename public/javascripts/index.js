var socket = io.connect();

socket.on('connect', function(data) {
  console.log("Conectado");
});

function send_room_on(){
  socket.emit('control_lamps', "lamp_room_on");
}

function send_room_off(){
  socket.emit('control_lamps', "lamp_room_off");
}

function send_curtain_open(){
  socket.emit('control_curtain', "curtain_open");
}

function send_curtain_close(){
  socket.emit('control_curtain', "curtain_close");
}
