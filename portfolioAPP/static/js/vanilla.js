function showGame() {
    var game = document.getElementById("the-game");
    if (game.style.display === "none") {
        game.style.display = "block";
    } else {
        game.style.display = "none";
    }
};
function hideStartBtn() {
    var StartBtn = document.getElementById("game-btn");
    if (StartBtn.style.display === "block") {
        StartBtn.style.display = "none";
    } else {
        StartBtn.style.display = "block";
    }
};
var killCount = 0;
function kill_1() {
    var killBtn = document.getElementById("kill-1")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_2() {
    var killBtn = document.getElementById("kill-2")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_3() {
    var killBtn = document.getElementById("kill-3")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_4() {
    var killBtn = document.getElementById("kill-4")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_5() {
    var killBtn = document.getElementById("kill-5")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_6() {
    var killBtn = document.getElementById("kill-6")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
};
function kill_7() {
    var killBtn = document.getElementById("kill-7")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    };
};
function gameOver() {
    var timeLeft = 5;
    var timerId = setInterval(countdown, 10000);
    var killGame = document.getElementById("the-game");
    function endGame(){
        if (killGame.style.display === "none"){
            killGame.style.display = "none";
        } else {
            killGame.style.display = "none"
        }};
    function countdown() {
        if (timeLeft == 0 || killCount !==7) {
            clearTimeout(timerId);
            alert("YOU LOOSE!!!!");
            return endGame();
        } else { 
            clearTimeout(timerId);
            alert("YOU WON!!!!");
            return endGame();
        }};
    console.log("Time Left:" + timerId)
    };

// function play() {
//     //var audio = new Audio('');
//     //audio.play();
// }