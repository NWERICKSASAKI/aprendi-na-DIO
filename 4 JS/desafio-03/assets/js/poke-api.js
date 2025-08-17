const pokeApi = {}

let whichID = 0;

function convertPokeApiDetailToPokemon(pokeDetail){
    const pokemon = new Pokemon();
    pokemon.number = pokeDetail.id
    pokemon.name = pokeDetail.name

    const types = pokeDetail.types.map( (typeSlot) => typeSlot.type.name )
    const [type1] = types

    pokemon.types = types
    pokemon.type = type1

    pokemon.photo = pokeDetail.sprites.other["official-artwork"].front_default
    pokemon.height = pokeDetail.height/10 // m
    pokemon.weight = pokeDetail.weight/10 // kg

    pokemon.abilities = pokeDetail.abilities.map( (abilitie_n) => abilitie_n.ability.name )

    return pokemon
}

pokeApi.getPokemonDetail = (pokemon) => {
    return fetch(pokemon.url)
    .then( (response) => response.json()) 
    .then( convertPokeApiDetailToPokemon )
}

pokeApi.getPokemons = (offset=0, limit=5) => {
    const url =  `https://pokeapi.co/api/v2/pokemon?offset=${offset}&limit=${limit}`
    return fetch(url)
        .then( (response) => response.json() ) // se der tudo certo
        .then( (jsonBody) => jsonBody.results)
        .then( (pokemons) => pokemons.map( pokeApi.getPokemonDetail ))
        .then( (detailRequests) => Promise.all(detailRequests) )
        .then( (pokemonDetails) => pokemonDetails) 
        .catch( (error) => console.log(error) )
}

// recebe uma array de promises
/* Promise.all([
    fetch('https://pokeapi.co/api/v2/pokemon/1'),
    fetch('https://pokeapi.co/api/v2/pokemon/2'),
    fetch('https://pokeapi.co/api/v2/pokemon/3')
]).then( (results) => console.log(results) )  */