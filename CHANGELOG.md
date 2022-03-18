# Log de atualizações

### Update em 18/03/2022
#### Versão do game: 36
* Adicionado o aceite do aviso de quando o login é feito via 
username e password.
* Threshold global calibrado para 0.7.
---
### Update em 06/03/2022
#### Versão do game: 35
* Alteração das imagens de conectar, quantidade de BCOIN, campo
de login e campo de senha.
* Threshold global calibrado para 0.8.
* O login com username/password (escolinha) agora funciona com
multiaccount em **abas** diferentes, o número de abas com o jogo
aberto deve ser igual ao número de username/password informados
na variável **login_credentials**, no **conf.py**.
**Obviamente você vai preferir esse tipo de login**.
* O login via Metamask no momento só está funcionando no Windows,
mas permanece da mesma forma, duas abas em cada janela, uma para
o jogo e outra para a Metamask em tela cheia.
* Função de print otimizada para o Linux, para funcionar
correntamente, não esqueça de instalar os pacotes **scrot**,
**python3-tk** e **python3-dev** via **apt**.
---
### Update em 24/02/2022
#### Versão do game: 33
* Adição da variável de configuração **login_with_metamask**,
você escolhe qual o método de autenticação informando **True**
ou **False**. Se **True**, tenha o cuidado de deixar a janela do
browser aberta com duas abas, uma para o Bombcrypto e outra
para a Metamask em tela cheia. Se **False**, não será necessária
a aba com a Metamask. O método de login com username e password não
suporta múltiplas abas e sim, múltiplas **janelas**, esteja
avisado.
* Adição da variável **login_credentials**, você informa os pares
de usuário:senha quando a variável **login_with_metamask** for
**False**, se você possui várias contas, basta duplicar a linha
**'username': 'password',** e informar as novas credenciais
**de acordo com o número de contas**.
* Pequenas mudanças em geral, não afeta o uso.