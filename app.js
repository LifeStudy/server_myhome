var express = require('express.io'),
child = require('child_process');
app = express();
socket = require('socket.io').listen(app.listen(8245));

app.sensors = {};

app.use(express.static(__dirname + '/public'));
app.http().io();

socket.on('connect', function (client) {
  client.on('control_lamps', function(lamps){
    console.log("Servidor " + lamps);

  if(lamps == "lamp_room_on"){
    action("lamps/lamp_room_on.py");
  }else if(lamps == "lamp_room_off"){
    action("lamps/lamp_room_off.py");
  }
  client.broadcast.emit("control_lamps", lamps);
  });
});

socket.on('connect', function (client) {
  client.on('control_curtain', function(curtain){
    console.log("Servidor " + curtain);

  if(curtain == "curtain_open"){
    action("curtain/stepper_left.py");
  }else if(curtain == "curtain_close"){
    action("curtain/stepper_right.py");
  }
  client.broadcast.emit("control_curtain", curtain);
  });
});

function action(file){
  var exec = child.exec;
  exec('python ./server_py/'+file, function(err, stdout, stderr){
    if(err){
      console.log(err);
    }
  });
}

console.log('Smart Home - C.I.A - 8245');
