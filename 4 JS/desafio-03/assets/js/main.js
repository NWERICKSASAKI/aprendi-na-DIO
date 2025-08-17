
// Fectch API já está disponível no browser mais modernos
// Google: Fetch API json


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

// window -  da acesso ao browser
// document - da acesso ao HTML



function covertPokemonTypesToLi(pokemonTypes){
    return pokemonTypes.map((typeSlot) => `<li class="type">${typeSlot.type.name}</li>`)
}

const pokemonList = document.getElementById('pokemonList')
const loadMoreButton = document.getElementById('loadMoreButton')
const limit = 5;
let offset = 0;

const maxRecords = 11; // pra remover o botao de carregar mais (ficar só na 1° geração)


pokemonList.addEventListener('click', (event) => {
  const card = event.target.closest('.pokemon');
  if (card) {
    // exemplo: pega o número do Pokémon que você já renderiza no span
    const id = card.querySelector('.number').textContent.replace('#', '');
    
    // redireciona para a página de detalhes
    window.location.href = `./pokemon_details.html?id=${id}`;
  }
});


function loadPokemonItens(offset,limit){
    pokeApi.getPokemons(offset,limit).then((pokemons = []) => {
        const newHTML = pokemons.map((pokemon) => `
            <li class="pokemon ${pokemon.type}">
                <span class="number">#${pokemon.number}</span>
                <span class="name">${pokemon.name}</span>
                <div class="detail">
                    <ol class="types">
                        ${pokemon.types.map(( type ) => `<li class="type ${type}">${type}</li>` ).join(' ')}
                    </ol>
                    <img src="${pokemon.photo}" 
                        alt="${pokemon.name}">
                </div>
            </li>
        `).join('')
        pokemonList.innerHTML += newHTML
    })

}

loadPokemonItens(offset,limit)

loadMoreButton.addEventListener("click", () => {
    offset += limit;
    const qtdRecordNextPage = offset + limit;
    
    if (qtdRecordNextPage >= maxRecords){
        const newLimit = maxRecords - offset;
        loadPokemonItens(offset,newLimit);
        loadMoreButton.parentElement.removeChild(loadMoreButton);
    } else {
        loadPokemonItens(offset,limit)
    }
})


