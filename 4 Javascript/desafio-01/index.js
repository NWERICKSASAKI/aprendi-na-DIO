/*
Instruções para entrega
# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000 = Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"

*/

function retonaNivel(nome, xp){
    if(xp >= 10_001){
        return "Radiante";
    } else if (xp >= 9_001){
        return "Imortal";
    } else if (xp >= 8_001){
        return "Ascendente";
    } else if (xp >= 7_001){
        return "Platina";
    } else if (xp >= 5_001){
        return "Ouro";
    } else if (xp >= 2_001){
        return "Prata";
    } else if (xp >= 1_001){
        return "Bronze";
    } else {
        return "Ferro";
    }

}

function main(){
    let equipeDeHerois = [ ["Maximus",12345] , ["Eugenio",9876] , ["Anasthacia",7654] , ["Ariranha", 999] ];

    for (i in equipeDeHerois){
        let nomeHeroi = equipeDeHerois[i][0];
        let xpHeroi = equipeDeHerois[i][1];
        let nivel = retonaNivel(nomeHeroi,xpHeroi);
        console.log(`O Herói de nome ${nomeHeroi} está no nível de ${nivel}`)
    }
}

main()