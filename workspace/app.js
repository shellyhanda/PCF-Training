var express = require("express");
var http = require("http");
var app = express();

app.get("/status", function(req, res){
return res.send('Server A\n');
});

http.createServer(app).listen(process.env.PORT, function() {
console.log("Listening on port " + process.env.PORT);
});
