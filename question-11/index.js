const https = require('https');
const fs = require('fs');
const express = require('express');
const path = require('path');
const app = express();
const port = 443;

// Serve static files from 'public' directory
// app.use(express.static('public'));

// Route for the home page
app.get('/', (req, res) => {
    console.log("HWAT")
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
const options = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem'),
};

// Create an HTTPS server
https.createServer(options, app).listen(443, '0.0.0.0', () => {
    console.log('Secure server running on https://<public-ip>:443');
});
