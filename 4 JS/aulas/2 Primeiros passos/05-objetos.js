// declaracao de objeto
// objeto é chave-valor
const vitor = { 
    nome: "Vitor J Guerra",
    idade: 25,
    sexo: "m",

    descrever: function(){ // pode ter uma função dentro de um objeto
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}`);
    }
};

console.log('nome: ' + vitor.idade);

vitor.altura = 169; // da pra incrementar
console.log('altura: ' + vitor.altura);

delete vitor.sexo; // assim se deleta um dos atributos
console.log(vitor)

vitor.descrever()

vitor.descrever = function(){
    console.log(`Meu nome agora não é mais ${this.nome}`);
}

vitor.descrever()

const atributo = 'idade';
console.log(vitor[atributo]);
console.log(vitor['nome']);