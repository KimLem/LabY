import { LabyrinthScene } from './modules/setMazer.js'
console.log("Success!")

var requestURL = 'JSON*s\\resource\\locator';
console.log("Success2!")
var request = new XMLHttpRequest();
console.log("Success3!")

request.open('GET', requestURL);
console.log("Success4!")
// request.onload = function () {
//     var userMazer = request.response;
//     // try {
//     console.log("YO1!!!")
//     mazerBuild(userMazer);
//     console.log("YO2!!!")
//     // }
//     // catch (exceptionVar) {
//     //     mazerBuild(JSON.parse(userMazer));
//     // }

// }

function mazerBuild(jsonObj) {
    var mazerName = document.createElement('h1');
    console.log("YO3!!!")
    mazerName.textContent = 'Labyrinth #' + jsonObj['Name'];
    header.appendChild(mazerName);
    var mScene = LabyrinthScene(jsonObj['rows'], jsonObj['columns'], height, width)
    mScene.drawScene(jsonObj['walls']);
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
