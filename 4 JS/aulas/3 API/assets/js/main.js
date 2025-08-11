
// Fectch API já está disponível no browser mais modernos
// Google: Fetch API json

const offset = 0
const limit = 10
const url =  `https://pokeapi.co/api/v2/pokemon?offset=${offset}&limit=${limit}`

// retorna uma Promise (processamento assincrono -> nao tem resposta imediata)
// Promise = promessa de um resultado, ou seja, uma hora você vai receber a resposta (se der tudo certo)
// Abaixo: Recebe a resposta e então executa a função

/*
    fetch(url)
        .then(function(response){ // se der tudo certo

            response
                .json()
                .then(function(responseBody){
                    console.log(responseBody)
            })

        })
        .catch(function(error){ // se der erro
            console.log(error)
        })
        .finally(function(){ // assim que terminar tudo
            console.log('Requisição concluída')
        })
*/

/* ENCADEAMENTO DE THEN
    fetch(url)
        .then(function(response){ // se der tudo certo
            return response.json()
        })
        .then(function(jsonBody){ // se pegar o body json
            console.log(jsonBody)
        })
        .catch(function(error){ // se der erro
            console.log(error)
        })
        .finally(function(){ // assim que terminar tudo
            console.log('Requisição concluída')
        })
*/


/* Arrow-function
    .then((response) => { // se der tudo certo
        return response.json()
    })

    //virou 
    .then( (response) => response.json() ) // se der tudo certo
*/

function covertPokemonToLi(pokemon){
    return `
        <li class="pokemon">
            <span class="number">#001</span>
            <span class="name">${pokemon.name}</span>
            <div class="detail">
                <ol class="types">
                    <li class="type">grass</li>
                    <li class="type">poison</li>
                </ol>
                <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png" alt="${pokemon.name}">
            </div>
        </li>
    `
}

fetch(url)
    .then( (response) => response.json() ) // se der tudo certo
    .then( (jsonBody) => jsonBody.results)
    .then( (pokemons) => {

        for (let i = 0; i < pokemons.length; i++) {
            const pokemon = pokemons[i];

            // window -  da acesso ao browser
            // document - da acesso ao HTML
            const pokemonList = document.getElementById('pokemonList')
            pokemonList.innerHTML += covertPokemonToLi(pokemon)
        }

        debugger // caso o DevTools esteja ativo
        console.log(pokemonsList)
    } )
    .catch( (error) => console.log(error) )// se der erro

console.log('por mais que esteja declarada depois, este print vai aparecer primeiro')

