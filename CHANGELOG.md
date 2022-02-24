# Log de atualizações

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