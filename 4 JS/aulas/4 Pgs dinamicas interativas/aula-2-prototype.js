/* --- Orientação a Protótipo

    um obj é uma coleção dinamica de chave-valor

    em orientação a protótipo
    protótipo é a base do objeto
*/

const pessoa = {
    genero: 'masculino'
}

const renan = {
    nome:'renan',
    idade:30,
    __proto__: pessoa // renan está herdando as propriedades de pessoa
                      // é a forma que fazemos Herança em JS
}

// ao tentar encontrar um atributo, ele procura 1° no objeto e depois vai nos protótipos
console.log(renan.genero)


/* Funções construtoras
   começa com letra maiúscula
*/

function Pessoa(nome, idade){
    this.nome = nome;
    this.idade = idade;
}

// se quiser colocar um método
Pessoa.prototype.falar = function(){
    console.log(`Meu nome é ${this.nome}`)
}

const erick = new Pessoa('erick',31)
console.log(erick)
erick.falar()

// Equivalente à / mesma coisa
// Classe foi montado com base em função construtora + prototipagem e métodos
class Humano {
    constructor(nome,idade){
        this.nome = nome;
        this.idade = idade;
    }

    falar() {
        console.log(`Meu nome é ${this.nome}`)
    }
}

/* SOBRESCRITA e SHADOWING */

const animal = {
    idade: 10
}

const abigail = {
    nome: 'abigail',
    idade: 9,
    __proto__: animal
}

console.log(abigail.idade) // 1° procura no OBJETO, caso nao encontrar vai no Protótipo


// Formas de criar Objetos
//
// 1) de forma literar
const homem={
    genero:'masculino'
}

// homem.__proto__

const eu = {
    nome:'erick',
    __proto__:homem
}

// 2) usando Object
const mim = Object.create(homem)
mim.nome = 'erick'
console.log(eu.genero, mim)



// 3) NEW

Pessoa.prototype.falar = function(){
    console.log(`Meu nome é ${this.nome}`)
}
const eusebio = new Pessoa('Eusebio',29)
eusebio.falar()

// 4) CALL
const eusebia = {
    genero:'feminino'
}
Pessoa.call(eusebia,'Eusebia',30)
console.log(eusebia)





String.prototype.toPLang = function(){
    return `P ${this}`
}

console.log('teste'.toPLang())


