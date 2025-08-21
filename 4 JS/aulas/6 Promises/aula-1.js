/*  Assincronismo - Promises

    não executa de forma imediata
    é um I/O

    coisas que nao temos controles e uma hora vai voltar pra gente

    exemplo: 
        * Ler um arquivo do disco
        * Navegar na internet
*/


new Promise( (resolve, reject) => {
    // ...    
    // ...    
    // resolve -- caso der certo    
    // ...    
    // ...    
    // reject -- caso der errado
})

// Promise funciona até com funções nao-assicronas
const promessaNumQualquer = new Promise( (resolve, reject) => {
    setTimeout(() => {
        const num = parseInt(Math.random()*100)
        resolve(num)
    },1000)
})

console.log('iniciou')
promessaNumQualquer
    .then( (value) => {
        console.log(value)
        return value + 100
    })
    .then( (value) => {
        console.log(value)
    })
    .catch( (error) =>{
        console.log(error)
    })
    .finally( () =>{
        console.log('finalizou')
    })
console.log('eai?')






/*  Manipulando arquivo  */
const fs = require('fs')
const path = require('path')
const filPath = path.resolve(__dirname, 'tarefas.csv')

// fs.readFile() - formato antigo
//const promessaLeituraCSV = fs.promises.readFile('4 JS/aulas/6 Promises/tarefas.csv')
const promessaLeituraCSV = fs.promises.readFile(filPath)

promessaLeituraCSV
    .then( (arquivo) => arquivo.toString('utf8') )
    .then( (textoDoCSV) => textoDoCSV.split('\n').slice(1) )
    .then( (linhasSemCabecalho) => linhasSemCabecalho.map( (linha) =>{
        const [nome,feito] = linha.split(';')
        return  {
            nome,
            feito: feito.trim() === 'true'
        }
    }))
    .then( (listaDeTarefas) => console.log(listaDeTarefas) )
    .catch((error) => console.log('deu ruim: ' + error))





/*  ASYNC AWAIT 

    forma diferente de usar promises
    then, catch e finally

    fica mais fácil de ler
    pq abstrai para uma forma procedural
*/

async function buscarArquivo(){ // só posso usar AWAIT se o tiver ASYNC 
    try{
        const arquivo = await fs.promises.readFile(filPath)
        const textoDoArquivo = arquivo.toString('utf-8')
        console.log(textoDoArquivo)
    } catch (error) {
        console.log(error)
    } finally {
        console.log('fim')
    }
}

buscarArquivo()


