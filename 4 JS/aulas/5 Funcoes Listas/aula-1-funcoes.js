/*
    First Class Function
    High Order Functions

        na prática, Uma função:
        * pode ser atribuida a uma variavel
        * pode ser passada como parametro
        * e também retornada como respostas
        * nome das funções são meros detalhes, só precisa da referência

*/

function falarMeuNome(){
    console.log(`Meu nome é Renan`)
}

const referenciaNova = falarMeuNome
referenciaNova()


// passando função na função
function falarMeuNomeCompleto(falarMeuNome){
    falarMeuNome()
    console.log('Johannsen de Paula')
    return
}

falarMeuNomeCompleto(falarMeuNome)


/*
    Function Declaration
    Function Expression
*/

// function declaration
function nomeDaFuncao(){
    console.log('nomeDaFuncao')
}

// function expression
const nomeDeOutraFuncao = function () { // devido ao hoisting → pode nao funcionar (erro)
    console.log('nomeDeOutraFuncao')
}

nomeDaFuncao()
nomeDeOutraFuncao()




/*
    Declaração Explícita - ✅ tem contexto
    Arrow Function       - ❌ não tem contexto / ✅ ajuda o código a ficar mais simples/enxuto
*/

function declaracaoExplicita(){
    console.log(this)
}

//                    () parametro
//                          {} corpo da função
const arrowFunction = () => {
    console.log(this)
}

const renan = {
    nome: 'Renan',
    declaracaoExplicita,
    arrowFunction
}

renan.declaracaoExplicita() // imprime todo o contexto
renan.arrowFunction() // não tem 'this'




/* CLOSURE ou FECHAMENTO
    quando a gente declara uma função, ela lembra o contexto de quando foi declarada.
*/

function soma(x){
    return function(y){
        return x+y;
    }

    // tambem equivalente
    return (y) => {
        return x+y;
    }
}

console.log( soma(10)(20) )

const somaParcial = soma(10)

console.log(somaParcial(20))


/* Formas de invocar função */

// declaração explicita
function teste(){
    console.log('teste')
}

teste()


// APPLY

const pessoa = {
    nome:'renan',
    idade:30
}

function gritar(prefixo){
    console.log(prefixo, this.nome)
}
            // contexto , [argumentos]
gritar.apply(pessoa, ['Sr.'])

// CALL
gritar.call(pessoa, 'Sr.')



/* Callbacks */
// recebendo uma Função como Parâmetros


function adicao(x,y){
    return x+y;
}

function multiplicacao(x,y){
    return x*y;
}

function calcular(x,operacao,y){
    console.log(operacao(x,y))
}

calcular(11, adicao, 22) // estrategy

// similar à
document.getElementById('btn1').addEventListener('click', () => {
    console.log('clicou')
})