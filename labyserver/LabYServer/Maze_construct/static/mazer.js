var requestURL = 'JSON*s\\resource\\locator';
var request = new XMLHttpRequest();

request.open('GET', requestURL);

request.onload = function () {
    var userMazer = request.response;
    try {
        mazerToSVG(userMazer);
    }
    catch (exceptionVar) {
        mazerToSVG(JSON.parse(userMazer));
    }

}

function mazerToSVG(jsonObj) {
    var mazerName = document.createElement('h1');
    mazerName.textContent = 'Labyrinth #' + jsonObj['Name'];
    header.appendChild(mazerName);

    //    var svg = document.createElement('img');
}
//function updateSVG(){}

function postMazerToServer(jsonObj) {
    try {
        post
    }
    catch (exceptionVar) {
        post(JSON.stringify(jsonObj));
    }
}