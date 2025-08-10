/* 
    1 - Crie uma classe para representar carros:

    Os carros possuem marca, uma cor e um gasto médio de combustível por km rodado.

    Crie um método que dado a quantidade de km e o preço do combustível nos dê o valor
    gasto em reais para realizar este percurso
*/

class Carro{
    marca;
    cor;
    gastoMedio;

    constructor(marca,cor,gastoMedio){
        this.marca = marca;
        this.cor = cor;
        this.gastoMedio = gastoMedio;
    }

    quantoCustaParaPercorrerEsseTrecho(trecho){
        console.log( this.gastoMedio)
        return this.gastoMedio * trecho
    }
}

const kiwi = new Carro('Renault', 'Prata', 20)
console.log(`Para percorrer 20km vou gastar ${kiwi.quantoCustaParaPercorrerEsseTrecho(20)}`)