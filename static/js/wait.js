var e = document.getElementById("count");
e.onclick = countDown;
let sec = 10;
let intervalId;

function countDown(){
    intervalId = setInterval(delta, 1000);
}

function delta(){
    if (sec>=0) {
        e.innerHTML = "<img src='/media/please-wait.png'/><h1>"+sec+"</h1>";
        sec--;
    }else{
        clearInterval(intervalId);
        document.getElementById("lower_btn").innerHTML = "<a href='/download/'><img src='/media/download.png'/></a>";
        location.assign("#lower_btn");
        e.innerHTML = "<h1>Bye</h1>";
    }
}