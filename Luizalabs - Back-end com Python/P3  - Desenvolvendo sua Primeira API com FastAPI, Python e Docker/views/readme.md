# Views

(Nem sempre usadas em APIs puras — depende do framework.)  
Camada que formata a saída (renderização de páginas ou transformação da resposta).

## Propósito

* Em aplicações Web tradicionais: renderizar HTML.
* Em APIs: às vezes ajustar a saída (DTOs, serializers).

## Quando usar

* Em APIs REST modernas: pode nem existir ou ser substituída por serializers/DTOs.
* Em frameworks como Django ou Rails: usado para gerar páginas ou respostas já formatadas.
