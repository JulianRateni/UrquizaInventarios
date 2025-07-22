const fs = require('fs')

function ReadDB(db="inventario.json"){
    const data = fs.readFileSync(db,"utf-8")
    return JSON.parse(data)
}

function WriteDB(obj,db="inventario.json"){
    if(!obj){return console.log("porfavor de un objeto para escribir")}

    try {
        fs.writeFileSync(db,JSON.stringify(obj))
        return console.log("exito")
    } catch (error) {
        return console.error(error)
    }
}