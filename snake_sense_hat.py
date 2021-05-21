from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.low_light = True
#qui metto dei colori che andro a usare 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
NO_LED = (0, 0, 0)

#qui metto un count down per dopo che una partita viene finita
def five_img():
    W = WHITE
    O = NO_LED
    img = [O, O, W, W, W, W, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, W, W, W, W, O, O,]
    return img


def four_img():
    W = WHITE
    O = NO_LED
    img = [O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, O, W, O, O, O,]
    return img


def three_img():
    W = WHITE
    O = NO_LED
    img = [O, O, W, W, W, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, W, W, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, W, W, W, W, O, O,]
    return img


def two_img():
    W = WHITE
    O = NO_LED
    img = [O, O, W, W, W, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, W, W, W, O, O,]
    return img


def one_img():
    W = WHITE
    O = NO_LED
    img = [O, O, O, O, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, W, O, W, O, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, W, W, W, O, O,]
    return img


images = [five_img, four_img, three_img, two_img, one_img]

UNA_PAUSA = 0.70
UN_PO_PIU_PRIMA_DEL_BORDO_A_DESTRA = 0
UN_PO_PIU_PRIMA_DEL_BORDO = 7
VAI_INDIETRO_QUANDO_SEI_SUL_BORDO = 8

while True:
    # metto delle variabili importanti in caso lo dimenticassi
    gameOverFlag = False
    snakeisbigger = False
    generatefood = False
    delay = 0.5
    delaydecrease = -0.02

    # qui comincia quel count down e richiamo la variabile images che ora fa un bell efetto
    for img in images:
        sense.set_pixels(img())
        time.sleep(UNA_PAUSA)

    # una posizione default per il serpente forse dovrei smettere di sctivere tuttu questi commenti
    posX = [3]
    posY = [6]

    # questa parte serve per mettere in posizioni random il cibo o pallini rossi 
    while True:
        foodX = random.randint(0, 7)
        foodY = random.randint(0, 7)
        if foodX != posX[0] or foodY != posY[0]:
            break

    # questo come la posizione default e la direzione in cui si dirige default anche se non mi piace questa 
    # ps alen cambia la posizione e trovane una migliore quando avrai tempo 
    # si mi sono totalmente dimenticato di cambiare sta posizione va be lo faccio domani
    x = 0
    y = -1


    # qui comincia il vero e proprio gioco non ho nemmeno cominciato e sto gia bestammiando magnifico
    # comunque questo e il loop del gioco
    while not gameOverFlag:
        # questo è un piccolo ceck se mangia ste palline o no
        if foodX == posX[0] and foodY == posY[0]:
            snakeisbigger = True
            generatefood = True
            #questa parte diminuiscie il delay ogni volta che mangia qualcosa
            delay += delaydecrease

        # questo serve a capire se ti mangi da solo perche scrivo sti commenti tanto me lo ricordo va be
        #forse passo al inglese bho non so nemmeno se funziona
        #update sta roba non so perche ma funziona e non ho intenzione di toccarla se funziona funziona
        for i in range(1, len(posX)):
            if posX[i] == posX[0] and posY[i] == posY[0]:
                gameOverFlag = True

        # proff non mi amazzi dovevo mettere questo break come faccievo mettevo un or nell while dell inizio del loop
        # serve per capire se sono morto o meno
        if gameOverFlag:
            break

        # ok dopo 3 ore di documentazione credo di aver capito come funziona sta roba ora dovrebbe teoricamente
        # funzionare credo ...
        # update: tutto funzionante ^^ oggi sono proprio felicie 
        events = sense.stick.get_events()
        for event in events:
            if event.direction == "left" and x != 1:
                x = -1
                y = 0
                
            elif event.direction == "right" and x != -1:
                x = 1
                y = 0
                
            elif event.direction == "up" and y != 1:
                y = -1
                x = 0
                
            elif event.direction == "down" and y != -1:
                y = 1
                x = 0
                

        # quanto il serpente mangia qualcosa diventa piu grande giusto  ecco questa è la funzione di questa parte del codice
        if snakeisbigger:
            snakeisbigger = False
            posX.append(0)
            posY.append(0)

        # questo è il continuo movimento del serpente mi ci è voluto un po per capire sto len
        for i in range((len(posX) - 1), 0, -1):
            posX[i] = posX[i - 1]
            posY[i] = posY[i - 1]

        posX[0] += x
        posY[0] += y

        # qui mette i bordi della mappa quindi se vai a un limite ti fa ritornare indietro
        if posX[0] > UN_PO_PIU_PRIMA_DEL_BORDO:
            posX[0] -= VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        elif posX[0] < UN_PO_PIU_PRIMA_DEL_BORDO_A_DESTRA:
            posX[0] += VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        if posY[0] > UN_PO_PIU_PRIMA_DEL_BORDO:
            posY[0] -= VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        elif posY[0] < UN_PO_PIU_PRIMA_DEL_BORDO_A_DESTRA:
            posY[0] += VAI_INDIETRO_QUANDO_SEI_SUL_BORDO

        # questo serve a far spawnare cibo in posizioni random
        if generatefood:
            generatefood = False
            retryFlag = True
            while retryFlag:
                foodX = random.randint(0, 7)
                foodY = random.randint(0, 7)
                retryFlag = False
                for x, y in zip(posX, posY):
                    if x == foodX and y == foodY:
                        retryFlag = True
                        break

        # update matrix:
        sense.clear()
        sense.set_pixel(foodX, foodY, RED)
        for x, y in zip(posX, posY):
            sense.set_pixel(x, y, GREEN)

        # snake speed (game loop delay):
        time.sleep(delay)
