import string
from otp.otpbase.OTPLocalizer_castillian_Property import *

# common locations
lTheBrrrgh = 'Frescolandia'
lDaisyGardens = 'Jardines de Daisy'
lDonaldsDock = "Puerto de Donald"
lDonaldsDreamland = "Sueñolandia de Donald"
lMinniesMelodyland = "Melodilandia de Minnie"
lToontownCentral = 'Centro de Toontown'
lGoofySpeedway = "Estadio de Goofy"
lOutdoorZone = "Acres de bellota de Chip y Dale"
lGolfZone = "Minigolf de Chip y Dale"

# common strings
lCancel = 'Cancelar'
lClose = 'Cerrar'
lOK = 'OK'
lNext = 'Siguiente'
lNo = 'No'
lQuit = 'Salir'
lYes = 'Si'

TheCogs = "Los bots"
Cog  = "Bot"
Cogs = "Bots"

# OTPDialog.py
DialogOK = lOK
DialogCancel = lCancel
DialogYes = lYes
DialogNo = lNo

# DistributedAvatar.py
WhisperNoLongerFriend = "%s ha abandonado tu lista de amigos."
WhisperNowSpecialFriend = "¡%s es ahora tu amigo secreto!"
WhisperComingToVisit = "%s viene a verte."
WhisperFailedVisit = "%s ha intentado venir a verte."
WhisperTargetLeftVisit = "%s se ha ido a otro sitio. ¡Prueba de nuevo!"
WhisperGiveupVisit = "%s no ha podido encontrarte porque te estás moviendo."
WhisperIgnored = "¡%s no te está haciendo caso!"
TeleportGreeting = "Hola, %s."
WhisperFriendComingOnline = "¡%s se está conectando!"
WhisperFriendLoggedOut = "%s ha cerrado la sesión."

DialogSpecial = "ooo"
DialogExclamation = "!"
DialogQuestion = "?"

# ChatInputNormal.py
ChatInputNormalSayIt = "Decírselo"
ChatInputNormalCancel = lCancel
ChatInputNormalWhisper = "Susurrar"
ChatInputWhisperLabel = "A %s"

# ChatInputSpeedChat.py
SCEmoteNoAccessMsg = "Todavía no tienes acceso\n a este emoticono."
SCEmoteNoAccessOK = lOK

# ChatGarbler.py
ChatGarblerDefault = ["bla"]

# ChatManager.py
ChatManagerChat = "Charla"
ChatManagerWhisperTo = "Susurrar a:"
ChatManagerWhisperToName = "Susurrar a:\n%s"
ChatManagerCancel = lCancel
ChatManagerWhisperOffline = "%s está desconectado."
OpenChatWarning = '¡Todavía no tienes "amigos secretos"! No puedes conversar con otros dibus a menos que sean tus amigos secretos.\n\nPara convertirte en amigo secreto de alguien, haz clic en él y selecciona "Secretos" en el panel de detalles. No hace falta decir que siempre puedes hablar con quien quieras por medio de la Charla rápida.'
OpenChatWarningOK = lOK
UnpaidChatWarning = 'Cuando te hayas suscrito, podrás usar este botón para charlar con tus amigos mediante el teclado. Hasta entonces, deberías usar la herramienta Charla rápida para conversar con los demás dibus.'
UnpaidChatWarningPay = "¡Suscríbete ya!"
UnpaidChatWarningContinue = "Continuar prueba gratuita"
PaidNoParentPasswordWarning = 'Una vez creada la contraseña parental, podrás activar este botón para charlar con tus amigos mediante el teclado. Hasta entonces, puedes usar la herramienta Charla rápida para conversar con los demás dibus.'
PaidNoParentPasswordWarningSet = "Crear la contraseña parental ahora"
PaidNoParentPasswordWarningContinue = "Seguir jugando"
NoSecretChatWarningTitle = "Controles parentales"
NoSecretChatWarning = 'Para que sea posible charlar con un amigo, la herramienta Amigos secretos debe estar activada. Para saber más cosas sobre la herramienta Amigos secretos y acceder a los controles parentales, diles a tus padres que abran la sesión con su contraseña parental.'
NoSecretChatWarningOK = lOK
NoSecretChatWarningCancel = lCancel
NoSecretChatWarningWrongPassword = 'Esa contraseña no es correcta. Introduce la contraseña parental que se creó al adquirir esta cuenta. No se trata de la misma contraseña que se emplea para jugar al juego.'
NoSecretChatAtAllTitle = "Charla de Amigos secretos"
# not sure what this should do in the new world order
NoSecretChatAtAll = 'Para charlar con un amigo, la herramienta Amigos secretos debe estar activada. La herramienta Amigos secretos permite a un miembro charlar con otro gracias al uso de un código secreto que se debe comunicar fuera del juego.\n\nPara activar esta herramienta sal de Toontown y actívala a través de Los Controles Parentales en Conecta Disney'
# not sure what this should do in the new world order
NoSecretChatAtAllOK = lOK

from otp.otpbase.OTPModules import TextProperties
from otp.otpbase.OTPModules import TextPropertiesManager

