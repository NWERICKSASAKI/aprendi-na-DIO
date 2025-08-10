/* 
    2 - Crie uma classe para representar pessoas.
    Para cada pessoa teremos os atributos nome, peso e altura.
    As pessoas devem ter a capacidade de dizer o valor do seu IMC (IMC = peso / (altura*altura));
    Instancie uma pessoa chaada José que tenha 70kg de peso e 1.75 de altura
    e peça ao José para dizer o valor do seu IMC;
*/

class Pessoa{
    nome;
    peso;
    altura;
    imc;

    constructor(nome, peso, altura){
        this.nome = nome;
        this.peso = peso;
        this.altura = altura
    }

    calcularImc(){
        this.imc = (this.peso / (this.altura * this.altura))
        console.log(`${this.nome} tem ${this.imc} de IMC`)
        return this.imc
    }
}

const Jose = new Pessoa('José', 70, 1.75)
Jose.calcularImc()