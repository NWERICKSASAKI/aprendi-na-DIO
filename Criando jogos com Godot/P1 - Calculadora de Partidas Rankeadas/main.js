function retornaRank(saldo){
    if (saldo <= 10) {
        return "Ferro"
    } else if (saldo <= 20) {
        return "Bronze"
    } else if (saldo <= 50) {
        return "Prata"
    } else if (saldo <= 80) {
        return "Ouro"
    } else if (saldo <= 90) {
        return "Diamente"
    } else if (saldo <= 100) {
        return "Lendário"
    } else if (saldo > 101) {
        return "Imortal"
    }
}

function main(vitorias, derrotas){
    let saldo = vitorias - derrotas
    let rank = retornaRank(saldo)
    print("O Herói tem de saldo de " + saldo + "está no nível de " + rank)
}
