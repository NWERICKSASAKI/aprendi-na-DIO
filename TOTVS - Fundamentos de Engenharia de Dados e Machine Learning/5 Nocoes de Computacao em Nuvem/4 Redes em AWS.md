# 4 Redes em AWS

## 4.1 Amazon VPC

Como organizamos nossos recursos nas AWS?

Como se conecta uma instância com outra instância?

**VPC** - *Virtual Private Cloud*  

* Permite construir e configurar redes virtuais na AWS  
* Sub-redes: privadas e públicas  
* "Tudo começa dentro de um VPC"  

## 4.2 Conectividade com AWS

Sup rede pública

IGW - É Gateway, conecta a interna a sub-rede pública, ela recebe as requisições externas e redireciona às suas sub-redes públicas.

Gateway Privado Virtual, conectar ao VPC à Internet.

AWS Direct Connect - serviço, basicamente é uma conexão direta (fibra ótica) do seu datacenter corporativo à AWS.

## 4.3 Sub-redes e listas de controle de acesso

Como dados trafegam em uma VPC?

### 4.3.1 Network ACLs

Toda sua sub rede tem um Network ACL que controla a entrada e saída das sub-redes.

Ele não guarda estado (stateless), ele trabalha com regras de entrada e saída de dados.

Eu chamei uma conexão de DB no IP X e porta Y, o ACL olha se tem regra para ese tipo de conexão e se estiver tudo OK permite a conexão, ou bloqueia caso não estiver mapeada.

Por padrão a Network ACLs permite toda entrada e saída, então assim que criá-lo precisa configurar as restrições.

### 4.3.2 Segurança para recursos

Um pacote chegou da internet, passa pelo gateway e network ACL, ai chega numa instância EC2 (e passa pelo grupo de segurança)

Grupos de segurança, pode-se criar grupos para suas instâncias EC2.

Essa camada de segurança adicional controla também o controle de tráfago e de entrada e saída de dados.

* Controle de tráfego de entrada e saída de instância EC2
* Comportamento Stateful (uma vez que o pacote chega até a entrada e é permitido entrar e *automaticamente pode sair*)
* Por padrão, ❌ nega todo o tráfego de entrada e ✅ permite todo tráfego de saída.
