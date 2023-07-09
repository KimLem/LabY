class LabyrinthScene {
    constructor(rows, columns, height, width) {
        this.rows = rows;
        this.columns = columns;
        this.height = height;
        this.width = width;
    }

    get vDimension() {
        return Math.floor(this.height / this.rows);
    }

    get hDimension() {
        return Math.floor(this.width / this.columns);
    }

    // /**
    //  * @param {(arg0: { Type: string; X: number; Y: number; }[]) => void} walls
    //  */
    // set wallsOnScene(walls) {
    //     this.walls = walls;
    // }

    drawScene(walls, wallWidth) {

        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");
        const wallsFactory = new WallsFactory();
        const vDim = this.vDimension;
        const hDim = this.hDimension;

        // ctx.scale(hDim, vDim);


        walls.forEach(wall => {
            wallsFactory.adjust(wall, ctx, vDim, hDim, wallWidth);
        });

        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, this.height, wallWidth);
        ctx.fillRect(0, 0, wallWidth, this.width);



    }

    clearScene() {
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");
        ctx.reset();
    }

}

class WallsFactory {
    adjust(wall, ctx, vDim, hDim, width) {
        let x = hDim * wall.X;
        let y = vDim * wall.Y;

        switch (wall.Type) {
            case 'horizontal':
                this.#getHWall(ctx, x, y, hDim, width);
                break;
            case 'vertical':
                this.#getVWall(ctx, x, y, vDim, width);
                break;
            default:
                console.log("Type Error");
                break;
        }
    }
    #getHWall(ctx, x, y, hDim, width) {
        ctx.fillStyle = "red";
        ctx.fillRect(x, y + hDim, hDim, width);
    }
    #getVWall(ctx, x, y, vDim, width) {
        ctx.fillStyle = "blue";
        ctx.fillRect(x + vDim, y, width, vDim);
    }
}

function mazerBuild() {

    // const canvas = document.getElementById("canvas");
    // const pMazer = document.getElementById("pMazer");
    // pMazer.style.visibility = 'hidden';

    let rows = 10;
    let columns = 10;
    let height = 100;
    let width = 100;
    let wallSize = 1;

    let mazerScene = new LabyrinthScene(rows, columns, height, width);
    console.log(mazerScene);

    // let walls2 = pMazer.value;
    console.log(walls);
    var walls = [{ "__Wall__": true, "Type": "vertical", "X": 1, "Y": 0 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 0 }, { "__Wall__": true, "Type": "horizontal", "X": 4, "Y": 0 },
    { "__Wall__": true, "Type": "horizontal", "X": 6, "Y": 0 }, { "__Wall__": true, "Type": "horizontal", "X": 8, "Y": 0 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 0 },
    { "__Wall__": true, "Type": "horizontal", "X": 9, "Y": 0 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 1 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 1 },
    { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 1 }, { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 1 }, { "__Wall__": true, "Type": "vertical", "X": 6, "Y": 1 },
    { "__Wall__": true, "Type": "horizontal", "X": 6, "Y": 1 }, { "__Wall__": true, "Type": "vertical", "X": 8, "Y": 1 }, { "__Wall__": true, "Type": "horizontal", "X": 8, "Y": 1 },
    { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 1 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 2 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 2 },
    { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 2 }, { "__Wall__": true, "Type": "horizontal", "X": 4, "Y": 2 }, { "__Wall__": true, "Type": "vertical", "X": 6, "Y": 2 },
    { "__Wall__": true, "Type": "vertical", "X": 7, "Y": 2 }, { "__Wall__": true, "Type": "horizontal", "X": 7, "Y": 2 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 2 },
    { "__Wall__": true, "Type": "horizontal", "X": 9, "Y": 2 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 3 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 3 },
    { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 3 }, { "__Wall__": true, "Type": "horizontal", "X": 4, "Y": 3 }, { "__Wall__": true, "Type": "vertical", "X": 5, "Y": 3 },
    { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 3 }, { "__Wall__": true, "Type": "horizontal", "X": 9, "Y": 3 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 4 },
    { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 3, "Y": 4 },
    { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 5, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 6, "Y": 4 },
    { "__Wall__": true, "Type": "vertical", "X": 7, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 4 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 3, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 6, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 7, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 8, "Y": 5 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 5 },
    { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 3, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 5, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 7, "Y": 6 }, { "__Wall__": true, "Type": "horizontal", "X": 7, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 8, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 6 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 7 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 7 }, { "__Wall__": true, "Type": "horizontal", "X": 3, "Y": 7 }, { "__Wall__": true, "Type": "horizontal", "X": 5, "Y": 7 }, { "__Wall__": true, "Type": "horizontal", "X": 7, "Y": 7 }, { "__Wall__": true, "Type": "vertical", "X": 8, "Y": 7 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 7 }, { "__Wall__": true, "Type": "vertical", "X": 0, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 8 }, { "__Wall__": true, "Type": "horizontal", "X": 1, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 4, "Y": 8 }, { "__Wall__": true, "Type": "horizontal", "X": 4, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 5, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 7, "Y": 8 }, { "__Wall__": true, "Type": "horizontal", "X": 7, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 8, "Y": 8 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 8 }, { "__Wall__": true, "Type": "horizontal", "X": 0, "Y": 9 }, { "__Wall__": true, "Type": "vertical", "X": 1, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 1, "Y": 9 }, { "__Wall__": true, "Type": "vertical", "X": 2, "Y": 9 },
    { "__Wall__": true, "Type": "horizontal", "X": 2, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 3, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 4, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 5, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 6, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 7, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 8, "Y": 9 }, { "__Wall__": true, "Type": "vertical", "X": 9, "Y": 9 }, { "__Wall__": true, "Type": "horizontal", "X": 9, "Y": 9 }];

    mazerScene.drawScene(walls, wallSize);


}

function setLabyrinth(dataLabyrinth) {

    let walls = dataLabyrinth.walls;
    let rows = dataLabyrinth.rows;
    let columns = dataLabyrinth.columns;
    let height = 100;
    let width = 100;
    let wallSize = 1;

    let mazerScene = new LabyrinthScene(rows, columns, height, width);
    mazerScene.clearScene();
    mazerScene.drawScene(walls, wallSize);


}

function getRequest2() {

    const url = "/labyrinth/getNewLabyrinth";


    fetch(url, {
        method: "GET",
    })
        .then((response) => {
            return response.json();
        }).then((data) => {
            setLabyrinth(data)
        });

    console.log(url);

}

function setLParams() {

    const url = "/labyrinth/setLParams";
    console.log("1");

    const data = { rows: document.getElementById(labyrinthRows), columns: document.getElementById(labyrinthColumns) };
    console.log(data);

    try {
        const response = fetch(url, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const json = response.json().then((data) => {
            setLabyrinth(data)
        });;
        console.log('Success:', JSON.stringify(json));
    } catch (error) {
        console.error('Error:', error);
    }

}
