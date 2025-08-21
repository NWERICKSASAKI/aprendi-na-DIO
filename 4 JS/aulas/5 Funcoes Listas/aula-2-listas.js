for (let index = 0; index < array.length; index++) {
    const element = array[index];
    
}

let lista = ['ana','bob','caio','dio']

// FOREACH
// é um pouco mais lento que o FOR tradicional

lista.forEach( (value, i, listRef) => {
    console.log(value, i, listRef)
})


// FILTER
listaNum = [1,2,3,4,5,6,7,8,9,10]
const listaDePares = listaNum.filter((element) => {
    return element % 2 === 0
})

console.log(listaDePares)


// MAP
class Pessoa {
    constructor(name){
        this.name=name
    }
}

const listaPessoas = [new Pessoa('Renan'), new Pessoa('Ana'), new Pessoa('Bob'), new Pessoa('Caio')]

/*
    const listaNomes = []
    for (let i = 0; i < listaPessoas.length; i++) {
        const element = listaPessoas[i];   
        listaNomes.push(element.name)
    }
*/

// equivalente à

/*
    const listaNomes = lista.map( (element) => {
    return element.name
    } )
*/

// equivalente à

const listaNomes = lista.map( (element) => element.name )
console.log(listaNomes)




// REDUCE
// percorrendo toda a lista e reduzir a um unico valor
const soma = listaNum.reduce( (previous,current) => {
    return previous + current
}, 0) // ,0 ← valor inicial do reduce


console.log(soma)



// JOIN 
// junta a lista em uma string
console.log( listaNum.join(' + ') )