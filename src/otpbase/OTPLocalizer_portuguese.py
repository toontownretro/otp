import string
from otp.otpbase.OTPLocalizer_portuguese_Property import *

# common locations
lTheBrrrgh = 'O Brrrgh'
lDaisyGardens = 'Jardim da Margarida'
lDonaldsDock = "Porto do Donald"
lDonaldsDreamland = "Sonholândia do Donald"
lMinniesMelodyland = "Melodilândia da Minnie"
lToontownCentral = 'Centro de Toontown'
lGoofySpeedway = "Autódromo do Pateta"
lOutdoorZone = "Bosque de Bolotas de Tico e Teco"
lGolfZone = "Minigolfe de Tico e Teco"

# common strings
lCancel = 'Cancelar'
lClose = 'Fechar'
lOK = 'OK'
lNext = 'Próximo'
lNo = 'Não'
lQuit = 'Sair'
lYes = 'Sim'

Cog = "Cog"
Cogs = "Cogs"

# OTPDialog.py
DialogOK = lOK
DialogCancel = lCancel
DialogYes = lYes
DialogNo = lNo
DialogDoNotShowAgain = "Não\nExibir de Novo"

# DistributedAvatar.py
WhisperNoLongerFriend = "%s saiu da sua lista de amigos."
WhisperNowSpecialFriend = "%s agora é seu amigo verdadeiro!"
WhisperComingToVisit = "%s está vindo visitar você."
WhisperFailedVisit = "%s tentou visitar você."
WhisperTargetLeftVisit = "%s foi para algum outro lugar. Tente novamente!"
WhisperGiveupVisit = "%s não conseguiu encontrá-lo porque você está se movendo!"
WhisperIgnored = "%s está ignorando você!"
TeleportGreeting = "Oi, %s."
WhisperFriendComingOnline = "%s está entrando on-line!"
WhisperFriendLoggedOut = "%s fez logout."
WhisperPlayerOnline = "%s on-line em %s"
WhisperPlayerOffline = "%s está off-line."
WhisperUnavailable = "Esse jogador não está mais disponível para cochichos."
DialogSpecial = "ooo"
DialogExclamation = "!"
DialogQuestion = "?"

# ChatInputNormal.py
ChatInputNormalSayIt = "Dizer"
ChatInputNormalCancel = lCancel
ChatInputNormalWhisper = "Cochichar"
ChatInputWhisperLabel = "Com %s"

# ChatInputSpeedChat.py
SCEmoteNoAccessMsg = "Você não tem acesso\na esta emoção ainda."
SCEmoteNoAccessOK = lOK

ParentLogin = "Login de Pais"
ParentPassword = "Senha de pais"

# ChatGarbler.py
ChatGarblerDefault = ["blá"]

# ChatManager.py
ChatManagerChat = "Chat"
ChatManagerWhisperTo = "Cochichar com:"
ChatManagerWhisperToName = "Cochichar com:\n%s"
ChatManagerCancel = lCancel
ChatManagerWhisperOffline = "%s está off-line."
OpenChatWarning = 'Você ainda não tem nenhum "Amigo secreto"! Você não pode conversar com outros Toons a menos que eles sejam seus Amigos secretos.\n\nPara se tornar Amigo secreto de alguém, clique na pessoa e selecione "Segredos" no painel de detalhes. É claro que você sempre poderá conversar com alguém pelo Chat rápido.'
OpenChatWarningOK = lOK
UnpaidChatWarning = 'Depois que você assinar o serviço, poderá ativar este botão para conversar com seus amigos usando o teclado. Até lá, você deve conversar com os outros Toons usando o Chat rápido.'
UnpaidChatWarningPay = "Assine já!"
UnpaidChatWarningContinue = "Continuar avaliação gratuita"
PaidNoParentPasswordWarning = 'Depois que você definir a sua senha de pais, poderá ativar este botão para conversar com seus amigos usando o teclado. Até lá, você deve conversar com os outros Toons usando o Chat rápido.'
UnpaidNoParentPasswordWarning = 'Depois de definir a senha dos pais, você pode ativar este botão para conversar com seus amigos usando o teclado. Para definir a senha dos pais, saia do Toontown e clique em "Preferências" em Serviços para membros na página do Toontown. Até então, você deve conversar com outros Toons usando o Chat Rápido.'
PaidNoParentPasswordWarningSet = "Definir senha de pais agora!"
PaidNoParentPasswordWarningContinue = "Continuar jogando"
PaidParentPasswordUKWarning = 'Depois que o Chat estiver ativado, você poderá usar este botão para conversar com seus amigos usando o teclado. Até lá, você deve conversar com os outros Toons usando o Chat rápido.'
PaidParentPasswordUKWarningSet = "Ativar Chat agora!"
PaidParentPasswordUKWarningContinue = "Continuar jogando"
NoSecretChatWarningTitle = "Controles disponíveis aos pais"
NoSecretChatWarning = 'Para conversar com um amigo, o recurso Chat Aberto de Amigos verdadeiros deve estar ativado. As crianças precisam que seus pais façam login e insiram a senha de pais para conhecer o recurso Chat Aberto de Amigos verdadeiros.'
RestrictedSecretChatWarning = 'Para pegar ou digitar um segredo, você deve inserir a Senha de pais. Você pode desativar esta solicitação alterando as suas opções de Amigos secretos.'
NoSecretChatWarningOK = lOK
NoSecretChatWarningCancel = lCancel
NoSecretChatWarningWrongPassword = 'Esta não é a senha correta. Insira a senha de pais criada na compra desta conta. Não é a mesma senha usada para os jogos.'
NoSecretChatAtAllTitle = "Chat Aberto de Amigos verdadeiros"
# not sure what this should do in the new world order
NoSecretChatAtAll = 'Para conversar com um amigo, o recurso Chat Aberto de Amigos verdadeiros deve estar ativado. O recurso Chat aberto de Amigos verdadeiros só permite que um membro converse com outro mediante um código secreto que deve ser comunicado fora do jogo.\nPara ativar este recurso ou para aprender mais sobre ele, saia de Toontown e clique em "Opções da conta" na página da web de Toontown.'
NoSecretChatAtAllAndNoWhitelistTitle = "Botão de Chat"
# not sure what this should do in the new world order
NoSecretChatAtAllAndNoWhitelist = "Você pode usar o botão azul de Chat para conversar com outros Toons utilizando o recurso Chat Rápido Plus ou Abrir Chat Aberto com Amigos verdadeiros.\n\nChat Rápido Plus é um chat em que os usuários podem conversar utilizando o dicionário Disney Chat Rápido Plus.\n\nAbrir Chat Aberto com Amigos verdadeiros é um chat em que os amigos podem conversar livremente entre si após fornecer um Código de Amigo Verdadeiro que deve ser comunicado fora do jogo.\n\nPara ativar ou obter uma descrição completa de cada um desses recursos, saia do Toontown e, em Serviços de Associado, no site do Toontown, clique em \"Preferências\"."
NoSecretChatAtAllOK = lOK
ChangeSecretFriendsOptions = "Alterar opções de Amigos secretos"
ChangeSecretFriendsOptionsWarning = "\nInsira a senha de pais para alterar suas opções de Amigos secretos."
ActivateChatTitle = "Opções de Amigos secretos"

WhisperToFormat = "Para %s %s"
WhisperToFormatName = "Para %s"
WhisperFromFormatName = "%s cochicha"

ThoughtOtherFormatName = "%s pensa"
ThoughtSelfFormatName = "Você pensa"

from otp.otpbase.OTPModules import TextProperties
from otp.otpbase.OTPModules import TextPropertiesManager

