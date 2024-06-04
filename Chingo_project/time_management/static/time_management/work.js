const timerBtn = document.querySelector('.time-btn');
const timerForm = document.getElementById('timer-form');
const dateStart = document.querySelector('.date-start');
const dateEnd = document.querySelector('.date-end');
const workTime = document.querySelector('.work-time');
const changeLight = document.querySelector('.light');

const begin = [];
workTime.style.display = 'none';




timerBtn.addEventListener('click', function(event){
    event.preventDefault();
    console.log("one");
    console.log(timerBtn.value);
    if(timerBtn.innerHTML === 'Start'){
        workTime.style.display = 'none';
        
        
        console.log("two");
        resetTimer();
        startTimer();
        timerBtn.style.backgroundColor = '#d60000';
        timerBtn.style.boxShadow = '0px 0px 40px 0px rgb(196 35 95 / 75%)';
        timerBtn.innerHTML = "End";
        const now = new Date();
        begin.push(now.toLocaleTimeString());
        console.log(now.toLocaleDateString());
        
    }else {
        const now = new Date();
        
        const amount = document.getElementById('timerDisplay').innerText;
        const end = now.toLocaleTimeString();
        const date = now.toLocaleDateString();
        timerBtn.style = 'inherit';
        timerBtn.innerHTML = "Start";
        console.log('three');
        endTimer();

        workTime.style.display = 'flex';

        workTime.innerHTML = `<strong>Дата: ${date}</strong><strong>Кол-во ${amount}</strong>`;
        
        fetch('/main', { // it should send to this site, like a <form method="post" acction=""> does
            method: 'POST',

            body: JSON.stringify({
                start: begin[0],
                end: end,
                date: date,
                amount: amount
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        })
        begin.pop();
    }
});


let timer;
let seconds = 0;
let minutes = 0;
let hours = 0;


function startTimer() {
    timer = setInterval(updateTimer, 1000);
    const now = new Date(); console.log(now);
}

function endTimer() {
    clearInterval(timer);
}

function resetTimer() {
    clearInterval(timer);
    seconds = 0;
    minutes = 0;
    hours = 0;
    document.getElementById('timerDisplay').innerText = "00:00:00";
}

function updateTimer() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
        if (minutes >= 60) {
            minutes = 0;
            hours++;
        }
    }

    const timeString = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds < 10 ? "0" + seconds : seconds);
    document.getElementById('timerDisplay').innerText = timeString;
}


var timeElement = document.getElementById('currentTime');
setInterval(function () {
  var currentTime = new Date();
  timeElement.textContent = currentTime.toLocaleTimeString();
}, 100000000);