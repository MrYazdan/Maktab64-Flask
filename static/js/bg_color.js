let bg1 = "black"
let bg2 = "orangered"

let color = true

setInterval(function () {
    document.body.style.backgroundColor = (color ? bg1 : bg2)
    color = !color
}, 2500)
