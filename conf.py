# Regula o nível de confiança para o bot considerar que encontrou a imagem requerida,
# um valor abaixo de 0.6 não é confiável, assim como um valor acima de 0.9 é impossível,
# se mesmo após vários testes o bot ainda continuar clicando no lugar inesperado, entre
# na pasta pics onde encontram-se todos os "alvos clicáveis" e substitua a imagem que
# ele está errando, pela mesma imagem, na sua resolução, assim irá funcionar, o padrão
# é 0.7
# !APENAS VALORES NUMÉRICOS de 0.6 até 0.9
threshold = 0.7

# Delay para logar novamente e colocar todos os bhero para trabalhar, informe sempre
# o tempo em segundos, calcule um tempo legal em que todos os seus bhero se recuperam
# e podem voltar ao trabalho, todos de uma vez, o padrão é 4400 segundos (1h e 22m)
# !APENAS VALORES NUMÉRICOS
time_to_rest = 4400

# Delay para logar novamente e fugir do erro das pedras com vida infinita (uhmm)
# e também salvar algum eventual bhero bugado no mapa, antes de dar o refresh, o bot
# vai voltar na tela inicial para evitar o bug do rollback (uhmm²), sempre informe o
# tempo em segundos, 360 segundos (6m) é o padrão
# !APENAS VALORES NUMÉRICOS
time_to_refresh = 360

# Número de tentavivas para procurar uma imagem requerida, se o bot não encontrar a
# imagem que procura, irá reinciar o processo novamente (recarregar o browser, conectar
# no jogo, etc...), 60 é o valor padrão, dá aproximadamente 1m procurando uma imagem
# !APENAS VALORES NUMÉRICOS
max_attempt_found_img = 30

# Se deseja ou não fazer login utilizando a Metamask, o padrão é True, mas, se você
# optar por False, tenha certeza de já ter criado seu login de usuário do Bombcrypto,
# se deseja logar sem a Metamask e tem dúvidas de como criar seu login, entre nos
# canais oficiais e veja o procedimento, no grupo https://t.me/BombCryptoBR você
# encontra o passo a passo na mensagem fixada #33, o padrão é True
# !APENAS VALORES BOOLEANOS, True OU False, SEM ASPAS
login_with_metamask = True

# Se optou por NÃO fazer login utilizando a Metamask e já criou seu login e senha do
# Bomcrypto, basta substituir os valores em username e password, MUITA ATENÇÃO se
# você está utilizando multiaccount, ou seja, mais de uma janela aberta com o jogo,
# duplique a linha "'username': 'password'," e vá colocando novos usuários e senhas
# de acordo com as contas que você configurou, informe as credenciais corretas, pois
# se o bot identificar o erro "Invalid username or password", a janela em questão será
# fechada, o número de janelas abertas deve ser igual ao número de pares username:password
# fornecidos
# !APENAS VALORES DE TEXTO, COM ASPAS, ESSA VARIÁVEL É UM DICTIONARY, MANTENHA O PADRÃO
login_credentials = {
    '': '',
}

# Se quer receber notificações do bot pelo telegram, sugerimos habilitar o envio de
# mensagens com True, pois a idéia é deixar esse bot rodando e ir viver sua vida
# normalmente, se por algum motivo ele parar de notificar, você tem a ciência de que
# o programa parou de executar
# !APENAS VALORES BOOLEANOS, True OU False, SEM ASPAS
telegram_notify = True

# Se decidiu receber notificações por telegram, informe o token de autenticação recebido
# ao falar com o @BotFather, no próprio telegram mesmo, igual o site oficial orienta
# link https://core.telegram.org/bots#3-how-do-i-create-a-bot
# !APENAS VALORES DE TEXTO, COM ASPAS
bot_token = ''

# Se decidiu receber notificações por telegram e informou o bot_token, você também deve
# informa o chat_id, ele é o Id da sua conversa com o bot, para descobrir seu chatId,
# mande uma mensagem para o seu bot, após isso, acesse o link https://api.telegram.org/bot<token>/getUpdates,
# substituindo o <token> pelo token recebido do @BotFather, procure pela chave "id" no json
# recebido, esse é o chatId
# !APENAS VALORES DE TEXTO, COM ASPAS
chat_id = ''

# Informe a partir de que horário (formato 24h, ex: 15:30) deseja que o bot envie um print da
# quantia total de bcoin até o momento, pelo Telegram, apenas uma vez, a cada 24h
# !APENAS VALORES DE TEXTO, COM ASPAS
time_notify_ammount_of_bcoin = '20:37'