shadow = TextProperties()
shadow.setShadow(-0.025, -0.025)
shadow.setShadowColor(0,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('sombra', shadow)

red = TextProperties()
red.setTextColor(1,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('vermelho', red)

green = TextProperties()
green.setTextColor(0,1,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('verde', green)

yellow = TextProperties()
yellow.setTextColor(1,1,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('amarelo', yellow)

midgreen = TextProperties()
midgreen.setTextColor(0.2,1,0.2,1)
TextPropertiesManager.getGlobalPtr().setProperties('verde-água', midgreen)

blue = TextProperties()
blue.setTextColor(0,0,1,1)
TextPropertiesManager.getGlobalPtr().setProperties('azul', blue)

white = TextProperties()
white.setTextColor(1,1,1,1)
TextPropertiesManager.getGlobalPtr().setProperties('branco', white)

black = TextProperties()
black.setTextColor(0,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('preto', black)

grey = TextProperties()
grey.setTextColor(0.5, 0.5, 0.5, 1)
TextPropertiesManager.getGlobalPtr().setProperties('cinza', grey)

ActivateChat = """O recurso Chat Aberto de Amigos verdadeiros só permite que um associado converse com outro mediante um código de Amigo verdadeiro que deve ser comunicado fora do jogo. Para obter uma descrição completa do recurso, clique aqui: O recurso Chat Aberto de Amigos verdadeiros não é moderado nem supervisionado. Se os pais deixarem seus filhos usarem a conta com o recurso Chat Aberto de Amigos verdadeiros ativado, aconselhamos que eles mesmos supervisionem os filhos durante a brincadeira. Depois que for ativado, o recurso Chat Aberto de Amigos verdadeiros ficará disponível até que alguém o desative. Ao ativar o recurso Chat Aberto de Amigos verdadeiros, você reconhece que, apesar de haver alguns riscos inerentes a ele, você foi informado de todos os riscos mencionados aqui, concordando em aceitá-los."""

ActivateChatYes = "Ativar"
ActivateChatNo = lCancel
ActivateChatMoreInfo = "Mais informações"
ActivateChatPrivacyPolicy = "Política de Privacidade"

ActivateChatPrivacyPolicy_Button1A = "Version 1"
ActivateChatPrivacyPolicy_Button1K = "Version 1"
ActivateChatPrivacyPolicy_Button2A = "Version 2"
ActivateChatPrivacyPolicy_Button2K = "Version 2"

PrivacyPolicyText_1A = [""" """]
PrivacyPolicyText_1K = [""" """]
PrivacyPolicyText_2A = [""" """]
PrivacyPolicyText_2K = [""" """]
PrivacyPolicyText_Intro = [""" """]
PrivacyPolicyClose = lClose

# SecretFriendsInfoPanel.py
SecretFriendsInfoPanelOk = lOK
SecretFriendsInfoPanelClose = lClose
SecretFriendsInfoPanelText = ["""
O recurso Chat Aberto de Amigos verdadeiros

O recurso Chat Aberto de Amigos verdadeiros permite que um membro converse diretamente com outro no Toontown On-line da Disney (o "Serviço") depois que os membros estabelecerem uma conexão de Amigos verdadeiros. Quando o seu filho tentar usar o recurso Chat Aberto de Amigos verdadeiros, solicitaremos que você insira a sua Senha de pais para indicar seu consentimento para que a criança use o recurso. Esta é uma descrição detalhada do processo de criação de uma conexão de Amigos secretos entre os membros fictícios chamados "Sandra" e "Marcos".
1. O responsável por Sandra e o responsável por Marcos ativam o recurso Chat aberto de Amigos verdadeiros inserindo suas respectivas Senhas de pais (a) nas áreas de Opções da conta do Serviço ou (b) quando for solicitado no jogo, em uma janela pop-up de Controles disponíveis aos pais.
2. Sandra pede um Código de Amigo verdadeiro (descrito abaixo) no Serviço.
""","""
3. O Código de Amigo verdadeiro de Sandra é comunicado a Marcos fora do Serviço. (O Código de Amigo verdadeiro de Sandra pode ser comunicado a Marcos diretamente por Sandra ou indiretamente, se Sandra revelar o Código de Amigo verdadeiro a outra pessoa.)
4. Marcos envia o Código de Amigo verdadeiro de Sandra ao Serviço dentro de 48 horas a partir da hora em que Sandra solicitou o Código de Amigo verdadeiro ao Serviço.
5. Em seguida, o Serviço notifica Marcos de que Sandra tornou-se sua Amiga verdadeira. Da mesma forma, o Serviço notifica Sandra de que Marcos tornou-se seu Amigo verdadeiro.
6. Sandra e Marcos podem agora conversar diretamente um com o outro até um deles escolher cancelar o seu relacionamento como Amigo verdadeiro, ou até que o recurso Chat Aberto de Amigos verdadeiros seja desativado para Sandra ou Marcos por um dos responsáveis por essas crianças. Então, a conexão de Amigos verdadeiros pode ser desativada a qualquer momento: (a) por um membro, que remove o Amigo verdadeiro de sua lista de amigos (conforme descrito no Serviço), ou (b) pelo responsável pelo membro, que desativa o recurso Chat Aberto de
Amigos verdadeiros na área Opções da conta do Serviço, seguindo as etapas definidas no recurso. 

O Código de Amigo verdadeiro é um código aleatório, gerado por computador, que é atribuído a um membro específico. O Código de Amigo verdadeiro precisa ser usado para ativar a conexão de Amigo verdadeiro dentro de 48 horas a partir da hora em que o membro solicitou o Código de Amigo verdadeiro; caso contrário, o Código de Amigo verdadeiro expirará e não poderá ser usado. Além disso, só se pode usar um único Código de Amigo verdadeiro para estabelecer uma conexão de Amigo verdadeiro. Para fazer conexões adicionais de Amigos verdadeiros, o membro precisará solicitar mais segredos, um para cada Amigo verdadeiro que quiser incluir. As Amizades verdadeiras não podem ser transferidas. Por exemplo, se Sandra se tornar Amiga verdadeira de Marcos, e Marcos se tornar Amigo verdadeiro de Jéssica, Sandra não se tornará automaticamente Amiga Verdadeira de Jéssica. Para que Sandra e Jéssica se

""",""" 
tornem Amigas verdadeiras, uma delas terá que solicitar um novo Código de Amigo verdadeiro ao Serviço e comunicar à outra. 

Os Amigos verdadeiros se comunicam entre si por meio de uma conversa interativa em formato livre. O conteúdo da conversa é inserido diretamente pelo membro participante e é processado pelo Serviço, cuja operação é realizada pelo Walt Disney Internet Group ("WDIG"), S. Buena Vista St., Burbank, CA 91521-7691. Apesar de recomendarmos aos membros não trocarem com outros membros informações pessoais como nome e sobrenome, e-mails, endereço postal ou números de telefone ao usarem o recurso Chat Aberto de Amigos verdadeiros, não podemos garantir que os membros seguirão a recomendação e que tais informações sejam preservadas. Embora o chat de Amigos verdadeiros seja automaticamente filtrado para evitar o uso da maioria dos palavrões, Chat Aberto de Amigos verdadeiros pode ser moderado e a Disney reserva-se o direito de moderar qualquer parte do Serviço que a Disney,
""","""
a seu exclusivo e absoluto critério, julgar necessário. No entanto, como chat aberto de amigos verdadeiros nem sempre será moderado, se os pais deixarem seus filhos usarem a conta com o recurso Chat Aberto de Amigos verdadeiros ativado no Serviço, aconselhamos que eles mesmos supervisionem os filhos durante a brincadeira. 

O WDIG não usa o conteúdo do chat Amigos verdadeiros para nenhum fim que não seja a comunicação do conteúdo ao amigo verdadeiro do membro, e não revela tal conteúdo a terceiros, exceto: (1) se exigido por lei; por exemplo, para cumprir uma ordem ou intimação judicial; (2) para fazer com que os Termos de Uso
""","""
aplicáveis ao Serviço (que podem ser acessados na página principal do Serviço) sejam respeitados; ou (3) para proteger a segurança dos Membros do Serviço e o Serviço propriamente dito. Mediante solicitação ao WDIG, o responsável por uma criança-membro pode analisar e mandar apagar qualquer conteúdo do recurso de chat Amigos secretos fornecidos pela criança em questão, desde que tal conteúdo já não tenha sido excluído dos registros pelo WDIG. Obedecendo à Children's Online Privacy Protection Act, uma lei americana de proteção à privacidade on-line para as crianças, estamos proibidos de condicionar a participação da criança em qualquer tipo de atividade (inclusive o recurso Chat de Amigos verdadeiros) ao fornecimento, por parte da criança, de mais informações pessoais do que o estritamente necessário para que ela participe de tais atividades. 

Além disso, conforme observado acima, reconhecemos o direito do responsável pela criança de não permitir que continuemos a deixar que a criança use o recurso Amigos verdadeiros. Ao ativar o recurso Chat Aberto de Amigos secretos, você reconhece que há alguns riscos inerentes ao chat, no qual os membros podem conversar uns com os outros usando o recurso Chat Aberto de Amigos verdadeiros, sendo que você foi informado de todos os riscos mencionados aqui, concordando em aceitá-los.
"""
]
#LeaveToPay = """Para efetuar a compra, o jogo sairá para Toontown.com.br"""
LeaveToPay = """Para efetuar a compra, você sairá do jogo e será direcionado para Toontown.com.br"""
LeaveToPayYes = "Comprar"
LeaveToPayNo = lCancel

#LeaveToSetParentPassword = """Para configurar a Senha de pais, o jogo sairá para Toontown.com.br"""
LeaveToSetParentPassword = """Para configurar a Senha de pais, você sairá do jogo e será direcionado para Toontown.com.br"""
LeaveToSetParentPasswordYes = "Definir senha"
LeaveToSetParentPasswordNo = lCancel

#LeaveToEnableChatUK = """Para ativar o chat, o jogo sairá para o site Toontown."""
LeaveToEnableChatUK = """Para ativar o chat, você sairá do jogo e será direcionado para o site Toontown."""
LeaveToEnableChatUKYes = "Ativar chat"
LeaveToEnableChatUKNo = lCancel

ChatMoreInfoOK = lOK
SecretChatDeactivated = 'O recurso "Amigos verdadeiros" foi desativado.'
RestrictedSecretChatActivated = 'O recurso "Amigos verdadeiros restritos" foi ativado!'
SecretChatActivated = 'O sistema "Amigos verdadeiros" foi ativado!\n\nSe você mudar de idéia e decidir desativar este recurso mais tarde, clique em "Opções da conta" na página da web de Toontown.'
SecretChatActivatedOK = lOK
SecretChatActivatedChange = "Alterar Opções"
ProblemActivatingChat = 'Ops! Não foi possível ativar o recurso de chat "Amigos verdadeiros".\n\n%s\n\nTente novamente mais tarde.'
ProblemActivatingChatOK = lOK

# MultiPageTextFrame.py
MultiPageTextFrameNext = lNext
MultiPageTextFramePrev = 'Anterior'
MultiPageTextFramePage = 'Página %s/%s'

# GuiScreen.py
GuiScreenToontownUnavailable = "Toontown parece estar temporariamente indisponível, ainda tentando..."
GuiScreenCancel = lCancel


# CreateAccountScreen.py
CreateAccountScreenUserName = "Nome da conta"
CreateAccountScreenPassword = "Senha"
CreateAccountScreenConfirmPassword = "Confirmar senha"
CreateAccountScreenCancel = lCancel
CreateAccountScreenSubmit = "Enviar"
CreateAccountScreenConnectionErrorSuffix = ".\n\nTente novamente mais tarde."
CreateAccountScreenNoAccountName = "Insira o nome da conta."
CreateAccountScreenAccountNameTooShort = "O nome da conta deve ter, pelo menos, %s caracteres. Tente novamente."
CreateAccountScreenPasswordTooShort = "A senha deve ter, pelo menos, %s caracteres. Tente novamente."
CreateAccountScreenPasswordMismatch = "As senhas inseridas não combinam. Tente novamente."
CreateAccountScreenUserNameTaken = "Este nome de usuário já existe. Tente novamente."
CreateAccountScreenInvalidUserName = "Nome de usuário inválido.\nTente novamente."
CreateAccountScreenUserNameNotFound = "Nome de usuário não encontrado.\nTente novamente ou crie uma nova conta."

# ToontownClientRepository.py
CRConnecting = "Conectando..."
# host, port
CRNoConnectTryAgain = "Não foi possível conectar-se a %s:%s. Tentar novamente?"
CRNoConnectProxyNoPort = "Não foi possível conectar-se a %s:%s.\n\nVocê está se comunicando com a Internet por via proxy, mas o seu proxy não permite conexões na porta %s.\n\nVocê deve abrir esta porta, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, é preciso entrar em contato com ele para abrir esta porta."
CRMissingGameRootObject = "Há alguns objetos do jogo principal ausentes. (A causa pode ser uma conexão de rede com falhas). Saindo do jogo."
CRNoDistrictsTryAgain = "Não há Regiões de Toontown disponíveis. Tentar novamente?"
CRRejectRemoveAvatar = "O Toon não pôde ser excluído, tente novamente mais tarde."
CRLostConnection = "A sua conexão de Internet à Toontown foi interrompida inesperadamente."
CRBootedReasons = {
    1: "Houve um problema inesperado. A conexão falhou, e você precisa se conectar novamente para voltar ao jogo.",
    100: "Você foi desconectado porque outra pessoa acabou de fazer login usando a sua conta em outro computador.",
    120: "Você foi desconectado porque houve um problema com sua autorização para usar o chat.",
    122: "Houve um problema inesperado quando você fez login em Toontown. Entre em contato com o Suporte ao Cliente de Toontown.",
    125: "Os arquivos de Toontown que você tem instalados parecem ser inválidos. Use o botão Jogar, no site oficial de Toontown na web, para executar Toontown.",
    126: "Você não está autorizado a usar privilégios administrativos.",
    127: "A problem has occurred with your Toon. Please contact Member Services via phone or email and reference Error Code 127.  Thank you.",
    151: "O administrador responsável pelos servidores de Toontown fez logout na sua conta.",
    152: "Foi relatada uma violação dos nossos termos de uso, com relação a '%(name)s'. Por segurança, colocamos uma restrição temporária na conta. Para obter mais detalhes, leia a mensagem enviada ao endereço de e-mail associado a '%(name)s'.",
    153: "A região de Toontown onde você estava jogando foi reiniciada. Todas as pessoas que estavam jogando nessa região foram desconectadas. Entretanto, você poderá conectar-se novamente e voltar direto ao jogo.",
    288: "Sinto muito, mas você usou todos os seus minutos disponíveis deste mês em Toontown.",
    349: "Sinto muito, mas você usou todos os seus minutos disponíveis deste mês em Toontown.",
    }
CRBootedReasonUnknownCode = "Houve um problema inesperado (código de erro %s). A conexão falhou, mas você ainda deve conseguir conectar-se novamente para voltar ao jogo."
CRTryConnectAgain = "\n\nTentar conectar-se novamente?"
# avName
CRToontownUnavailable = "Toontown parece estar temporariamente indisponível, ainda tentando..."
CRToontownUnavailableCancel = lCancel
CRNameCongratulations = "PARABÉNS!!"
CRNameAccepted = "O seu nome foi\naprovado pelo Conselho de Toons.\n\nA partir de agora,\nvocê terá o nome\n\"%s\""
CRServerConstantsProxyNoPort = "Não foi possível contatar %s.\n\nVocê está se comunicando com a Internet por via proxy, mas o seu proxy não permite conexões na porta %s.\n\nVocê deve abrir esta porta, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, é preciso entrar em contato com ele para abrir esta porta."
CRServerConstantsProxyNoCONNECT = "Não foi possível contatar %s.\n\nVocê está se comunicando com a Internet por via proxy, mas o seu proxy não permite o método CONECTAR.\n\nVocê deve ativar este recurso, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, é preciso entrar em contato com ele para abrir esta porta."
CRServerConstantsTryAgain = "Não foi possível contatar %s.\n\nO servidor de contas da Toontown deve estar temporariamente fora do ar ou deve haver algum problema na conexão de Internet.\n\nTentar novamente?"
CRServerDateTryAgain = "Não foi possível obter a data do servidor de %s. Tentar novamente?"
AfkForceAcknowledgeMessage = "O seu Toon ficou com sono e foi para a cama."
PeriodTimerWarning = "O seu limite de tempo em Toontown neste mês está quase no fim!"
PeriodForceAcknowledgeMessage = "Você usou todos os seus minutos disponíveis em Toontown neste mês. Volte e jogue mais no próximo mês!"
CREnteringToontown = "Entrando em Toontown..."

# DownloadWatcher.py
# phase, percent
DownloadWatcherUpdate = "Fazendo o download de %s"
DownloadWatcherInitializing = "Inicializando Download..."

# LoginScreen.py
LoginScreenUserName = "Nome da Conta"
LoginScreenPassword = "Senha"
LoginScreenLogin = "Login"
LoginScreenCreateAccount = "Criar Conta"
LoginScreenQuit = lQuit
LoginScreenLoginPrompt = "Por favor, digite um nome de usuário e uma senha."
LoginScreenBadPassword = "Senha errada.\nTente novamente."
LoginScreenInvalidUserName = "Nome de usuário inválido.\nTente novamente."
LoginScreenUserNameNotFound = "Nome de usuário não encontrado.\nTente novamente ou crie uma nova conta."
LoginScreenPeriodTimeExpired = "Sinto muito, mas você já usou todos os seus minutos disponíveis deste mês. Volte no início do próximo mês."
LoginScreenNoNewAccounts = "Sinto muito, no momento não estamos aceitando novas contas."
LoginScreenTryAgain = "Tente novamente"


# SpeedChat

# Avatar.py
DialogSpecial = "ooo"
DialogExclamation = "!"
DialogQuestion = "?"
# Cutoff string lengths to determine how much barking to play
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20

# Used several places in the game. Defined globally because
# we keep changing the name
GlobalSpeedChatName = "Chat rápido"

# Toontown Speedchat
SCMenuPromotion = "PROMOCIONAL"
SCMenuElection = "ESCOLHA"
SCMenuEmotions = "EMOÇÕES"
SCMenuCustom = "MINHAS FRASES"
SCMenuResistance = "UNIR!"
SCMenuPets = "BICHINHOS"
SCMenuPetTricks = "TRUQUES"
SCMenuCog = "FALAS DE COGS"
SCMenuHello = "OLÁ"
SCMenuBye = "TCHAU"
SCMenuHappy = "FELIZ"
SCMenuSad = "TRISTE"
SCMenuFriendly = "AMIGÁVEL"
SCMenuSorry = "DESCULPE"
SCMenuStinky = "FEDIDO"
SCMenuPlaces = "LUGARES"
SCMenuToontasks = "TAREFAS TOON"
SCMenuBattle = "BATALHA"
SCMenuGagShop = "LOJA DE PIADAS"
SCMenuFactory = "FÁBRICA"
SCMenuKartRacing = "CORRIDA"
SCMenuFactoryMeet = "ENCONTRO"
SCMenuCFOBattle = "DIRETOR FINANCEIRO"
SCMenuCFOBattleCranes = "GUINDASTES"
SCMenuCFOBattleGoons = "BRUTAMONTES"
SCMenuCJBattle = "JUIZ-CHEFE"
SCMenuCEOBattle = "PRESIDENTE"
SCMenuGolf = "GOLFE"
SCMenuWhiteList = "LISTA DE PERMISSÕES"
SCMenuPlacesPlayground = "PÁTIO"
SCMenuPlacesEstate = "PROPRIEDADE"
SCMenuPlacesCogs = "COGS"
SCMenuPlacesWait = "ESPERE"
SCMenuFriendlyYou = "Você..."
SCMenuFriendlyILike = "Eu gosto de..."
SCMenuPlacesLetsGo = "Vamos..."
SCMenuToontasksMyTasks = "MINHAS TAREFAS"
SCMenuToontasksYouShouldChoose = "Eu acho que você deveria escolher..."
SCMenuToontasksINeedMore = "Preciso de mais..."
SCMenuBattleGags = "PIADAS"
SCMenuBattleTaunts = "PROVOCAÇÕES"
SCMenuBattleStrategy = "ESTRATÉGIA"
SCMenuBoardingGroup              = "ABORDAGEM"
SCMenuParties                    = "FESTAS"
SCMenuAprilToons                 = "TOONS DE ABRIL"
SCMenuSingingGroup               = "CANTANDO"
SCMenuCarol                      = "CANÇÕES NATALINAS"
SCMenuSillyHoliday                   = "MEDIDOR DE BOBAGENS"
SCMenuVictoryParties             = "FESTAS DA VITÓRIA"
SCMenuSellbotNerf                = "ROBÔ VENDEDOR TEMPESTADE"
SCMenuJellybeanJam               = "Dança de Balinhas"
SCMenuHalloween                  = "HALLOWEEN"
SCMenuWinter                     = "INVERNO"
SCMenuSellbotInvasion            = "SELLBOT INVASION"
SCMenuFieldOffice                = "ESCRITÓRIOS DE CAMPO"
SCMenuIdesOfMarch                = "VERDE"
SCMenuLawbotNerf                 = "ROBÔS DA LEI PERDERAM"

# FriendSecret.py
FriendSecretNeedsPasswordWarningTitle = "Controles disponíveis aos pais"
FriendSecretNeedsParentLoginWarning = """Para conseguir ou digitar um Código de Amigo Verdadeiro, um dos seus pais ou responsáveis precisa fazer o login. Você pode desativar esta pergunta alterando suas opções de Amigos Verdadeiros."""
FriendSecretNeedsPasswordWarning = """Para pegar ou digitar um segredo, você deve inserir a Senha de pais. Você pode desativar esta solicitação alterando as suas opções de Amigos secretos."""
FriendSecretNeedsPasswordWarningOK = lOK
FriendSecretNeedsPasswordWarningCancel = lCancel
FriendSecretNeedsPasswordWarningWrongUsername = """Esse não é o nome de usuário correto. Digite o nome de usuário da conta de pais. Esse não é o mesmo nome de usuário que é usado para jogar."""
FriendSecretNeedsPasswordWarningWrongPassword = """Esta não é a senha correta. Insira a Senha de pais criada na compra desta conta. Não é a mesma senha usada para os jogos."""
FriendSecretIntro = "Se você estiver jogando Toontown Online da Disney com alguém que conhece no mundo real, poderá tornar-se Amigo secreto dessa pessoa. Você pode conversar com seus Amigos secretos usando o teclado. Os outros Toons não entenderão o que vocês estiverem falando.\n\nVocê pode conseguir isto obtendo um segredo. Conte o segredo só ao seu amigo, e a mais ninguém. Quando o seu amigo digitar o seu segredo na tela, vocês dois serão Amigos secretos em Toontown!"
FriendSecretGetSecret = "Obter um segredo"
FriendSecretEnterSecret = "Se você tiver um segredo de alguém conhecido, digite-o aqui."
FriendSecretOK = lOK
FriendSecretEnter = "Inserir segredo"
FriendSecretCancel = lCancel
FriendSecretGettingSecret = "Obtendo segredo. . ."
FriendSecretGotSecret = "Este é o seu novo segredo. Não deixe de anotá-lo em algum lugar!\n\nVocê só pode dar este segredo a uma pessoa. Depois que alguém digitar o seu segredo, ele não funcionará para nenhuma outra pessoa. Se você quiser dar um segredo para mais de uma pessoa, obtenha outro.\n\nO segredo só funcionará nos próximos dois dias. O seu amigo terá que digitá-lo antes que expire, caso contrário, não funcionará.\n\nO segredo é:"
FriendSecretTooMany = "Sinto muito, você não pode ter mais segredos hoje. Você já obteve mais do que a parte que lhe cabia!\n\nTente novamente amanhã."
FriendSecretTryingSecret = "Tentando usar segredo. . ."
FriendSecretEnteredSecretSuccess = "Agora, você é Amigo secreto de %s!"
FriendSecretTimeOut = "Sorry, secrets are not working right now."
FriendSecretEnteredSecretUnknown = "Este segredo não existe. Tem certeza de que digitou certo?\n\nSe você tiver digitado certo, ele pode ter expirado. Peça ao seu amigo para pegar outro segredo para você (ou pegue um novo você mesmo e dê ao seu amigo)."
FriendSecretEnteredSecretFull = "Você não pode fazer amizade com %s porque um de vocês dois possui amigos demais na lista."
FriendSecretEnteredSecretFullNoName = "Vocês não podem fazer amizade porque um de vocês dois possui amigos demais na lista."
FriendSecretEnteredSecretSelf = "Você acabou de digitar seu próprio segredo! Agora, ninguém mais poderá usar este segredo."
FriendSecretEnteredSecretWrongProduct = "Você digitou o tipo errado de Código de Amigo Verdadeiro.\nEste jogo utiliza códigos que começam com '%s'."
FriendSecretNowFriends = "Agora, você é Amigo secreto de %s!"
FriendSecretNowFriendsNoName = "Agora, vocês são Amigos secretos!"
FriendSecretDetermineSecret = "Que tipo de Amigo Verdadeiro você quer ter?"
FriendSecretDetermineSecretAvatar = "Avatar"
FriendSecretDetermineSecretAvatarRollover = "Um amigo somente neste jogo"
FriendSecretDetermineSecretAccount = "Conta"
FriendSecretDetermineSecretAccountRollover = "Um amigo em toda a rede Disney.com"

# GuildMember.py
GuildMemberTitle = "Opções do Associado"
GuildMemberPromote = "Tornar-se Oficial"
GuildMemberPromoteInvite = "Make Veteran"
GuildMemberDemoteInvite = "Demote to Veteran"
GuildMemberGM = "Tornar-se Guildmaster (Mestre da Guilda)"
GuildMemberGMConfirm = "Confirm"
GuildMemberDemote = "Rebaixar"
GuildMemberKick = "Expulsar Associado"
GuildMemberCancel = lCancel
GuildMemberOnline = "entrou on-line."
GuildMemberOffline = "saiu e está off-line."
GuildPrefix = "(G):"
GuildNewMember = "Novo Associado da Guilda"
GuildMemberUnknown = "Desconhecido"
GuildMemberGMMessage = "Warning! Would you like to give up leadership of your guild and make %s your guild master?\n\nYou will become an officer"

# GuildInvitee.py
GuildInviteeOK = lOK
GuildInviteeNo = lNo
GuildInviteeInvitation = "%s convida você para se juntar a %s."

GuildRedeemErrorInvalidToken = "Sinto muito, esse código é inválido. Por favor, tente novamente."
GuildRedeemErrorGuildFull = "Sinto muito, a guilda já tem muitos associados."

# FriendInvitee.py
FriendInviteeTooManyFriends = "%s quer fazer amizade com você, mas você já tem muitos amigos em sua lista!"
FriendInviteeInvitation = "%s quer fazer amizade com você."
FriendInviteeInvitationPlayer = "O jogador de %s\\ quer fazer amizade com você."
FriendNotifictation = "%s agora é seu amigo."
FriendInviteeOK = lYes
FriendInviteeNo = lNo
GuildInviterWentAway = "%s não está mais presente."
GuildInviterAlready = "%s já está na guilda."
GuildInviterBusy = "%s está ocupado no momento."
GuildInviterNotYet = "Convidar %s para se juntar à sua guilda?"
GuildInviterCheckAvailability = "Convidando %s para se juntar à sua guilda."
GuildInviterOK = lOK
GuildInviterNo = lNo
GuildInviterCancel = lCancel
GuildInviterYes = lYes
GuildInviterTooFull = "A guilda está completa."
GuildInviterNo = lNo
GuildInviterClickToon = "Clique no pirata que deseja convidar."
GuildInviterTooMany = "Isso é um inseto"
GuildInviterNotAvailable = "%s está ocupado no momento; tente mais tarde."
GuildInviterGuildSaidNo = "%s não quer participar."
GuildInviterAlreadyInvited = "%s já foi convidado."
GuildInviterEndGuildship = "Expulsar %s da guilda?"
GuildInviterFriendsNoMore = "%s saiu da guilda."
GuildInviterSelf = "Você já está na guilda!"
GuildInviterIgnored = "%s está ignorando você."
GuildInviterAsking = "Perguntando a %s para se juntar à guilda."
GuildInviterGuildSaidYes = "%s vai participar!"
GuildInviterFriendKickedOut = "%s has kicked out %s from the Guild."
GuildInviterFriendKickedOutP = "%s have kicked out %s from the Guild."
GuildInviterFriendInvited = "%s has invited %s to the Guild."
GuildInviterFriendInvitedP = "%s have invited %s to the Guild."
GuildInviterFriendPromoted = "%s has promoted %s to the rank of %s."
GuildInviterFriendPromotedP = "%s have promoted %s to the rank of %s."
GuildInviterFriendDemoted = "%s has demoted %s to the rank of %s."
GuildInviterFriendDemotedP = "%s have demoted %s to the rank of %s."
GuildInviterFriendPromotedGM = "%s has named %s as the new %s"
GuildInviterFriendPromotedGMP = "%s have named %s as the new %s"
GuildInviterFriendDemotedGM = "%s has been named by %s as the new GuildMaster who became the rank of %s"
GuildInviterFriendDemotedGMP = "%s have been named by %s as the new GuildMaster who beaome the rank of %s"

# FriendInviter.py
FriendOnline = "entrou on-line."
FriendOffline = "saiu e está off-line."
FriendInviterOK = lOK
FriendInviterCancel = lCancel
FriendInviterStopBeingFriends = "Interromper amizade"
FriendInviterConfirmRemove = "Remove"
FriendInviterYes = lYes
FriendInviterNo = lNo
FriendInviterClickToon = "Clique no Toon com o qual deseja fazer amizade."
FriendInviterTooMany = "Você tem amigos demais na lista e não pode adicionar mais nenhum agora. Você terá que remover alguns amigos se desejar fazer amizade com %s."
FriendInviterToonTooMany = "Você tem amigos Tonns demais em sua lista para poder acrescentar um agora. Remova alguns amigos Tonns se quiser fazer amizade com %s."
FriendInviterPlayerTooMany = "Você tem amigos jogadores demais em sua lista para poder acrescentar um agora. Remova alguns amigos jogadores se quiser fazer amizade com %s."
FriendInviterNotYet = "Deseja fazer amizade com %s?"
FriendInviterCheckAvailability = "Verificando se %s está disponível."
FriendInviterNotAvailable = "%s está ocupado(a) agora; tente novamente mais tarde."
FriendInviterCantSee = "Isso só funciona se puder ver %s."
FriendInviterNotOnline = "Isso só funciona se %s estiver on-line"
FriendInviterNotOpen = "%s não tem um bate-papo aberto, use segredos para fazer amigos"
FriendInviterWentAway = "%s saiu."
FriendInviterAlready = "%s já é seu(sua) amigo(a)."
FriendInviterAlreadyInvited = "%s já recebeu o convite."
FriendInviterAskingCog = "Pedindo a %s para fazer amizade com você."
FriendInviterAskingPet = "%s pula à sua volta, corre em círculos e lambe seu rosto."
FriendInviterAskingMyPet = "%s já é seu(sua) MELHOR amigo(a)."
FriendInviterEndFriendship = "Tem certeza de que você deseja interromper a amizade com %s?"
FriendInviterFriendsNoMore = "%s não é mais seu(sua) amigo(a)."
FriendInviterSelf = "Você já tem amizade com você mesmo(a)!"
FriendInviterIgnored = "%s está ignorando você."
FriendInviterAsking = "Pedindo a %s para fazer amizade com você."
FriendInviterFriendSaidYes = "%s disse sim!"
FriendInviterPlayerFriendSaidYes = "Agora, você fez amizade com o jogador de %s, %s!"
FriendInviterFriendSaidNo = "%s agradece, mas disse não."
FriendInviterFriendSaidNoNewFriends = "%s não está procurando novos amigos no momento."
FriendInviterOtherTooMany = "%s já tem amigos demais!"
FriendInviterMaybe = "%s não conseguiu responder."
FriendInviterDown = "Não foi possível fazer amizade agora."

#Talk Path Labels
TalkGuild = "G"
TalkParty = "P"
TalkPVP = "PVP"

#Spam Blocked Message
AntiSpamInChat = '***Envio de Spam***'

#IgnoreConfirm.py
IgnoreConfirmOK = lOK
IgnoreConfirmCancel = lCancel
IgnoreConfirmYes = lYes
IgnoreConfirmNo = lNo
IgnoreConfirmNotYet = "Deseja continuar a Ignorar %s?"
IgnoreConfirmAlready = "Você já está ignorando %s."
IgnoreConfirmSelf = "Você não pode ignorar a si mesmo(a)!"
IgnoreConfirmNewIgnore = "Você está ignorando %s."
IgnoreConfirmEndIgnore = "Você não está mais ignorando %s."
IgnoreConfirmRemoveIgnore = "Parar de ignorar %s?"

# Emote.py
# List of emotes in the order they should appear in the SpeedChat.
# Must be in the same order as the function list (EmoteFunc) in Emote.py
EmoteList = [
 "Aceno",
 "Feliz",
 "Triste",
 "Raivoso",
 "Sonolento",
 "Dar de ombros",
 "Dançante",
 "Piscar",
 "Entediado",
 "Palmas",
 "Surpreso",
 "Confuso",
 "Debochar",
 "Saudar",
 "Muito triste",
 "Sorrisão",
 "Risada",
 lYes,
 lNo,
 lOK,
 "Surpresa",
 "Choro",
 "Alegre",
 "Raiva",
 "Risada"
##    "Sing Note G1",
##    "Sing Note A",
##    "Sing Note B",
##    "Sing Note C",
##    "Sing Note D",
##    "Sing Note E",
##    "Sing Note F",
##    "Sing Note G2",
##    "Sing Note Rest",
 ]

EmoteWhispers = [
 "%s acena.",
 "%s está feliz.",
 "%s está triste.",
 "%s está furioso.",
 "%s está sonolento.",
 "%s dá de ombros.",
 "%s dança.",
 "%s pisca.",
 "%s está entediado.",
 "%s aplaude.",
 "%s está surpreso.",
 "%s está confuso.",
 "%s debocha de você.",
 "%s saúda você.",
 "%s está muito triste.",
 "%s sorri.",
 "%s dá risada.",
 "%s diz '"+lYes+"'.",
 "%s diz '"+lNo+"'.",
 "%s diz '"+lOK+"'.",
 "%s se surpreende.",
 "%s está chorando.",
 "%s está alegre.",
 "%s está com raiva.",
 "%s está rindo.",
 "is singing note G1",
 "is singing note A",
 "is singing note B",
 "is singing note C",
 "is singing note D",
 "is singing note E",
 "is singing note F",
 "is singing note G2"
 ]

# Reverse lookup:  get the index from the name.
# !!! DO NOT TRANSLATE THIS !!!
EmoteFuncDict = {
    "Wave"   : 0,
    "Happy"  : 1,
    "Sad"    : 2,
    "Angry"  : 3,
    "Sleepy" : 4,
    "Shrug"  : 5,
    "Dance"  : 6,
    "Think"   : 7,
    "Bored"  : 8,
    "Applause" : 9,
    "Cringe" : 10,
    "Confused"  : 11,
    "Belly Flop"  : 12,
    "Bow"    : 13,
    "Banana Peel" : 14,
    "Resistance Salute" : 15,
    "Laugh" : 16,
    "Yes"   : 17,
    "No"    : 18,
    "OK"     : 19,
    "Surprise" : 20,
    "Cry" : 21,
    "Delighted" : 22,
    "Furious" : 23,
    "Laugh" : 24,
    "Sing Note G1" : 25,
    "Sing Note A" : 26,
    "Sing Note B" : 27,
    "Sing Note C" : 28,
    "Sing Note D" : 29,
    "Sing Note E" : 30,
    "Sing Note F" : 31,
    "Sing Note G2" : 32,
    }

# SuitDialog.py
SuitBrushOffs = {
    'f':  ["Estou atrasado para uma reunião.",
           ],
    'p':  ["Sai fora.",
           ],
    'ym': ['As vaquinhas de presépio dizem NÃO.',
           ],
    None: ["É o meu dia de folga.",
           "Acho que você está no escritório errado.",
           "Fale para o seu pessoal falar com o meu.",
           "Você não tem cacife para se encontrar comigo.",
           "Fale com o meu assistente."]
    }

SuitFaceoffTaunts = {
    'b':  ["Você tem uma doação para mim?",
           "Você vai detestar perder a parada.",
           "Você não vai ter salvação.",
           "Sou \"A Positivo\", portanto, vou ganhar.",
           "\"O\"não seja tão \"Negativo\".",
           "É uma surpresa você ter me achado; não tenho parada.",
           "Vou precisar fazer uma rápida contagem em você.",
           "Em breve, você vai precisar comer biscoito e tomar um suco.",
           "Quando eu terminar, você vai precisar dar uma descansada.",
           "Só vai doer um pouquinho.",
           "Vou deixar você tonto.",
           "Na hora certa, só estou um pouquinho abaixo.",
           ],
    'm':  ["Você não sabe com quem está se metendo.",
           "Nunca se meteu com alguém da minha turma?",
           "Isso é bom, quando um não quer dois não se misturam.",
           "Vamos fazer amizade.",
           "Parece um bom lugar para confraternizar.",
           "Não é confortável?",
           "Vocês estão se unindo com a derrota.",
           "Vou me juntar a você no negócio.",
           "Tem certeza de que está pronto para a união?",
           ],
    'ms': ["Prepare-se para uma sacudida.",
           "Melhor você sair do caminho.",
           "Olha a frente.",
           "Acho que é minha vez.",
           "Isso deve agitar você.",
           "Prepare-se para ser movido.",
           "Estou pronto para dar o meu passo.",
           "Cuidado Toon, você está em terreno instável.",
           "Este deve ser um momento de movimento.",
           "Sinto um impulso de derrotar você.",
           "Você ainda está tremendo?",
           ],
    'hh': ["Estou na sua frente nesta caçada.",
           "Você está caçando encrenca da grande.",
           "A sua cabeça está na mira do caçador de cabeças.",
           "Que bom, estava atrás de você.",
           "Vou perseguir você por isto.",
           "Fique de olho!",
           "Parece que você está perdido nesta caçada.",
           "Está indo pela mesma trilha que eu?",
           "Um troféu perfeito para a minha coleção.",
           "Você vai ter uma dor de cabeça...",
           "Não perca o rumo comigo.",
           ],
    'tbc': ["Cuidado, vou adoçar você.",
            "Pode me chamar de Coquinho.",
            "Tem certeza? Às vezes ajo como um Cãocadão.",
            "Finalmente, estava achando que você ia me deixar aqui à mercê das formigas.",
            "Vou queimar o seu coco.",
            "Não acha que eu sou um docinho de coco?",
            "Você vai virar cocada comigo.",
            "As pessoas me acham durão.",
            "Cuidado, eu sei a sua data de validade.",
            "Cuidado, sou uma fera neste jogo.",
            "Bater você vai ser mole.",
            ],
    'cr': ["ATAQUE!",
           "Você não é adequado para a minha corporação.",
           "Prepare-se para ser atacado.",
           "Parece que você está preparado para assumir o comando da aventura.",
           "Esta roupa não é apropriada para ambientes corporativos.",
           "Você parece estar bem vulnerável.",
           "É hora de botar os bens em seu nome.",
           "Estou em uma cruzada a favor da eliminação dos Toons.",
           "Você fica sem defesa contra as minhas idéias.",
           "Relaxa, você vai ver que vai ser melhor assim.",
           ],
    'mh': ["Está preparado para a minha tomada?",
           "Luz, câmera, ação!",
           "Vai começar a rodar.",
           "Hoje o papel do Toon derrotado será feito por - VOCÊ!",
           "Esta cena vai ser cortada.",
           "Já sei qual vai ser a minha motivação para esta cena.",
           "Está preparado para a sua cena final?",
           "Estou pronto para passar os seus créditos no final.",
           "Eu disse para você não me chamar.",
           "O show tem que continuar.",
           "Não tem negócio igual a este!",
           "Espero que você não se esqueça das suas falas.",
           ],
    'nc': ["Parece que o seu número está em alta.",
           "Prefere ser destruído com ou sem cobertura crocante?",
           "Agora, você está destruído.",
           "Já está na hora de dizimar todos estes números?",
           "Vamos fazer uma matemática.",
           "Onde você gostaria de fazer uma subtração hoje?",
           "Você me deu uma coisa para calcular!",
           "Não vai ser fácil.",
           "Vai em frente, pegue um número qualquer.",
           "Vou destruir você com os meus cálculos.",
           ],
    'ls': ["É hora de recolher o seu empréstimo.",
           "Você tem estado na pior.",
           "O empréstimo agora tem que ser pago.",
           "Hora de liquidar a dívida.",
           "Bom, você queria um adiantamento e conseguiu.",
           "Você terá que pagar por isso.",
           "É hora de devolver o que pegou.",
           "Pode me dar uma mãozinha?",
           "Ainda bem que você está aqui, isto está uma loucura.",
           "Podemos fazer um lanchinho?",
           "Deixe-me dar um tasco.",
           ],
    'mb': ["Está na hora de trazer os sacos.",
           "Posso ensacar isso.",
           "Papel ou plástico?",
           "Você tem o tíquete da bagagem?",
           "Lembre-se de que o dinheiro não vai fazer você feliz.",
           "Cuidado, tenho muita bagagem.",
           "Você está prestes a ficar no vermelho.",
           "O dinheiro vai fazer o seu mundo girar.",
           "Sou muito rico para o seu bico.",
           "Você nunca poderá ter tanto dinheiro!",
           ],
    'rb': ["Você foi roubado.",
           "Vou roubar esta vitória de você.",
           "Sou um chato de galochas!",
           "Espero que você ainda possa sorrir para o barão.",
           "Você terá que denunciar este roubo.",
           "Mãos ao alto.",
           "Sou um adversário nobre.",
           "Vou levar tudo o que você tem.",
           "Você pode chamar isto de roubo no bairro.",
           "Você já devia saber que não se fala com estranhos.",
           ],
    'bs': ["Nunca vire as costas para mim.",
           "Você não vai voltar mesmo.",
           "Retire o que disse, ou então...!",
           "Sou bom em cortar custos.",
           "Tenho as costas quentes.",
           "Agora, não dá mais para voltar atrás.",
           "Sou o melhor e posso provar.",
           "Ôôô, parado aí, Toon.",
           "Deixe-me dar cobertura a você.",
           "Você vai ter uma dor de cabeça infernal.",
           "Tenho um golpe perfeito.",
           ],
    'bw': ["Quero sair bem na foto.",
           "Você me arrepia os cabelos.",
           "Posso deixar assim para sempre, se quiser.",
           "Parece que você vai ficar com a cara boa.",
           "Você não consegue encarar a verdade.",
           "Acho que é sua vez de mudar de cor.",
           "Estou tão feliz que você chegou na hora de mudar o visual.",
           "Você está encrencado.",
           "Vou deixar você doidão.",
           "Sou um baita de um Toonzinho.",
           ],
    'le': ["Cuidado, sou legal mas nem tanto.",
           "Eu pulo de galho em galho, mas alguns quebram.",
           "Vou fazer a lei chegar até você.",
           "Você já devia saber que tenho instintos criminosos.",
           "Vou fazer você ter pesadelos jurídicos.",
           "Você não vai ganhar esta batalha.",
           "Isto é tão divertido que deveria ser proibido por lei.",
           "Legalmente falando, você é muito pequeno para lutar comigo.",
           "Não há limites para os meus botes.",
           "Chamo isso de prisão de cidadão.",
           ],
    'sd': ["Você nunca saberá quando vou parar.",
           "Deixe-me levar você para uma volta.",
           "Vida social é comigo mesmo.",
           "Vou colocar você em um agito.",
           "Você parece precisar de animação.",
           "A festa está rolando, mas Toons não entram.",
           "Você não vai gostar do meu pitaco nisto.",
           "Você vai ficar fora de controle.",
           "Você se importa de dar umas voltinhas comigo?",
           "Tenho minha própria teoria sobre o assunto.",
           ],
    'f': ["Vou falar sobre você com o chefe!",
          "Posso ser apenas um puxa-saco, mas sou demais.",
          "Estou usando você para subir os vários degraus dentro da empresa.",
          "Você não vai gostar do jeito como eu trabalho.",
          "O chefe está contando comigo para deter você.",
          "Você vai ficar bonito no meu currículo.",
          "Você terá que passar por cima de mim primeiro.",
          "Vamos ver como você classifica meu desempenho funcional.",
          "Eu me sobressaio na eliminação de Toons.",
          "Você jamais conhecerá o meu chefe.",
          "Vou mandar você de volta para o Pátio.",
          ],
    'p':  ["Eu vou apagar você!",
           "Ei, você não pode ficar mandando em mim.",
           "Sou o número 2!",
           "Vou cortar você.",
           "Vou ter que me fazer mais claro.",
           "Deixe-me ir direto ao ponto.",
           "Rápido, eu fico irritado com facilidade.",
           "Odeio quando as coisas ficam bobas.",
           "Então, você quer arriscar a própria sorte?",
           "Você me passou o lápis?",
           "Cuidado, posso deixar uma marca.",
           ],
    'ym': ["Concordo com tudo.",
           "Não sei o que significa não.",
           "Quer me conhecer? Eu digo sim sempre.",
           "Você precisa de uma força positiva.",
           "Vou deixar uma impressão positiva.",
           "Ainda não me enganei.",
           "Sim, estou pronto para você.",
           "Acha mesmo que quer fazer isto?",
           "Você certamente terminará com saldo positivo nessa.",
           "Confirmando a hora da sua reunião.",
           "Não aceito não como resposta.",
           ],
    'mm': ["Vou entrar neste negócio.",
           "Às vezes, os piores venenos vêm em pequenos frascos.",
           "Nenhum trabalho é insignificante para mim.",
           "Quero o trabalho feito direito, por isso eu mesmo o faço.",
           "Você precisa de alguém para gerenciar os seus bens.",
           "Que bom, um projeto.",
           "Bem, você conseguiu me achar.",
           "Acho que você precisa de alguma organização.",
           "Vou cuidar de você em dois tempos.",
           "Estou observando tudo que você faz.",
           "Tem certeza de que deseja fazer isto?",
           "Vamos fazer da minha maneira.",
           "Vou estar na sua cola.",
           "Posso ser bem intimidador.",
           ],
    'ds': ["Você está caindo no meu golpe!",
           "Você vai encolher com meu ataque.",
           "Espere retornos minúsculos.",
           "Você vai deixar de existir.",
           "Não me peça nenhuma dispensa.",
           "Vou precisar fazer alguns cortes.",
           "As coisas parecem estar despedaçadas para você.",
           "Por que você parece tão machucado?",
           ],
    'cc': ["Surpreso de saber de mim?",
           "Você ligou?",
           "Está pronto para aceitar as minhas tarifas?",
           "Este aqui sempre recolhe alguma coisa.",
           "Eu opero bem as linhas.",
           "Espere um segundo, estou aqui.",
           "Estava esperando a minha ligação?",
           "Estava torcendo para você atender a minha ligação.",
           "Vou deixar uma sensação tocante.",
           "Sempre faço ligações diretas.",
           "Cara, tem boi na linha.",
           "Esta ligação terá um custo para você.",
           "Você tem um pepino nesta linha.",
           ],
    'tm': ["Meu plano é tornar isto inconveniente para você.",
           "Posso incluir você em um seguro?",
           "Você não deveria ter me atendido.",
           "Você não vai conseguir se livrar de mim agora.",
           "Tá chateado? Que bom.",
           "Estava pensando em atropelar você.",
           "Vou inverter as cobranças desta ligação.",
           "Tenho alguns itens bem caros para você hoje.",
           "Se deu mal, eu faço ligações locais.",
           "Estou preparado para fechar este negócio rapidinho.",
           "Vou usar um monte de recursos seus.",
           ],
    'nd': ["Na minha opinião, seu nome está na lama.",
           "Espero que não se importe se eu jogar o seu nome na boca das matildes.",
           "A gente já não se conhece?",
           "Depressa, vou almoçar com o Dr. Celebridade.",
           "Eu falei que conheço o Amizade Fácil?",
           "Você nunca vai me esquecer.",
           "Conheço todas as pessoas certas para detonar você.",
           "Acho que vou passar aí.",
           "Estou a fim de detonar alguns Toons.",
           "Eu te disse, detonei.",
           ],
    'gh': ["Diz aí, Toon.",
           "O bicho vai pegar.",
           "Vou gostar disso.",
           "Você vai acabar vendo as minhas garras.",
           "Vamos assinar embaixo.",
           "Vamos direto ao que interessa.",
           "Não cutuca a onça com vara curta, ou você vai acabar mal.",
           "Você vai acabar gostando da minha pinta.",
           "Olha que eu viro uma onça.",
           "Você não vai escapar das minhas garras.",
           "Você quer que eu safe a onça?",
           "Se ficar o bicho come, se correr o bicho pega.",
           "As marcas das minhas unhas afiadas estão na parede.",
           ],
    'sc': ["Vamos logo acabar com esta farsa.",
           "Você está prestes a ficar no vermelho.",
           "Você está prestes a pagar taxas abusivas.",
           "O projeto vai ser de fachada.",
           "Esta fraude vai ser moleza.",
           "Logo, logo você vai cair na minha arapuca.",
           "Vamos embromar um pouquinho.",
           "Veio cedo para ver o meu truque, né?",
           "Tenho pavio curto com Toons.",
           "Logo vou armar minha armadilha para você.",
           "Você está prestes a cair na minha lábia.",
           ],
    'pp': ["Meu aperto de mão é forte.",
           "Minha mão é de ferro.",
           "Você não quer que a vaca vá pro brejo, ou quer?",
           "Seu sorriso vai ficar pálido como leite.",
           "Tenho um lugar para você, mas não pense que sou mão-aberta.",
           "Deixe e pagar na mesma moeda.",
           "Dou tchau com a mão fechada.",
           "Vou provar que você não está sonhando.",
           "Cabeças vão rolar, e eu vou ganhar.",
           "Dou uma moedinha pelas suas piadas.",
           ],
    'tw': ["Vamos ter que dar duro.",
           "É o Pão-duro.",
           "Vou ter que cortar a sua verba.",
           "É a melhor oferta que você pode fazer?",
           "Vamos logo. Tempo é dinheiro.",
           "Você vai descobrir como dou duro.",
           "Você está na corda bamba.",
           "Prepare-se para a dureza.",
           "Você não conhece o pão que o diabo amassou.",
           "Vou ter que apertar o cinto.",
           "Vou fazer um rombo no seu orçamento.",
           ],
    'bc': ["Adoro subtrair Toons.",
           "Pode contar comigo para fazer você pagar.",
           "O negócio é contar as moedinhas.",
           "Contar é comigo mesmo.",
           "Sou um contador de balinhas.",
           "Sua planilha de gastos está excedendo o limite.",
           "É hora de fazer uma auditoria.",
           "Vamos entrar no meu escritório.",
           "Onde você estava? Eu contava com você.",
           "Estou esperando por você há um milhão de horas.",
           "Você não vale um níquel.",
           ],
    'bf': ["Parece que você chegou na hora do lanche.",
           "Estou pronto para o banquete.",
           "Sou um comedor de Toons.",
           "Êba, hora do almoço.",
           "Na hora certa! Preciso de um lanchinho.",
           "Gostaria de alguma opinião sobre o meu desempenho.",
           "Vamos falar sobre o que interessa.",
           "Você vai descobrir que tenho um talento imensurável.",
           "Bom, preciso de um pequeno estímulo.",
           "Adoraria se você almoçasse comigo.",
           ],
    'tf': ["Está na hora de nosso duelo!",
           "Melhor encarar a derrota.",
           "Prepare-se para enfrentar o seu pior pesadelo!",
           "Encare os fatos: eu sou melhor que você.",
           "Duas cabeças pensam melhor que uma.",
           "Se um não quer, dois não brigam. Quer brigar?",
           "Você está duplamente encrencado.",
           "Qual face você quer que o derrote?",
           "Eu sou demais para você.",
           "Você não sabe com quem está se metendo.",
           "Você está preparado para encarar sua derrota?",
           ],
    'dt': ["Você terá trabalho em dobro comigo.",
           "Veja se você consegue enfrentar meu golpe duplo.",
           "Trabalho para um ARMÁRIO 4x4 muito mau.",
           "Está na hora de um golpe duplo.",
           "Meu plano é ter duas FONTES.",
           "Você não vai gostar do meu jogo duplo.",
           "Talvez queira pensar duas vezes nisso.",
           "Prepare-se para uma LIGAÇÃO dupla.",
           "Talvez queira aplicar uma dose dupla contra mim.",
           "Duplas, alguém??",
           ],
    'ac': ["Eu vou botar você prá correr desta cidade!",
           "Está ouvindo uma sirene?",
           "Vou gostar disso.",
           "Adoro a emoção da perseguição.",
           "Vou dar um passa-fora.",
           "Você tem seguro?",
           "Espero que tenha trazido uma maca.",
           "Duvido que você possa comigo.",
           "É só ralação a partir daqui.",
           "Em breve você vai precisar de uma ambulância.",
           "Não é piada.",
           "Vou passar a parada para você.",
           ]
    }

# These are all the standard SpeedChat phrases.
# The indices must fit into 16 bits (0..65535)
SpeedChatStaticTextCommon = {
    # top-level
    1 : lYes,
    2 : lNo,
    3 : lOK,
    4 : "SPEEDCHAT PLUS",
    }

SpeedChatStaticTextToontown = {
    # Hello
    100 : "Oi!",
    101 : "Olá!",
    102 : "E aí?",
    103 : "Ôpa!",
    104 : "Tudo certo?",
    105 : "Oi, pessoal!",
    106 : "Bem-vindo a Toontown!",
    107 : "Tudo em cima?",
    108 : "Tudo bem?",
    109 : "Alô?",

    # Bye
    200 : "Tchau!",
    201 : "Até mais!",
    202 : "Te vejo por aí!",
    203 : "Bom dia pra você!",
    204 : "Divirta-se!",
    205 : "Boa sorte!",
    206 : "Já volto.",
    207 : "Tenho que ir.",
    208 : "Eu volto já!",
    209 : "Eu só tenho alguns minutos.",

    # Happy
    300 : ":-)",
    301 : "Valeu!",
    302 : "Maneiro!",
    303 : "Legal!",
    304 : "Iuhuu!",
    305 : "É isso aí!",
    306 : "Ah, ah!",
    307 : "He, he!",
    308 : "Uau!",
    309 : "Demais!",
    310 : "Iahuuuuu!",
    311 : "Nossa!",
    312 : "Uhuu!",
    313 : "Iupii!!",
    314 : "Dez!",
    315 : "Toontástico!",

    # Sad
    400 : ":-(",
    401 : "Ah, não!",
    402 : "Êpa!",
    403 : "Droga!",
    404 : "Ai, ai, ai!",
    405 : "Ahhh!",
    406 : "Puxa!",
    407 : "Não!!!",
    408 : "Pôxa vida!",
    409 : "Hã?",
    410 : "Preciso de mais pontos de Risadas.",

    # Friendly
    500 : "Valeu!",
    501 : "Sem problemas.",
    502 : "De nada!",
    503 : "Sempre que quiser!",
    504 : "Não, obrigado.",
    505 : "Bom trabalho de equipe!",
    506 : "Isso foi divertido!",
    507 : "Vamos ser amigos!",
    508 : "Vamos trabalhar juntos!",
    509 : "Vocês são demais!",
    510 : "Você é novo aqui?",
    511 : "Ganhou?",
    512 : "Acho arriscado prá você.",
    513 : "Quer ajuda?",
    514 : "Você me ajuda?",
    515 : "Você já veio aqui antes?",

    # Friendly "Você..."
    600 : "Você parece legal.",
    601 : "Você é incrível!",
    602 : "Você é maneiro!",
    603 : "Você é um gênio!",

    # Friendly "Gosto..."
    700 : "Gosto do seu nome.",
    701 : "Gosto do seu jeito.",
    702 : "Gosto da sua camisa.",
    703 : "Gosto da sua saia.",
    704 : "Gosto do seu short.",
    705 : "Gosto deste jogo!",

    # Sorry
    800 : "Desculpe!",
    801 : "Ops!",
    802 : "Desculpe, agora estou lutando com Cogs!",
    803 : "Desculpe, agora estou conseguindo balinhas!",
    804 : "Desculpe, agora estou completando uma Tarefa Toon!",
    805 : "Desculpe, tive que sair de repente.",
    806 : "Desculpe, fiquei preso.",
    807 : "Desculpe, não posso.",
    808 : "Não pude esperar mais.",
    809 : "Não entendi.",
    810 : "Use o %s." % GlobalSpeedChatName,
    811 : "Desculpe, estou ocupado pescando!",
    812 : "Desculpe, estou dentro de um prédio!",
    813 : "Desculpe, estou ajudando um amigo!",
    814 : "Desculpe, estou ocupado numa corrida de kart!",
    815 : "Desculpe, estou fazendo jardinagem agora!",
    816 : "Não posso entrar no elevador agora.",
    817 : "Desculpe, estou jogando golfe agora!",
    818 : "Desculpe, minha Lista de Amigos está cheia.",

    # Stinky
    900 : "Ôpa!",
    901 : "Vá embora!!",
    902 : "Pare com isso!",
    903 : "Isso não foi legal!",
    904 : "Não seja mau!",
    905 : "Você é nojento!",
    906 : "Envie um relatório de problemas.",
    907 : "Estou atolado.",

    # Places
    1000 : "Vamos!",
    1001 : "Você pode se teletransportar até a mim?",
    1002 : "Podemos ir?",
    1003 : "Para onde devemos ir?",
    1004 : "Em que direção?",
    1005 : "Esta direção.",
    1006 : "Siga-me.",
    1007 : "Espere por mim!",
    1008 : "Vamos esperar pelo meu amigo.",
    1009 : "Vamos encontrar outros Tonns.",
    1010 : "Espere aqui.",
    1011 : "Espere um minuto.",
    1012 : "Vamos nos encontrar aqui.",
    1013 : "Você pode ir até a minha casa?",
    1014 : "Não espere por mim.",
    1015 : "Espere!",
    1016 : "Venha dar uma olhada no meu jardim.",
    1017 : "Vamos pegar o próximo.",

    # Places "Vamos..."
    1100 : "Vamos pegar o bondinho!",
    1101 : "Vamos voltar para o pátio!",
    1102 : "Vamos lutar com %s!" % Cogs,
    1103 : "Vamos tomar um edifício %s!" % Cog,
    1104 : "Vamos entrar no elevador!",
    1105 : "Vamos para o Centro de Toontown!",
    1106 : "Vamos para o Porto do Donald!",
    1107 : "Vamos para a Melodilândia da Minnie!",
    1108 : "Vamos para os Jardins da Margarida!",
    1109 : "Vamos para O Brrrgh!",
    1110 : "Vamos para a Sonholândia do Donald!",
    1111 : "Vamos para a %s !" % lGoofySpeedway,
    1112 : "Vamos para a minha casa!",
    1113 : "Vamos para a sua casa!",
    1114 : "Vamos para o Quartel do Robô Vendedor!",
    1115 : "Vamos lutar com o VP!",
    1116 : "Vamos entrar na Fábrica!",
    1117 : "Vamos pescar!",
    1118 : "Vamos pescar na minha casa!",
    1119 : "Vamos para o Quartel do Robô Mercenário!",
    1120 : "Vamos lutar com o Diretor Financeiro!",
    1121 : "Vamos entrar na Casa da Moeda!",
    1122 : "Vamos para o Quartel do Robô da Lei!",
    1123 : "Vamos lutar com o Juiz Chefe!",
    1124 : "Vamos para o Escritório do Promotor Público!",
    1125 : "Vamos para %s!" % lOutdoorZone,
    1126 : "Vamos para %s!" % lGolfZone,
    1127 : "Vamos para o Quartel do Robô Chefe!",
    1128 : "Vamos lutar com o Presidente!",
    1129 : "Vamos para o Campo de Golfe Cog!",
    #1130 : "Let's go take over a Cogdominium!",
    1130 : "Let's go take over a Field Office!",

    # Toontasks
    1200 : "Em que Tarefa Toon você está trabalhando?",
    1201 : "Vamos trabalhar nisto.",
    1202 : "Isto não é o que estou procurando.",
    1203 : "Vou procurar isto.",
    1204 : "Não está nesta rua.",
    1205 : "Não encontrei ainda.",
    1206 : "Preciso de mais Méritos por Cogs.",
    1207 : "Preciso de mais peças de vestimentas de Cogs.",
    1208 : "Não é disso que você precisa.",
    1209 : "Achei o que você precisa.",
    1210 : "Eu preciso de mais Cograna.",
    1211 : "Eu preciso de mais Avisos ao Júri.",
    1212 : "Preciso de mais Ações.",
    1213 : "Eu preciso de mais Peças de Vestimenta de Robô Mercenário.",
    1214 : "Eu preciso de mais Peças de Vestimenta de Robô da Lei.",
    1215 : "Preciso de mais Peças de Robô Chefe.",

    1299 : "Preciso pegar uma Tarefa Toon.",

    # Toontasks "Acho que você devia escolher..."
    1300 : "Acho que você devia escolher Toonar.",
    1301 : "Acho que você devia escolher Sonora.",
    1302 : "Acho que você devia escolher Cadente.",
    1303 : "Acho que você devia escolher Armadilha.",
    1304 : "Acho que você devia escolher Isca.",

    # Battle
    1400 : "Anda!",
    1401 : "Que tiro!",
    1402 : "Que piada!",
    1403 : "Não me acertou!",
    1404 : "Conseguiu!",
    1405 : "Conseguimos!",
    1406 : "Ataque!",
    1407 : "Moleza!",
    1408 : "Esta foi fácil!",
    1409 : "Corre!",
    1410 : "Socorro!",
    1411 : "Ufa!",
    1412 : "Estamos em apuros.",
    1413 : "Preciso de mais piadas.",
    1414 : "Preciso de uma Toonar.",
    1415 : "Você deve passar.",
    1416 : "Vamos conseguir!",

    # Battle "Vamos usar..."
    1500 : "Vamos usar toonar!",
    1501 : "Vamos usar armadilha!",
    1502 : "Vamos usar isca!",
    1503 : "Vamos usar sonora!",
    1504 : "Vamos usar lançamento!",
    1505 : "Vamos usar esguicho!",
    1506 : "Vamos usar cadente!",

    # Battle TAUNTS
    1520 : "É hora do Rock!",
    1521 : "Isso deve doer.",
    1522 : "Pegue!",
    1523 : "Entrega especial!",
    1524 : "Você ainda está aqui?",
    1525 : "Ai, que medo!",
    1526 : "Esta vai deixar cicatriz!",

    # Battle STRATEGY
    1550 : "Vou usar uma armadilha.",
    1551 : "Vou usar uma isca.",
    1552 : "Vou usar uma cadente.",
    1553 : "Você devia usar uma piada diferente.",
    1554 : "Vamos todos no mesmo Cog.",
    1555 : "Você devia escolher um Cog diferente.",
    1556 : "Vá no Cog mais fraco primeiro.",
    1557 : "Vá no Cog mais forte primeiro.",
    1558 : "Economize as piadas mais poderosas.",
    1559 : "Não use som em Cogs dominados por iscas.",

    # Gag Shop
    1600 : "Tenho piadas suficientes.",
    1601 : "Preciso de mais balinhas.",
    1602 : "Eu também.",
    1603 : "Vamos nessa!",
    1604 : "Mais um?",
    1605 : "Jogar de novo?",
    1606 : "Vamos jogar de novo.",

    # Factory
    1700 : "Vamos nos separar.",
    1701 : "Vamos ficar juntos.",
    1702 : "Vamos lutar com os Cogs.",
    1703 : "Pise no interruptor.",
    1704 : "Passe pela porta.",

    # Sellbot Factory
    1803 : "Estou na Entrada principal.",
    1804 : "Estou no Salão.",
    1805 : "Estou no corredor fora do Salão.",
    1806 : "Estou no corredor fora do Salão.",
    1807 : "Estou na Sala de engrenagens.",
    1808 : "Estou na Sala da caldeira.",
    1809 : "Estou na Passarela leste.",
    1810 : "Estou no Misturador de tinta.",
    1811 : "Estou no Depósito do Misturador de tinta.",
    1812 : "Estou na Passarela do Silo Oeste.",
    1813 : "Estou na Sala de tubulações.",
    1814 : "Estou nas escadas da Sala de tubulações.",
    1815 : "Estou na Sala de dutos.",
    1816 : "Estou na Entrada lateral.",
    1817 : "Estou no Beco sinistro.",
    1818 : "Estou fora do Salão de lava.",
    1819 : "Estou no Salão de lava.",
    1820 : "Estou no Depósito de lava.",
    1821 : "Estou na Passarela oeste.",
    1822 : "Estou na Sala de óleo.",
    1823 : "Estou na Vigilância do Armazém.",
    1824 : "Estou no Armazém.",
    1825 : "Estou fora do Misturador de tinta.",
    1827 : "Estou fora da Sala de óleo.",
    1830 : "Estou na Sala de controle do Silo Leste.",
    1831 : "Estou na Sala de controle do Silo Oeste.",
    1832 : "Estou na Sala de controle do Silo Central.",
    1833 : "Estou no Silo Leste.",
    1834 : "Estou no Silo Oeste.",
    1835 : "Estou no Silo Central.",
    1836 : "Estou no Silo Oeste.",
    1837 : "Estou no Silo Leste.",
    1838 : "Estou na Passarela do Silo Leste.",
    1840 : "Estou no topo do Silo Oeste.",
    1841 : "Estou no topo do Silo Leste.",
    1860 : "Estou no Elevador do Silo Oeste.",
    1861 : "Estou no Elevador do Silo Leste.",

    # Sellbot Factory continued
    1903 : "Vamos nos encontrar na Entrada principal.",
    1904 : "Vamos nos encontrar no Salão.",
    1905 : "Vamos nos encontrar no corredor fora do salão.",
    1906 : "Vamos nos encontrar no corredor fora do salão.",
    1907 : "Vamos nos encontrar na Sala de engrenagens.",
    1908 : "Vamos nos encontrar na Sala da caldeira.",
    1909 : "Vamos nos encontrar na Passarela leste.",
    1910 : "Vamos nos encontrar no Misturador de tinta.",
    1911 : "Vamos nos encontrar no Depósito do Misturador de tinta.",
    1912 : "Vamos nos encontrar na Passarela do Silo Oeste.",
    1913 : "Vamos nos encontrar na Sala de tubulações.",
    1914 : "Vamos nos encontrar nas escadas da Sala de tubulações.",
    1915 : "Vamos nos encontrar na Sala de dutos.",
    1916 : "Vamos nos encontrar na Entrada lateral.",
    1917 : "Vamos nos encontrar no Beco sinistro.",
    1918 : "Vamos nos encontrar fora do Salão de lava.",
    1919 : "Vamos nos encontrar no Salão de lava.",
    1920 : "Vamos nos encontrar no Depósito de lava.",
    1921 : "Vamos nos encontrar na Passarela oeste.",
    1922 : "Vamos nos encontrar na Sala de óleo.",
    1923 : "Vamos nos encontrar na Vigilância do Armazém.",
    1924 : "Vamos nos encontrar no Armazém.",
    1925 : "Vamos nos encontrar fora do Misturador de tinta.",
    1927 : "Vamos nos encontrar fora da Sala de óleo.",
    1930 : "Vamos nos encontrar na Sala de controle do Silo Leste.",
    1931 : "Vamos nos encontrar na Sala de controle do Silo Oeste.",
    1932 : "Vamos nos encontrar na Sala de controle do Silo Central.",
    1933 : "Vamos nos encontrar no Silo Leste.",
    1934 : "Vamos nos encontrar no Silo Oeste.",
    1935 : "Vamos nos encontrar no Silo Central.",
    1936 : "Vamos nos encontrar no Silo Oeste.",
    1937 : "Vamos nos encontrar no Silo Leste.",
    1938 : "Vamos nos encontrar na Passarela do Silo Leste.",
    1940 : "Vamos nos encontrar no topo do Silo Oeste.",
    1941 : "Vamos nos encontrar no topo do Silo Leste.",
    1960 : "Vamos nos encontrar no Elevador do Silo Oeste.",
    1961 : "Vamos nos encontrar no Elevador do Silo Leste.",

    # These are used only for the style settings in the OptionsPage
    # These should never actually be spoken or listed on the real speed chat
    2000 : "Lilás",
    2001 : "Azul",
    2002 : "Ciano",
    2003 : "Azul petróleo",
    2004 : "Verde",
    2005 : "Amarelo",
    2006 : "Laranja",
    2007 : "Vermelho",
    2008 : "Rosa",
    2009 : "Marrom",
    # Shader specific
    2050 : "None",
    2051 : "B&W",
    2052 : "Sepia",

    # CFO battle
    2100 : "Opere o guindaste.",
    2101 : "Posso operar o guindaste?",
    2102 : "Preciso de prática para operar o guindaste.",
    2103 : "Escolha um brutamontes desativado.",
    2104 : "Jogue o brutamontes no Diretor Financeiro.",
    2105 : "Agora jogue um cofre!",
    2106 : "Não jogue o cofre agora!",
    2107 : "O cofre vai derrubar o capacete dele.",
    2108 : "O cofre vai virar o novo capacete dele.",
    2109 : "Não consigo chegar a nenhum cofre.",
    2110 : "Não consigo chegar a nenhum brutamontes.",

    2120 : "Desative os brutamontes.",
    2121 : "Prefiro desativar os brutamontes.",
    2122 : "Preciso de prática para desativar brutamontes.",
    2123 : "Fique por perto.",
    2124 : "Fique circulando.",
    2125 : "Preciso circular.",
    2126 : "Procure alguém que precise de ajuda.",

    2130 : "Guarde os tesouros.",
    2131 : "Pegue os tesouros.",
    2132 : "Preciso de tesouros!",
    2133 : "Cuidado!",

    # CJ battle
    2200 : "Você precisa acertar a balança.",
    2201 : "Eu vou acertar a balança.",
    2202 : "Eu preciso de ajuda com a balança!",
    2203 : "Você precisa atordoar os Cogs.",
    2204 : "Eu vou atordoar os Cogs.",
    2205 : "Eu preciso de ajuda com os Cogs!",
    2206 : "Eu preciso de mais evidências.",
    2207 : "Eu fico com as cadeiras da fileira de cima.",
    2208 : "Eu fico com as cadeiras da fileira de baixo.",
    2209 : "Saia da frente! Não podemos atingir o prato.",
    2210 : "Eu faço as piadas Toonar.",
    2211 : "Eu não tenho peso bônus.",
    2212 : "Eu tenho peso bônus de 1.",
    2213 : "Eu tenho peso bônus de 2.",
    2214 : "Eu tenho peso bônus de 3.",
    2215 : "Eu tenho peso bônus de 4.",
    2216 : "Eu tenho peso bônus de 5.",
    2217 : "Eu tenho peso bônus de 6.",
    2218 : "Eu tenho peso bônus de 7.",
    2219 : "Eu tenho peso bônus de 8.",
    2220 : "Eu tenho peso bônus de 9.",
    2221 : "Eu tenho peso bônus de 10.",
    2222 : "Eu tenho peso bônus de 11.",
    2223 : "Eu tenho peso bônus de 12.",

    # CEO battle
    2300 : "Você alimenta os Cogs à esquerda.",
    2301 : "Vou alimentar os Cogs à esquerda.",
    2302 : "Você alimenta os Cogs à direita.",
    2303 : "Vou alimentar os Cogs à direita.",
    2304 : "Você alimenta os Cogs à frente.",
    2305 : "Vou alimentar os Cogs à frente.",
    2306 : "Você alimenta os Cogs de trás.",
    2307 : "Vou alimentar os Cogs de trás.",
    2308 : "Você usa a garrafa de água com gás.",
    2309 : "Vou usar a garrafa de água com gás.",
    2310 : "Você usa o taco de golfe.",
    2311 : "Vou usar o taco de golfe.",
    2312 : "Vou servir esta mesa.",
    2313 : "Pode servir esta mesa?",
    2314 : "Alimente o mesmo Cog de novo.",
    2315 : "Depressa, seu Cog está com fome!",
    2316 : "Reserve os lanches para Toons mais tristes.",
    2317 : "Pegue os lanches antes que eles caiam.",


    #Kart Racing Phrases
    #IMPORTANT: if you change numbers or add/subtract lines here than be
    # sure to adjust the kart racing menu guid dict below
    # Invites/Destinations
    3010 : "Alguém quer apostar corrida?",
    3020 : "Vamos apostar corrida!",
    3030 : "Quer apostar corrida?",
    3040 : "Vamos mostrar nossos karts!",
    3050 : "Não tenho tíquetes suficientes.",
    3060 : "Vamos apostar outra corrida!",
    3061 : "Quer apostar outra corrida?",

    #Places
    3150 : "Preciso ir à Loja do kart.",
    3160 : "Vamos para a pista de corrida!",
    3170 : "Vamos para a largada para mostrar nossos karts!",
    3180 : "Vou para a largada mostrar meu kart!",
    3190 : "A gente se encontra na pista de corrida!",
    3110 : "O ponto de encontro é a Loja do kart!",
    3130 : "Onde a gente se encontra?",

    #Races
    3200 : "Onde você quer correr?",
    3201 : "Vamos escolher uma corrida diferente.",
    3210 : "Vamos fazer uma corrida de aquecimento." ,
    3211 : "Vamos fazer um campeonato de corrida.",
    3220 : "Eu gosto da corrida do Estádio dos Nerds!",
    3221 : "Eu gosto da corrida do Autódromo Rústico!",
    3222 : "Eu gosto da corrida do Circuito da Cidade!",
    3223 : "Eu gosto da corrida do Coliseu Saca-Rolhas!",
    3224 : "Eu gosto da corrida da Pista de Pulos!",
    3222 : "Eu gosto da corrida do Circuito da Cidade!",
    3230 : "Vamos correr no Estádio dos Nerds!",
    3231 : "Vamos correr no Autódromo Rústico!",
    3232 : "Vamos correr no Circuito da Cidade!",
    3233 : "Vamos correr no Coliseu Saca-Rolhas!",
    3234 : "Vamos correr na Pista de Pulos!",
    3235 : "Vamos correr na Avenida da Neve!",

    #Tracks
    3600 : "Em que pista você quer correr?",
    3601 : "Escolha uma pista!",
    3602 : "A gente pode correr em uma pista diferente?",
    3603 : "Vamos escolher uma pista diferente!",
    3640 : "Quero correr na primeira pista!",
    3641 : "Quero correr na segunda pista!",
    3642 : "Quero correr na terceira pista!",
    3643 : "Quero correr na quarta pista!",
    3660 : "Não quero correr na primeira pista!",
    3661 : "Não quero correr na segunda pista!",
    3662 : "Não quero correr na terceira pista!",
    3663 : "Não quero correr na quarta pista!",

    #Compliments
    3300 : "Uau! Você é RÁPIDO!",
    3301 : "Você é muito rápido para mim!",
    3310 : "Boa corrida!",
    3320 : "Eu me amarrei no seu kart!",
    3330 : "Uma corrida maravilhosa!",
    3340 : "Seu kart é muito maneiro!",
    3350 : "Seu kart é incrível!",
    3360 : "Seu kart é maravilhoso!",

    #Taunts (commented out taunts are for possible purchase lines)
    #3400 : "Coma a minha poeira!",
    3400 : "Tá com medo de me enfrentar?",
    3410 : "Vejo você na linha de chegada!",
    #3420 : "Você é mais devagar que tartaruga!",
    3430 : "Sou rápido como um raio!",
    #3440 : "Sou mais veloz que a luz!",
    3450 : "Você nunca vai me alcançar!",
    3451 : "Você nunca vai me derrotar!",
    3452 : "Ninguém consegue bater o meu tempo!",
    3453 : "Vamos embora, molenga!",
    3460 : "Me dá outra chance!",
    3461 : "Foi sorte a sua!",
    3462 : "Uh-huu! Essa foi perto!",
    3470 : "Uau, pensei que você tinha me vencido!",
    #3500 : "Dá uma olhada na minha máquina!",
    #3510 : "Olha só as minhas rodas!",
    #3540 : "Vruum! Vruum!",
    #3560 : "Eu já vi Cogs mais rápidos que isso!",
    #3600 : "Sou o mais rápido dos mais rápidos!",

    # Golf phrases

    # Play
    4000 : "Vamos jogar minigolfe!",
    4001 : "Vamos jogar de novo!",
    4002 : "Quer jogar golfe?",

    # Courses
    4100 : "Vamos jogar no 'Tacada e Caminhada'.",
    4101 : "Vamos jogar no 'Tacadas Divertidas'.",
    4102 : "Vamos jogar no 'Todas as Tacadas'.",
    4103 : "Esse percurso é fácil demais.",
    4104 : "Esse percurso é difícil demais.",
    4105 : "Esse percurso está ótimo.",

    # Tips
    4200 : "Tente ficar mais para a esquerda.",
    4201 : "Tente ficar mais para a direita.",
    4202 : "Tente ficar bem no meio.",
    4203 : "Tente bater mais forte.",
    4204 : "Tente bater mais fraco.",
    4205 : "Tente mirar mais para a esquerda.",
    4206 : "Tente mirar mais para a direita.",
    4207 : "Tente mirar bem no meio.",

    # Comments
    4300 : "Por pouco!",
    4301 : "Que tacada sensacional!",
    4302 : "Essa foi uma tacada de sorte.",
    4303 : "Quero mais uma chance...",
    4304 : "Essa é muito fácil.",
    4305 : "Bola!",
    4306 : "Shhhh!",
    4307 : "Grande jogo!",

    # Boarding Group phrases

    5000 : "Vamos formar um Grupo de Abordagem.",
    5001 : "Junte-se ao meu Grupo de Abordagem.",
    5002 : "Você pode me convidar para o seu Grupo de Abordagem?",
    5003 : "Já faço parte de um Grupo de Abordagem.",
    5004 : "Sair do seu Grupo de Abordagem.",
    5005 : "Estamos abordando agora.",
    5006 : "Aonde vamos?",
    5007 : "Preparados?",
    5008 : "Vamos!",
    5009 : "Não saia dessa área ou sairá do Grupo de Abordagem.",

    # Let's Go to...
    5100 : "Vamos para o Três da Frente.",
    5101 : "Vamos para o Seis do Meio.",
    5102 : "Vamos para o Nove dos Fundos.",
    5103 : "Vamos para a Batalha do Presidente.",
    5104 : "Vamos para a Batalha do V. P. Sênior.",
    5105 : "Vamos para a Entrada da Frente.",
    5106 : "Vamos para a Entrada dos Fundos.",
    5107 : "Vamos para a Casa da Moeda.",
    5108 : "Vamos para a Casa da Moeda de Dólar.",
    5109 : "Vamos para a Casa da Moeda de Barras de Ouro.",
    5110 : "Vamos para a Batalha do Diretor Financeiro.",
    5111 : "Vamos para a Batalha do Juiz-Chefe.",
    5112 : "Vamos para o Escritório da Lei A.",
    5113 : "Vamos para o Escritório da Lei B.",
    5114 : "Vamos para o Escritório da Lei C.",
    5115 : "Vamos para o Escritório da Lei D.",

    # We're going to...
    5200 : "Estamos indo para o Três da Frente.",
    5201 : "Estamos indo para o Seis do Meio.",
    5202 : "Estamos indo para o Nove dos Fundos.",
    5203 : "Estamos indo para a Batalha do Presidente.",
    5204 : "Estamos indo para a Batalha do V. P. Sênior.",
    5205 : "Estamos indo para a Entrada da Frente.",
    5206 : "Estamos indo para a Entrada dos Fundos.",
    5207 : "Estamos indo para a Casa da Moeda.",
    5208 : "Estamos indo para a Casa da Moeda de Dólar.",
    5209 : "Estamos indo para a Casa da Moeda de Barras de Ouro.",
    5210 : "Estamos indo para a Batalha do Diretor Financeiro.",
    5211 : "Estamos indo para a Batalha do Juiz-Chefe.",
    5212 : "Estamos indo para o Escritório da Lei A.",
    5213 : "Estamos indo para o Escritório da Lei B.",
    5214 : "Estamos indo para o Escritório da Lei C.",
    5215 : "Estamos indo para o Escritório da Lei D.",

    # Parties General Phrases
    5300 : "Vamos para uma festa.",
    5301 : "Vejo você na festa!",
    5302 : "Minha festa começou!",
    5303 : "Venha para minha festa!",
    # Parties Phrases when inside a party
    5304 : "Vamos brincar de Cabo de Guerra!",
    5305 : "Vamos brincar de Pega-pega!",
    5306 : "Vamos dançar!",
    5307 : "Para a pista de dança!",
    5308 : "Lançar fogos de artifício!",
    5309 : "Veja como eu pulo!",
    5310 : "Gosto dessa música!",
    5311 : "Essa música é legal!",
    5312 : "Esta festa é maneira!",
    5313 : "Sua festa é animada!",
    5314 : "Trampolins são divertidos!",
    5315 : "É hora da diversão!",
    5316 : "Canhões são uma curtição!",
    5317 : "O tempo está acabando!",
    5318 : "Decoração bacana.",
    5319 : "Eu queria comer esse bolo!",
    5320 : "Esses fogos de artifício são lindos!",
    5321 : "Cogs não entram!",
    5322 : "Queria comer este bolo!",

    # Promotional Considerations
    10000 : "A escolha é sua!",
    10001 : "Você vai votar em quem?",
    10002 : "A minha candidata é a Galinha!",
    10003 : "Nada de caca! Vote na Vaca!",
    10004 : "Não fique no vácuo! Vote no Macaco!",
    10005 : "Mantenha o curso! Vote no Urso!",
    10006 : "Pense gordo! Vote no Porco!",
    10007 : "Vote no Bode - com ele a gente pode!",

    # cog phrases for disguised toons
    # (just references to cog dialog above)

    # common cog phrases
    20000 : SuitBrushOffs[None][0],
    20001 : SuitBrushOffs[None][1],
    20002 : SuitBrushOffs[None][2],
    20003 : SuitBrushOffs[None][3],
    20004 : SuitBrushOffs[None][4],

    # specific cog phrases
    20005: SuitFaceoffTaunts['bf'][0],
    20006: SuitFaceoffTaunts['bf'][1],
    20007: SuitFaceoffTaunts['bf'][2],
    20008: SuitFaceoffTaunts['bf'][3],
    20009: SuitFaceoffTaunts['bf'][4],
    20010: SuitFaceoffTaunts['bf'][5],
    20011: SuitFaceoffTaunts['bf'][6],
    20012: SuitFaceoffTaunts['bf'][7],
    20013: SuitFaceoffTaunts['bf'][8],
    20014: SuitFaceoffTaunts['bf'][9],

    20015: SuitFaceoffTaunts['nc'][0],
    20016: SuitFaceoffTaunts['nc'][1],
    20017: SuitFaceoffTaunts['nc'][2],
    20018: SuitFaceoffTaunts['nc'][3],
    20019: SuitFaceoffTaunts['nc'][4],
    20020: SuitFaceoffTaunts['nc'][5],
    20021: SuitFaceoffTaunts['nc'][6],
    20022: SuitFaceoffTaunts['nc'][7],
    20023: SuitFaceoffTaunts['nc'][8],
    20024: SuitFaceoffTaunts['nc'][9],

    20025: SuitFaceoffTaunts['ym'][0],
    20026: SuitFaceoffTaunts['ym'][1],
    20027: SuitFaceoffTaunts['ym'][2],
    20028: SuitFaceoffTaunts['ym'][3],
    20029: SuitFaceoffTaunts['ym'][4],
    20030: SuitFaceoffTaunts['ym'][5],
    20031: SuitFaceoffTaunts['ym'][6],
    20032: SuitFaceoffTaunts['ym'][7],
    20033: SuitFaceoffTaunts['ym'][8],
    20034: SuitFaceoffTaunts['ym'][9],
    20035: SuitFaceoffTaunts['ym'][10],

    20036: SuitFaceoffTaunts['ms'][0],
    20037: SuitFaceoffTaunts['ms'][1],
    20038: SuitFaceoffTaunts['ms'][2],
    20039: SuitFaceoffTaunts['ms'][3],
    20040: SuitFaceoffTaunts['ms'][4],
    20041: SuitFaceoffTaunts['ms'][5],
    20042: SuitFaceoffTaunts['ms'][6],
    20043: SuitFaceoffTaunts['ms'][7],
    20044: SuitFaceoffTaunts['ms'][8],
    20045: SuitFaceoffTaunts['ms'][9],
    20046: SuitFaceoffTaunts['ms'][10],

    20047: SuitFaceoffTaunts['bc'][0],
    20048: SuitFaceoffTaunts['bc'][1],
    20049: SuitFaceoffTaunts['bc'][2],
    20050: SuitFaceoffTaunts['bc'][3],
    20051: SuitFaceoffTaunts['bc'][4],
    20052: SuitFaceoffTaunts['bc'][5],
    20053: SuitFaceoffTaunts['bc'][6],
    20054: SuitFaceoffTaunts['bc'][7],
    20055: SuitFaceoffTaunts['bc'][8],
    20056: SuitFaceoffTaunts['bc'][9],
    20057: SuitFaceoffTaunts['bc'][10],

    20058: SuitFaceoffTaunts['cc'][0],
    20059: SuitFaceoffTaunts['cc'][1],
    20060: SuitFaceoffTaunts['cc'][2],
    20061: SuitFaceoffTaunts['cc'][3],
    20062: SuitFaceoffTaunts['cc'][4],
    20063: SuitFaceoffTaunts['cc'][5],
    20064: SuitFaceoffTaunts['cc'][6],
    20065: SuitFaceoffTaunts['cc'][7],
    20066: SuitFaceoffTaunts['cc'][8],
    20067: SuitFaceoffTaunts['cc'][9],
    20068: SuitFaceoffTaunts['cc'][10],
    20069: SuitFaceoffTaunts['cc'][11],
    20070: SuitFaceoffTaunts['cc'][12],

    20071: SuitFaceoffTaunts['nd'][0],
    20072: SuitFaceoffTaunts['nd'][1],
    20073: SuitFaceoffTaunts['nd'][2],
    20074: SuitFaceoffTaunts['nd'][3],
    20075: SuitFaceoffTaunts['nd'][4],
    20076: SuitFaceoffTaunts['nd'][5],
    20077: SuitFaceoffTaunts['nd'][6],
    20078: SuitFaceoffTaunts['nd'][7],
    20079: SuitFaceoffTaunts['nd'][8],
    20080: SuitFaceoffTaunts['nd'][9],

    20081: SuitFaceoffTaunts['ac'][0],
    20082: SuitFaceoffTaunts['ac'][1],
    20083: SuitFaceoffTaunts['ac'][2],
    20084: SuitFaceoffTaunts['ac'][3],
    20085: SuitFaceoffTaunts['ac'][4],
    20086: SuitFaceoffTaunts['ac'][5],
    20087: SuitFaceoffTaunts['ac'][6],
    20088: SuitFaceoffTaunts['ac'][7],
    20089: SuitFaceoffTaunts['ac'][8],
    20090: SuitFaceoffTaunts['ac'][9],
    20091: SuitFaceoffTaunts['ac'][10],
    20092: SuitFaceoffTaunts['ac'][11],

    20093: SuitFaceoffTaunts['tf'][0],
    20094: SuitFaceoffTaunts['tf'][1],
    20095: SuitFaceoffTaunts['tf'][2],
    20096: SuitFaceoffTaunts['tf'][3],
    20097: SuitFaceoffTaunts['tf'][4],
    20098: SuitFaceoffTaunts['tf'][5],
    20099: SuitFaceoffTaunts['tf'][6],
    20100: SuitFaceoffTaunts['tf'][7],
    20101: SuitFaceoffTaunts['tf'][8],
    20102: SuitFaceoffTaunts['tf'][9],
    20103: SuitFaceoffTaunts['tf'][10],

    20104: SuitFaceoffTaunts['hh'][0],
    20105: SuitFaceoffTaunts['hh'][1],
    20106: SuitFaceoffTaunts['hh'][2],
    20107: SuitFaceoffTaunts['hh'][3],
    20108: SuitFaceoffTaunts['hh'][4],
    20109: SuitFaceoffTaunts['hh'][5],
    20110: SuitFaceoffTaunts['hh'][6],
    20111: SuitFaceoffTaunts['hh'][7],
    20112: SuitFaceoffTaunts['hh'][8],
    20113: SuitFaceoffTaunts['hh'][9],
    20114: SuitFaceoffTaunts['hh'][10],

    20115: SuitFaceoffTaunts['le'][0],
    20116: SuitFaceoffTaunts['le'][1],
    20117: SuitFaceoffTaunts['le'][2],
    20118: SuitFaceoffTaunts['le'][3],
    20119: SuitFaceoffTaunts['le'][4],
    20120: SuitFaceoffTaunts['le'][5],
    20121: SuitFaceoffTaunts['le'][6],
    20122: SuitFaceoffTaunts['le'][7],
    20123: SuitFaceoffTaunts['le'][8],
    20124: SuitFaceoffTaunts['le'][9],

    20125: SuitFaceoffTaunts['bs'][0],
    20126: SuitFaceoffTaunts['bs'][1],
    20127: SuitFaceoffTaunts['bs'][2],
    20128: SuitFaceoffTaunts['bs'][3],
    20129: SuitFaceoffTaunts['bs'][4],
    20130: SuitFaceoffTaunts['bs'][5],
    20131: SuitFaceoffTaunts['bs'][6],
    20132: SuitFaceoffTaunts['bs'][7],
    20133: SuitFaceoffTaunts['bs'][8],
    20134: SuitFaceoffTaunts['bs'][9],
    20135: SuitFaceoffTaunts['bs'][10],

    20136: SuitFaceoffTaunts['cr'][0],
    20137: SuitFaceoffTaunts['cr'][1],
    20138: SuitFaceoffTaunts['cr'][2],
    20139: SuitFaceoffTaunts['cr'][3],
    20140: SuitFaceoffTaunts['cr'][4],
    20141: SuitFaceoffTaunts['cr'][5],
    20142: SuitFaceoffTaunts['cr'][6],
    20143: SuitFaceoffTaunts['cr'][7],
    20144: SuitFaceoffTaunts['cr'][8],
    20145: SuitFaceoffTaunts['cr'][9],

    20146: SuitFaceoffTaunts['tbc'][0],
    20147: SuitFaceoffTaunts['tbc'][1],
    20148: SuitFaceoffTaunts['tbc'][2],
    20149: SuitFaceoffTaunts['tbc'][3],
    20150: SuitFaceoffTaunts['tbc'][4],
    20151: SuitFaceoffTaunts['tbc'][5],
    20152: SuitFaceoffTaunts['tbc'][6],
    20153: SuitFaceoffTaunts['tbc'][7],
    20154: SuitFaceoffTaunts['tbc'][8],
    20155: SuitFaceoffTaunts['tbc'][9],
    20156: SuitFaceoffTaunts['tbc'][10],

    20157: SuitFaceoffTaunts['ds'][0],
    20158: SuitFaceoffTaunts['ds'][1],
    20159: SuitFaceoffTaunts['ds'][2],
    20160: SuitFaceoffTaunts['ds'][3],
    20161: SuitFaceoffTaunts['ds'][4],
    20162: SuitFaceoffTaunts['ds'][5],
    20163: SuitFaceoffTaunts['ds'][6],
    20164: SuitFaceoffTaunts['ds'][7],

    20165: SuitFaceoffTaunts['gh'][0],
    20166: SuitFaceoffTaunts['gh'][1],
    20167: SuitFaceoffTaunts['gh'][2],
    20168: SuitFaceoffTaunts['gh'][3],
    20169: SuitFaceoffTaunts['gh'][4],
    20170: SuitFaceoffTaunts['gh'][5],
    20171: SuitFaceoffTaunts['gh'][6],
    20172: SuitFaceoffTaunts['gh'][7],
    20173: SuitFaceoffTaunts['gh'][8],
    20174: SuitFaceoffTaunts['gh'][9],
    20175: SuitFaceoffTaunts['gh'][10],
    20176: SuitFaceoffTaunts['gh'][11],
    20177: SuitFaceoffTaunts['gh'][12],

    20178: SuitFaceoffTaunts['pp'][0],
    20179: SuitFaceoffTaunts['pp'][1],
    20180: SuitFaceoffTaunts['pp'][2],
    20181: SuitFaceoffTaunts['pp'][3],
    20182: SuitFaceoffTaunts['pp'][4],
    20183: SuitFaceoffTaunts['pp'][5],
    20184: SuitFaceoffTaunts['pp'][6],
    20185: SuitFaceoffTaunts['pp'][7],
    20186: SuitFaceoffTaunts['pp'][8],
    20187: SuitFaceoffTaunts['pp'][9],

    20188: SuitFaceoffTaunts['b'][0],
    20189: SuitFaceoffTaunts['b'][1],
    20190: SuitFaceoffTaunts['b'][2],
    20191: SuitFaceoffTaunts['b'][3],
    20192: SuitFaceoffTaunts['b'][4],
    20193: SuitFaceoffTaunts['b'][5],
    20194: SuitFaceoffTaunts['b'][6],
    20195: SuitFaceoffTaunts['b'][7],
    20196: SuitFaceoffTaunts['b'][8],
    20197: SuitFaceoffTaunts['b'][9],
    20198: SuitFaceoffTaunts['b'][10],
    20199: SuitFaceoffTaunts['b'][11],

    20200: SuitFaceoffTaunts['f'][0],
    20201: SuitFaceoffTaunts['f'][1],
    20202: SuitFaceoffTaunts['f'][2],
    20203: SuitFaceoffTaunts['f'][3],
    20204: SuitFaceoffTaunts['f'][4],
    20205: SuitFaceoffTaunts['f'][5],
    20206: SuitFaceoffTaunts['f'][6],
    20207: SuitFaceoffTaunts['f'][7],
    20208: SuitFaceoffTaunts['f'][8],
    20209: SuitFaceoffTaunts['f'][9],
    20210: SuitFaceoffTaunts['f'][10],

    20211: SuitFaceoffTaunts['mm'][0],
    20212: SuitFaceoffTaunts['mm'][1],
    20213: SuitFaceoffTaunts['mm'][2],
    20214: SuitFaceoffTaunts['mm'][3],
    20215: SuitFaceoffTaunts['mm'][4],
    20216: SuitFaceoffTaunts['mm'][5],
    20217: SuitFaceoffTaunts['mm'][6],
    20218: SuitFaceoffTaunts['mm'][7],
    20219: SuitFaceoffTaunts['mm'][8],
    20220: SuitFaceoffTaunts['mm'][9],
    20221: SuitFaceoffTaunts['mm'][10],
    20222: SuitFaceoffTaunts['mm'][11],
    20223: SuitFaceoffTaunts['mm'][12],
    20224: SuitFaceoffTaunts['mm'][13],

    20225: SuitFaceoffTaunts['tw'][0],
    20226: SuitFaceoffTaunts['tw'][1],
    20227: SuitFaceoffTaunts['tw'][2],
    20228: SuitFaceoffTaunts['tw'][3],
    20229: SuitFaceoffTaunts['tw'][4],
    20230: SuitFaceoffTaunts['tw'][5],
    20231: SuitFaceoffTaunts['tw'][6],
    20232: SuitFaceoffTaunts['tw'][7],
    20233: SuitFaceoffTaunts['tw'][8],
    20234: SuitFaceoffTaunts['tw'][9],
    20235: SuitFaceoffTaunts['tw'][10],

    20236: SuitFaceoffTaunts['mb'][0],
    20237: SuitFaceoffTaunts['mb'][1],
    20238: SuitFaceoffTaunts['mb'][2],
    20239: SuitFaceoffTaunts['mb'][3],
    20240: SuitFaceoffTaunts['mb'][4],
    20241: SuitFaceoffTaunts['mb'][5],
    20242: SuitFaceoffTaunts['mb'][6],
    20243: SuitFaceoffTaunts['mb'][7],
    20244: SuitFaceoffTaunts['mb'][8],
    20245: SuitFaceoffTaunts['mb'][9],

    20246: SuitFaceoffTaunts['m'][0],
    20247: SuitFaceoffTaunts['m'][1],
    20248: SuitFaceoffTaunts['m'][2],
    20249: SuitFaceoffTaunts['m'][3],
    20250: SuitFaceoffTaunts['m'][4],
    20251: SuitFaceoffTaunts['m'][5],
    20252: SuitFaceoffTaunts['m'][6],
    20253: SuitFaceoffTaunts['m'][7],
    20254: SuitFaceoffTaunts['m'][8],

    20255: SuitFaceoffTaunts['mh'][0],
    20256: SuitFaceoffTaunts['mh'][1],
    20257: SuitFaceoffTaunts['mh'][2],
    20258: SuitFaceoffTaunts['mh'][3],
    20259: SuitFaceoffTaunts['mh'][4],
    20260: SuitFaceoffTaunts['mh'][5],
    20261: SuitFaceoffTaunts['mh'][6],
    20262: SuitFaceoffTaunts['mh'][7],
    20263: SuitFaceoffTaunts['mh'][8],
    20264: SuitFaceoffTaunts['mh'][9],
    20265: SuitFaceoffTaunts['mh'][10],
    20266: SuitFaceoffTaunts['mh'][11],

    20267: SuitFaceoffTaunts['dt'][0],
    20268: SuitFaceoffTaunts['dt'][1],
    20269: SuitFaceoffTaunts['dt'][2],
    20270: SuitFaceoffTaunts['dt'][3],
    20271: SuitFaceoffTaunts['dt'][4],
    20272: SuitFaceoffTaunts['dt'][5],
    20273: SuitFaceoffTaunts['dt'][6],
    20274: SuitFaceoffTaunts['dt'][7],
    20275: SuitFaceoffTaunts['dt'][8],
    20276: SuitFaceoffTaunts['dt'][9],

    20277: SuitFaceoffTaunts['p'][0],
    20278: SuitFaceoffTaunts['p'][1],
    20279: SuitFaceoffTaunts['p'][2],
    20280: SuitFaceoffTaunts['p'][3],
    20281: SuitFaceoffTaunts['p'][4],
    20282: SuitFaceoffTaunts['p'][5],
    20283: SuitFaceoffTaunts['p'][6],
    20284: SuitFaceoffTaunts['p'][7],
    20285: SuitFaceoffTaunts['p'][8],
    20286: SuitFaceoffTaunts['p'][9],
    20287: SuitFaceoffTaunts['p'][10],

    20288: SuitFaceoffTaunts['tm'][0],
    20289: SuitFaceoffTaunts['tm'][1],
    20290: SuitFaceoffTaunts['tm'][2],
    20291: SuitFaceoffTaunts['tm'][3],
    20292: SuitFaceoffTaunts['tm'][4],
    20293: SuitFaceoffTaunts['tm'][5],
    20294: SuitFaceoffTaunts['tm'][6],
    20295: SuitFaceoffTaunts['tm'][7],
    20296: SuitFaceoffTaunts['tm'][8],
    20297: SuitFaceoffTaunts['tm'][9],
    20298: SuitFaceoffTaunts['tm'][10],

    20299: SuitFaceoffTaunts['bw'][0],
    20300: SuitFaceoffTaunts['bw'][1],
    20301: SuitFaceoffTaunts['bw'][2],
    20302: SuitFaceoffTaunts['bw'][3],
    20303: SuitFaceoffTaunts['bw'][4],
    20304: SuitFaceoffTaunts['bw'][5],
    20305: SuitFaceoffTaunts['bw'][6],
    20306: SuitFaceoffTaunts['bw'][7],
    20307: SuitFaceoffTaunts['bw'][8],
    20308: SuitFaceoffTaunts['bw'][9],

    20309: SuitFaceoffTaunts['ls'][0],
    20310: SuitFaceoffTaunts['ls'][1],
    20311: SuitFaceoffTaunts['ls'][2],
    20312: SuitFaceoffTaunts['ls'][3],
    20313: SuitFaceoffTaunts['ls'][4],
    20314: SuitFaceoffTaunts['ls'][5],
    20315: SuitFaceoffTaunts['ls'][6],
    20316: SuitFaceoffTaunts['ls'][7],
    20317: SuitFaceoffTaunts['ls'][8],
    20318: SuitFaceoffTaunts['ls'][9],
    20319: SuitFaceoffTaunts['ls'][10],

    20320: SuitFaceoffTaunts['rb'][0],
    20321: SuitFaceoffTaunts['rb'][1],
    20322: SuitFaceoffTaunts['rb'][2],
    20323: SuitFaceoffTaunts['rb'][3],
    20324: SuitFaceoffTaunts['rb'][4],
    20325: SuitFaceoffTaunts['rb'][5],
    20326: SuitFaceoffTaunts['rb'][6],
    20327: SuitFaceoffTaunts['rb'][7],
    20328: SuitFaceoffTaunts['rb'][8],
    20329: SuitFaceoffTaunts['rb'][9],

    20330: SuitFaceoffTaunts['sc'][0],
    20331: SuitFaceoffTaunts['sc'][1],
    20332: SuitFaceoffTaunts['sc'][2],
    20333: SuitFaceoffTaunts['sc'][3],
    20334: SuitFaceoffTaunts['sc'][4],
    20335: SuitFaceoffTaunts['sc'][5],
    20336: SuitFaceoffTaunts['sc'][6],
    20337: SuitFaceoffTaunts['sc'][7],
    20338: SuitFaceoffTaunts['sc'][8],
    20339: SuitFaceoffTaunts['sc'][9],
    20340: SuitFaceoffTaunts['sc'][10],

    20341: SuitFaceoffTaunts['sd'][0],
    20342: SuitFaceoffTaunts['sd'][1],
    20343: SuitFaceoffTaunts['sd'][2],
    20344: SuitFaceoffTaunts['sd'][3],
    20345: SuitFaceoffTaunts['sd'][4],
    20346: SuitFaceoffTaunts['sd'][5],
    20347: SuitFaceoffTaunts['sd'][6],
    20348: SuitFaceoffTaunts['sd'][7],
    20349: SuitFaceoffTaunts['sd'][8],
    20350: SuitFaceoffTaunts['sd'][9],

    # Pets/Doodles
    21000: 'Aqui, amigão!',
    21001: 'Aqui, amigona!',
    21002: 'Parado.',
    21003: 'Bom garoto!',
    21004: 'Boa menina!',
    21005: 'Rabisco bonzinho.',
    21006: 'Por favor, não me chateie.',

    # Pet/Doodle Tricks
    21200: 'Pule!',
    21201: 'Dê a pata!',
    21202: 'Finja de morto!',
    21203: 'Role!',
    21204: 'Dê cambalhota!',
    21205: 'Dance!',
    21206: 'Fale!',

    # Phrases for April Toon's week
    30100 : "Feliz Semana Abril Toons!",
    30101 : "Bem-vindo à minha festa da Semana Abril Toons!",
    30102 : "The Silly Meter is back in Toon Hall!",
    30110 : "Mickey está nos Jardins da Margarida.",
    30111 : "Margarida está na Central Toontown.",
    30112 : "Minnie está no Brrrgh.",
    30113 : "Pluto está na Terra da Melodia.",
    30114 : "Donald, sonâmbulo, está perambulando no Circuito.",
    30115 : "Pateta está na Terra dos Sonhos.",

    30120 : "Mickey está imitando Margarida!",
    30121 : "Margarida está imitando Mickey!",
    30122 : "Minnie está imitando Pluto!",
    30123 : "Pluto está imitando Minnie!",
    30124 : "Pluto está falando!",
    30125 : "Pateta está imitando Donald!",
    30126 : "Donald está sonhando que é o Pateta!",

    30130 : "Veja como posso saltar longe.",
    30131 : "Uau, você saltou realmente longe!",
    30132 : "Ei, Doodles podem falar!",
    30133 : "O seu Doodle acabou de falar?",
    30140 : "As coisas certamente são bobinhas por aqui!",
    30141 : "As coisas são bobinhas mesmo, hein?",

    # Phrases for Sellbot Nerf Event
    30150 : "Aqui está a Operação: Robô Vendedor Tempestade!",
    30151 : "As Torres dos Robô Vendedor tiveram seus poderes sugados por Doodles!",
    30152 : "O VP teve seus poderes sugados por Doodles!",
    30153 : "Todos podem lutar contra o VP agora!",
    30154 : "Você não precisa de um Traje de Robô Vendedor para lutar contra o VP!",
    30155 : "Você ganha um Traje de Aluguel quando entrar nas Torres dos Robôs Vendedores.",
    30156 : "Você gosta do meu Traje de Aluguel? Desculpe-me pelos alfinetes!",
    30157 : "É melhor ter oito Toons para lutar contra o VP.",
    30158 : "Você vai me ajudar a lutar contra o VP?",
    30159 : "Você quer lutar contra o VP junto comigo?",
    30160 : "Você gostaria de se juntar ao meu grupo Robô Vendedor VP?",
    30161 : "Eu estou procurando por um Toon com um Traje de Aluguel para lutar contra o VP.",
    30162 : "Eu tenho um Traje de Aluguel, e estou ansioso para lutar contra o VP.",
    30163 : "Passe pelas portas e consiga o Traje de Aluguel.",
    30164 : "Evite os Cogs na recepção! Poupe seus itens para os de dentro!",
    30165 : "Temos que derrotar estes Cogs antes!",
    30166 : "Bata nos barris para conquistar seus gags.",
    30167 : "Bata no barril para ganhar um Toon-up.",
    30168 : "Agora temos que combater alguns Skelecogs!",
    30169 : "Pule e toque na gaiola do Toon para ganhar tortas!",
    30170 : "Agora vamos lutar contra o VP!",
    30171 : "Mire suas tortas apertando a tecla Del.",
    30172 : "Dois Toons devem arremessar tortas pelas portas abertas do VP.!",
    30173 : "Eu surpreendo o VP pela frente.",
    30174 : "Eu surpreendo o VP por trás.",
    30175 : "Salte quando o VP salta!",

    # Phrases for Jellybean Jam
    30180 : "Meu banco contém 12.000 balinhas!",
    30181 : "Preciso encher meu novo banco de balinha!",
    30182 : "Quer pegar balinhas?",
    30183 : "Consegui balinhas em dobro no Bonde!",
    30184 : "Consegui balinhas em dobro na pescaria!",
    30185 : "Consegui balinhas em dobro em um grupo!",
    30186 : "Quero adotar um Doodle!",
    30187 : "Eu adotei um Doodle!",
    30188 : "Vou adotar um Doodle com todas essas balinhas!",
    30189 : "Há novas camisetas Cattlelog para grupos de balinhas!",
    30190 : "A Tropa Toon está lançando grupos de balinhas no Bosque de Bolotas!",
    30191 : "Balinhas, por favor!",
    30192 : "Não seja mau, me dê uma bala!",
    30193 : "Quem quer balinhas?",
    30194 : "Dance por balinhas!",

    # Phrases for caroling
    30200 : "Decore os salões... ",
    30201 : "Faça muitas tortas...",
    30202 : "Toons alegres...",
    30203 : "Cabeças de bonecos de neve...",
    30204 : "A felicidade de Toontown...",
    30205 : "Atraia alegria...",

    30220 : "Decore os salões com neve em spray!\nBoas Festas!",
    30221 : "Carregue seu trenó com tortas!\nBoas Festas!",
    30222 : "Toons alegres derrotam a maldade dos Cogs!\nBoas Festas!",
    30223 : "Os bonecos de neve estão de cabeça quente hoje!\nBoas Festas!",
    30224 : "Toontown está feliz. Que venha o que vier!\nBoas Festas!",
    30225 : "Atraia alegria para Toontown!\nBoas Festas!",

    # Phrases for Halloween
    30250: "Bu!",
    30251: "Feliz Halloween!",
    30252: "Assustador!",

    # Phrases for Christmas
    30275: "Boas-festas!",
    30276: "Feliz Ano-Novo!",
    30277: "Tenha um inverno maravilhoso!",

    # Phrases for Silly Story
    30301 : "Você viu o Medidor de Bobagens?",
    30302 : "O Medidor de Bobagens está no Salão de Desenhos.",
    30303 : "As coisas certamente são bobinhas por aqui!",
    30304 : "Eu vi um hidrante se mexendo!",
    30305 : "Toontown está ganhando vida!",
    30306 : "Já esteve no novo escritório do Flippy?",
    30307 : "Eu causei uma Onda de Bobagem na batalha!",
    30308 : "Vamos derrotar alguns Cogs para deixar Toontown mais bobinha!",

    30309 : "O Medidor de Bobagens está maior e mais doido do que nunca!",
    30310 : "Um monte de hidrantes ganhou vida!",
    30311 : "Eu vi uma caixa de correio se mexendo!",
    30312 : "Eu vi uma lixeira acordando!",
    30313 : "Quão bobo pode ser isso?",
    30314 : "O que vai acontecer a seguir?",
    30315 : "Algo bobinho, aposto!",
    30316 : "Já causou uma Onda de Bobagem?",
    30317 : "Vamos derrotar alguns Cogs para deixar Toontown mais bobinha!",

    30318 : "Invasão de Cogs!",
    30319 : "Chegando!",
    30320 : "Vamos impedir esses Cogs de avançarem!",
    30321 : "Errei as Ondas de Bobagens!",
    30322 : "Vamos impedir a Invasão!",
    30323 : "Agora Toontown está mais bobinha do que nunca!",
    30324 : "Você viu alguma coisa ganhar vida?",
    30325 : "Meus favoritos são os hidrantes!",
    30326 : "Minhas favoritas são as caixas de correio!",
    30327 : "Minhas favoritas são as lixeiras!",

    30328 : "Viva! Impedimos a Invasão de Cogs",
    30329 : "Um hidrante me ajudou na batalha!",
    30330 : "Um hidrante reforçou meus Itens de Esguicho!",
    30331 : "Uma lixeira me deu um Toon-Up!",
    30332 : "Uma caixa de correio ajudou com os Itens de Arremesso!",

    # Phrases for Victory Parties (warning 30400 is in use)
    30350 : "Bem-vindos à minha festa da vitória!",
    30351 : "Esta é uma ótima festa da vitória!",
    30352 : "Mostramos àqueles Cogs quem é que manda!",
    30353 : "Bom trabalho em ajudar a impedir as invasões de Cogs!",
    30354 : "Aposto que isto está deixando os Cogs doidos!",

    30355 : "Vamos encarar uma Cog-O-War!",
    30356 : "Minha equipe venceu na Cog-O-War!",
    30357 : "É legal ter hidrantes, lixeiras e caixas de correio aqui!",
    30358 : "Gosto quando o balão do Doodle morde o Cog!",
    30359 : "Gosto do balão do Cog coberto de sorvete!",
    30360 : "Gosto quando o Cog agita seus braços!",
    30361 : "Pulei na cara de um Cog!",

    # Phrases for Sellbot Field Offices
    30400: "The Sellbots are invading!",
    30401: "The V.P. was hopping mad about Operation: Storm Sellbot ...",
    30402: "He's sending the Sellbots in to invade Toontown!",
    30403: "Let's go fight some Sellbots!",
    30404: "There's a new kind of building in Toontown!",
    30405: "Have you seen the Mover & Shaker Field Offices?",
    30406: "The V.P. created them as a reward for the Movers & Shakers.",
    30407: "Let's go defeat a Field Office!",
    30408: "I got an SOS Card for defeating a Field Office!",
    30409: "Clear the map by exploring the maze.",
    30410: "Destroy the Cogs by hitting them with water balloons!",
    30411: "Movers & Shakers take two balloons to destroy.",
    30412: "Look out for falling objects!",
    30413: "Watch out for the Cogs!",
    30414: "Collect Jokes to get a Toon-up at the end!",
    30415: "When the room shakes, a Mover & Shaker is nearby.",
    30416: "Defeat all four Movers & Shakers to open the exit!",
    30417: "The exit is open!",
    30418: "It's the Boss!",

    # Phrases for Ides Of March
    30450: "It's easy to be green!",
    30451: "Visit Green Bean Jeans and you can be green too!",
    30452: "It's on Oak Street in Daisy Gardens.",

    # Phrases for Lawbot Nerf Event
    30460 : "Operation: Lawbots Lose is here!",
    30461 : "The Doodles have done it again!",
    30462 : "The Chief Justice had his power drained by Doodles!",
    30463 : "Everyone can fight the Chief Justice right now!",
    30464 : "You don't need a Lawbot Disguise to fight the CJ!",
    30465 : "You get a Rental Suit when you go into the Courtroom in Lawbot HQ.",
    30466 : "Do you like my Rental Suit? The safety pins are so stylish!",
    30467 : "It's best to have eight Toons to fight the CJ.",
    30468 : "Will you help me fight the CJ?",
    30469 : "Would you like to join my Lawbot CJ group?",
    30470 : "I am looking for a Toon with a Rental Suit to fight the CJ.",
    30471 : "I have a Rental Suit, and want to fight the CJ!",
    30472 : "Just walk through the doors to get your Rental Suit.",
    30473 : "Save your gags for the Cogs inside!",
    30474 : "We have to defeat these Cogs first!",
    30475 : "Bump the barrels to get a Toon-up.",
    30476 : "Use the Chief Justice SpeedChatMenu!",
    30477 : "Now we have to fill the jury chairs with Toons!",
    30478 : "The more Toons we get in, the easier it will be to defeat the CJ!",
    30479 : "Now we fight the Chief Justice!",
    30480 : "Touch the witness stand to collect evidence.",
    30481 : "Watch out for the gavels!",
    30482 : "When you hit the scale, the CJ turns red!",
    30483 : "When the Cogs get evidence in the scale, the CJ turns green!",
    30484 : "Something cool happens if we stun all the Cogs at once!",
    30485 : "Throw evidence at Toons to give them a Toon-up!",

    # Phrases for Singing
##    9000 : 'Middle ' + 'G1',
##    9001 : 'Middle ' + 'A',
##    9002 : 'Middle ' + 'B',
##    9003 : 'Middle ' + 'C',
##    9004 : 'Middle ' + 'D',
##    9005 : 'Middle ' + 'E',
##    9006 : 'Middle ' + 'F',
##    9007 : 'Middle ' + 'G2'
    }

SpeedChatStaticTextPirates = {
    # PIRATES ROOT - TOP LEVEL
    50001 : 'Sim',
    50002 : 'Não',
    50003 : 'Arrr!',
    50004 : 'Sim, sim, Capitão!',
    50005 : 'Ok',

    # EXPRESSIONS
    50100 : "Todos a bordo!",
    50101 : "Ei, marujo!",
    50102 : "Alto lá!",
    50103 : "Abram caminho!",
    50104 : "Caramba!",
    50105 : "Me explodiram!",
    50106 : "Ei, você!",
    50107 : "Claro, claro, Capitão!",
    50108 : "Ande na prancha!",
    50109 : "Continue!",
    50110 : "Não vai sobrar ninguém para contar a história...",
    50111 : "A finer bunch of Scoundrels yarrr eyes have never seen!",
    50112 : "Fool me once, shame on me. Fool me twice, good luck in Davy Jones' Locker.",
    50113 : "Ready your bravery, hoist the sails, a Caribbean Pirate never fails!",

    # EXPRESSIONS - GREETINGS
    50700 : "Ahoy!",
    50701 : "Ahoy, colega!",
    50702 : "Yo-Ho-Ho",
    50703 : "Basta!",
    50704 : "Ei, Fanfarrão.",

    # EXPRESSIONS - GOODBYES
    50800 : "Até a próxima.",
    50801 : "Bons ventos levem você.",
    50802 : "Boa sorte.",


    # EXPRESSIONS - FRIENDLY
    50900 : "Como está, colega?",
    50901 : "",

    # EXPRESSIONS - HAPPY
    51000 : "Está chovendo dobrões de ouro!",
    51001 : "Que o vento sopre forte, o sol aqueça nossas faces e os canhões disparem certeiros!",

    # EXPRESSIONS - SAD
    51100 : "Hoje estou atravessando mares tempestuosos.",

    # EXPRESSIONS - SORRY
    51200 : "Me desculpe, colega.",
    51201 : "Perdão.",
    51202 : "Desculpe, estava ocupado antes.",
    51203 : "Sinto muito, já tenho planos.",
    51204 : "Desculpe, não preciso fazer isso.",

    # COMBAT
    51300 : "Ataque o mais fraco!",
    51301 : "Ataque o mais forte!",
    51302 : "Ataque meu alvo!",
    51303 : "Preciso de ajuda!",
    51304 : "Não consigo causar dano!",
    51305 : "Acho que estamos encrencados.",
    51306 : "Cerque o mais poderoso.",
    51307 : "Vamos fugir.",
    51308 : "Não deixe escapar!",

    # SEA COMBAT
    51400 : "Disparar a toda carga!",
    51401 : "Bombordo! (esquerda)",
    51402 : "Estibordo! (direita)",
    51403 : "Chegando!",
    51404 : "Virando de lado!",
    51405 : "Costado! Protejam-se!",
    51406 : "Aos canhões!",
    51407 : "Disparar!",
    51408 : "Cessar fogo!",
    51409 : "Mire no mastro!",
    51410 : "Mire no casco!",
    51411 : "Preparar para abordar!",
    51412 : "Ela está virando de lado.",
    51413 : "A toda vela!",
    51414 : "Está escapando.",
    51415 : "Temos uma inundação!",
    51416 : "Não podemos continuar!",
    51417 : "Não posso disparar!",
    51418 : "Vamos encontrar um porto para os reparos.",
    51419 : "Homem ao mar!",
    51420 : "Inimigo localizado.",
    51421 : "Gentilmente, colegas!",

    # PLACES
    50400 : "Içar velas.",
    50401 : "Vamos sair daqui.",
    50402 : "Let's get out of here.",
    50403 : "Let's get out of here.",
    50404 : "Let's get out of here.",

    # PLACES - LETS SAIL...
    51500 : "Vamos navegar até Port Royal.",
    51501 : "Vamos navegar até Tortuga.",
    51502 : "Vamos navegar até Padres Del Fuego.",
    51503 : "Vamos navegar até Devil's Anvil (a Bigorna do Diabo).",
    51504 : "Vamos navegar até Kingshead (a Coroa do Rei).",
    51505 : "Vamos navegar até Isla Perdida.",
    51506 : "Vamos navegar até Cuba.",
    51507 : "Vamos navegar até Tormenta.",
    51508 : "Vamos navegar até a Ilha Outcast (dos Excluídos).",
    51509 : "Vamos navegar até Driftwood.",
    51510 : "Vamos navegar até Cutthroat (a Garganta Cortada).",
    51511 : "Vamos navegar até a Ilha Rumrunner (dos Contrabandistas).",
    51512 : "Vamos navegar até Isla Cangrejos.",

    # PLACES - LETS HEAD TO...
    51600 : "Vamos para a cidade.",
    51601 : "Vamos para as docas.",
    51602 : "Vamos para a taverna.",

    # PLACES - LETS HEAD TO... - PORT ROYAL
    51800 : "Vamos para o Forte Charles.",
    51801 : "Vamos para o Palácio do Governador.",

    # PLACES - WHERE IS ..?
    52500 : "Onde estou, colega?",

    # DIRECTIONS
    51700 : "Chegamos lá.",
    51701 : "Não sei.",
    51702 : "Estamos na ilha errada.",
    51703 : "Isso é na cidade.",
    51704 : "Parece que é fora da cidade.",
    51705 : "Terão de procurar dentro da selva.",
    51706 : "Nas profundezas da terra.",
    51707 : "Oh, deve ser pela costa.",

    # Insults
    50200 : "Seu rato de porão!",
    50201 : "Seu cão sarnento!",
    50202 : "Vejo você no fundo do mar!",
    50203 : "Patife!",
    50204 : "Marujo de terra firme!",
    50205 : "Cabeça de bagre!",
    50206 : "Você precisa de uma espada afiada e inteligência aguçada.",
    50207 : "Você tem teias de aranha na cabeça, colega!",
    50208 : "Cuidado com o que fala ou corto sua língua!",
    50209 : "Touch me loot and you get the boot!",
    50210 : "The horizon be as empty as yer head.",
    50211 : "You're a canvas shy of a full sail, aren't ye mate?",

    # Compliments
    50300 : "Belo disparo, colega!",
    50301 : "Um golpe bem dado!",
    50302 : "Boa tentativa!",
    50303 : "Que bom ver você!",
    50304 : "Mostramos a eles!",
    50305 : "Vocês não são tão ruins assim!",
    50306 : "Que bela pilhagem fizemos!",

    # Adventures
    50500 : "Vamos içar velas!",
    50501 : "Suba a bordo! Estamos zarpando!",
    50502 : "Vamos saquear!",
    50503 : "Vamos navegar até Bilgewater!",
    50504 : "Vamos navegar até Port Royale.",
    50505 : "Vamos usar um Mapa do Tesouro!",
    50506 : "Vamos retornar ao Porto.",

    # Ships
    50600 : "Bombordo! (esquerda)",
    50601 : "Estibordo! (direita)",
    50602 : "Chegando!",
    50603 : "Costado! Protejam-se!",
    50604 : "Armar canhões!",
    50605 : "Disparar!",
    50606 : "Cessar fogo!",
    50607 : "Mire no mastro!",
    50608 : "Mire no casco!",
    50609 : "Preparar para abordar!",
    50610 : "Ela está virando de lado!",
    50611 : "Disparar a toda carga!",
    50612 : "A toda vela!",
    50613 : "Arrr! Estamos indo!",
    50614 : "Está escapando!",
    50615 : "Temos uma inundação!",
    50616 : "Não podemos continuar!",
    50617 : "Precisamos de reparos!",
    50618 : "Recuar!",
    50619 : "Homem ao mar!",
    50620 : "Basta! Uma Esquadra Ligeira imunda!",

    # Card Games
    52400  : "May luck be my lady.",
    52401 : "I think these cards be marked!",
    52402 : "Blimey cheater!",

    # Card Games - Poker
    51900 : "That's a terrible flop!",
    51901 : "Trying to buy the hand, are ye?",
    51902 : "Ye be bluffing.",
    51903 : "I don't think ye had it.",
    51904 : "Saved by the river.",

    # Card Games - Blackjack
    52600 : "Hit me.",
    52601 : "Can I get another dealer?",

    # Minigames
    # Minigames - Fishing
    53101 : "I caught a fish!",
    53102 : "I saw a Legendary Fish!",
    53103 : "What did you catch?",
    53104 : "This will make a whale of a tale!",
    53105 : "That was a beauty!",
    53106 : "Arr, the sea is treacherous today.",
    53107 : "What a bountiful haul of fish!",
    53110 : "Do you have the Legendary Lure?",
    53111 : "Have you ever caught a Legendary Fish?",
    53112 : "Can you sail on a fishing boat?",
    53113 : "Where is the Fishing Master?",
    53114 : "Have you completed your fish collection?",
    # Minigames - Cannon Defense
    53120 : "Fire at my target!",
    53121 : "Fire at the ship closest to the shore!",
    53122 : "There's a ship getting away!",
    53123 : "Fire at the big ships!",
    53124 : "Fire at the small ships!",
    53125 : "More are coming!",
    53126 : "We're not going to last much longer!",
    53127 : "Shoot the barrels!",
    53128 : "We've got new ammo!",
    53129 : "Sturdy defense, mates!",
    # Minigames - Potion Brewing
    53141 : "Look at the potion I made!",
    53142 : "Have you completed your potion collection?",
    53143 : "Where is the Gypsy?",
    53144 : "What potion is that?",
    53145 : "This potion was easy enough.",
    53146 : "This potion was hard brewin', I tell ye!",
    # Minigames - Repair
    53160 : "We need someone to bilge pump!",
    53161 : "We need someone to scrub!",
    53162 : "We need someone to saw!",
    53163 : "We need someone to brace!",
    53164 : "We need someone to hammer!",
    53165 : "We need someone to patch!",
    53166 : "I'll do it!",
    53167 : "Keep it up, this ship won't repair itself!",
    53168 : "Great job repairing the ship!",

    # Invitations
    52100 : "Want to group up?",
    52101 : "Join me crew?",

    # Invitations - Hunting
    52200 : "Fight some skeletons?",
    52201 : "Fight some crabs?",

    # Invitations - Versus
    52300 : "How 'bout a game of Mayhem?",
    52301 : "Join me Mayhem game.",
    52302 : "Want to start a Mayhem game?",
    52303 : "Want to start a team battle game?",
    52304 : "Join me team battle game.",

    # Invitations - Minigames
    52350 : "Join my Cannon Defense.",
    52351 : "Want to start a Cannon Defense?",
    52352 : "Can you lend me a hand with Repair?",
    52353 : "We need to Repair the ship now!",
    52354 : "Care to catch some fish?",
    52355 : "Want to go fishing with me?",
    52356 : "Join me crew for some fishin'?",
    52357 : "Time to brew some potions!",
    52358 : "You should try your hand at brewing potions.",

    # PLACES - WHERE IS..? - PORT ROYAL (LEGACY)
    52000 : "",

    # PLACES - WHERE IS..? - PORT ROYAL (Legacy)
    52000 : "",

    # PLACES - WHERE IS..? - TORTUGA (Legacy)
    52700 : "",

    # PLACES - WHERE IS..? - PADRES DEL FUEGO (Legacy)
    53000 : "",

    # PLACES - WHERE IS..? - PADRES DEL FUEGO - LOS PADRES (Legacy)
    52800 : "",

    # PLACES  - WHERE IS..? - PADRES DEL FUEGO - LAS PULGAS (Legacy)
    52900 : "",

    # Adventures (LEGACY)
    50500 : "",

    # Ships (LEGACY)
    50600 : "",

    # Greetings
    60100 : "Oi",
    60101 : "Olá!",
    60102 : "Oi!",
    60103 : "Ei!",
    60104 : "Oi, pessoal!",
    60105 : "Como é que está?",
    60106 : "Qual é?",

    # Bye
    60200 : "Tchau!",
    60201 : "Até mais!",
    60202 : "Vejo você por aí!",
    60203 : "Volto já!",
    60204 : "Tenho que ir.",

    # Happy
    60300 : ":-)",
    60301 : "Legal!",
    60302 : "É isso aí!",
    60303 : "Ha ha!",
    60304 : "Que fofo!",
    60305 : "É isso aí!",
    60306 : "Que maneiro!",
    60307 : "Irado!",
    60308 : "Incrível!",
    60309 : "Uau!",

    # Sad
    60400 : ":-(",
    60401 : "Aahh!",
    60402 : "Poxa, cara!",
    60403 : "Ai!",
    60404 : "Poxa!",

    # Places
    60500 : "Cadê você?",
    60501 : "Vamos para a Loja da Entrada!",
    60502 : "Vamos para a Discoteca!",
    60503 : "Vamos para Toontown.",
    60504 : "Vamos para os Piratas do Caribe!",

    # Animated Emotes
    60505 : "Girar moeda",
    60506 : "Dançar",
    60507 : "Canto 1",
    60508 : "Canto 2",
    60509 : "Dançar animado",
    60510 : "Dormir",
    60511 : "Flexionar",
    60512 : "Tocar Alaúde",
    60513 : "Tocar Flauta",
    60514 : "Frustração",
    60515 : "Procurando",
    60516 : "Bocejar",
    60517 : "Ajoelhar",
    60518 : "Varrer",
    60519 : "Enfeitar",
    60520 : "Bocejar",
    60521 : "Dançar",
    60522 : "Não",
    60523 : "Sim",
    60524 : "Rir",
    60525 : "Aplaudir",
    60526 : "Sorrir",
    60527 : "Raiva",
    60528 : "Medo",
    60529 : "Triste",
    60530 : "Comemorar",
    60668 : "Comemorar",
    60669 : "Dormir",
    60602 : "Furioso",
    60614 : "Aplaudir",
    60622 : "Assustado",
    60640 : "Rir",
    60652 : "Triste",
    60657 : "Sorrir",
    60664 : "Acenar",
    60665 : "Piscar",
    60666 : "Bocejar",
    60669 : "Dormir",
    60670 : "Dançar",
    60676 : "Flertar",
    60677 : "Dança do Zumbi",
    60678 : "Barulhento",

    # Valentines day emote string options
    60671 : "Olá, sou um Pirata e estou aqui para roubar seu coração.",
    60672 : "Acabo de encontrar o tesouro que procurava.",
    60673 : "Se você fosse uma meleca te pegava primeiro.",
    60674 : "Vem sempre aqui em Tortuga?",
    60675 : "Você tem um mapa? Acabo de me perder em seu olhar.",

    65000 : "Sim",
    65001 : "Não",

    60909 : "Check Hand",
    }

SpeedChatStaticText = SpeedChatStaticTextCommon

# Emote IDs - These are used in SC to determine if a msg is a animated emote
Emotes_Root = "EMOÇÕES"
Emotes_Dances = "Danças"
Emotes_General = "Geral"
Emotes_Music = "Música"
Emotes_Expressions = "Emoções"
Emote_ShipDenied = "Não é possível se emocionar ao navegar."
Emote_MoveDenied = "Não é possível se emocionar ao mover-se."
Emote_CombatDenied = "Não é possível se emocionar ao lutar."
Emote_CannonDenied = "Não é possível se emocionar ao usar um canhão."
Emote_SwimDenied = "Não é possível se emocionar ao nadar."
Emote_ParlorGameDenied = "Não é possível se emocionar durante um jogo de salão."
Emotes = (60505, 60506, 60509, 60510, 60511, 60516, 60519, 60520, 60521, 60522, 60523, 60524, 60525, 60526, 60527, 60528, 60529, 60530, 60602, 60668, 60614, 60622, 60640, 60644, 60652, 60657, 60664, 60665, 60666, 60669, 60612, 60661, 60645, 60629, 60641, 60654, 60630, 60670, 60633,
          # Valentines Day Emote
          60676,
          # Yes/No
          65000, 65001
          )

# These indexes, defined above, will construct a submenu in the FACTORY menu
# to allow the user to describe all the places he might want to meet
SCFactoryMeetMenuIndexes = (1903, 1904, 1906, 1907, 1908, 1910, 1913,
                            1915, 1916, 1917, 1919, 1922, 1923,
                            1924, 1932, 1940, 1941)


# CustomSCStrings: SpeedChat phrases available for purchase.  It is
# safe to remove entries from this list, which will disable them for
# use from any toons who have already purchased them.  Note that the
# index numbers are stored directly in the database, so once assigned
# to a particular phrase, a given index number should never be
# repurposed to any other phrase.
CustomSCStrings = {
    # Series 1
    10 : "Bom...",
    20 : "Por que não?",
    30 : "Claro!",
    40 : "É assim que se faz isso.",
    50 : "Maravilha!",
    60 : "E aí?",
    70 : "Mas claro!",
    80 : "Bingo!",
    90 : "Você só pode estar brincando...",
    100 : "Parece legal.",
    110 : "Que loucura!",
    120 : "Caramba!",
    130 : "Que confusão!",
    140 : "Não se preocupe.",
    150 : "Grrrr!",
    160 : "Qual é a boa?",
    170 : "Ei, ei, ei!",
    180 : "Vejo você amanhã.",
    190 : "Até a próxima.",
    200 : "Tchau-tchau, pica-pau.",
    210 : "Até outra hora, galinha d'angola.",
    220 : "Vou precisar ir daqui a pouco.",
    230 : "Não conheço isso!",
    240 : "Você está fora daqui!",
    250 : "Ai, isso dói!",
    260 : "Peguei você!",
    270 : "Por favor!",
    280 : "Obrigadíssimo!",
    290 : "Você está ditando moda!",
    300 : "Dá licença!",
    310 : "Posso ajudar?",
    320 : "É o que eu estou falando!",
    330 : "Jabuti perde tempo querendo aprender lição de águia.",
    340 : "Macacos me mordam!",
    350 : "Isso é especial!",
    360 : "Vamos parar de fazer bagunça!",
    370 : "O gato comeu sua língua?",
    380 : "Agora é com você!",
    390 : "Feio que dói.",
    400 : "Preciso ver um Toon.",
    410 : "Não dei a mínima!",
    420 : "Não vai amarelar!",
    430 : "Você é uma isca fácil.",
    440 : "Sei lá!",
    450 : "Tudo a ver!",
    460 : "Gracinha!",
    470 : "Você que manda!",
    480 : "É isso aí, garoto!",
    490 : "Vem me pegar, se você conseguir!",
    500 : "Você precisa se recuperar antes.",
    510 : "Você precisa de mais Pontos de risadas.",
    520 : "Estou de volta em um minuto.",
    530 : "Estou com fome.",
    540 : "Isso mesmo!",
    550 : "Estou com sono.",
    560 : "Estou pronto!",
    570 : "Estou de aborrecido.",
    580 : "Amo isso!",
    590 : "Isso foi muito legal!",
    600 : "Pule!",
    610 : "Ganhou piadas?",
    620 : "O que houve?",
    630 : "Vai devagar.",
    640 : "Devagar e sempre.",
    650 : "Gol!",
    660 : "Pronto?",
    670 : "Tudo OK!",
    680 : "Vai!",
    690 : "Vamos por aqui!",
    700 : "Você ganhou!",
    710 : "Meu voto é sim.",
    720 : "Meu voto é não.",
    730 : "Me inclui nessa.",
    740 : "Me inclui fora dessa.",
    750 : "Fica aqui, eu volto.",
    760 : "Rapidinho!",
    770 : "Você viu aquilo?",
    780 : "O que foi isso?",
    790 : "Nojento!",
    800 : "Não ligo.",
    810 : "Justo o que eu precisava.",
    820 : "Vamos botar lenha na fogueira!",
    830 : "Por aqui, galera!",
    840 : "Que coisa é essa?",
    850 : "A sorte está lançada.",
    860 : "Eu ouvi isso!",
    870 : "Você está falando comigo?",
    880 : "Valeu, vou estar por aqui por uma semana.",
    890 : "Hmm.",
    900 : "Eu pego este.",
    910 : "Peguei!",
    920 : "É meu!",
    930 : "Toma pra você.",
    940 : "Afaste-se, pode ser perigoso.",
    950 : "Não esquenta!",
    960 : "Minha nossa!",
    970 : "Puxa!",
    980 : "Uuuuhuuu!",
    990 : "Todos a bordo!",
    1000 : "Caramba!",
    1010 : "A curiosidade matou o gato.",
    # Series 2
    2000 : "Tome juízo!",
    2010 : "Que bom ver você!",
    2020 : "Você que sabe.",
    2030 : "Está se saindo bem?",
    2040 : "Antes tarde do que nunca!",
    2050 : "Bravo!",
    2060 : "Mas, falando sério, pessoal...",
    2070 : "Está a fim de se juntar a nós?",
    2080 : "Te pego depois!",
    2090 : "Mudou de idéia?",
    2100 : "Vem pegar!",
    2110 : "Ai, meu Deus!",
    2120 : "Prazer em conhecer.",
    2130 : "Não faça nada que eu não faria!",
    2140 : "Nem pense nisso!",
    2150 : "Não abandone o barco!",
    2160 : "Não segura a respiração.",
    2170 : "Nem me fale.",
    2180 : "É fácil falar.",
    2190 : "Já chega!",
    2200 : "Excelente!",
    2210 : "Incrível encontrar você aqui!",
    2220 : "Dá um tempo.",
    2230 : "Gostei de saber.",
    2240 : "Vai em frente que eu quero ver!",
    2250 : "Vai em frente!",
    2260 : "Muito bom!",
    2270 : "Legal ver você!",
    2280 : "Tenho que me mandar.",
    2290 : "Tenho que ir embora.",
    2300 : "Agüenta firme.",
    2310 : "Espera um segundo.",
    2320 : "Curta bastante!",
    2330 : "Divirta-se!",
    2340 : "Não tenho o dia todo!",
    2350 : "Segura a onda!",
    2360 : "Viajou!",
    2370 : "Não acredito!",
    2380 : "Duvido.",
    2390 : "Devo essa a você.",
    2400 : "Estou lendo sua mente, você é claro como água.",
    2410 : "Eu acho isso.",
    2420 : "Acho que você devia passar.",
    2430 : "Quem dera ter dito isso.",
    2440 : "Se eu fosse você não faria isso.",
    2450 : "Seria ótimo!",
    2460 : "Estou ajudando meu amigo.",
    2470 : "Estou aqui a semana toda.",
    2480 : "Imagina só!",
    2490 : "Na hora H...",
    2500 : "O que tiver de ser, será.",
    2510 : "Só estou pensando alto.",
    2520 : "Mantenha o contato.",
    2530 : "Depois da tempestade vem o lamaçal!",
    2540 : "Rapidinho!",
    2550 : "Sinta-se em casa.",
    2560 : "Talvez outra hora.",
    2570 : "Posso me juntar a vocês?",
    2580 : "Que lugar legal, o seu.",
    2590 : "Foi ótimo falar com você.",
    2600 : "Sem dúvida.",
    2610 : "Sem brincadeira!",
    2620 : "Nem por um decreto.",
    2630 : "Tenha a santa paciência!",
    2640 : "Por mim tudo bem.",
    2650 : "Tá legal.",
    2660 : "Sorria!",
    2670 : "O que você disse?",
    2680 : "Tchaaaan!",
    2690 : "Calma aí.",
    2700 : "Até prá vocês!",
    2710 : "Quem desdenha quer comprar.",
    2720 : "Muito maneiro!",
    2730 : "Muito engraçado.",
    2740 : "O truque é esse!",
    2750 : "Está acontecendo uma invasão de Cogs!",
    2760 : "Vacilo.",
    2770 : "Cuidado!",
    2780 : "Bem feito!",
    2790 : "O que está acontecendo?",
    2800 : "O que está havendo?",
    2810 : "Para mim está certo.",
    2820 : "Certo, chefe.",
    2830 : "Pode apostar.",
    2840 : "Faça as contas.",
    2850 : "Por que está saindo tão cedo?",
    2860 : "Você me faz rir!",
    2870 : "Vai direto.",
    2880 : "Você está decaindo!",
    # Series 3
    3000 : "O que quiser.",
    3010 : "Você se importa se eu me juntar a vocês?",
    3020 : "Verifique, OK?",
    3030 : "Não esteja tão certo disso.",
    3040 : "Não liga se eu fizer isso.",
    3050 : "Não sacrifica!",
    3060 : "Você não conhece?",
    3070 : "Não liga para mim.",
    3080 : "Descobri!",
    3090 : "Imagine só!",
    3100 : "Pode esquecer!",
    3110 : "Está indo para o mesmo lugar que eu?",
    3120 : "Melhor para você!",
    3130 : "Que coisa.",
    3140 : "Aproveita!",
    3150 : "Fica de olho!",
    3160 : "E lá vamos nós de novo.",
    3170 : "Que tal essa!",
    3180 : "Que você acha?",
    3190 : "Eu acho que sim.",
    3200 : "Acho que não.",
    3210 : "Dou uma resposta mais tarde.",
    3220 : "Sou todo ouvidos.",
    3230 : "Agora não dá.",
    3240 : "Não estou brincando!",
    3250 : "Estou de queixo caído.",
    3260 : "Continue sorrindo.",
    3270 : "Depois me fala!",
    3280 : "Deixa a torta voar!",
    3290 : "Eu também tenho certeza.",
    3300 : "Pare de demorar!",
    3310 : "Caramba, o tempo voou.",
    3320 : "Sem comentários.",
    3330 : "Agora você está falando minha língua!",
    3340 : "Por mim tudo bem.",
    3350 : "Bom conhecer você.",
    3360 : "Tá legal.",
    3370 : "Com certeza.",
    3380 : "Valeu mesmo.",
    3390 : "É por aí.",
    3400 : "É isso!",
    3410 : "Hora de dormir.",
    3420 : "Confie em mim!",
    3430 : "Até a próxima.",
    3440 : "Espere acordado!",
    3450 : "Muito bem!",
    3460 : "O que traz você aqui?",
    3470 : "O que aconteceu?",
    3480 : "E agora?",
    3490 : "Você primeiro.",
    3500 : "Pegue a esquerda.",
    3510 : "Bem que você queria!",
    3520 : "Você está com problemas!",
    3530 : "Você é demais!",

    # Series 4
 4000 : "Os Tonns mandam na área!",
    4010 : "Besteirol de Cog!",
    4020 : "Toons de todo o mundo, uni-vos!",
    4030 : "E aí, parceiro!",
    4040 : "Muitíssimo obrigado.",
    4050 : "Vamos lá, novato.",
    4060 : "Tô indo pra caminha.",
    4070 : "Tô doido pra ir!",
    4080 : "Esta cidade é pequena demais para nós dois!",
    4090 : "Vá embora!",
    4100 : "Puxa!!!",
    4110 : "É ouro!",
    4120 : "Boa viagem!",
    4130 : "Tá na hora de sumir...",
    4140 : "Debandar!",
    4150 : "Ficou com a pulga atrás da orelha?",
    4160 : "Me poupe!",
    4170 : "Perfeito.",
    4180 : "Aposto.",
    4190 : "Pé na estrada!",
    4200 : "Então, adivinha!",
    4210 : "Tô de novo na ativa!",
    4220 : "Procure os suspeitos de sempre.",
    4230 : "Vamos agitar!",
    4240 : "O céu é o limite.",
    4250 : "Estou me preparando.",
    4260 : "Segura a onda!",
    4270 : "Não acerto uma.",
    4280 : "Voltem todos agora.",
    4290 : "É uma verdadeira lavada!",
    4300 : "Não vai amarelar.",
    4310 : "Tá se achando?",
    4320 : "Que bagunça é essa aqui?",
    4330 : "Vamos parar com esta preguiça!",
    4340 : "Só não vê quem não quer.",
    4350 : "É um colírio para os olhos!",
    4360 : "Nossas opções estão acabando.",
    4370 : "Tire esse peso das costas.",
    4380 : "Que paisagem maravilhosa!",
    4390 : "Você vai ver só!",
    # Series 6
    6000 : "Quero doce!",
    6010 : "Sou que nem formiga com doce.",
    6020 : "Foi feito no grito.",
    6030 : "Fácil como tirar doce de criança!",
    6040 : "Leve três e pague um.",
    6050 : "Eles vão sentir o gostinho!",
    6060 : "É a parte ruim da história.",
    6070 : "Você não pode assobiar e chupar cana.",
    6080 : "Tô me sentindo como uma criança em uma loja de doces.",
    6090 : "Seis deste, meia dúzia do outro...",
    6100 : "Rapadura é doce mas não é mole não.",
    6110 : "Tem que fritar o peixe de olho no gato.",
    6120 : "É sopa no mel.",
    6130 : "Mas temos que pisar em ovos.",
    6140 : "Vamos melar os trabalhos!",
    6150 : "Você é um coco duro de quebrar!",
    6160 : "É assim que o bolo desanda.",
    6170 : "Café com leite.",
    6180 : "Tá tentando adoçar a minha boca?",
    6190 : "Tem que tomar água pra ajudar a descer.",
    6200 : "Você é o que você come!",
    6210 : "É mamão com açúcar!",
    6220 : "Deixa de ser bananão!",
    6230 : "Azedinho doce.",
    6240 : "Molezinha!",
    6250 : "Olha o bicho-papão!",
    6260 : "Olha o sorvete aí, gente!",
    6270 : "Não vamos enfeitar o bolo não.",
    6280 : "Toc, toc, toc...",
    6290 : "Quem é?",
    # Series 7
    7000 : "Pára de macaquice!",
    7010 : "Entrou areia.",
    7020 : "Macaco de imitação.",
    7030 : "Eles te passaram a perna.",
    7040 : "Parece história pra boi dormir.",
    7050 : "Só tô de palhaçada contigo.",
    7060 : "Quem quer ser a bola da vez?",
    7070 : "É papagaio de pirata...",
    7080 : "Uma macacada só!",
    7090 : "Macacos me mordam!",
    7100 : "Cada macaco no seu galho.",
    7110 : "E a beca?",
    7120 : "Não ouço.",
    7130 : "Não vejo.",
    7140 : "Não falo.",
    7150 : "Cada um para um lado, macacada.",
    7160 : "Lá fora é uma selva.",
    7170 : "Você é o rei da selva!",
    7180 : "Tudo ótimo!",
    7190 : "Tô enlouquecendo!",
    7200 : "Vamos entrar no ritmo!",
    7210 : "Este lugar está muito cheio!",
    7220 : "Adeus, vida cruel.",
    7230 : "Acabei numa furada.",
    7230 : "Pé na tábua.",
    7240 : "Balinhas não crescem em árvores!",

    # Halloween
    10000 : "Este lugar é uma cidade-fantasma.",
    10001 : "Bonita roupa!",
    10002 : "Acho que este lugar é assombrado.",
    10003 : "Gostosuras ou travessuras!",
    10004 : "Buuuuu!",
    10005 : "Feliz Assombração!",
    10006 : "Feliz Dia das Bruxas!",
    10007 : "Está na hora de eu virar uma abóbora.",
    10008 : "Fantasmático!",
    10009 : "Sinistro!",
    10010 : "Isso é horripilante!",
    10011 : "Detesto aranhas!",
    10012 : "Você ouviu?",
    10013 : "Você não tem nem uma sombra de chance!",
    10014 : "Me assustou!",
    10015 : "Horrível!",
    10016 : "Bizarro!",
    10017 : "Isso foi muito estranho....",
    10018 : "Esqueletos no seu armário?",
    10019 : "Assustei você?",

    # Fall Festivus
    11000 : "Ah! Marmelada!",
    11001 : "Melhor desamarrar a cara!",
    11002 : "Brrr!",
    11003 : "Fica calmo!",
    11004 : "Vem pegar!",
    11005 : "Não dá uma de peru, para morrer de véspera.",
    11006 : "Glu-glu-glu!",
    11007 : "Boas Festas!",
    11008 : "Feliz Ano Novo!",
    11009 : "Um bom feriado para você!",
    11010 : "Feliz Dia do Peru!",
    11011 : "Ho! Ho! Ho!",
    11012 : "\"Noel\" problema.",
    11013 : "\"Noel\" surpresa nenhuma.",
    11014 : "Deixa bater o sino, pequenino!",
    11015 : "Raspa o tacho.",
    11016 : "Feliz Natal!",
    11017 : "Com \"nataleza\"!",
    11018 : "Até o Natal, tudo bem!",
    11019 : "Você vai se \"arrenapender\"!",

    # Valentines
    12000 : "Fica comigo!",
    12001 : "Vem ser meu amorzinho!",
    12002 : "Feliz Dia dos Namorados!",
    12003 : "Ahhh, que bonitinho.",
    12004 : "Estou apaixonado por você.",
    12005 : "Amor de pombinhos.",
    12006 : "Te amo!",
    12007 : "Quer ser meu amor?",
    12008 : "Você é uma graça.",
    12009 : "Você é doce como mel.",
    12010 : "Fofura.",
    12011 : "Você precisa de um abraço.",
    12012 : "Muito fofo!",
    12013 : "Que fofo!",
    12014 : "Batatinha quando nasce...",
    12015 : "Esparrama pelo chão...",
    12016 : "Que gracinha!",
    12050 : "EU AMO acabar com Cogs!",
    12051 : "Você é um estouro!",
    12052 : "Só tenho olhos para você!",
    12053 : "Você é mais doce do que uma bala!",
    12054 : "Eu ADORARIA ter você em minha Festa Dia dos namorados!",

    # St. Patricks Day
    13000 : "Tenho você no coração!",
    13001 : "Feliz Páscoa!",
    13002 : "Você não está vestindo marrom-chocolate!",
    13003 : "Sorte de iniciante marrom-chocolate.",
    13004 : "Estou chocolate de inveja.",
    13005 : "Seu sortudo!",
    13006 : "Você é o meu trevo de quatro folhas!",
    13007 : "Você é o meu talismã!",

    # Summer Estate Party phrases (seasonal catalog)
    14000 : "Vamos dar uma festa de verão na Propriedade!",
    14001 : "É hora da festa!",
    14002 : "O último a chegar ao lago é um Cog do padre!",
    14003 : "Hora de treinar Rabisco em Grupo!",
    14004 : "Hora de treinar Rabisco!",
    14005 : "Seu Rabisco é legal!",
    14006 : "Que truques seu Rabisco pode fazer?",
    14007 : "Hora do Pinball de Canhão!",
    14008 : "O Pinball de Canhão é demais!",
    14009 : "Sua Propriedade é demais!",
    14010 : "Seu Jardim é legal!",
    14011 : "Sua Propriedade é legal!",




    #Potential racing phrases for purchase

    }


# indices into cog phrase arrays
SCMenuCommonCogIndices = (20000, 20004)
SCMenuCustomCogIndices = {
    'bf' : (20005, 20014),
    'nc' : (20015, 20024),
    'ym' : (20025, 20035),
    'ms' : (20036, 20046),
    'bc' : (20047, 20057),
    'cc' : (20058, 20070),
    'nd' : (20071, 20080),
    'ac' : (20081, 20092),
    'tf' : (20093, 20103),
    'hh' : (20104, 20114),
    'le' : (20115, 20124),
    'bs' : (20125, 20135),
    'cr' : (20136, 20145),
    'tbc' : (20146, 20156),
    'ds' : (20157, 20164),
    'gh' : (20165, 20177),
    'pp' : (20178, 20187),
    'b' : (20188, 20199),
    'f' : (20200, 20210),
    'mm' : (20211, 20224),
    'tw' : (20225, 20235),
    'mb' : (20236, 20245),
    'm' : (20246, 20254),
    'mh' : (20255, 20266),
    'dt' : (20267, 20276),
    'p' : (20277, 20287),
    'tm' : (20288, 20298),
    'bw' : (20299, 20308),
    'ls' : (20309, 20319),
    'rb' : (20320, 20329),
    'sc' : (20330, 20340),
    'sd' : (20341, 20350),
    }


# Pirates Speedchat
PSCMenuGreetings = "CUMPRIMENTOS"
PSCMenuGoodbyes = "DESPEDIDAS"
PSCMenuFriendly = "AMIGÁVEL"
PSCMenuHappy = "FELIZ"
PSCMenuSad = "TRISTE"
PSCMenuSorry = "DESCULPA"
PSCMenuCombat = "COMBATE"
PSCMenuSeaCombat = "COMBATE NO MAR"
PSCMenuPlaces = "LUGARES"
PSCMenuLetsSail = "VAMOS\\NAVEGAR..."
PSCMenuLetsHeadTo = "VAMOS\\PARA..."
PSCMenuHeadToPortRoyal = "PORT ROYAL"
PSCMenuWhereIs = "ONDE ESTÁ ..?"
PSCMenuWhereIsPortRoyal = "PORT ROYAL"
PSCMenuWhereIsTortuga = "TORTUGA"
PSCMenuWhereIsPadresDelFuego = "PADRES DEL FUEGO"
PSCMenuWhereIsLasPulgas = "LAS PULGAS"
PSCMenuWhereIsLosPadres = "LOS PADRES"
PSCMenuDirections = "DIREÇÕES"
PSCMenuInsults = "INSULTOS"
PSCMenuCompliments = "ELOGIOS"
PSCMenuCardGames = "JOGOS DE CARTAS"
PSCMenuPoker = "PÔQUER"
PSCMenuBlackjack = "VINTE E UM"
PSCMenuMinigames = "MINIGAMES"
PSCMenuFishing = "FISHING"
PSCMenuCannonDefense = "CANNON DEFENSE"
PSCMenuPotions = "POTION BREWING"
PSCMenuRepair = "REPAIR"
PSCMenuInvitations = "CONVITES"
PSCMenuVersusPlayer = "VERSUS"
PSCMenuHunting = "PERSEGUIÇÃO"
PSCMenuQuests = "MISSÕES"
PSCMenuGM = "GM"



# Grandfathered Speedchat Headers
PSCMenuShips = "NAVIOS"
PSCMenuAdventures = "AVENTURA"


# Gateway Speedchat
GWSCMenuHello     = "CUMPRIMENTOS"
GWSCMenuBye       = "DESPEDIDAS"
GWSCMenuHappy     = "FELIZ"
GWSCMenuSad       = "TRISTE"
GWSCMenuPlaces     = "LUGARES"

# NamePanel.py - PickAName/TypeAName
RandomButton = "Aleatório"
TypeANameButton = "Digite um nome"
PickANameButton = "Escolha um nome"
NameShopSubmitButton = "Enviar"
RejectNameText = "Este nome não é permitido. Tente novamente."
WaitingForNameSubmission = "Enviando o seu nome..."

NameShopNameMaster = "NameMaster_portuguese.txt"
NameShopPay = "Assine já!"
NameShopPlay = "Avaliação gratuita"
NameShopOnlyPaid = "Somente usuários pagantes\npodem dar nomes aos seus Toons.\nAté que você se inscreva\nseu nome será\n"
NameShopContinueSubmission = "Continuar envio"
NameShopChooseAnother = "Escolha outro nome"
NameShopToonCouncil = "O Conselho de Toons\nanalisará o seu\nnome."+ \
                      "A análise pode\nlevar alguns dias.\nEnquanto você espera\nseu nome será\n"
PleaseTypeName = "Digite o seu nome:"
AllNewNames = "Todos os novos nomes\ndevem ser aprovados\npelo Conselho de Toons."
NameShopNameRejected = "O nome\nenviado foi\nrejeitado."
NameShopNameAccepted = "Parabéns!\nO nome\nenviado foi\naceito!"
NoPunctuation = "Não é permitido usar caracteres de pontuação nos nomes!"
PeriodOnlyAfterLetter = "Você pode usar um ponto no nome, mas apenas depois de uma letra."
ApostropheOnlyAfterLetter = "Você pode usar um apóstrofo no nome, mas apenas depois de uma letra."
NoNumbersInTheMiddle = "Dígitos numéricos podem não aparecer no meio da palavra."
ThreeWordsOrLess = "Seu nome deve ter três palavras ou menos."
CopyrightedNames = (
    "mickey",
    "mickey mouse",
    "mickeymouse",
    "minnie",
    "minnie mouse",
    "minniemouse",
    "donald",
    "donald duck",
    "donaldduck",
    "pluto",
    "pateta",
    )

# NameCheck.py
NCTooShort = 'Este nome é muito curto.'
NCNoDigits = 'O nome não pode conter números.'
NCNeedLetters = 'Cada palavra do nome deve conter algumas letras.'
NCNeedVowels = 'Cada palavra do nome deve conter algumas vogais.'
NCAllCaps = 'O seu nome não pode estar todo em maiúsculas.'
NCMixedCase = 'Este nome tem muitas letras em minúsculas.'
NCBadCharacter = "O seu nome não pode conter o caractere '%s'"
NCRepeatedChar = "Your name has too many of the character '%s'"
NCGeneric = 'Sinto muito, este nome não vai funcionar.'
NCTooManyWords = 'O seu nome não pode ter mais de quatro palavras.'
NCDashUsage = ("Hifens podem ser usados apenas para ligar duas palavras (como em 'Bu-Bu').")
NCCommaEdge = "O seu nome não pode começar ou terminar com vírgula."
NCCommaAfterWord = "Você não pode começar uma palavra com vírgula."
NCCommaUsage = ('Este nome não usa vírgulas corretamente. As vírgulas devemintercalar duas palavras, como no nome "Dr. Quack, MD".As vírgulas devem também ser seguidas por um espaço.')
NCPeriodUsage = ('Este nome não usa pontos corretamente. Os pontos são permitidos somente em palavras como "Sr.", "Sra.", "J.P." etc.')
NCApostrophes = 'Este nome tem muitos apóstrofos.'

# AvatarDetailPanel.py
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = "Fechar"
AvatarDetailPanelLookup = "Procurando detalhes de %s."
AvatarDetailPanelFailedLookup = "Não foi possível obter detalhes de %s."
AvatarDetailPanelPlayer = "Jogador: %(player)s\Mundo: %(world)s\nLocal: %(location)s"
AvatarDetailPanelOnline = "Região: %(district)s\nLocation: %(location)s"
AvatarDetailPanelOffline = "Região: off-line\nLocal: off-line"

# AvatarPanel.py
AvatarPanelFriends = "Amigos"
AvatarPanelWhisper = "Cochichar"
AvatarPanelSecrets = "Segredos"
AvatarPanelGoTo = "Ir para"
AvatarPanelIgnore = "Ignorar"
AvatarPanelStopIgnore = "Parar de Ignorar"
AvatarPanelEndIgnore = "Encerrar Ignorar"
AvatarPanelTrade = "Trocar"
#AvatarPanelCogDetail = "Dept: %s\nNível: %s\n"
AvatarPanelCogLevel = "Nível: %s"
AvatarPanelCogDetailClose = "Fechar"

# TeleportPanel.py
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Tentando ir para %s."
TeleportPanelNotAvailable = "%s está ocupado(a) agora; tente novamente mais tarde."
TeleportPanelIgnored = "%s está ignorando você."
TeleportPanelNotOnline = "%s não está on-line neste momento."
TeleportPanelWentAway = "%s saiu."
TeleportPanelUnknownHood = "Você não sabe ir para %s!"
TeleportPanelUnavailableHood = "%s não está disponível agora; tente novamente mais tarde."
TeleportPanelDenySelf = "Você não pode ir lá por conta própria!"
TeleportPanelOtherShard = "%(avName)s está na região %(shardName)s, e você está na região %(myShardName)s. Deseja ir para %(shardName)s?"

KartRacingMenuSections = [
 -1,
 "LUGARES",
 "CORRIDAS",
 "PISTAS",
 "ELOGIOS",
 "PROVOCAÇÕES"
]

AprilToonsMenuSections = [
 -1,
 "CUMPRIMENTOS",
 "PROPRIEDADE",
 "PERGUNTAS",
 "RESPOSTAS"
]

SillyHolidayMenuSections = [
 -1,
 "Mundo",
 "Batalha",
]

CarolMenuSections = [
 -1
]

VictoryPartiesMenuSections = [
 -1,
 "PARTY",
 "ITEMS",
]

GolfMenuSections = [
 -1,
 "PERCURSOS",
 "DICAS",
 "COMENTÁRIOS",
]

BoardingMenuSections = [
"GRUPO",
"Vamos para...",
"Estamos indo para...",
-1,
]

SellbotNerfMenuSections = [
 -1,
 'REUNINDO',
 'TORRES/VP Robô Vendedor',
]

LawbotNerfMenuSections = [
 -1,
 'REUNINDO',
 'COURTHOUSE/CJ',
]

JellybeanJamMenuSections = [
 'OBTER BALINHAS',
 'GASTAR BALINHAS',
# 'GRUPOS DE BALINHAS',
]

WinterMenuSections = [
 'CANÇÕES NATALINAS',
 -1,
]

HalloweenMenuSections = [
 -1
]

SingingMenuSections = [
 -1
]

WhiteListMenu = [
-1,
"LISTA DE PERMISSÕES"
]

SellbotInvasionMenuSections = [
 -1,
]

SellbotFieldOfficeMenuSections = [
 -1,
 'STRATEGY',
]

IdesOfMarchMenuSections = [
 -1,
]

# TTAccount.py
# Fill in %s with phone number from account server
TTAccountCallCustomerService = "Favor entrar em contato com o Atendimento ao Consumidor em %s."
# Fill in %s with phone number from account server
TTAccountCustomerServiceHelp = "\nSe precisar de ajuda, favor entrar em contato com o Atendimento ao Comsumidor em %s."
TTAccountIntractibleError = "Um erro ocorreu."


def timeElapsedString(timeDelta):
    timeDelta = abs(timeDelta)
    if timeDelta.days > 0:
        if timeDelta.days == 1:
            return "1 dia atrás"
        else:
            return "%s dias atrás" % timeDelta.days

    elif timeDelta.seconds / 3600 > 0:
        if timeDelta.seconds / 3600 == 1:
            return "1 hora atrás"
        else:
            return "%s horas atrás" % (timeDelta.seconds / 3600)

    else:
        if timeDelta.seconds / 60 < 2:
            return "1 minuto atrás"
        else:
            return "%s minutos atrás" % (timeDelta.seconds / 60)
