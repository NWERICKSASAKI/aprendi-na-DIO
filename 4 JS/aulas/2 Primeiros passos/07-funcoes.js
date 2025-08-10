// importacao

function print(texto){
    console.log(texto);
}

function gets(){
    return 10;
}

module.exports = {
    gets: gets, // se tem o mesmo nome, nao precisa declarar :nome
    print: print
}

// ou pode ser assim tambem
// module.exports.gets = gets;