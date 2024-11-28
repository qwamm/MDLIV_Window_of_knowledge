var http = require("http"),
    httpProxy = require("http-proxy");

var frontProxy = new httpProxy.createProxyServer({
    target: {
        host: "localhost",
        port: 3002,
    },
});
var backProxy = new httpProxy.createProxyServer({
    target: {
        host: '127.0.0.1',
        port: 8080,
    },
});
var server = http.createServer(function (req, res) {
    console.log(req.url);
    if (req.url.startsWith("/api")) {
        backProxy.web(req, res);
    } else {
        frontProxy.web(req, res);
    }
});
server.on("upgrade", function (req, socket, head) {
    frontProxy.ws(req, socket, head);
});
console.log("listening on port 5050");
server.listen(80);