shadow = TextProperties()
shadow.setShadow(-0.025, -0.025)
shadow.setShadowColor(0,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('shadow', shadow)

red = TextProperties()
red.setTextColor(1,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('red', red)

green = TextProperties()
green.setTextColor(0,1,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('green', green)

yellow = TextProperties()
yellow.setTextColor(1,1,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('yellow', yellow)

midgreen = TextProperties()
midgreen.setTextColor(0.2,1,0.2,1)
TextPropertiesManager.getGlobalPtr().setProperties('midgreen', midgreen)

blue = TextProperties()
blue.setTextColor(0,0,1,1)
TextPropertiesManager.getGlobalPtr().setProperties('blue', blue)

white = TextProperties()
white.setTextColor(1,1,1,1)
TextPropertiesManager.getGlobalPtr().setProperties('white', white)

black = TextProperties()
black.setTextColor(0,0,0,1)
TextPropertiesManager.getGlobalPtr().setProperties('black', black)

grey = TextProperties()
grey.setTextColor(0.5, 0.5, 0.5, 1)
TextPropertiesManager.getGlobalPtr().setProperties('grey', grey)

ActivateChat = """La herramienta Amigos secretos permite a los socios charlar entre sí gracias al uso de un código secreto que se debe comunicar fuera del juego. Para obtener toda la información, haz clic aquí:

La herramienta Amigos secretos no está moderada ni supervisada. Si los padres permiten a sus hijos usar su cuenta con la opción Amigos secretos activada, les aconsejamos que los supervisen mientras juegan. Una vez activada, la herramienta Amigos secretos está disponible hasta que se desactiva.

Al activar la herramienta Amigos secretos, los padres reconocen que existen ciertos riesgos inherentes a la posibilidad de charla de la herramienta y reconocen que han sido informados sobre dichos riesgos y están de acuerdo en aceptarlos."""

ActivateChatYes = "Activar"
ActivateChatNo = lCancel
ActivateChatMoreInfo = "Más información"
ActivateChatPrivacyPolicy = "Normas de confidencialidad"

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
La herramienta Amigos secretos

La herramienta Amigos secretos permite a los socios conversar directamente entre sí mediante en Disney's Toontown Online (en lo sucesivo, el "Servicio"). Para ello, los socios deben establecer una conexión de Amigos secretos. Cuando su hijo intente usar la herramienta Amigos secretos, le pediremos que introduzca su contraseña parental para confirmar su consentimiento al uso de dicha herramienta. A continuación se describe con detalle proceso de creación de una conexión de Amigos secretos entre dos socios imaginarios a los que llamaremos "Susana" y "Miguel".
1. Los padres de Susana y los de Miguel activan la herramienta Amigos secretos, introduciendo sus contraseñas parentales (a) en las Opciones de cuenta del Servicio o (b) cuando el juego se lo requiera en una ventana emergente de Control parental.
2. Susana solicita un Secreto (descrito más adelante) desde dentro del Servicio.
""","""
3. El Secreto de Susana se envía a Miguel fuera del Servicio. (Susana le puede comunicar su Secreto a Miguel directamente o indirectamente, a través de otra persona.)
4. Miguel envía el Secreto de Susana al Servicio en un plazo de 48 horas a partir del momento en que Susana lo ha solicitado.
5. El Servicio comunica a Miguel que Susana se ha convertido en su amiga secreta. De igual modo, el Servicio notifica a Susana que Miguel se ha convertido en su amigo secreto.
6. Ahora, Susana y Miguel pueden charlar entre sí hasta que uno de ellos decida que el otro deje de ser su amigo secreto o hasta que los padres de Susana o Miguel desactiven la herramienta Amigos secretos. Por tanto, la conexión Amigos secretos puede ser desactivada en cualquier momento por:
""","""
(a) Un socio que borre a otro de su lista de amigos secretos (de la forma
descrita en el Servicio) o (b) los padres de un socio que desactiven la herramienta Amigos secretos por medio de las Opciones de cuenta del Servicio (siguiendo los pasos allí establecidos).

Un Secreto es un código informático generado al azar y asignado a un socio en concreto. Es necesario usar el Secreto para activar la conexión de Amigos secretos dentro de un plazo de 48 horas a partir del momento de su solicitud. De lo contrario, el Secreto caduca y no se puede utilizar. Además, un secreto sólo se puede usar para establecer una sola conexión de Amigos Secretos. Para crear más conexiones de Amigos secretos, el socio debe solicitar un Secreto adicional para cada uno de los nuevos amigos.

Las amistades secretas no se transfieren. Por ejemplo, si Susana es amiga
""","""
secreta de Miguel y Miguel es amigo secreto de Ana, Susana no se convierte automáticamente en amiga secreta de Ana. Para que Susana y Ana se hagan
amigas secretas, una de ellas deberá solicitar un nuevo Secreto al Servicio y
comunicárselo a la otra.

Los amigos secretos se comunican entre sí mediante un servicio de conversación interactivo de formato libre. El contenido de esta conversación es escrito directamente por el socio participante y procesado a través del Servicio, que está gestionado por Walt Disney Internet Group ("WDIG"), 506 2nd Avenue, Suite 2100, Seattle, WA 98104, EE.UU. (teléfono +1 (509) 742-4698; correo electrónico: ms_support@help.go.com). Aunque aconsejamos a los socios que no intercambien datos personales, como sus nombres y apellidos, direcciones de correo electrónico, direcciones postales o números de teléfono mientras utilizan la herramienta Amigos secretos, no
""","""
podemos garantizar que tales intercambios de información personal no se produzcan. Aunque el servicio de conversación de Amigos secretos tiene un filtro automático de palabras malsonantes y obscenas, no está moderado ni  supervisado por nosotros. Si los padres permiten a sus hijos usar su cuenta con la opción Amigos secretos activada, les aconsejamos que los supervisen mientras juegan en el Servicio..

WDIG no hace uso del contenido de las conversaciones de Amigos secretos para ningún otro propósito que no sea el de comunicar dicho contenido al amigo secreto del socio, y no divulga ese contenido a terceros excepto en los siguientes casos: (1) Si la ley lo requiere, por ejemplo, para acatar una orden o citación judicial; (2) para hacer cumplir las Condiciones de uso aplicables al Servicio (a las que se puede acceder en la página principal del Servicio); (3) para proteger la seguridad de los socios del Servicio y del Servicio mismo.
""","""
Los padres de un niño pueden, previa petición a WDIG, revisar y borrar el contenido de cualquier conversación mantenida por ese niño, suponiendo que dicho contenido no haya sido ya borrado por WDIG de sus archivos. Según lo estipulado en la Ley estadounidense para la protección del menor en medios electrónicos (Children's Online Privacy Protection Act), no estamos autorizados a condicionar la participación de un niño en ninguna actividad (lo que incluye Amigos secretos) en base a la revelación por parte del niño de más información personal de la razonablemente necesaria para participar en tal actividad.

Además, tal y como se menciona anteriormente, reconocemos el derecho de los padres a negarse a permitir que el niño siga utilizando la herramienta Amigos secretos. Al activar la herramienta Amigos secretos, los padres reconocen que existen ciertos riesgos inherentes a la posibilidad de charlar de los socios por medio de dicha herramienta, y reconocen que han sido informados sobre dichos riesgos y están de acuerdo en aceptarlos.
"""
]

LeaveToPay = """Para adquirir Toontown, el producto irá a Toontown.com."""
LeaveToPayYes = "Adquirir"
LeaveToPayNo = lCancel

LeaveToSetParentPassword = """In order to set parent account password, the game will exit to the Toontown website."""
LeaveToSetParentPasswordYes = "Set Password"
LeaveToSetParentPasswordNo = lCancel

LeaveToEnableChatUK = """In order to enable chat, the game will exit to the Toontown website."""
LeaveToEnableChatUKNo = lCancel

ChatMoreInfoOK = lOK
SecretChatActivated = '¡La herramienta "Amigos secretos" ha sido activada!\n\nSi más tarde cambias de opinión y decides desactivar esta herramienta, haz clic en "Opciones de cuenta" en la página web de Toontown.'
SecretChatActivatedOK = lOK
ProblemActivatingChat = '¡Vaya! No hemos podido activar la herramienta de charla "Amigos secretos".\n\n%s\n\nVuelve a intentarlo más tarde.'
ProblemActivatingChatOK = lOK

# MultiPageTextFrame.py
MultiPageTextFrameNext = lNext
MultiPageTextFramePrev = 'Anterior'
MultiPageTextFramePage = 'Página %s/%s'

# GuiScreen.py
GuiScreenToontownUnavailable = "Toontown no parece estar disponible por el momento, seguimos intentándolo..."
GuiScreenCancel = lCancel


# CreateAccountScreen.py
CreateAccountScreenUserName = "Nombre de la cuenta"
CreateAccountScreenPassword = "Contraseña"
CreateAccountScreenConfirmPassword = "Confirmar contraseña"
CreateAccountScreenCancel = lCancel
CreateAccountScreenSubmit = "Siguiente"
CreateAccountScreenConnectionErrorSuffix = ".\n\nVuelve a intentarlo más tarde."
CreateAccountScreenNoAccountName = "Escribe un nombre de cuenta."
CreateAccountScreenAccountNameTooShort = "El nombre de cuenta debe tener al menos %s caracteres. Inténtalo de nuevo."
CreateAccountScreenPasswordTooShort = "La contraseña debe tener al menos %s caracteres. Inténtalo de nuevo."
CreateAccountScreenPasswordMismatch = "Las contraseñas que has escrito no coinciden. Inténtalo de nuevo."
CreateAccountScreenUserNameTaken = "Ese nombre de usuario ya existe. Inténtalo de nuevo."
CreateAccountScreenInvalidUserName = "Nombre de usuario no válido.\nInténtalo de nuevo."
CreateAccountScreenUserNameNotFound = "No se ha encontrado el nombre de usuario.\nInténtalo de nuevo o crea otra cuenta."

# ToontownClientRepository.py
CRConnecting = "Conectando..."
# host, port
CRNoConnectTryAgain = "Imposible conectar con %s:%s. ¿Quieres intentarlo de nuevo?"
CRNoConnectProxyNoPort = "Imposible conectar con %s:%s.\n\nTe estás conectando al Internet a través de un proxy que no permite las conexiones al puerto %s.\n\nPara jugar a Toontown es necesario abrir este puerto o desactivar el proxy. Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con él para que abra este puerto."
CRNoDistrictsTryAgain = "No hay distritos de Toontown disponibles. ¿Deseas intentarlo de nuevo?"
CRLostConnection = "Tu conexión de Internet a Toontown se ha interrumpido inesperadamente."
CRBootedReasons = {
    1: "Se ha producido un problema inesperado. Se ha perdido la conexión, pero deberías poder conectarte de nuevo y volver al juego.",
    100: "Has sido desconectado porque otra persona que ha abierto una sesión con tu cuenta en otro ordenador.",
    120: "Has sido desconectado debido a un problema con tu autorización para usar la charla mediante el teclado.",
    122: "Se ha producido un problema inesperado en la conexión con Toontown. Ponte en contacto con el Servicio de atención al cliente de Toontown.",
    125: "Tus archivos instalados de Toontown parecen ser incorrectos. Pulsa el botón Jugar de la página web oficial de Toontown para ejecutar el juego.",
    126: "No tienes privilegios de administrador.",
    127: "A problem has occurred with your Toon. Please contact Member Services via phone, email or live chat and reference Error Code 127. Thank you.",
    151: "Tu sesión ha sido cerrada por un administrador de los servidores de Toontown.",
    152: "There has been a reported violation of our Terms of Use connected to '%(name)s'. For more details, please review the message sent to the e-mail address associated with '%(name)s'.",
    153: "Se ha reiniciado el distrito de Toontown en el que te hallabas. Todos los que estaban en ese distrito han sido desconectados. Sin embargo, deberías poder conectarte de nuevo para volver al juego.",
    288: "Lo sentimos, pero has gastado todos los minutos de que disponías en Toontown este mes.",
    349: "Lo sentimos, pero has gastado todos los minutos de que disponías en Toontown este mes.",
    }
CRBootedReasonUnknownCode = "Ha surgido un problema inesperado (código de error %s). Se ha perdido la conexión, pero deberías poder conectarte de nuevo y volver al juego."
CRTryConnectAgain = "\n\n¿Quieres intentar conectarte de nuevo?"
# avName
CRToontownUnavailable = "Toontown no parece estar disponible por el momento; seguimos intentándolo..."
CRToontownUnavailableCancel = lCancel
CRNameCongratulations = "¡¡ENHORABUENA!!"
CRNameAccepted = "Tu nombre ha sido\naprobado por el Consejo Dibu.\n\nA partir de ahora,\nte llamarás\n\"%s\""
CRServerConstantsProxyNoPort = "Imposible ponerse en contacto con %s.\n\nTe estás conectando al Internet a través de un proxy que no permite conexiones al puerto %s.\n\nPara jugar a Toontown es necesario abrir este puerto o desactivar el proxy. Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con él para que abra este puerto."
CRServerConstantsProxyNoCONNECT = "Imposible ponerse en contacto con %s.\n\nTe estás conectando al Internet a través de un proxy que no es compatible con el método CONNECT.\n\nPara jugar a Toontown es necesario activar esta opción o desactivar el proxy. Si el proxy ha sido suministrado por tu proveedor de Internet, debes ponerte en contacto con él para activar esta opción."
CRServerConstantsTryAgain = "Imposible ponerse en contacto con %s.\n\nEl servidor de la cuenta de Toontown podría estar inoperativo en este momento, o puede ser que haya surgido un problema con tu conexión de Internet.\n\n¿Deseas intentarlo de nuevo?"
CRServerDateTryAgain = "Imposible obtener la fecha del servidor de %s. ¿Deseas intentarlo de nuevo?"
AfkForceAcknowledgeMessage = "A tu dibu le ha entrado sueño y se ha ido a la cama."
PeriodTimerWarning = "¡Tu límite de tiempo en Toontown este mes casi ha terminado!"
PeriodForceAcknowledgeMessage = "Has gastado todos los minutos de que disponías en Toontown este mes. ¡Ven otra vez a jugar el mes que viene!"
CREnteringToontown = "Entrando a Toontown..."

# DownloadWatcher.py
# phase, percent
DownloadWatcherUpdate = "Descargando %s."
DownloadWatcherInitializing = "Iniciando descarga..."

# LoginScreen.py
LoginScreenUserName = "Nombre de la cuenta"
LoginScreenPassword = "Contraseña"
LoginScreenLogin = "Inicio de sesión"
LoginScreenCreateAccount = "Crear cuenta"
LoginScreenQuit = lQuit
LoginScreenLoginPrompt = "Introduce un nombre de usuario y una contraseña."
LoginScreenBadPassword = "Contraseña incorrecta.\nInténtalo de nuevo."
LoginScreenInvalidUserName = "Nombre de usuario incorrecto.\nInténtalo de nuevo."
LoginScreenUserNameNotFound = "No se ha encontrado el nombre de usuario.\nInténtalo de nuevo o crea otra cuenta."
LoginScreenPeriodTimeExpired = "Lo sentimos, pero ya has gastado todos los minutos de que disponías en Toontown este mes. Vuelve a principios del mes que viene."
LoginScreenNoNewAccounts = "Lo sentimos mucho, pero no aceptamos nuevas cuentas en este momento."
LoginScreenTryAgain = "Inténtalo de nuevo"


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
GlobalSpeedChatName = "Charla rápida"

# Toontown Speedchat
SCMenuPromotion  = "PROMOTIONAL"
SCMenuElection  = "ELECTION"

SCMenuEmotions  = "EMOCIONES"
SCMenuCustom    = "MIS FRASES"

SCMenuResistance = "UNITE!"
SCMenuPets      = "MASCOTAS"
SCMenuPetTricks = "ACROBACIAS"

SCMenuCog       = "COG SPEAK"
SCMenuHello     = "HOLA"
SCMenuBye       = "ADIÓS"
SCMenuHappy     = "FELIZ"
SCMenuSad       = "TRISTE"
SCMenuFriendly  = "AMIGABLE"
SCMenuSorry     = "LO SIENTO"
SCMenuStinky    = "FÉTIDO"
SCMenuPlaces    = "LUGARES"
SCMenuToontasks = "DIBUTAREAS"
SCMenuBattle    = "COMBATE"
SCMenuGagShop   = "BROMAS"
SCMenuFactory   = "FABRICA"
SCMenuKartRacing   = "RACING"
SCMenuFactoryMeet = "ENCUENTRO"

SCMenuFactoryMeet = "MEET"
SCMenuCFOBattle = "DIRECTOR FINANCIERO"
SCMenuCFOBattleCranes = "CRANES"
SCMenuCFOBattleGoons = "GOONS"
SCMenuCJBattle = "JUEZ"
SCMenuCEOBattle = "DIRECTOR GENERAL"
SCMenuGolf   = "GOLF"
SCMenuWhiteList = "WHITELIST"
SCMenuPlacesPlayground           = "DIBUPARQUE"
SCMenuPlacesEstate               = "HACIENDA"
SCMenuPlacesCogs                 = "BOTS"
SCMenuPlacesWait                 = "WAIT"

SCMenuFriendlyYou = "Eres..."
SCMenuFriendlyILike = "me gusta..."
SCMenuPlacesLetsGo  = "Vamos a..."
SCMenuToontasksMyTasks = "Mis tareas"
SCMenuToontasksYouShouldChoose = "Creo que deberias escoger..."

SCMenuToontasksINeedMore         = "I need more..."
SCMenuBattleGags                 = "BROMAS"
SCMenuBattleTaunts               = "TAUNTS"
SCMenuBattleStrategy             = "ESTRATEGIA"
SCMenuBoardingGroup              = "EMBARQUE"
SCMenuParties                    = "FIESTAS"
SCMenuAprilToons                 = "APRIL TOONS'"
SCMenuSingingGroup               = "SINGING"
SCMenuSillyHoliday                   = "SILLY METER"
SCMenuVictoryParties             = "VICTORY PARTIES"
SCMenuSellbotNerf                = "STORM SELLBOT"
SCMenuJellybeanJam               = "JELLYBEAN WEEK"
SCMenuHalloween                  = "HALLOWEEN"
SCMenuWinter                     = "INVIERNO"
SCMenuSellbotInvasion            = "SELLBOT INVASION"
SCMenuFieldOffice                = "FIELD OFFICES"
SCMenuIdesOfMarch                = "VERDE"
SCMenuLawbotNerf                 = "LAWBOTS LOSE"

# FriendSecret.py
FriendSecretNeedsPasswordWarningTitle = "Parental Controls"
FriendSecretNeedsParentLoginWarning = """To get or enter a True Friend Code, log in with the Parent Account. You can disable this prompt by changing your True Friend options."""
FriendSecretNeedsPasswordWarning = """To get or enter a True Friend Code, you must enter the Parent Account Password. You can disable this prompt by changing your True Friends options."""
FriendSecretNeedsPasswordWarningOK = lOK
FriendSecretNeedsPasswordWarningCancel = lCancel
FriendSecretNeedsPasswordWarningWrongUsername = """That's not the correct username. Please enter the username of the parental account. This is not the same username used to play the game."""
FriendSecretNeedsPasswordWarningWrongPassword = """That's not the correct password. Please enter the password of the parental account. This is not the same password used to play the game."""
FriendSecretIntro = "Si estás jugando a Disney's Toontown Online con alguien que conozcas en la vida real, los dos pueden convertirse en amigos secretos. Puedes charlar con tus amigos secretos usando el teclado. Los demás dibus no entenderán lo que estás diciendo.\n\nPara hacer esto, necesitas obtener un Secreto. Transmítele el Secreto a tu amigo y a nadie más. Cuando tu amigo escriba el Secreto en su pantalla, los dos seran amigos secretos en Toontown."
FriendSecretGetSecret = "Obtener Secreto"
FriendSecretEnterSecret = "Si tienes un Secreto de alguien que conozcas, escríbelo aquí."
FriendSecretOK = lOK
FriendSecretCancel = lCancel
FriendSecretGettingSecret = "Obteniendo Secreto. . ."
FriendSecretGotSecret = "Aquí tienes tu nuevo Secreto. ¡No te olvides de anotarlo!\n\nPuedes dar este Secreto solamente a una persona. Cuando alguien escriba tu Secreto, éste no valdrá ya para nadie más. Si deseas dar un Secreto a alguien más, tienes que pedir otro.\n\nEl Secreto sólo valdrá durante los dos días siguientes. Tu amigo tendrá que escribirlo antes de que desaparezca, o de lo contrario el proceso no funcionará.\n\nTu Secreto es:"
FriendSecretTooMany = "Lo siento, no puedes tener más Secretos hoy. ¡Ya has tenido más que suficientes!\n\nPrueba de nuevo mañana."
FriendSecretTryingSecret = "Probando Secreto. . ."
FriendSecretEnteredSecretSuccess = "¡Ya eres amigo secreto de %s!"
FriendSecretEnteredSecretUnknown = "Ése no es el Secreto de nadie. ¿Seguro que lo has escrito bien?\n\nSi lo has escrito correctamente, tal vez haya caducado. Pídele a tu amigo que te obtenga un Secreto nuevo (o consigue tú uno y dáselo a tu amigo)."
FriendSecretEnteredSecretFull = "No puedes ser amigo de %s porque uno de los dos tiene demasiados amigos en la lista."
FriendSecretEnteredSecretFullNoName = "No pueden ser amigos porque uno de los dos tiene demasiados amigos en la lista."
FriendSecretEnteredSecretSelf = "¡Acabas de escribir tu propio Secreto! Ahora, nadie más puede usar ese Secreto."
FriendSecretNowFriends = "¡Ya eres amigo secreto de %s!"
FriendSecretNowFriendsNoName = "¡Ya sois amigos secretos!"

# FriendInvitee.py
FriendInviteeTooManyFriends = "%s desea ser tu amigo, pero ya tienes demasiados amigos en tu lista."
FriendInviteeInvitation = "A %s le gustaría ser tu amigo."
FriendInviteeOK = lOK
FriendInviteeNo = lNo

# FriendInviter.py
FriendInviterOK = lOK
FriendInviterCancel = lCancel
FriendInviterStopBeingFriends = "Dejar de ser amigo"
FriendInviterYes = lYes
FriendInviterNo = lNo
FriendInviterClickToon = "Haz clic en el dibu del que deseas ser amigo."
FriendInviterTooMany = "No puedes añadir más amigos a tu lista porque ya tienes demasiados. Si quieres ser amigo de %s, tendrás que quitar algunos amigos de tu lista."
FriendInviterNotYet = "¿Quieres ser amigo de %s?"
FriendInviterCheckAvailability = "Comprobando si %s está disponible."
FriendInviterNotAvailable = "%s está ocupado ahora mismo. Inténtalo más tarde."
FriendInviterWentAway = "%s se ha marchado."
FriendInviterAlready = "%s ya es tu amigo."
FriendInviterAskingCog = "Preguntando a %s si quiere ser tu amigo."
FriendInviterEndFriendship = "¿Seguro que quieres dejar de ser amigo de %s?"
FriendInviterFriendsNoMore = "%s ya no es tu amigo."
FriendInviterSelf = "¡ Ya eres tu propio amigo!"
FriendInviterIgnored = "%s no te está haciendo caso."
FriendInviterAsking = "Preguntando a %s si quiere ser tu amigo."
FriendInviterFriendSaidYes = "¡%s ha dicho que sí!"
FriendInviterFriendSaidNo = "%s ha dicho que no, gracias."
FriendInviterFriendSaidNoNewFriends = "%s no quiere tener amigos nuevos ahora mismo."
FriendInviterOtherTooMany = "¡%s ya tiene demasiados amigos!"
FriendInviterMaybe = "%s no ha podido responder."
FriendInviterDown = "Imposible hacer amigos ahora."

#Talk Path Labels
TalkGuild = "G"
TalkParty = "P"
TalkPVP = "PVP"

#Spam Blocked Message
AntiSpamInChat = "***Spamming***"

#IgnoreConfirm.py
IgnoreConfirmOK = lOK
IgnoreConfirmCancel = lCancel
IgnoreConfirmYes = lYes
IgnoreConfirmNo = lNo
IgnoreConfirmNotYet = "Would you like to Ignore %s?"
IgnoreConfirmAlready = "You are already ignoring %s."
IgnoreConfirmSelf = "You cannot ignore yourself!"
IgnoreConfirmNewIgnore = "You are ignoring %s."
IgnoreConfirmEndIgnore = "You are no longer ignoring %s."
IgnoreConfirmRemoveIgnore = "Stop ignoring %s?"

# Emote.py
# List of emotes in the order they should appear in the SpeedChat.
# Must be in the same order as the function list (EmoteFunc) in Emote.py
EmoteList = [
    "Wave",
    "Happy",
    "Sad",
    "Angry",
    "Sleepy",
    "Shrug",
    "Dance",
    "Think",
    "Bored",
    "Applause",
    "Cringe",
    "Confused",
    "Belly Flop",
    "Bow",
    "Banana Peel",
    "Resistance Salute",
    "Laugh",
    lYes,
    lNo,
    lOK,
    "Surprise",
    "Cry",
    "Delighted",
    "Furious",
    "Laugh",
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
    "%s waves.",
    "%s is happy.",
    "%s is sad.",
    "%s is angry.",
    "%s is sleepy.",
    "%s shrugs.",
    "%s dances.",
    "%s thinks.",
    "%s is bored.",
    "%s applauds.",
    "%s cringes.",
    "%s is confused.",
    "%s does a belly flop.",
    "%s bows to you.",
    "%s slips on a banana peel.",
    "%s gives the resistance salute.",
    "%s laughs.",
    "%s says '"+lYes+"'.",
    "%s says '"+lNo+"'.",
    "%s says '"+lOK+"'.",
    "%s is surprised.",
    "%s is crying.",
    "%s is delighted.",
    "%s is furious.",
    "%s is laughing.",
    "is singing note G1"
    ]

# Reverse lookup:  get the index from the name.
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
    lYes    : 17,
    lNo     : 18,
    lOK     : 19,
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
    'f':  ["Llego tarde a una reunión",
           ],
    'p':  ["Lárgate",
           ],
    'ym': ['Al sonriente no le hace gracia',
           ],
    None: ["Es mi día libre",
           "Creo que te has equivocado de despacho",
           "Que tu secretaria llame a la mía",
           "No tengo tiempo para reunirme contigo",
           "Habla con mi ayudante"]
    }

SuitFaceoffTaunts = {
    'b':  ["¿Me haces una donación?",
           "Te voy a dejar hecho unos zorros.",
           "Te voy a dejar más seco que la mojama.",
           "Hay que ser \"RH positivo\" ante la vida.",
           "Oh, no seas tan \"RH negativo\".",
           "Me sorprende que me hayas encontrado, soy muy escurridizo.",
           "Voy a tener que hacerte una transfusión rápida.",
           "Pronto vas a tener que tomarte un bocadillo y un zumito.",
           "Cuando acabe contigo no vas a poder ni levantarte.",
           "No mires, sólo te pinchará un poquito.",
           "Vas a marearte un poquito.",
           "Justo a tiempo, estaba un poco sediento.",
           ],
    'm':  ["No sabes con quién estás confraternizando.",
           "¿Has confraternizado alguna vez con gente como yo?",
           "Estupendo, confraternicemos pues.",
           "¡Me encanta confraternizar!",
           "Parece un buen sitio para confraternizar.",
           "Qué situación más tierna, ¿no?",
           "Vas a confraternizar con la derrota.",
           "Voy a hacer que confraternices con el suelo.",
           "¿Seguro que quieres confraternizar conmigo?",
           ],
    'ms': ["Prepárate; soy muy mandón.",
           "Más te valdría quitarte de en medio.",
           "Te mando que te largues.",
           "Creo que me toca mandar.",
           "Vas a ver adónde te mando.",
           "Cuando mando, los demás tiemblan.",
           "Hoy me he levantado de lo más mandón.",
           "Cuidado, dibu, te va a caer encima un mandoble.",
           "Te voy a mandar bien lejos.",
           "El corazón me manda que te zurre.",
           "¿Necesitas que te manden un poco?",
           ],
    'hh': ["Te saco una cabeza.",
           "Vas de cráneo, me parece.",
           "Creo que has perdido la cabeza.",
           "Estupendo. Tenía ganas de coleccionar tu cocorota.",
           "Te vas a quedar sin cabeza por esto.",
           "¡Cabeza al frente!",
           "Me parece que la cabeza te ha jugado una mala pasada.",
           "Qué poca cabeza estás teniendo.",
           "Un trofeo perfecto para mi colección.",
           "Vas a tener un buen dolor de cabeza.",
           "¡Cuidado, no pierdas la cabeza!",
           ],
    'tbc': ["Te voy a pescar con las manos.",
            "Puedes llamarme Cachalote.",
            "Ten cuidado. A veces soy como un tiburón blanco.",
            "Por fin, ya pensaba que me estabas dando sedal.",
            "Voy a cocinarte a la sal.",
            "¿Qué tal me sienta el escabeche?",
            "Ven aquí, voy a quitarte las escamas.",
            "Te va a pasar igual que a Jonás.",
            "Cuidadito, te he preparado un buen cebo.",
            "¿Te gusta que te preparen al pil-pil?",
            "¡Te voy a dar un buen pez-cozón!",
            ],
    'cr': ["¡DESPEDIDO!",
           "No encajas en mi colectivo.",
           "Vas a ser expulsado de la hermandad.",
           "No pareces defender los intereses comunes.",
           "Ese atuendo no es propio de tu colectivo.",
           "Te gusta sacar los pies del tiesto, ¿eh?",
           "Te voy a expulsar del colegio profesional.",
           "Un esquirol, ¿eh? ¡Vas a ver!",
           "No defiendes bien las ideas del colectivo.",
           "Relájate; esto es por el bien del colectivo.",
           ],
    'mh': ["¿Estás listo para mi escena?",
           "¡Luces, cámaras, acción!",
           "¡Estamos rodando!",
           "¡Hoy te toca desempeñar el papel del dibu derrotado!",
           "Por esta escena me van a dar el Oscar.",
           "Acabo de encontrar la inspiración para esta escena.",
           "¿Estás listo para tu escena final?",
           "No vas a aparecer ni en los créditos finales.",
           "No pienso firmarte ni un autógrafo.",
           "Voy a rodar contigo una escena de terror.",
           "¡Me encanta zurrar a los extras como tú!",
           "Espero que no olvides tu parte del guión.",
           ],
    'nc': ["Parece que tu balance no cuadra.",
           "Creo que tienes un déficit enorme.",
           "Déjame que equilibre tus cuentas.",
           "¡Estás en números rojos!",
           "¡Vas a tener que contabilizar tu factura del hospital!",
           "¿En qué columna te pongo? ¿Debe o haber?",
           "Eres un cero a la izquierda.",
           "Tu presupuesto está muy desequilibrado.",
           "Cuando acabe contigo no vas a saber ni contar.",
           "Voy a contar las veces que te machaco.",
           ],
    'ls': ["Es la hora de que pagues tu préstamo.",
           "Te he prestado demasiado tiempo.",
           "Es el momento del vencimiento.",
           "Venga, vamos a saldar cuentas.",
           "Pediste un anticipo y te lo voy a dar.",
           "Vas a pagar por esto.",
           "Llegó el día del ajuste de cuentas.",
           "¿Me prestas una oreja?",
           "Me alegro de que estés aquí; quiero lo que es mío.",
           "Voy a prestarte una paliza.",
           "Te voy a ofrecer un interés especial.",
           ],
    'mb': ["Es la hora de recoger la calderilla.",
           "Eres dinero suelto para mí.",
           "¿En efectivo o con tarjeta?",
           "¿Tienes el recibo?",
           "Recuerda que el dinero no da la felicidad.",
           "Me parece que andas escaso de fondos.",
           "Vas a tener un pequeño problema de efectivo.",
           "Después de esto, te veo pidiendo calderilla.",
           "Soy demasiado rico para mancharme las manos contigo.",
           "¡No hay dinero suficiente para satisfacerme!",
           ],
    'rb': ["Te han robado.",
           "Te voy a robar la victoria.",
           "¡Soy un barón del incordio!",
           "Soy la nobleza avasalladora.",
           "Vas a tener que denunciar este robo.",
           "Tengo la sangre azul... Veamos la tuya.",
           "Soy un rival noble.",
           "Te voy a dejar pelado.",
           "Supongo que esto es un robo a mano desarmada.",
           "¿No sabías que no se debe hablar con desconocidos?",
           ],
    'bs': ["Nunca me des la espalda.",
           "Te voy a dar un buen espaldarazo.",
           "Vas de espaldas por la vida.",
           "Se me da bien cortar el lomo.",
           "¿Te hago la acupuntura en la espalda?",
           "¡De espaldas contra la pared!",
           "¿Quieres que te haga cosquillas en la espalda?",
           "Me encanta jugar con las espalderas.",
           "Deja que te rasque la espalda.",
           "¡Date la vuelta, alguien viene!",
           "¡Mira, a tu espalda!",
           ],
    'bw': ["¿Quieres que te pase el cepillo?",
           "Sólo de verte se me riza el pelo.",
           "Si quieres hacemos esto permanente.",
           "Creo que vas a tener las puntas un poco abiertas.",
           "Creo que estás un poco bisoño.",
           "Te voy a teñir todo el cuerpo de morado.",
           "Has venido justo a tiempo para que te dé un buen repaso.",
           "Se te va a caer el pelo.",
           "Sólo de verte me salen entradas.",
           "Se te va a poner el pelo blanco.",
           ],
    'le': ["Creo que no tienes defensa posible. ",
           "Estoy picado contigo.",
           "Va a caer todo el peso de la ley encima de ti.",
           "Deberías saber que, cuando llevo la toga, soy implacable.",
           "Lo tuyo es un caso perdido de antemano.",
           "Creo que te va a caer cadena perpetua.",
           "Esto es tan divertido que debería ser ilegal.",
           "Lo siento; te tendrás que defender a ti mismo.",
           "Mis honorarios son bastante altos. ¿Podrás permitírtelos?",
           "Te voy a hacer trizas en el estrado.",
           ],
    'sd': ["Voy a anunciar tu fin.",
           "Deja que proclame tu derrota.",
           "El portavoz va anunciar tu desaparición.",
           "El mundo entero va a saber lo acabado que estás.",
           "Te vendría bien alguien que hablase por ti.",
           "¡Uy! ¡Al verte se me corta la voz!",
           "Deja que me aclare la voz un momento.",
           "Cuando acabe contigo no vas a tener voz ni voto.",
           "Podría anunciar mi victoria antes de tiempo.",
           "Damas y caballeros, este dibu es penoso.",
           ],
    'f': ["¡Me voy a chivar al jefe de ti!",
          "¡Soy un secuaz, pero soy muy pertinaz!",
          "Gracias a ti voy a conseguir un ascenso.",
          "No creo que te guste mi forma de trabajar.",
          "El jefe cuenta conmigo para ponerte fin.",
          "Vas a hacer que gane puntos ante el jefe.",
          "Primero tendrás que vértelas conmigo.",
          "Veamos qué te parece mi trabajo.",
          "Se me da de miedo deshacerme de los dibus.",
          "Nunca llegarás a ver a mi jefe.",
          "Te voy a enviar de vuelta al dibuparque.",
          ],
    'p':  ["¡Voy a borrarte de un plumazo!",
           "¡Chúpate ésta, pelele!",
           "¡Voy a cargar las tintas!",
           "Esto está adquiriendo tintes dramáticos...",
           "Deja que te aplique un poco de secante.",
           "Te voy a archivar para siempre.",
           "Deprisa, tengo que fichar pronto.",
           "Habré acabado contigo antes de que la tinta se seque.",
           "¡Nuestro encuentro hará correr ríos de tinta!",
           "Creo que tienes la tinta un poco seca, déjame que te vea.",
           "¡Cuidado, que mancho!",
           ],
    'ym': ["Lástima que esto no te vaya a gustar.",
           "Odio que la gente esté seria.",
           "Sonríe, la vida es bella... Aunque no para ti. Una sonrisa vale por cien dibus.",
           "Necesitas algo de alegría en tu vida.",
           "Después de esto se te va a quedar sonrisa de tonto.",
           "Mi sonrisa desarma a cualquiera.",
           "Al verte, he sonreído más todavía.",
           "¿Te gusta mi sonrisa? ¡Vas a recordarla mucho tiempo!",
           "Te veo y sonrío para mis adentros.",
           "¿Una sonrisita antes de que acabe contigo?",
           "No sonríes nada... No me extraña.",
           ],
    'mm': ["¡Voy tomar el control de tus negocios!",
           "Las grandes palizas vienen a veces en frasco pequeño.",
           "Ningún reto que queda grande.",
           "Cuando quiero que algo salga bien, lo hago yo mismo.",
           "Necesitas a alguien que te gestione bien.",
           "¡Qué bien, un proyecto!",
           "Te voy a gestionar una buena lección.",
           "Hay que reorganizarte la agenda del día.",
           "Voy a gestionar tu presencia aquí.",
           "Estoy vigilando todos tus movimientos.",
           "¿Seguro que te atreves?",
           "Haremos esto a mi manera.",
           "No te pienso quitar el ojo de encima.",
           "Vas a ver lo que es acoso laboral.",
           ],
    'ds': ["¡Vas a irte a la calle!",
           "Tu puesto de trabajo peligra.",
           "Creo que tu perfil no se ajusta a mis necesidades.",
           "Ya no nos eres de utilidad.",
           "Yo que tú empezaba a pedir entrevistas.",
           "Tendré que hacer algunos ajustes de plantilla.",
           "Tienes poco futuro en mi empresa.",
           "Voy a tener que hacer algunos recortes.",
           ],
    'cc': ["Hola, ¿llevas algo suelto?",
           "Te devolveré lo que te debo mañana sin falta.",
           "¿Me dejas que llame desde tu móvil?",
           "¿Me invitas a comer? Me dejado la cartera en casa.",
           "¿Qué tienes hoy de comida?",
           "Me gusta tu ropa; creo que me la voy a quedar.",
           "Hoy vas a prestarme dinerito, ¿verdad?",
           "No te preocupes; siempre lo devuelvo todo.",
           "Creo que me voy a quedar una semanita en tu casa.",
           "Creo que voy a hacer unos recados en tu coche.",
           "Seguro que tus zapatos me quedan bien.",
           "Me encanta como cocinas; ¡voy a aficionarme a tu casa!",
           "He puesto mi línea telefónica a tu nombre.",
           ],
    'tm': ["Nunca he visto un producto peor que tú.",
           "Con mi superquitamanchas salen borrones como tú.",
           "Te voy a aplastar con mi megabdominator.",
           "Si acabo contigo, me regalo un cuchillo de cocina.",
           "Tu final está disponible con una llamada. ¡Date prisa! ¡Tu fin está al caer!",
           "Acabe con los dibus molestos con \"zurradibu\".",
           "¡Te voy a poner los superéxitos de los bots!",
           "¿Cansado de tu figura? ¡Yo tengo la solución!",
           "¿No sabes qué hacer con tu pelo? ¡Llámame!",
           "Acepto tarjetas de crédito.",
           "Cuando acabe contigo, no habrás probado nada igual.",
           ],
    'nd': ["Seguro que mi coche corre más que el tuyo. ",
           "Supongo que sabrás que tengo mucho más dinero que tú.",
           "Contigo no tengo ni para empezar.",
           "Venga, deprisa, que tengo que comer con el Sr. Hollywood.",
           "¿Te había dicho que conozco al pez gordo?",
           "Soy íntimo amigo del mandamás.",
           "Conozco a gente que sabría encargarse de ti.",
           "¿Sabes con quién estás hablando?",
           "Acabaré rápidamente contigo; he quedado con gente importante.",
           "Lo siento; no me suelo codear con dibus como tú.",
           ],
    'gh': ["¡Hombre, un dibu! ¡Qué alegría machacarte!",
           "¡Qué bien! ¡Un dibu al que zurrar!",
           "¡Me lo voy a pasar de lo lindo contigo!",
           "¡Yupiii! ¡Tenía ganas de vérmelas con un dibu!",
           "¡Vas a ver lo que es bueno!",
           "¡Cómo me alegro de no volver a verte!",
           "Encantado de conocer... ¡tu fin!",
           "¡Cuánto tiempo sin verte! ¡Y cuánto más va a pasar!",
           "¡He estado años esperando este momento!",
           "¡Me siento feliz de poder zurrarte!",
           "¡Hurra! ¡Un dibu tiernecito!",
           "¡Hoooola! ¿Cómo quieres que acabe contigo?",
           "¡Un dibu! ¡Déjame que te estreche bien la mano!",
           ],
    'sc': ["¡Voy a hacerte calderilla!",
           "Vas a tener un pequeño problema de efectivo.",
           "No acepto tus divisas.",
           "No tengo cambio para ti.",
           "Cuando acabe contigo, no vas a valer ni un céntimo.",
           "Creo que la inflación te va a venir muy mal.",
           "Te voy a depreciar en breve.",
           "Mmm, creo que no llevo dibus sueltos.",
           "Cuando acabe contigo no te va a quedar ni un céntimo.",
           "¿Llevas calderilla para tu vuelta al dibuparque?",
           "No acepto propinas de un dibu.",
           ],
    'pp': ["Espera, te voy a aligerar de peso. ",
           "¿No notas que te falta algo?",
           "Yo que tú guardaría bien la cartera.",
           "¿Te has acordado de cerrar con llave tu casa?",
           "Me encanta tu reloj; creo que me lo voy a quedar.",
           "Vas a volver al dibuparque pelado de gominolas.",
           "Lo siento; tengo que requisarte unas cosillas.",
           "¿Me dejas ver qué llevas en los bolsillos?",
           "¿Algo que declarar?",
           "¡Otro dibu al que desplumar!",
           ],
    'tw': ["No esperes que dé ni los buenos días.",
           "Para ti soy el Sr. Roñoso.",
           "Voy a cortarte los fondos.",
           "¿Es ésa la mejor oferta que tienes?",
           "Venga, deprisa. El tiempo es oro.",
           "¡Soy de la hermandad del puño cerrado!",
           "Creo que tu oferta no me convence.",
           "Vas a tener que ofrecer mucho más, me temo.",
           "A ver si puedes permitirte esto.",
           "No te pienso dar ni una oportunidad.",
           "Voy a pegarles un buen bocado a tus fondos.",
           ],
    'bc': ["Me encanta contar cuentos a los dibus.",
           "Cuenta conmigo para pasarlo mal.",
           "Cuenta con que te voy a zurrar bien.",
           "¿Te cuento un cuento de miedo?",
           "Aquí el que cuenta soy yo.",
           "Cuenta con volver al dibuparque.",
           "Después de esto, no lo vas a contar.",
           "Este cuento va a acabar mal para ti.",
           "No tengas cuento...",
           "Cuando acabe contigo, no te van a salir las cuentas.",
           "Tenía unas cuantas cuentas pendientes contigo...",
           ],
    'bf': ["Todos me dicen que tengo mucho morro.",
           "Siempre le hecho morro a la vida.",
           "Hay que tener morro para venir aquí.",
           "Tienes bastante morro, ¿no crees?",
           "Justo a tiempo, te voy a hinchar los morros.",
           "Tengo un morro que me lo piso.",
           "Para ganarme le vas a tener que echar mucho morro.",
           "Tu morro no está a la altura de las circunstancias.",
           "Te voy a mandar al dibuparque de un morrazo.",
           "Vas a ver mis morros por última vez.",
           ],
    'tf': ["¡Por fin nos vemos las caras!",
           "¡Vas a tener que encarar la derrota!",
           "¿A que no sabes hacia dónde estoy mirando?",
           "Como tengo dos caras, es difícil que me las rompan.",
           "Dos caras son mejor que una.",
           "¿Cuál de mis dos caras te gusta más?",
           "Creo que te llaman en el dibuparque.",
           "¿Qué cara quieres que se encargue de ti?",
           "Tengo bastante más cara que tú.",
           "No sabes la cara que tengo...",
           "Lo mire por donde lo mire, siempre te veo...",
           ],
    'dt': ["Ha llegado el momento de embaucar a alguien.",
           "Oye, hay un elefante detrás de ti.",
           "¿Quieres que le eche un poco de cara al asunto?",
           "¿Cuál de mis dos caras dice la verdad?",
           "Yo que tú encaraba la salida.",
           "No te va a gustar mi doble juego.",
           "Yo que tú me lo pensaba dos veces.",
           "Prepárate para una ración DOBLE.",
           "Vas a ver mis caras en sueños.",
           "Para vencerme hacen falta dos como tú.",
           ],
    'ac': ["¡Te voy a perseguir hasta el dibuparque!",
           "¿No oyes una sirena?",
           "Ja, ja, cómo voy a disfrutar.",
           "Me encanta la emoción de la persecución.",
           "¡Corre, corre, que te pillo!",
           "¿Te has hecho un seguro?",
           "Espero que te hayas traído una camilla.",
           "Dudo que aguantes mi ritmo.",
           "A partir de aquí se te va a hacer todo cuesta arriba.",
           "Pronto vas a necesitar atención médica urgente.",
           "Esto no es para reírse.",
           "Espero que te gusten los hospitales.",
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
    100 : "¡Buenas!",
    101 : "¡Hola!",
    102 : "¡Muy Buenas!",
    103 : "¡Eh!",
    104 : "¿Qué hay?",
    105 : "¡Hola a todos!",
    106 : "¡Bienvenido a Toontown!",
    107 : "¿Qué tal?",
    108 : "¿Cómo estás?",
    109 : "¿Hola?",

    # Bye
    200 : "¡Chao!",
    201 : "¡Nos vemos!",
    202 : "¡Hasta la vista!",
    203 : "¡Que pases un buen día!",
    204 : "¡Diviértete!",
    205 : "¡Buena suerte!",
    206 : "Vuelvo enseguida.",
    207 : "Tengo que irme.",
    208 : "I'll be back later!",
    209 : "I only have a few minutes.",

    # Happy
    300 : ":-)",
    301 : "¡Hey!",
    302 : "¡Hurra!",
    303 : "¡chupi!",
    304 : "¡Yujuuu!",
    305 : "¡Sí!",
    306 : "¡Ja, ja!",
    307 : "¡Ji, ji!",
    308 : "¡Guau!",
    309 : "¡Fantástico!",
    310 : "¡Yepaa!",
    311 : "¡Estupendo!",
    312 : "¡Yupii!",
    313 : "¡Yipee!",
    314 : "¡Yiii ja!",
    315 : "¡Dibufantástico!",

    # Sad
    400 : ":-(",
    401 : "¡Oh no!",
    402 : "¡Oh oh!",
    403 : "¡Caramba!",
    404 : "¡Vaya!",
    405 : "¡Ay!",
    406 : "¡Uf!",
    407 : "¡¡¡No!!!",
    408 : "¡Auuu!",
    409 : "¿Eh?",
    410 : "Necesito más puntos de risa.",

    # Friendly
    500 : "¡Gracias!",
    501 : "No hay de qué.",
    502 : "¡De nada!",
    503 : "¡A tu disposición!",
    504 : "No, gracias a ti.",
    505 : "¡Buen trabajo en equipo!",
    506 : "¡Qué divertido!",
    507 : "¡Sé mi amigo!",
    508 : "¡Trabajemos en equipo!",
    509 : "¡Sois estupendos!",
    510 : "¿Eres nuevo aquí?",
    511 : "¿Has ganado?",
    512 : "Creo que esto es demasiado para ti.",
    513 : "¿Quieres que te ayude?",
    514 : "¿Puedes ayudarme?",
    515 : "Have you been here before?",

    # Friendly "You..."
    600 : "Pareces simpático.",
    601 : "¡Eres genial!",
    602 : "¡Eres la bomba!",
    603 : "¡Eres sensacional!",

    # Friendly "I like..."
    700 : "Me gusta tu nombre.",
    701 : "Me gusta tu aspecto.",
    702 : "Me gusta tu camiseta.",
    703 : "Me gusta tu falda.",
    704 : "Me gustan tus shorts.",
    705 : "¡Me gusta este juego!",

    # Sorry
    800 : "¡Lo siento!",
    801 : "¡Vaya!",
    802 : "¡Lo siento, estoy peleando con los bots!",
    803 : "¡Lo siento, estoy obteniendo gominolas!",
    804 : "¡Lo siento, estoy haciendo una dibutarea!",
    805 : "Lo siento, he tenido que marcharme repentinamente.",
    806 : "Discúlpame, me retrasé.",
    807 : "Lo siento, no puedo.",
    808 : "No he podido esperar más.",
    809 : "No te entiendo.",
    810 : "Usa la %s." % GlobalSpeedChatName,
    811 : "Sorry, I'm busy fishing!",
    812 : "Sorry, I'm in a building!",
    813 : "Sorry, I'm helping a friend!",
    814 : "Sorry, I'm busy kart racing!",
    815 : "Sorry, I'm busy gardening!",
    816 : "I can't get on the elevator now.",
    817 : "Sorry, I'm busy golfing!",
    818 : "Sorry, my Friends List is full.",
    
    # Stinky
    900 : "¡Eh!",
    901 : "¡Vete de aquí!",
    902 : "¡Deja de hacer eso!",
    903 : "¡Eso es mala educación!",
    904 : "¡No seas malo!",
    905 : "¡Hueles mal!",
    906 : "Envía un informe de error.",
    907 : "No me puedo mover, porque hay un error.",

    # Places
    1000 : "¡Vamos!",
    1001 : "¿Puedes teletransportarte a donde estoy?",
    1002 : "¿Nos vamos?",
    1003 : "¿Adónde deberíamos ir?",
    1004 : "¿Por qué camino?",
    1005 : "Por aquí.",
    1006 : "Sígueme.",
    1007 : "¡Espérame!",
    1008 : "Vamos a esperar a mi amigo.",
    1009 : "Vamos a buscar a otros dibus.",
    1010 : "Espera aquí.",
    1011 : "Espera un momento.",
    1012 : "Nos encontraremos aquí.",
    1013 : "¿Puedes venir a mi casa?",
    1014 : "Don't wait for me.",
    1015 : "Wait!",
    1016 : "Come check out my garden.",
    1017 : "Let's catch the next one.",

    # Places "Let's go..."
    1100 : "¡Vámonos en el tranvía!",
    1101 : "¡Vamos a volver al dibuparque!",
    1102 : "¡Vamos a luchar contra los %s!" % Cogs,
    1103 : "¡Vamos a tomar un edificio %s!" % Cog,
    1104 : "¡Vamos al ascensor!",
    1105 : "¡Vamos al Centro de Toontown!",
    1106 : "¡Vamos a Puerto Donald!",
    1107 : "¡Vamos a Melodilandia de Minnie!",
    1108 : "¡Vamos a los Jardines de Daisy!",
    1109 : "¡Vamos a Frescolandia!",
    1110 : "¡Vamos a Sueñolandia de Donald!",
    1111 : "Let's go to %s!" % lGoofySpeedway,
    1112 : "Let's go to my house!",
    1113 : "Let's go to your house!",
    1114 : "Let's go to Sellbot HQ!",
    1115 : "Let's go fight the VP!",
    1116 : "Let's go in the Factory!",
    1117 : "Let's go fishing!",
    1118 : "Let's go fishing at my house!",
    1119 : "Let's go to Cashbot HQ!",
    1120 : "Let's go fight the CFO!",
    1121 : "Let's go in the Mint!",
    1122 : "Let's go to Lawbot HQ!",
    1123 : "Let's go fight the Chief Justice!",
    1124 : "Let's go in the District Attorney's Office!",
    1125 : "Let's go to %s!" % lOutdoorZone,
    1126 : "Let's go to %s!" % lGolfZone,
    1127 : "Let's go to Bossbot HQ!",
    1128 : "Let's go fight the CEO!",
    1129 : "Let's go in the Cog Golf Courses!",
    1130 : "Let's go take over a Field Office!",

    # Toontasks
    1200 : "¿En qué dibutarea estás trabajando?",
    1201 : "Ocupémonos de eso.",
    1202 : "Esto no es lo que busco.",
    1203 : "Voy a buscar eso.",
    1204 : "No está en esta calle.",
    1205 : "Todavía no lo he encontrado.",
    1206 : "I need more Merits.",
    1207 : "I need more Sellbot Suit Parts.",
    1208 : "This isn't what you need.",
    1209 : "I found what you need.",
    1210 : "I need more Cogbucks.",
    1211 : "I need more Jury Notices.",
    1212 : "I need more Stock Options.",
    1213 : "I need more Cashbot Suit Parts.",
    1214 : "I need more Lawbot Suit Parts.",
    1215 : "I need more Bossbot Suit Parts.",

    1299 : "Necesito que me asignen una dibutarea.",

    # Toontasks "I think you should choose..."
    1300 : "Creo que debes usarun curadibu.",
    1301 : "Creo que debes usar un sonido.",
    1302 : "Creo que debes usar una caída.",
    1303 : "Creo que debes usar un cebo.",
    1304 : "Creo que debes usar una trampa.",

    # Battle
    1400 : "¡Deprisa!",
    1401 : "¡Buen Disparo!",
    1402 : "¡Buena Broma!",
    1403 : "¡No me has dado!",
    1404 : "¡Lo has conseguido!",
    1405 : "¡Lo hemos hecho!",
    1406 : "¡Sigue así!",
    1407 : "¡Está chupado!",
    1408 : "¡Qué facil!",
    1409 : "¡Corre!",
    1410 : "¡Socorro!",
    1411 : "¡Uf!",
    1412 : "Tenemos problemas.",
    1413 : "Necesito más bromas.",
    1414 : "Necesito un curadibu.",
    1415 : "Deberías pasar.",
    1416 : "We can do this!",

    # Battle GAGS
    1500 : "¡Usemos un curadibu!",
    1501 : "¡Usemos una trampa!",
    1502 : "¡Usemos un cebo!",
    1503 : "¡Usemos un sonido!",
    1504 : "¡Usemos un lanzamiento!",
    1505 : "¡Usemos un chorro!",
    1506 : "¡Usemos una caida!",

    # Battle TAUNTS
    1520 : "Rock and roll!",
    1521 : "That's gotta hurt.",
    1522 : "Catch!",
    1523 : "Special delivery!",
    1524 : "Are you still here?",
    1525 : "I'm SO scared!",
    1526 : "That's going to leave a mark!",

    # Battle STRATEGY
    1550 : "I'm going to use trap.",
    1551 : "I'm going to use lure.",
    1552 : "I'm going to use drop.",
    1553 : "You should use a different gag.",
    1554 : "Let's all go for the same Cog.",
    1555 : "You should choose a different Cog.",
    1556 : "Go for the weakest Cog first.",
    1557 : "Go for the strongest Cog first.",
    1558 : "Save your powerful gags.",
    1559 : "Don't use sound on lured Cogs.",

    # Gag Shop
    1600 : "Tengo suficientes bromas.",
    1601 : "Necesito más gominolas.",
    1602 : "Yo también.",
    1603 : "¡Deprisa!",
    1604 : "¿Una más?",
    1605 : "¿Quieres jugar otra vez?",
    1606 : "Jugemos de nuevo.",

    # Factory
    1700 : "Separémonos.",
    1701 : "No nos separemos.",
    1702 : "Vamos a luchar contra los bots.",
    1703 : "Salta encima del interruptor.",
    1704 : "Atraviesa la puerta.",

    # Sellbot Factory
    1803 : "Estoy en la entrada principal.",
    1804 : "Estoy en el vestíbulo.",
    1805 : "Estoy en la entrada que da al vestíbulo.",
    1806 : "Estoy en la entrada que da al vestíbulo.",
    1807 : "Estoy en la sala de máquinas.",
    1808 : "Estoy en la sala de calderas.",
    1809 : "Estoy en la pasarela este.",
    1810 : "Estoy en la mezcladora de pintura.",
    1811 : "Estoy en la sala donde se guarda la mezcladora de pintura.",
    1812 : "Estoy en la pasarela del silo oeste.",
    1813 : "Estoy en la sala de tuberías.",
    1814 : "Estoy en las escaleras que dan a la sala de tuberías.",
    1815 : "Estoy en la sala de conductos.",
    1816 : "Estoy en la entrada de servicio.",
    1817 : "Estoy en el callejón del Pisotón.",
    1818 : "Estoy fuera de la sala de la lava.",
    1819 : "Estoy en la sala de la lava.",
    1820 : "Estoy en la sala donde se guarda la lava.",
    1821 : "Estoy en la pasarela oeste.",
    1822 : "Estoy en la sala del aceite.",
    1823 : "Estoy en la cabina de vigilancia del almacén.",
    1824 : "Estoy en el almacén.",
    1825 : "Estoy fuera de la mezcladora de pintura.",
    1827 : "Estoy fuera de la sala del aceite.",
    1830 : "Estoy en la sala de control del silo este.",
    1831 : "Estoy en la sala de control del silo oeste.",
    1832 : "Estoy en la sala de control del silo central.",
    1833 : "Estoy en el silo este.",
    1834 : "Estoy en el silo oeste.",
    1835 : "Estoy en el silo central.",
    1836 : "Estoy en el silo oeste.",
    1837 : "Estoy en el silo este.",
    1838 : "Estoy en la pasarela del silo este.",
    1840 : "Estoy encima del silo oeste.",
    1841 : "Estoy encima del silo este.",
    1860 : "Estoy en el ascensor del silo oeste.",
    1861 : "Estoy en el ascensor del silo este.",

    # Sellbot Factory continued
    1903 : "Reunámonos en la entrada principal.",
    1904 : "Reunámonos en el vestíbulo.",
    1905 : "Reunámonos en la entrada que da al vestíbulo.",
    1906 : "Reunámonos en la entrada que da al vestíbulo.",
    1907 : "Reunámonos en la sala de máquinas.",
    1908 : "Reunámonos en la sala de calderas.",
    1909 : "Reunámonos en la pasarela este.",
    1910 : "Reunámonos en la mezladora de pintura.",
    1911 : "Reunámonos en la sala donde se guarda la mezcladora de pintura.",
    1912 : "Reunámonos en la pasarela del silo oeste.",
    1913 : "Reunámonos en la sala de tuberías.",
    1914 : "Reunámonos en las escaleras que dan a la sala de tuberías.",
    1915 : "Reunámonos en la sala de conductos.",
    1916 : "Reunámonos en la entrada de servicio.",
    1917 : "Reunámonos en el callejón del Pisotón.",
    1918 : "Reunámonos fuera de la sala de la lava.",
    1919 : "Reunámonos en la sala de la lava.",
    1920 : "Reunámonos en la sala donde se guarda la lava.",
    1921 : "Reunámonos en la pasarela oeste.",
    1922 : "Reunámonos en la sala del aceite.",
    1923 : "Reunámonos en la cabina de vigilancia del almacén.",
    1924 : "Reunámonos en el almacén.",
    1925 : "Reunámonos fuera de la mezcladora de pintura.",
    1927 : "Reunámonos fuera de la sala del aceite.",
    1930 : "Reunámonos en la sala de control del silo este.",
    1931 : "Reunámonos en la sala de control del silo oeste.",
    1932 : "Reunámonos en la sala de control del silo central.",
    1933 : "Reunámonos en el silo este.",
    1934 : "Reunámonos en el silo oeste.",
    1935 : "Reunámonos en el silo central.",
    1936 : "Reunámonos en el silo oeste.",
    1937 : "Reunámonos en el silo este.",
    1938 : "Reunámonos en la pasarela del silo este.",
    1940 : "Reunámonos encima del silo oeste.",
    1941 : "Reunámonos encima del silo este.",
    1960 : "Reunámonos en el ascensor del silo oeste.",
    1961 : "Reunámonos en el ascensor del silo este.",

    # These are used only for the style settings in the OptionsPage
    # These should never actually be spoken or listed on the real speed chat
    2000 : "Morado",
    2001 : "Azul",
    2002 : "Añil",
    2003 : "Aguamarina",
    2004 : "Verde",
    2005 : "Amarillo",
    2006 : "Naranja",
    2007 : "Rojo",
    2008 : "Rosa",
    2009 : "Marrón",
    # Shader specific
    2050 : "None",
    2051 : "B&W",
    2052 : "Sepia",

    # CFO battle
    2100 : "Please operate the crane.",
    2101 : "May I operate the crane?",
    2102 : "I need practice operating the crane.",
    2103 : "Pick up a disabled goon.",
    2104 : "Throw the goon at the CFO.",
    2105 : "Throw a safe now!",
    2106 : "Don't throw a safe now!",
    2107 : "A safe will knock off his helmet.",
    2108 : "A safe will become his new helmet.",
    2109 : "I can't reach any safes.",
    2110 : "I can't reach any goons.",

    2120 : "Please disable the goons.",
    2121 : "I would rather disable goons.",
    2122 : "I need practice disabling goons.",
    2123 : "Please stay nearby.",
    2124 : "Keep moving.",
    2125 : "I need to keep moving.",
    2126 : "Look for someone who needs help.",

    2130 : "Please save the treasures.",
    2131 : "Take the treasures.",
    2132 : "I need treasures!",
    2133 : "Look out!",

    # CJ battle
    2200 : "You need to hit the scale.",
    2201 : "I will hit the scale.",
    2202 : "I need help with the scale!",
    2203 : "You need to stun the Cogs.",
    2204 : "I will stun the Cogs.",
    2205 : "I need help with the Cogs!",
    2206 : "I need more evidence!",
    2207 : "I'm shooting for chairs in the top row.",
    2208 : "I'm shooting for chairs in the bottom row.",
    2209 : "Move out of the way! We can't hit the pan.",
    2210 : "I'll do Toon-Ups for us.",
    2211 : "I don't have any bonus weight.",
    2212 : "I have a bonus weight of 1.",
    2213 : "I have a bonus weight of 2.",
    2214 : "I have a bonus weight of 3.",
    2215 : "I have a bonus weight of 4.",
    2216 : "I have a bonus weight of 5.",
    2217 : "I have a bonus weight of 6.",
    2218 : "I have a bonus weight of 7.",
    2219 : "I have a bonus weight of 8.",
    2220 : "I have a bonus weight of 9.",
    2221 : "I have a bonus weight of 10.",
    2222 : "I have a bonus weight of 11.",
    2223 : "I have a bonus weight of 12.",    

    # CEO battle
    2300 : "You feed the Cogs on the left.",
    2301 : "I'll feed the Cogs on the left.",
    2302 : "You feed the Cogs on the right.",
    2303 : "I'll feed the Cogs on the right.",
    2304 : "You feed the Cogs in the front.",
    2305 : "I'll feed the Cogs in the front.",
    2306 : "You feed the Cogs in the back.",
    2307 : "I'll feed the Cogs in the back.",
    2308 : "You use the seltzer bottle.",
    2309 : "I'll use the seltzer bottle.",
    2310 : "You use the golf tee.",
    2311 : "I'll use the golf tee.",
    2312 : "I'll serve this table.",
    2313 : "Can you serve this table?",
    2314 : "Feed the same cog again.",
    2315 : "Hurry, your cog is hungry!",
    2316 : "Please save the snacks for sadder toons.",
    2317 : "Take the snacks before they fall.",
    
    
    #Kart Racing Phrases
    #IMPORTANT: if you change numbers or add/subtract lines here than be
    # sure to adjust the kart racing menu guid dict below
    # Invites/Destinations
    3010 : "Anyone want to race?",
    3020 : "Let's race!",
    3030 : "Want to race?",
    3040 : "Let's show off our karts!",
    3050 : "I don't have enough tickets.",
    3060 : "Let's race again!",
    3061 : "Want to race again?",


    #Places
    3150 : "I need to go to the Kart Shop.",
    3160 : "Let's go to the Race Tracks!",
    3170 : "Let's go to Pit Row to show off our karts!",
    3180 : "I'm going to Pit Row to show off my kart!",
    3190 : "Meet me at the Race Tracks!",
    3110 : "Meet up near the Kart Shop!",
    3130 :  "Where should we meet?",

    #Races
    3200 : "Where do you want to race?",
    3201 : "Let's pick a different race.",
    3210 : "Let's do a practice race.",
    3211 : "Let's do a battle race.",
    3220 : "I like the Screwball Stadium race!",
    3221 : "I like the Rustic Raceway race!",
    3222 : "I like the City Circuit race!",
    3223 : "I like the Corkscrew Coliseum race!",
    3224 : "I like the Airborne Acres race!",
    3225 : "I like the Blizzard Boulevard race!",
    3230 : "Let's race in the Screwball Stadium!",
    3231 : "Let's race on the Rustic Raceway!",
    3232 : "Let's race on the City Circuit!",
    3233 : "Let's race in the Corkscrew Coliseum!",
    3234 : "Let's race on the Airborne Acres!",
    3235 : "Let's race on the Blizzard Boulevard!",

    #Tracks
    3600 : "Which track do you want to race on?",
    3601 : "Pick a track!",
    3602 : "Can we race on a different track?",
    3603 : "Let's pick a different track!",
    3640 : "I want to race on the first track!",
    3641 : "I want to race on the second track!",
    3642 : "I want to race on the third track!",
    3643 : "I want to race on the fourth track!",
    3660 : "I don't want to race on the first track!",
    3661 : "I don't want to race on the second track!",
    3662 : "I don't want to race on the third track!",
    3663 : "I don't want to race on the fourth track!",

    #Compliments
    3300 : "Wow! You are FAST!",
    3301 : "You're too fast for me!",
    3310 : "Good race!",
    3320 : "I really like your kart!",
    3330 : "Sweet ride!",
    3340 : "Your kart is cool!",
    3350 : "Your kart is awesome!",
    3360 : "Your kart is totally sweet!",

    #Taunts (commented out taunts are for possible purchase lines)
    #3400 : "Eat my dust!",
    3400 : "Too scared to race me?",
    3410 : "See you at the finish line!",
    #3420 : "You're slow as molasses!",
    3430 : "I'm as fast as lightning!",
    #3440 : "I'm faster than the speed of light!",
    3450 : "You'll never catch me!",
    3451 : "You'll never beat me!",
    3452 : "No one can beat my time!",
    3453 : "Hurry up slow pokes!",
    3460 : "Give me another shot!",
    3461 : "You got lucky!",
    3462 : "Ooooh! That was a close one!",
    3470 : "Wow, I thought you had me beat!",
    #3500 : "Check out my ride!",
    #3510 : "Look at my wheels!",
    #3540 : "Vroom! Vroom!",
    #3560 : "I've seen Cogs move faster!",
    #3600 : "I'm the fastest of the fast!",


    # Golf phrases

    # Play
    4000 : "Let's play minigolf!",
    4001 : "Let's play again!",
    4002 : "Want to golf?",

    # Courses
    4100 : "Let's play 'Walk In The Par.'",
    4101 : "Let's play 'Hole Some Fun.'",
    4102 : "Let's play 'The Hole Kit and Caboodle.'",
    4103 : "That course is too easy.",
    4104 : "That course is too hard.",
    4105 : "That course is just right.",

    # Tips
    4200 : "Try standing more to the left.",
    4201 : "Try standing more to the right.",
    4202 : "Try standing right in the middle.",
    4203 : "Try hitting it harder.",
    4204 : "Try hitting it softer.",
    4205 : "Try aiming more to the left.",
    4206 : "Try aiming more to the right.",
    4207 : "Try aiming right down the middle.",

    # Comments
    4300 : "So close!",
    4301 : "What a great shot!",
    4302 : "That was a lucky shot.",
    4303 : "I'll take a mulligan...",
    4304 : "That's a gimme.",
    4305 : "Fore!",
    4306 : "Shhhh!",
    4307 : "Good game!",

    # Boarding Group phrases

    5000 : "Let's form a Boarding Group.",
    5001 : "Join my Boarding Group.",
    5002 : "Can you invite me to your Boarding Group?",
    5003 : "I'm already in a Boarding Group.",
    5004 : "Leave your Boarding Group.",
    5005 : "We are boarding now.",
    5006 : "Where are we going?",
    5007 : "Are we ready?",    
    5008 : "Let's Go!",
    5009 : "Don't leave this area or you will leave the Boarding Group.",

    # Let's Go to...
    5100 : "Let's go to the Front Three.",
    5101 : "Let's go to the Middle Six.",
    5102 : "Let's go to the Back Nine.",
    5103 : "Let's go to the C.E.O. Battle.",
    5104 : "Let's go to the Senior V.P Battle.",
    5105 : "Let's go to the Front Entrance.",
    5106 : "Let's go to the Side Entrance.",    
    5107 : "Let's go to the Coin Mint.",
    5108 : "Let's go to the Dollar Mint.",
    5109 : "Let's go to the Bullion Mint.",
    5110 : "Let's go to the C.F.O. Battle.",
    5111 : "Let's go to the Chief Justice Battle.",
    5112 : "Let's go to the Lawbot A Office.",
    5113 : "Let's go to the Lawbot B Office.",
    5114 : "Let's go to the Lawbot C Office.",
    5115 : "Let's go to the Lawbot D Office.",

    # We're going to...
    5200 : "We're going to the Front Three.",
    5201 : "We're going to the Middle Six.",
    5202 : "We're going to the Back Nine.",
    5203 : "We're going to the C.E.O. Battle.",
    5204 : "We're going to the Senior V.P Battle.",
    5205 : "We're going to the Front Entrance.",
    5206 : "We're going to the Side Entrance.",    
    5207 : "We're going to the Coin Mint.",
    5208 : "We're going to the Dollar Mint.",
    5209 : "We're going to the Bullion Mint.",
    5210 : "We're going to the C.F.O. Battle.",
    5211 : "We're going to the Chief Justice Battle.",
    5212 : "We're going to the Lawbot A Office.",
    5213 : "We're going to the Lawbot B Office.",
    5214 : "We're going to the Lawbot C Office.",
    5215 : "We're going to the Lawbot D Office.",

    # Parties General Phrases
    5300 : "Let's go to a party.",
    5301 : "See you at the party!",
    5302 : "My party has started!",
    5303 : "Come to my party!",
    # Parties Phrases when inside a party
    5304 : "Welcome to my party!",
    5305 : "This party rules!",
    5306 : "Your party is fun!",
    5307 : "It's party time!",
    5308 : "Time is running out!",
    5309 : "No cogs allowed!",
    5310 : "I like this song!",
    5311 : "This music is great!",
    5312 : "Cannons are a blast!",
    5313 : "Watch me jump!",
    5314 : "Trampolines are fun!",
    5315 : "Let's play Catch!",
    5316 : "Let's dance!",
    5317 : "To the dance floor!",
    5318 : "Let's play Tug of War!",    
    5319 : "Start the fireworks!",
    5320 : "These fireworks are beautiful!",
    5321 : "Nice decorations.",
    5322 : "I wish I could eat this cake!",    
        
    # Promotional Considerations
    10000 : "The choice is yours!",
    10001 : "Who are you voting for?",
    10002 : "I'm pickin' Chicken!",
    10003 : "Vote now! Vote Cow!",
    10004 : "Go bananas! Vote Monkey!",
    10005 : "Be a honey! Vote Bear!",
    10006 : "Think big! Vote Pig!",
    10007 : "Vote Goat - and that's all she wrote!",

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
    21000: 'Here boy!',
    21001: 'Here girl!',
    21002: 'Stay.',
    21003: 'Good boy!',
    21004: 'Good girl!',
    21005: 'Nice Doodle.',
    21006: 'Please don\'t bother me.',

    # Pet/Doodle Tricks
    21200: 'Jump!',
    21201: 'Beg!',
    21202: 'Play dead!',
    21203: 'Rollover!',
    21204: 'Backflip!',
    21205: 'Dance!',
    21206: 'Speak!',

    # Phrases for April Toon's week
    30100 : "Happy April Toons' Week!",
    30101 : "Welcome to my April Toons' Week party!",
    30110 : "Mickey is in Daisy Gardens.",
    30111 : "Daisy is in Toontown Central.",
    30112 : "Minnie is in The Brrrgh.",
    30113 : "Pluto is in Melodyland.",
    30114 : "Donald is sleepwalking at the Speedway.",
    30115 : "Goofy is in Dreamland.",
    
    30120 : "Mickey is acting like Daisy!",
    30121 : "Daisy is acting like Mickey!",
    30122 : "Minnie is acting like Pluto!",
    30123 : "Pluto is acting like Minnie!",
    30124 : "Pluto is talking!",
    30125 : "Goofy is acting like Donald!",
    30126 : "Donald is dreaming he is Goofy!",
    
    30130 : "Watch how far I can jump.",
    30131 : "Wow, you jumped really far!",
    30132 : "Hey, Doodles can talk!",
    30133 : "Did your Doodle just talk?",
    30140 : "Things sure are silly around here!",
    30141 : "How sillier could things get?",

    # Phrases for Sellbot Nerf Event
    30150 : "Operation: Storm Sellbot is here!",
    30151 : "Sellbot Towers had its power drained by Doodles!",
    30152 : "The VP had his power drained by Doodles!",
    30153 : "Everyone can fight the VP right now!",
    30154 : "You don't need a Sellbot Disguise to fight the VP!",
    30155 : "You get a Rental Suit when you go into Sellbot Towers.",
    30156 : "Do you like my Rental Suit? Sorry about the safety pins!",
    30157 : "It's best to have eight Toons to fight the VP.",
    30158 : "Will you help me fight the VP?",
    30159 : "Do you want to fight the VP with me?",
    30160 : "Would you like to join my Sellbot VP group?",
    30161 : "I am looking for a Toon with a Rental Suit to fight the VP.",
    30162 : "I have a Rental Suit, and am looking to fight the VP.",
    30163 : "Just walk through the doors to get your Rental Suit.",
    30164 : "Save your gags for the Cogs inside!",
    30165 : "We have to defeat these Cogs first!",
    30166 : "Bump the barrels to gag up.",
    30167 : "Bump the barrel to get a Toon-up.",
    30168 : "Now we have to fight some Skelecogs!",
    30169 : "Jump up and touch the Toon's cage for pies!",
    30170 : "Now we fight the VP!",
    30171 : "Aim your pies by pressing the Delete button.",
    30172 : "Two Toons should throw pies through the VP's open doors!",
    30173 : "I'll stun the VP from the front.",
    30174 : "I'll stun the VP from the back.",
    30175 : "Jump when the VP jumps!",

    # Phrases for Jellybean Jam
    30180 : "I got double jellybeans on the Trolley!",
    30181 : "I got double jellybeans from fishing!",
    30182 : "I got double jellybeans at a party!",
    30183 : "Jellybeans jellybeans jellybeans!",
    30184 : "I'm really keen to earn a bean!",
    30185 : "Don't be smelly, get beans of jelly!",
    30186 : "I'm gonna adopt a Doodle with all these jellybeans!",
    30187 : "What am I gonna spend all these jellybeans on?",
    30188 : "I'm gonna throw a huge party!",
    30189 : "I'm gonna decorate my whole Estate!",
    30190 : "I'm gonna buy a whole new wardrobe!",
    30191 : "Jellybeans, please!",
    30192 : "Don't be mean, give a bean!",
    
    # Phrases for caroling
    30200 : "Deck the halls... ",
    30201 : "Load some pies...",
    30202 : "Joyful toons...",
    30203 : "Snowman heads...",
    30204 : "Toontown's merry...",
    30205 : "Lure good cheer...",
    
    30220 : "Deck the halls with seltzer spray!\nHappy Winter Holiday!",
    30221 : "Load some pies into your sleigh!\nHappy Winter Holiday!",
    30222 : "Joyful toons bring Cogs dismay!\nHappy Winter Holiday!",
    30223 : "Snowman heads are hot today!\nHappy Winter Holiday!",
    30224 : "Toontown's merry, come what may!\nHappy Winter Holiday!",
    30225 : "Lure good cheer the Toontown way!\nHappy Winter Holiday!",

    # Phrases for Halloween
    30250: "Boo!",
    30251: "Happy Halloween!",
    30252: "Spooky!",

    # Phrases for Christmas
    30275: "Happy holidays!",
    30276: "Season's greetings!",
    30277: "Have a Wonderful Winter!",    
    
    # Phrases for Silly Story
    30301 : "Have you seen the Silly Meter?",
    30302 : "The Silly Meter is in Toon Hall.",
    30303 : "Things sure are getting silly around here!",
    30304 : "I saw a fire hydrant moving!",
    30305 : "Toontown is coming to life!",
    30306 : "Have you been to Flippy's new office?",
    30307 : "I caused a Silly Surge in battle!",
    30308 : "Let's defeat some Cogs to make Toontown sillier!",
    
    30309 : "The Silly Meter is bigger and crazier than ever!",
    30310 : "Lots of hydrants have come alive!",
    30311 : "I saw a mail box moving!",
    30312 : "I watched a trash can wake up!",
    30313 : "How silly can it get?",
    30314 : "What\'s going to happen next?",
    30315 : "Something silly, I bet!",
    30316 : "Have you caused a Silly Surge yet?",
    30317 : "Let's defeat some Cogs to make Toontown sillier!",
    
    30318 : "Cog Invasion!",
    30319 : "Incoming!",
    30320 : "Let\'s stop those Cogs!",
    30321 : "I miss the Silly Surges!",
    30322 : "Let\'s go stop an Invasion!",
    30323 : "Toontown is sillier than ever now!",
    30324 : "Have you seen something come alive?",
    30325 : "My favorites are the fire hydrants!",
    30326 : "My favorites are the mailboxes!",
    30327 : "My favorites are the trash cans!",
    
    30328 : "Hooray! We stopped the Cog invasions!",
    30329 : "A hydrant helped me in battle!",
    30330 : "A hydrant boosted my Squirt Gags!",
    30331 : "A trash can boosted my Toon-Up Gags!",
    30332 : "A mailbox helped my Throw Gags!",
    
    # Phrases for Victory Parties (warning 60400 is in use)
    30350: "Welcome to my Victory Party!",
    30351: "This is a great Victory Party!",
    30352: "We showed those Cogs who's boss!",
    30353: "Good job helping end the Cog invasions!",
    30354: "I bet this is driving the Cogs crazy!",
    
    30355: "Let's play Cog-O-War!",
    30356: "My team won at Cog-O-War!",
    30357: "It's nice to have fire hydrants, trash cans, and mailboxes here!",
    30358: "I like the balloon of the Doodle biting the Cog!",
    30359: "I like the balloon of the Cog covered in ice cream!",
    30360: "I like the wavy Cog that flaps his arms!",
    30361: "I jumped on a Cog's face!",

    # Phrases for Sellbot Field Offices
    30400 : "The Sellbots are invading!",
    30401 : "The V.P. was hopping mad about Operation: Storm Sellbot ...",
    30402 : "He's sending the Sellbots in to invade Toontown!",
    30403 : "Let's go fight some Sellbots!",
    30404 : "There's a new kind of building in Toontown!",
    30405 : "Have you seen the Mover & Shaker Field Offices?",
    30406 : "The V.P. created them as a reward for the Movers & Shakers.",
    30407 : "Let's go defeat a Field Office!",
    30408 : "I got an SOS Card for defeating a Field Office!",
    30409 : "Clear the map by exploring the maze.",
    30410 : "Destroy the Cogs by hitting them with water balloons!",
    30411 : "Movers & Shakers take two balloons to destroy.",
    30412 : "Look out for falling objects!",
    30413 : "Watch out for the Cogs!",
    30414 : "Collect Jokes to get a Toon-up at the end!",
    30415 : "When the room shakes, a Mover & Shaker is nearby.",
    30416 : "Defeat all four Movers & Shakers to open the exit!",
    30417 : "The exit is open!",
    30418 : "It's the Boss!",

    # Phrases for Ides Of March
    30450 : "It's easy to be green!",
    30451 : "Visit Green Bean Jeans and you can be green too!",
    30452 : "It's on Oak Street in Daisy Gardens.",

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
    30476 : "Use the Chief Justice SpeedChat Menu!",
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
    50001 : 'Aye',
    50002 : 'Nay',
    50003 : 'Yes',
    50004 : 'No',
    50005 : 'Ok',

    # EXPRESSIONS
    50100 : "Gangway!",
    50101 : "Blimey!",
    50102 : "Well blow me down!",
    50103 : "Walk the plank!",
    50104 : "Dead men tell no tales....",
    50105 : "Shiver me timbers!",
    50106 : "Salty as a Kraken's kiss.",
    50107 : "Treasure be the measure of our pleasure!",
    50108 : "I don't fear death - I attune it.",
    

    # EXPRESSIONS - GREETINGS
    50700 : "Ahoy!",
    50701 : "Ahoy, mate!",
    50702 : "Yo-Ho-Ho",
    50703 : "Avast!",
    50704 : "Hey Bucko.",

    # EXPRESSIONS - GOODBYES
    50800 : "Until next time.",
    50801 : "May fair winds find ye.",
    50802 : "Godspeed.",


    # EXPRESSIONS - FRIENDLY
    50900 : "How are ye, mate?",
    50901 : "",

    # EXPRESSIONS - HAPPY
    51000 : "It's like the sky is raining gold doubloons!",
    51001 : "May a stiff wind be at our backs, the sun on our faces and our cannons fire true!",

    # EXPRESSIONS - SAD
    51100 : "I be sailing some rough waters today.",

    # EXPRESSIONS - SORRY
    51200 : "Me apologies, mate.",
    51201 : "Sorry.",
    51202 : "Sorry, I was busy before.",
    51203 : "Sorry, I already have plans.",
    51204 : "Sorry, I don't need to do that.",

    # COMBAT
    51300 : "Attack the weakest one!",
    51301 : "Attack the strongest one!",
    51302 : "Attack me target!",
    51303 : "I be needing help!",
    51304 : "I can't do any damage!",
    51305 : "I think we be in trouble.",
    51306 : "Surround the most powerful one.",
    51307 : "We should retreat.",
    51308 : "Run for it!",

    # SEA COMBAT
    51400 : "Fire a Broadside!",
    51401 : "Port Side! (left)",
    51402 : "Starboard Side! (right)",
    51403 : "Incoming!",
    51404 : "Come about!",
    51405 : "Broadside! Take Cover!",
    51406 : "To the Cannons!",
    51407 : "Open fire!",
    51408 : "Hold yer fire!",
    51409 : "Aim for the masts!",
    51410 : "Aim for the hull!",
    51411 : "Prepare to board!",
    51412 : "She's coming about.",
    51413 : "Ramming speed!",
    51414 : "We've got her on the run.",
    51415 : "We be taking on water!",
    51416 : "We can't take anymore!",
    51417 : "I don't have a shot!",
    51418 : "Let's find port for repair.",
    51419 : "Man overboard!",
    51420 : "Enemy spotted.",
    51421 : "Handsomely now, mates!",

    # PLACES
    50400 : "Let's set sail.",
    50401 : "Let's get out of here.",


    # PLACES - LETS SAIL...
    51500 : "Let's sail to Port Royal.",
    51501 : "Let's sail to Tortuga.",
    51502 : "Let's sail to Padres Del Fuego.",
    51503 : "Let's sail to Devil's Anvil.",
    51504 : "Let's sail to Kingshead.",
    51505 : "Let's sail to Isla Perdida.",
    51506 : "Let's sail to Cuba.",
    51507 : "Let's sail to Tormenta.",
    51508 : "Let's sail to Outcast Isle.",
    51509 : "Let's sail to Driftwood.",
    51510 : "Let's sail to Cutthroat.",
    51511 : "Let's sail to Rumrunner's Isle.",
    51512 : "Let's sail to Isla Cangrejos.",
    
    # PLACES - LETS HEAD TO...
    51600 : "Let's head into town.",
    51601 : "Let's go to the docks.",
    51602 : "Let's head to the tavern.",    

    # PLACES - LETS HEAD TO... - PORT ROYAL
    51800 : "Let's go to Fort Charles.",
    51801 : "Let's go to the Governor's Mansion.",

    # PLACES - WHERE IS ..?
    52500 : "Where be I, mate?",

    # DIRECTIONS
    51700 : "Yer already there.",
    51701 : "I don't know.",
    51702 : "Yer on the wrong island.",
    51703 : "That's in town.",
    51704 : "Look just outside of town.",
    51705 : "Ye will have to search through the jungle.",
    51706 : "Deeper inland.",
    51707 : "Oh, that be by the coast.",

    # Insults
    50200 : "Bilge rat!",
    50201 : "Scurvy dog!",
    50202 : "See ye in Davy Jones locker!",
    50203 : "Scoundrel!",
    50204 : "Landlubber!",
    50205 : "Addle-minded fool!",
    50206 : "You need a sharp sword and sharper wits.",
    50207 : "Ye be one doubloon short of a full hull mate!",
    50208 : "Watch yer tongue or I'll pickle it with sea salt!",
    50209 : "Touch me loot and you get the boot!",
    50210 : "The horizon be as empty as yer head.",
    50211 : "You're a canvas shy of a full sail, aren't ye mate?",

    # Compliments
    50300 : "Fine shooting mate!",
    50301 : "A well placed blow!",
    50302 : "Nice shot!",
    50303 : "Well met!",
    50304 : "We showed them!",
    50305 : "Yer not so bad yerself!",
    50306 : "A fine plunder haul!",

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
    60100 : "Hi!",
    60101 : "Hello!",
    60102 : "Hey!",
    60103 : "Yo!",
    60104 : "Hi everybody!",
    60105 : "How are you doing?",
    60106 : "What's Up?",

    # Bye
    60200 : "Bye!",
    60201 : "Later!",
    60202 : "See ya!",
    60203 : "I'll be right back.",
    60204 : "I need to go.",

    # Happy
    60300 : ":-)",
    60301 : "Cool!",
    60302 : "Yeah!",
    60303 : "Ha ha!",
    60304 : "Sweet!",
    60305 : "Yeah!",
    60306 : "That rocks!",
    60307 : "Funky!",
    60308 : "Awesome!",
    60309 : "Wow!",

    # Sad
    60400 : ":-(",
    60401 : "Doh!",
    60402 : "Aw man!",
    60403 : "Ouch!",
    60404 : "Bummer!",

    # Places
    60500 : "Where are you?",
    60501 : "Let's go to the Gateway Store.",
    60502 : "Let's go to the Disco Hall.",
    60503 : "Let's go to Toontown.",
    60504 : "Let's go to Pirates of the Carribean.",

    # Animated Emotes
    60505 : "Flip coin",
    60506 : "Dance",
    60507 : "Chant 1",
    60508 : "Chant 2",
    60509 : "Dance a jig",
    60510 : "Sleep",
    60511 : "Flex",
    60512 : "Play Lute",
    60513 : "Play Flute",
    60514 : "Frustrated",
    60515 : "Searching",
    60516 : "Yawn",
    60517 : "Kneel",
    60518 : "Sweep",
    60519 : "Primp",
    60520 : "Yawn",
    60521 : "Dance",
    60522 : "No",
    60523 : "Yes",
    60524 : "Laugh",
    60525 : "Clap",
    60526 : "Smile",
    60527 : "Anger",
    60528 : "Fear",
    60529 : "Sad",
    60530 : "Celebrate",
    60668 : "Celebrate",
    60669 : "Sleep",
    60602 : "Angry",
    60614 : "Clap",
    60622 : "Scared",
    60640 : "Laugh",
    60652 : "Sad",
    60657 : "Smile",
    60664 : "Wave",
    60665 : "Wink",
    60666 : "Yawn",
    60669 : "Sleep",
    60670 : "Dance",
    60676 : "Flirt",
    60677 : "Zombie dance",
    60678 : "Noisemaker",

    # Valentines day emote string options
    60671 : "Hello, I'm a Pirate, and I'm here to steal your heart.",
    60672 : "I just found the treasure I've been searching for.",
    60673 : "If you were a booger, I'd pick you first.",
    60674 : "Come to Tortuga often?",
    60675 : "Do you have a map? I just keep getting lost in your eyes.",

    65000 : "Yes",
    65001 : "No",
    
    60909 : "Check Hand",
    
    }

SpeedChatStaticText = SpeedChatStaticTextCommon

# Emote IDs - These are used in SC to determine if a msg is a animated emote
Emotes_Root = "EMOTES"
Emotes_Dances = "Dances"
Emotes_General = "General"
Emotes_Music = "Music"
Emotes_Expressions = "Emotions"
Emote_ShipDenied = "Cannot emote while sailing."
Emote_MoveDenied = "Cannot emote while moving." 
Emote_CombatDenied = "Cannot emote while in combat."
Emote_CannonDenied = "Cannot emote while using a cannon."
Emote_SwimDenied = "Cannot emote while swimming."
Emote_ParlorGameDenied = "Cannot emote while playing a parlor game."
Emotes = (60505, 60506, 60509, 60510, 60511, 60516, 60519, 60520, 60521, 60522, 60523, 60524, 60525, 60526, 60527, 60528, 60529, 60530, 60602, 60607, 60611, 60614, 60615, 60622, 60627, 60629, 60632, 60636, 60638, 60640, 60644, 60652, 60654, 60657, 60658, 60663, 60664, 60665, 60666, 60668, 60669, 60612, 60661, 60645, 60629, 60641, 60654, 60630, 60670, 60633,
          # Valentines Day Emote
          60676,
          # Halloween Emote
          60677,
          # Yes/No
          65000, 65001,
          # Kneel
          60517,
          # New Years Emote
          60678,
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
    10 : "Está bien.",
    20 : "¿Porque no?",
    30 : "¡Naturalmente!",
    40 : "Esa es la manera de hacerlo.",
    50 : "¡Exacto!",
    60 : "¿Que pasa?",
    70 : "¡Por supuesto!",
    80 : "Bingo!",
    90 : "Debes de estar bromeando...",
    100 : "Me suena bien.",
    110 : "¡Qué locura!",
    120 : "¡Impresionante!",
    130 : "¡Por amor de Dios!",
    140 : "No te preocupes.",
    150 : "¡Grrrr!",
    160 : "¿Alguna novedad?",
    170 : "¡Eh, eh, eh!",
    180 : "Hasta mañana.",
    190 : "Hasta otra vez.",
    200 : "Nos vemos.",
    210 : "Hasta la vista.",
    220 : "Tengo que irme pronto.",
    230 : "¡No sé nada de esto!",
    240 : "¡Largo de aquí!",
    250 : "¡Ay! ¡Cómo duele!",
    260 : "¡Te tengo!",
    270 : "¡Por favor!",
    280 : "¡Mil gracias!",
    290 : "¡Me encanta cómo vas!",
    300 : "¡Perdona!",
    310 : "¿Te puedo ayudar?",
    320 : "¡A eso me refería!",
    330 : "Si no aguantas el calor, no te acerques al horno.",
    340 : "¡Truenos y relampagos!",
    350 : "¡Pero qué cosa más especial!",
    360 : "¡Deja de enredar!",
    370 : "¿Te ha comido la lengua el gato?",
    380 : "¡Estás metido en un buen lío!",
    390 : "Pero mira lo que tenemos aquí...",
    400 : "Tengo que ir a ver a un dibu.",
    410 : "¡No te enfades!",
    420 : "¡No seas gallina!",
    430 : "Eres un blanco fácil.",
    440 : "¡Lo que sea!",
    450 : "¡Totalmente!",
    460 : "¡Estupendo!",
    470 : "¡Fantástico!",
    480 : "¡Por supuesto!",
    490 : "¡A que no me pillas!",
    500 : "Primero tienes que curarte.",
    510 : "Necesitas más puntos de risa.",
    520 : "Vuelvo en un momento.",
    530 : "Tengo hambre.",
    540 : "¡Sí, claro!",
    550 : "Tengo sueño.",
    560 : "¡Estoy listo!",
    570 : "Estoy aburrido.",
    580 : "¡Me encanta!",
    590 : "¡Qué emocionante!",
    600 : "¡Salta!",
    610 : "¿Tienes bromas?",
    620 : "¿Qué pasa?",
    630 : "Poco a poco.",
    640 : "Despacito y buena letra.",
    650 : "¡Gol!",
    660 : "¡Prepararse!",
    670 : "¡Listos!",
    680 : "¡Ya!",
    690 : "¡Vamos por aquí!",
    700 : "¡Has ganado!",
    710 : "Yo voto que sí.",
    720 : "Yo voto que no.",
    730 : "Cuenta conmigo.",
    740 : "No cuentés conmigo.",
    750 : "Quédate aquí, vuelvo enseguida.",
    760 : "¡Qué rápido!",
    770 : "¿Has visto eso?",
    780 : "¿A qué huele eso?",
    790 : "¡Qué hediondo!",
    800 : "No me importa.",
    810 : "Justo lo que el medico ordenó.",
    820 : "¡Que empiece la fiesta!",
    830 : "¡Por aquí todos!",
    840 : "¿Qué pasa?",
    850 : "El cheque está en el correo.",
    860 : "¡Te he oído!",
    870 : "¿Me estas hablando?",
    880 : "Gracias, estaré aquí toda la semana.",
    890 : "Mmm.",
    900 : "Yo me ocupo de éste.",
    910 : "¡Lo tengo!",
    920 : "¡Es mio!",
    930 : "Por favor, toma esto.",
    940 : "No te acerques; esto puede ser peligroso.",
    950 : "¡No te preocupes!",
    960 : "¡Vaya!",
    970 : "¡Guau!",
    980 : "¡Uuuuuu!",
    990 : "¡Todos a bordo!",
    1000 : "¡Que fantastico!",
    1010 : "La curiosidad mató al gato.",
    # Series 2
    2000 : "¡Vamos, no seas infantil!",
    2010 : "¡Qué alegría de verte!",
    2020 : "No faltaba más.",
    2030 : "No te habrás metido en líos, ¿verdad?",
    2040 : "¡Mejor tarde que nunca!",
    2050 : "¡Bravo!",
    2060 : "No, en serio, amigos...",
    2070 : "¿Te animas?",
    2080 : "¡Nos vemos luego!",
    2090 : "¿Has cambiado de idea?",
    2100 : "¡Si lo quieres, ven a cogerlo!",
    2110 : "¡Ay, dios mío!",
    2120 : "Encantado de conocerte.",
    2130 : "¡No hagas nada que yo no haría!",
    2140 : "¡Ni se te ocurra!",
    2150 : "¡No tires la toalla!",
    2160 : "Mejor espera sentado.",
    2170 : "No preguntes.",
    2180 : "Para ti todo es muy fácil.",
    2190 : "¡Ya está bien!",
    2200 : "¡Estupendo!",
    2210 : "¡Vaya, qué casualidad!",
    2220 : "¡Déjame en paz!",
    2230 : "Y yo que me alegro.",
    2240 : "Venga, que me voy a divertir un rato.",
    2250 : "¡A por todas!",
    2260 : "¡Bien hecho!",
    2270 : "¡Qué alegría de verte!",
    2280 : "Me tengo que pirar.",
    2290 : "Me tengo que largar.",
    2300 : "Espera.",
    2310 : "Un momento.",
    2320 : "¡Disfruta como un loco!",
    2330 : "¡Diviértete!",
    2340 : "Oye, que no tengo todo el día…",
    2350 : "¡Un momento!",
    2360 : "¡Qué pamplinas!",
    2370 : "¡No me lo puedo creer!",
    2380 : "Lo dudo mucho.",
    2390 : "Te debo una.",
    2400 : "Te oigo perfectamente.",
    2410 : "Creo que sí.",
    2420 : "Creo que deberías pasar.",
    2430 : "Ya lo podía haber dicho yo.",
    2440 : "Ni se te ocurra.",
    2450 : "¡Por mí, encantado!",
    2460 : "Estoy ayudando a mi amigo.",
    2470 : "Me quedo toda la semana.",
    2480 : "¡Imagínate!",
    2490 : "Justo a tiempo...",
    2500 : "Todavía no ha acabado la cosa.",
    2510 : "Estaba pensando en voz alta.",
    2520 : "No te pierdas; llama de vez en cuando.",
    2530 : "¡Garbanzos en remojo!",
    2540 : "¡Muévete!",
    2550 : "Ponte cómodo.",
    2560 : "En otro momento, quizás.",
    2570 : "¿Interrumpo?",
    2580 : "¡Menuda choza!",
    2590 : "Bueno, una charla muy agradable.",
    2600 : "Sin lugar a dudas.",
    2610 : "¡No me digas!",
    2620 : "Ni por asomo.",
    2630 : "¡Qué cara!",
    2640 : "Por mí, vale.",
    2650 : "¡Vale!",
    2660 : "¡Sonrían, por favor!",
    2670 : "¿Qué?",
    2680 : "¡Pachán!",
    2690 : "Tómatelo con calma.",
    2700 : "¡Chao!",
    2710 : "Gracias, pero mejor no.",
    2720 : "¡Esto es el acabóse!",
    2730 : "Qué bueno.",
    2740 : "¡Justo lo que necesitaba!",
    2750 : "¡"+TheCogs+" nos invaden!",
    2760 : "¡Arrivederci!",
    2770 : "¡Cuidado!",
    2780 : "¡Muy bien!",
    2790 : "¿Qué se cuece?",
    2800 : "¿Qué pasa?",
    2810 : "Por mí, vale.",
    2820 : "Sí, señor.",
    2830 : "Por supuesto.",
    2840 : "Haz el cálculo.",
    2850 : "¿Ya te vas?",
    2860 : "¡No me hagas reír!",
    2870 : "Vete por la derecha.",
    2880 : "¡Despídete de este mundo!",
    # Series 3
    3000 : "Lo que tú digas.",
    3010 : "¿Molesto?",
    3020 : "La cuenta, por favor.",
    3030 : "Yo no estaría tan seguro.",
    3040 : "No te voy a decir que no.",
    3050 : "Tampoco te partas la crisma…",
    3060 : "Lo sabes muy bien.",
    3070 : "Yo, como si no estuviera.",
    3080 : "¡Eureka!",
    3090 : "¡Imagínate!",
    3100 : "¡Ni lo sueñes!",
    3110 : "¿Vienes conmigo?",
    3120 : "¡Muy bien!",
    3130 : "¡Por dios!",
    3140 : "¡Que disfrutes!",
    3150 : "¡Ánimo!",
    3160 : "Otra vez.",
    3170 : "¡Toma ya!",
    3180 : "¡Ahí tienes!",
    3190 : "Eso creo.",
    3200 : "Ni de broma.",
    3210 : "Luego te contesto.",
    3220 : "Soy todo oídos.",
    3230 : "Estoy ocupado.",
    3240 : "¡Que no estoy de broma!",
    3250 : "Me he quedado de una piedra.",
    3260 : "Venga, ánimo.",
    3270 : "¡Mantenme al corriente!",
    3280 : "¡Lluvia de tartas!",
    3290 : "Lo mismo digo.",
    3300 : "¡Andando, que es gerundio!",
    3310 : "El tiempo vuela.",
    3320 : "Sin comentarios.",
    3330 : "¡Así se habla!",
    3340 : "Por mí, bien.",
    3350 : "Encantado.",
    3360 : "Vale.",
    3370 : "Claro que sí.",
    3380 : "Muchísimas gracias.",
    3390 : "Así me gusta.",
    3400 : "¡Así se hace!",
    3410 : "Me voy para el catre.",
    3420 : "¡Hazme caso!",
    3430 : "Hasta la próxima.",
    3440 : "¡Espera un momentito!",
    3450 : "¡Así se hace!",
    3460 : "¿Cómo tú por aquí?",
    3470 : "¿Qué ha pasado?",
    3480 : "¿Ahora qué?",
    3490 : "Después de ti.",
    3500 : "Vete por la izquierda.",
    3510 : "¡Eso es lo que tú querrías!",
    3520 : "¡Date por muerto!",
    3530 : "¡Menudo eres tú!",

    # Series 4
    4000 : "Toons rule!",
    4010 : "Cogs drool!",
    4020 : "Toons of the world unite!",
    4030 : "Howdy, partner!",
    4040 : "Much obliged.",
    4050 : "Get along, little dogie.",
    4060 : "I'm going to hit the hay.",
    4070 : "I'm chomping at the bit!",
    4080 : "This town isn't big enough for the two of us!",
    4090 : "Saddle up!",
    4100 : "Draw!!!",
    4110 : "There's gold in them there hills!",
    4120 : "Happy trails!",
    4130 : "This is where I ride off into the sunset...",
    4140 : "Let's skedaddle!",
    4150 : "You got a bee in your bonnet?",
    4160 : "Lands sake!",
    4170 : "Right as rain.",
    4180 : "I reckon so.",
    4190 : "Let's ride!",
    4200 : "Well, go figure!",
    4210 : "I'm back in the saddle again!",
    4220 : "Round up the usual suspects.",
    4230 : "Giddyup!",
    4240 : "Reach for the sky.",
    4250 : "I'm fixing to.",
    4260 : "Hold your horses!",
    4270 : "I can't hit the broad side of a barn.",
    4280 : "Y'all come back now.",
    4290 : "It's a real barn burner!",
    4300 : "Don't be a yellow belly.",
    4310 : "Feeling lucky?",
    4320 : "What in Sam Hill's goin' on here?",
    4330 : "Shake your tail feathers!",
    4340 : "Well, don't that take all.",
    4350 : "That's a sight for sore eyes!",
    4360 : "Pickins is mighty slim around here.",
    4370 : "Take a load off.",
    4380 : "Aren't you a sight!",
    4390 : "That'll learn ya!",
    # Series 6
    6000 : "I want candy!",
    6010 : "I've got a sweet tooth.",
    6020 : "That's half-baked.",
    6030 : "Just like taking candy from a baby!",
    6040 : "They're cheaper by the dozen.",
    6050 : "Let them eat cake!",
    6060 : "That's the icing on the cake.",
    6070 : "You can't have your cake and eat it too.",
    6080 : "I feel like a kid in a candy store.",
    6090 : "Six of one, half a dozen of the other...",
    6100 : "Let's keep it short and sweet.",
    6110 : "Keep your eye on the doughnut not the hole.",
    6120 : "That's pie in the sky.",
    6130 : "But it's wafer thin.",
    6140 : "Let's gum up the works!",
    6150 : "You're one tough cookie!",
    6160 : "That's the way the cookie crumbles.",
    6170 : "Like water for chocolate.",
    6180 : "Are you trying to sweet talk me?",
    6190 : "A spoonful of sugar helps the medicine go down.",
    6200 : "You are what you eat!",
    6210 : "Easy as pie!",
    6220 : "Don't be a sucker!",
    6230 : "Sugar and spice and everything nice.",
    6240 : "It's like butter!",
    6250 : "The candyman can!",
    6260 : "We all scream for ice cream!",
    6270 : "Let's not sugar coat it.",
    6280 : "Knock knock...",
    6290 : "Who's there?",
    # Series 7
    7000 : "Quit monkeying around!",
    7010 : "That really throws a monkey-wrench in things.",
    7020 : "Monkey see, monkey do.",
    7030 : "They made a monkey out of you.",
    7040 : "That sounds like monkey business.",
    7050 : "I'm just monkeying with you.",
    7060 : "Who's gonna be monkey in the middle?",
    7070 : "That's a monkey off my back...",
    7080 : "This is more fun than a barrel of monkeys!",
    7090 : "Well I'll be a monkey's uncle.",
    7100 : "I've got monkeys on the brain.",
    7110 : "What's with the monkey suit?",
    7120 : "Hear no evil.",
    7130 : "See no evil.",
    7140 : "Speak no evil.",
    7150 : "Let's make like a banana and split.",
    7160 : "It's a jungle out there.",
    7170 : "You're the top banana.",
    7180 : "Cool bananas!",
    7190 : "I'm going bananas!",
    7200 : "Let's get into the swing of things!",
    7210 : "This place is swinging!",
    7220 : "I'm dying on the vine.",
    7230 : "This whole affair has me up a tree.",
    7230 : "Let's make like a tree and leave.",
    7240 : "Jellybeans don't grow on trees!",

    # Halloween
    10000 : "Esto es una ciudad fantasma.",
    10001 : "¡Bonito disfraz!",
    10002 : "Creo que esto está embrujado.",
    10003 : "¡Chuches o venganza!",
    10004 : "¡Buuu!",
    10005 : "¡Feliz embrujamiento!",
    10006 : "¡Feliz Halloween!",
    10007 : "Es la hora de convertirme en una calabaza.",
    10008 : "¡Fantasmástico!",
    10009 : "¡Espeluznante!",
    10010 : "¡Qué miedo da!",
    10011 : "¡Odio las arañas!",
    10012 : "¿Has oído eso?",
    10013 : "¡Tienes menos posibilidades que un fantasma!",
    10014 : "¡Me has asustado!",
    10015 : "¡Qué susto!",
    10016 : "¡Qué monstruoso!",
    10017 : "Eso ha sido muy raro...",
    10018 : "¿Habrán esqueletos en el armario?",
    10019 : "¿Te he asustado?",

    # Fall Festivus
    11000 : "Anda, que estás más relleno que un pavo en Navidad",
    11001 : "¡No me vengas con pucheros!",
    11002 : "¡Brrr!",
    11003 : "¡Tranqui, colega!",
    11004 : "¡Ven a por ello!",
    11005 : "Qué pavo eres.",
    11006 : "¡glu, glu, glu!",
    11007 : "¡Felices vacaciones!",
    11008 : "¡Feliz año nuevo!",
    11009 : "Sé bueno que los Reyes Magos lo ven todo.",
    11010 : "¡Feliz pavo!",
    11011 : "¡No te atragantes con las uvas!",
    11012 : "Estás más ilocalizable que Papá Noel en Nochebuena.",
    11013 : "Va más rápido que las campanadas de Fin de Año.",
    11014 : "¡Que nieve!",
    11015 : "Trae para acá.",
    11016 : "¡Felices Fiestas!",
    11017 : "Estoy más mosqueado que un pavo oyendo panderetas.",
    11018 : "¡Nevando voy, nevando vengo!",
    11019 : "¡Te vas a arrepentir, tronco!",
    11020 : "Have a Wonderful Winter!",

    # Valentines
    12000 : "Si el mundo fuera un pañuelo…, serías mi moco preferido.",
    12001 : "¡Te quieroooooooo!",
    12002 : "¡Feliz día de San Valentín!",
    12003 : "Oooh, qué bonito.",
    12004 : "Me gustas un montón.",
    12005 : "Amor incondicional.",
    12006 : "¡Te quiero! ¿Me oyes?",
    12007 : "¿Quedamos por San Valentín?",
    12008 : "Gracias, mi vida.",
    12009 : "Gracias, cariñín.",
    12010 : "Qué guapo eres.",
    12011 : "Qué guapa eres.",
    12012 : "¡Estupendo!",
    12013 : "¡Qué bien!",
    12014 : "Las rosas son rojas...",
    12015 : "Las violetas azuladas...",
    12016 : "¡Qué bonito!",
    12050 : "I LOVE busting Cogs!",
    12051 : "You're dynamite!",
    12052 : "I only have hypno-eyes for you!",
    12053 : "You're sweeter than a jellybean!",
    12054 : "I'd LOVE for you to come to my ValenToon's party!",

    # St. Patricks Day
    13000 : "Llegó el verano y los mosquitos mueren entre aplausos.",
    13001 : "¡Feliz veraneo!",
    13002 : "¡Con las chanclas y a la playa!",
    13003 : "Si la piscina es honda… ¿El mar es toyota?",
    13004 : "Tengo más problemas que las Vacaciones Santillana.",
    13005 : "Buen viaje, y si el avión viene demorado, tú ponte “deverde”.",
    13006 : "¡Te repites más que Verano Azul!",
    13007 : "¡Que disfrutes del sol!",

    # Summer Estate Party phrases (seasonal catalog)
    14000 : "Let's have a summer Estate party!",
    14001 : "It's party time!",
    14002 : "Last one in the pond is a rotten Cog!",
    14003 : "Group Doodle training time!",
    14004 : "Doodle training time!",
    14005 : "Your Doodle is cool!",
    14006 : "What tricks can your Doodle do?",
    14007 : "Time for Cannon Pinball!",
    14008 : "Cannon Pinball rocks!",
    14009 : "Your Estate rocks!",
    14010 : "Your Garden is cool!",
    14011 : "Your Estate is cool!",




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

# NamePanel.py - PickAName/TypeAName
RandomButton = "Al azar"
TypeANameButton = "Escribe un nombre"
PickANameButton = "Juego de los nombres"
NameShopSubmitButton = "Enviar"
RejectNameText = "Ese nombre no está permitido. Inténtalo de nuevo."
WaitingForNameSubmission = "Se está enviando tu nombre..."

NameShopNameMaster = "NameMaster_castillian.txt"
NameShopPay = "¡Suscríbete ya!"
NameShopPlay = "Prueba gratuita"
NameShopOnlyPaid = "Solo los usuarios abonados\npueden poner nombre a sus dibus.\nHasta que te suscribas,\ntu nombre será\n"
NameShopContinueSubmission = "Continuar envío"
NameShopChooseAnother = "Elegir otro nombre"
NameShopToonCouncil = "El Consejo Dibu\nrevisará tu\nnombre.  " + \
                      "La revisión puede\ntardar unos días.\nMientras esperas,\ntu nombre será\n "
PleaseTypeName = "Escribe tu nombre:"
ToonAlreadyExists = "¡Ya tienes un dibu llamado %s!"
AllNewNames = "All new names\nmust be approved\nby the Name Council."
NameShopNameRejected = "El nombre que \nenviaste fue \nrechazado."
NameShopNameAccepted = "¡Felicitaciones!\nEl nombre que \nenviaste fue \naceptado."
NoPunctuation = "¡No puedes usar signos de puntuación en tu nombre!"
PeriodOnlyAfterLetter = "Tu nombre puede incluir un punto, pero solo después de una letra."
ApostropheOnlyAfterLetter = "Tu nombre puede incluir un apóstrofo, pero solo después de una letra."
NoNumbersInTheMiddle = "Es posible que los números no aparezcan si están en medio de una palabra."
ThreeWordsOrLess = "Tu nombre debe tener un máximo de tres palabras."
CopyrightedNames = (
    "mickey",
    "mickey mouse",
    "mickeymouse",
    "minnie",
    "minnie mouse",
    "minniemouse",
    "donald",
    "pato donald",
    "patodonald",
    "pluto",
    "goofy",
    )

# NameCheck.py
NCTooShort = 'Ese nombre es demasiado corto.'
NCNoDigits = 'Tu nombre no puede contener números.'
NCNeedLetters = 'Todas las palabras de tu nombre deben contener letras.'
NCNeedVowels = 'Todas las palabras de tu nombre deben contener vocales.'
NCAllCaps = 'Tu nombre no puede estar por completo en mayúsculas.'
NCMixedCase = 'Ese nombre tiene demasiadas mayúsculas.'
NCBadCharacter = "Tu nombre no puede contener el caracter '%s'"
NCGeneric = 'Lo siento, ese nombre no sirve.'
NCTooManyWords = 'Tu nombre no puede tener más de cuatro palabras.'
NCDashUsage = ("Solo puedes usar los guiones para unir dos palabras "
               "(como en \"Bu-bu\").")
NCCommaEdge = "Tu nombre no puede comenzar ni terminar con una coma."
NCCommaAfterWord = "No puedes comenzar una palabra con una coma."
NCCommaUsage = ('Ese nombre no emplea las comas correctamente. Las comas deben '
                'unir dos palabras, como en el nombre \"Dr. Pato, cirujano\"". '
                'Además, las comas deben ir seguidas por un espacio.')
NCPeriodUsage = ('Ese nombre no emplea los puntos correctamente. Sólo se permiten '
                 'los puntos en palabras como \"Sr.\", \"Sra.\", \"J.T.\", etc.')
NCApostrophes = 'Ese nombre tiene demasiados apóstrofos.'

# AvatarDetailPanel.py
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = "Buscando datos de %s."
AvatarDetailPanelFailedLookup = "Imposible obtener datos de %s."
AvatarDetailPanelPlayer = "Jugador: %(player)s\nMundo: %(world)s\nLugar: %(location)s"
AvatarDetailPanelOnline = "Distrito: %(district)s\nLugar: %(location)s"
AvatarDetailPanelOffline = "Distrito: sin conexión\nLocalidad: sin conexión"

# AvatarPanel.py
AvatarPanelFriends = "Amigos"
AvatarPanelWhisper = "Susurrar"
AvatarPanelSecrets = "Secretos"
AvatarPanelGoTo = "Ir a"
AvatarPanelIgnore = "Ignorar"
AvatarPanelStopIgnoring = "Dejar de ignorar"
#AvatarPanelCogDetail = "Dept: %s\nNivel: %s\n"
AvatarPanelCogLevel = "Nivel: %s"
AvatarPanelCogDetailClose = lClose

# TeleportPanel.py
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Intentando ir a %s."
TeleportPanelNotAvailable = "%s está ocupado en este momento. Inténtalo más tarde."
TeleportPanelIgnored = "%s te está ignorando."
TeleportPanelNotOnline = "%s no está conectado en este momento."
TeleportPanelWentAway = "%s se marchó."
TeleportPanelUnknownHood = "¡No sabes cómo llegar a %s!"
TeleportPanelUnavailableHood = "%s no está disponible en este momento. Inténtalo más tarde."
TeleportPanelDenySelf = "¡No puedes ir tú solo!"
TeleportPanelOtherShard = "%(avName)s está en el distrito %(shardName)s, y tú estás en el distrito %(myShardName)s. ¿Quieres cambiarte a %(shardName)s?"

KartRacingMenuSections = [
 -1,
 "PLACES",
 "COURSES",
 "PISTES",
 "COMPLIMENTS",
 "MOQUERIE"
]

AprilToonsMenuSections = [
 -1,
 "GREETINGS",
 "PLAYGROUNDS",
 "CHARACTERS",
 "ESTATES"
]

SillyHolidayMenuSections = [
-1,
"WORLD",
"BATTLE",
]

CarolMenuSections = [
-1,
]

VictoryPartiesMenuSections = [
 -1,
 "PARTY",
 "ITEMS",
]

GolfMenuSections = [
 -1,
 "COURSES",
 "ASTUCES",
 "COMMENTAIRES",
]

BoardingMenuSections = [
"GROUP",
"Let's go to...",
"We're going to...",
-1,
]

SellbotNerfMenuSections = [
-1,
"GROUPING",
"SELLBOT TOWERS/VP",
]

LawbotNerfMenuSections = [
-1,
"GROUPING",
"COURTHOUSE/CJ",
]

JellybeanJamMenuSections = [
"GET JELLYBEANS",
"SPEND JELLYBEANS",
]

WinterMenuSections = [
"CAROLING",
-1
]

HalloweenMenuSections = [
-1
]

SingingMenuSections = [
-1
]

WhiteListMenu = [
-1,
"LISTEBLANCHE"
]

SellbotInvasionMenuSections = [
-1
]

SellbotFieldOfficeMenuSections = [
-1,
"STRATEGY"
]

IdesOfMarchMenuSections = [
-1
]

# TTAccount.py
# Fill in %s with phone number from account server
TTAccountCallCustomerService = "Para ponerte en contacto con el Servicio de atención al cliente, llama al %s."
# Fill in %s with phone number from account server
TTAccountCustomerServiceHelp = "\n\nSi necesitas ayuda, ponte en contacto con el Servicio de atención al cliente, en el número %s."
TTAccountIntractibleError = "Se produjo un error."
