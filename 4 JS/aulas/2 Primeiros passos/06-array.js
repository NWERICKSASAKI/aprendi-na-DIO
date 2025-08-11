const contante = 1;
let variavel = 1;
const objeto = {};
const listaAlunos = ['Ana','Bob','Carlos'];

// lista aceita varios tipos de dados

// adicionando
listaAlunos.push('Diego');
listaAlunos[4] = 'Euler';

// substituindo
listaAlunos[1] = 'Bia';

// retirando
listaAlunos.pop(); // o último
listaAlunos.shift(); // o primeiro


console.log(listaAlunos);


// percorrendo a lista ///////////////////////////
// com estrutura de repetição
const notas = [5,7,8,2,5,8];
let numProvas = notas.length;
let soma_nota = 0;

soma_nota = 0;
for (let i = 0; i < notas.length; i++) {
    soma_nota += notas[i];
}

// ou
soma_nota = 0;
for (let i in notas){
    soma_nota += notas[i];
}

console.log(`A média é ${soma_nota/numProvas}`)

///////////////////////////////////////////////
// string também é considerando um Array
const nome = 'Vitor Johansen Guerra' 
for (i in nome){
    console.log(nome[i])
}