const express = require('express');
const app = express();
const http = require('http');

const hostname = '127.0.0.1';
const port = 5011;

const server = http.createServer(app);

const { Server } = require("socket.io");
const io = new Server(server);

// const server = http.createServer((req, res) => {
// 	res.statusCode = 200;
//   	res.setHeader('Content-Type', 'text/plain');
//   	res.end('Sysmon App is Up and Running!\n');
// });

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// io.on('connection', (socket) => {
//   console.log('a user connected');
//   socket.on('disconnect', () => {
//     console.log('user disconnected');
//   });
// });

io.on('connection', (socket) => {
  socket.on('chat message', (msg) => {
    console.log('message: ' + msg);
  });
});

server.listen(port, hostname, () => {
  	console.log(`Server running at http://${hostname}:${port}`);
});






