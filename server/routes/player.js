var express = require('express');
var router = express.Router();
const { spawn } = require('child_process');

const playerPath = '/home/pi/xmas2k20/jamLights/hardware/main.py';
const stopPlayer = '/home/pi/xmas2k20/jamLights/hardware/stopPlayer.py';
var playerInstance;

router.get('/play',
    (req, res, next) => {
        playerInstance = spawn('python3', [playerPath]);
        res.send('playing');
    }
);

router.get('/stop',
    (req, res, next) => {
        playerInstance = null;
        spawn('python3', [stopPlayer]);
        res.send('stopped');
    }
)

module.exports = router;
