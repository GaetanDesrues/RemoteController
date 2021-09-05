const express = require('express');
const app = express();
const http = require('http');

const hostname = '127.0.0.1';
const port = 5011;

const server = http.createServer(app);

const io = require('socket.io')(server, {allowEIO3: true});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});


io.on('connection', (socket) => {
    console.log('a user connected');

    // socket.on('updt', (msg) => {
    //     console.log('received message: ' + msg["msg"]);
    //     io.emit('pupdt', msg);  // broadcast after receive
    // });

    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
});






