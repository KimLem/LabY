class LabyrinthScene {
    constructor(rows, columns, height, width) {
        this.rows = rows;
        this.columnns = columns;
        this.height = height;
        this.width = width;
    }

    get vDimension() {
        return Math.floor(this.height / this.rows);
    }

    get hDimeиnsion() {
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
        const vDim = this.vDimension();
        const hDim = this.hDimension();

        walls.forEach(wall => {
            wallsFactory.adjust(wall, ctx, vDim, hDim, wallWidth);
        });

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
        ctx.fillStyle = "green";
        ctx.fillRect(x, y, x + hDim, y + width);
    }
    #getVWall(ctx, x, y, vDim, width) {
        ctx.fillStyle = "green";
        ctx.fillRect(x, y, x + width, y + vDim);
    }
}
export { LabyrinthScene };
// var puk = new LabyrinthScene(5, 10, 900, 1600);
// var walls = [{ Type: "horizontal", X: 10, Y: 20 }, { Type: "vertical", X: 20, Y: 30 }, { Type: "horizontal", X: 40, Y: 50 }];
// puk.drawScene(walls, 10);
// console.log(puk)
