import express from "express"
import fetch from "node-fetch";
const hostname = 'localhost';
const port = 3010;

const app = express();
app.get('/', function(req, res) {
    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);
    
  fetch(`https://pubchem.olfactory.dev.metacell.us/molecules/${req.query.id}`, {
    mode: 'no-cors',
    headers: {
      'Access-Control-Allow-Origin':'*'
    }
  })
  .then(response => { return response.json() })
  .then((data) => {

    res.writeHead(200, { 'Content-Type': 'application/json' })
    res.write(JSON.stringify(data));
    res.end();
  })
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});