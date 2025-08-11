// Classe é a definição
// Instancia é a ocorrencia
class Pessoa{
    nome;
    idade;
    sexo;
    cidade;
    anoDeNascimento

    // constructor é o que acontece quando é instanciado
    constructor(nome, idade){
        this.nome = nome;
        this.idade = idade;
        this.anoDeNascimento = 2025-idade;
    }
    // dentro classe nao precisa declarar function
    descrever() {
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}`);
    }
}

// instancionando uma pessoa nova
const vitor = new Pessoa('Vitor J Guerra', 25);
vitor.sexo = 'm';
vitor['cidade'] = 'São Paulo';

console.log(vitor);
vitor.descrever();

//

const erick = new Pessoa('Erick', 31);

function compararPessoa(p1, p2){
    // retorna quem é a mais velha
    if (p1.idade > p2.idade){
        console.log(`${p1.nome} é a mais velha que ${p2.nome}`);
    } else if (p1.idade < p2.idade){
        console.log(`${p2.nome} é a mais velha que ${p1.nome}`);
    } else {
        console.log(`${p2.nome} e ${p1.nome} tem a mesma idade`)
    }
}


compararPessoa(erick,vitor)