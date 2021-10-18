function showGame() {
    var game = document.getElementById("the-game");
    if (game.style.display === "none") {
        game.style.display = "block";
    } else {
        game.style.display = "none";
    }
}
function hideStartBtn() {
    var StartBtn = document.getElementById("game-btn");
    if (StartBtn.style.display === "block") {
        StartBtn.style.display = "none";
    } else {
        StartBtn.style.display = "block";
    }
}
var killCount = 0
function kill_1() {
    var killBtn = document.getElementById("kill-1")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function kill_2() {
    var killBtn = document.getElementById("kill-2")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function kill_3() {
    var killBtn = document.getElementById("kill-3")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function kill_4() {
    var killBtn = document.getElementById("kill-4")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function kill_5() {
    var killBtn = document.getElementById("kill-5")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function kill_6() {
    var killBtn = document.getElementById("kill-6")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}function kill_7() {
    var killBtn = document.getElementById("kill-7")
    if (killBtn.style.display === "block") {
        killBtn.style.display = "none";
        killCount ++;
    } else {
        killBtn.style.display = "block";
    }
}
function gameOver() {
        var timeLeft = 30;
        var showTimer = document.getElementById("timer");
        var timerId = setInterval(countdown, 10000);
        function endGame(){
            alert("GAME OVER");
            var killGame = document.getElementById("the-game")
            if (killGame.style.display === "none"){
                killGame.style.display = "none";
                } else {
                killGame.style.display = "none";
                }
            }
        function countdown() {
            if (timeLeft == -1 || killCount !==7) {
            clearTimeout(timerId);
            endGame();
        } else {
            alert("Thanks For Playing");
            }
        }
    }
// function play() {
//     //var audio = new Audio('');
//     //audio.play();
// }
console.log(killCount)