const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Dummy server data
const serverInfo = {
    name: "VanillaCord",
    description: "Minecraft is a game about placing blocks and going on adventures. Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles..."
};

// Middleware
app.use(bodyParser.json());

// Serve static files
app.use(express.static('public'));

// API endpoints
app.get('/api/server-info', (req, res) => {
    res.json(serverInfo);
});

app.post('/api/execute-command', (req, res) => {
    const { command } = req.body;
    // Execute command here (e.g., start, stop, restart)
    // For demonstration, just return the command
    res.send(`Executing command: ${command}`);
});

// Start server
app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
