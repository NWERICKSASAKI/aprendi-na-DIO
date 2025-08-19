// JS é fracamente tipado
var varFracamenteTipodo = 1
varFracamenteTipodo = 'viu, trocou'

// É case sensitive

// COERÇÃO DE DADOS
// tenta alterar os tipos para realizar as operações (COERÇÃO)
var var1 = 10;
var var2 = '20';


// var
// vaza dos escopos
// é declarada ao inicar o código (mas nao atribuido até chegar na sua linha)

// var 1 = 'teste' // var1 é alterado de tipo
// console.log(var1 + var2) concatena como texto
// console.log(var1 + var2) concatena como texto
console.log('var1 - var2 = ', var1 - var2) // converte o texto '20' em numero p/ realizar a operação


// hoisting
// ele pega todas as DECLARACOES de funções e variaveis (mas nao a ATRIBUIÇÃO),
// joga pra cima e roda ele a partir da 1° linha

console.log('texto = ',texto) // retorna undefined
var texto = 'texto'

teste() // funciona independente da localização da declaração
function teste(){
    console.log('function teste() = teste')
}

var teste2 = function(){
    console.log('var teste2 = function() = teste2')
}
teste2() // mas se declarar função atraves de variaveis, nao vai rodar devido ao hoisting (se posicionado antes)



if(true){
    var var_true = 10; // essa declaração vai ser içada
}
if(false){
    var var_false = 10; // essa declaração vai ser içada
}
console.log('var_true , var_false',var_true,var_false);


function variavel(){
    var var_funcao = 10; // o hoisting nao chega aqui
}



// let 
// se restringe a qualquer bloco (if while for {})
// fica no escopo do bloco
if(true){
    let let_true = 10; // nao será lido pra deste escopo
}

// const
// nao aceita reatribuição
const num = 10
// num = 11
// retorna erro



// --- CONVENÇÕES PARA DECLARAÇÃO DE VARIAVIES
//
// Variaveis
// ✅ pode começar com:
//  * letra minuscula;
//  * dolar;
//  * underline (restrita àquele espoco)
//  * usa-se camelCase para palavras compostas
// ❌ nao pode começar com numero 

// Constante
// ✅ deixar o nome da constante em CAIXA_ALTO
const PI = 3.1415




/*  TIPO DE DADOS NO JS

    6 primitivos: boolean, null, underfined, number, string e symbol
    * Primitivos são imutáveis
        let oi = 'ola'
        oi = 10
        (nao mudou, foi reatribuido)

    1 compostos: objeto 
    * Objetos é possível alterar suas atributos e carregam métodos
        const objeto = {num = 10}
        objeto.num = 20 
        (mudou o dado)

*/

//  TIPO DE COMPARAÇÃO
    console.log("10 == '10' → ", 10 == '10') // leva em conta a coerção (tenta converter)
    console.log("10 === '10' → ", 10 === '10') // não há coerção


/*  Boolean
    ! é o not
    !! é usado para converter em Boolean

    if('') → '' false
      !''  → true
      !!'' → false
*/
console.log("!!'' → ",!!'')

/* NULL x UNDEFINED

    null 
     - representa a ausencia de valor
     - "Esta variavel nao tem valor!"

    undefined
     - ausencia de declaração (inexistencia do atributo)
     - "Essa variavel nao foi declarada!"

*/
const pessoa = { nome:null, endereco:undefined}
console.log("pessoa.nome, pessoa.idade, pessoa.endereco → ", pessoa.nome, pessoa.idade, pessoa.endereco)



// --- NUMERO
// tudo é NUMBER
console.log(typeof 10, typeof 10.1, typeof NaN, typeof +Infinity, typeof -Infinity) // number number ...

/* --- Double Precision 64-bits binary format IEEE 754

    é a representação numérica do javascript (acontece em varias outras linguas)
    as contas são realizadas de forma binária
    exemplo:
    0.1 + 0.2 = 0.30000000000000004
*/

console.log("0.1 + 0.2 = ", 0.1 + 0.2)

/* 
    cuidado ao utilizar matematica precisa
    recorrer ao tipo diferente de representação

    mais detalhes: 
    https://0.30000000000000004.com/

    utilizar bibliotecas ou API
    decimal.js
*/



/*  --- STRING

    "texto"
    'texto' - usado convencionalmente
    `texto` - usado quando quer concatenar

*/

// quando a gente quer representar um HTML
console.log('<div id="10">teste</div>');
console.log("<div id=\"10\">teste</div>"); // aqui precisa usar o escape \ antes das aspas duplas


// template literal
const id = 10
console.log(`
    <div id="${id}">
        teste
    </div>
    `); // deste modo aceita quebra de linha
    // caso fosse na declaração de aspas teria que colocar \n


/* --- SYMBOL

    p/ identificadores de objetos
    garante que seja único
    está relacionado ao local da memória reservado (é unico para cada declaração

*/
const x = Symbol('10');
const y = Symbol('10');
console.log("(ambos são Symbol('10'))   →   x === y   →  ",x === y); // falso pq ambos são únicos


/* --- OBJETOS

    pode se colocar atributo
    (inclusive dinamicamente = fora da declaraçãodo objeto)
    chave:valor

*/

const pessoa1 = {
    nome:"Erick",
    idade:31,
    "país de origem":'Japão',
    falar:function(){
        console.log(`meu nome é ${this.nome}`)
    }
}
pessoa1.sobrenome = "Sasaki"
pessoa1['nacionalidade']="Brasileiro"

console.log(pessoa1)
pessoa1.falar()

const z = pessoa1.falar
z() // ele nao tem nome pq isolou à variavel a função do objeto