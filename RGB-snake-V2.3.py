

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
    gameover = False
    snakegrow = False
    randomfood = False
    movementdelay = 0.5
    movementdecrease = -0.02

    # qui comincia quel count down e richiamo la variabile images che ora fa un bell efetto
    for img in images:
        sense.set_pixels(img())
        time.sleep(UNA_PAUSA)

    # una posizione default per il serpente forse dovrei smettere di sctivere tuttu questi commenti
    snakePosX = [3]
    snakePosY = [6]

    # questa parte serve per mettere in posizioni random il cibo o pallini rossi 
    while True:
        foodPosX = random.randint(0, 7)
        foodPosY = random.randint(0, 7)
        if foodPosX != snakePosX[0] or foodPosY != snakePosY[0]:
            break

    # questo come la posizione default e la direzione in cui si dirige default anche se non mi piace questa 
    # ps alen cambia la posizione e trovane una migliore quando avrai tempo 
    # si mi sono totalmente dimenticato di cambiare sta posizione va be lo faccio domani
    movementX = 0
    movementY = -1


    # qui comincia il vero e proprio gioco non ho nemmeno cominciato e sto gia bestammiando magnifico
    # comunque questo e il loop del gioco
    while not gameover:

              

        # questo serve a capire se ti mangi da solo perche scrivo sti commenti tanto me lo ricordo va be
        #forse passo al inglese bho non so nemmeno se funziona
        #update sta roba non so perche ma funziona e non ho intenzione di toccarla se funziona funziona
        for i in range(1, len(snakePosX)):
            if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
                gameover = True

        # proff non mi amazzi dovevo mettere questo break come faccievo mettevo un or nell while dell inizio del loop
        # serve per capire se sono morto o meno
        if gameover:
            break

        # ok dopo 3 ore di documentazione credo di aver capito come funziona sta roba ora dovrebbe teoricamente
        # funzionare credo ...
        # update: tutto funzionante ^^ oggi sono proprio felicie 
        events = sense.stick.get_events()
        for event in events:
            if event.direction == "left" and movementX != 1:
                movementX = -1
                movementY = 0
                
            elif event.direction == "right" and movementX != -1:
                movementX = 1
                movementY = 0
                
            elif event.direction == "up" and movementY != 1:
                movementY = -1
                movementX = 0
                
            elif event.direction == "down" and movementY != -1:
                movementY = 1
                movementX = 0
                


        
        
        
        # quanto il serpente mangia qualcosa diventa piu grande giusto  ecco questa è la funzione di questa parte del codice
        
        # ho cambiato un po tutto e ho spostato il codice non riesco piu a trovarla ^^


        # questo è il continuo movimento del serpente mi ci è voluto un po per capire sto len
        for i in range((len(snakePosX) - 1), 0, -1):
            snakePosX[i] = snakePosX[i - 1]
            snakePosY[i] = snakePosY[i - 1]

        snakePosX[0] += movementX
        snakePosY[0] += movementY

        # qui mette i bordi della mappa quindi se vai a un limite ti fa ritornare indietro
        if snakePosX[0] > UN_PO_PIU_PRIMA_DEL_BORDO:
            snakePosX[0] -= VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        elif snakePosX[0] < UN_PO_PIU_PRIMA_DEL_BORDO_A_DESTRA:
            snakePosX[0] += VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        if snakePosY[0] > UN_PO_PIU_PRIMA_DEL_BORDO:
            snakePosY[0] -= VAI_INDIETRO_QUANDO_SEI_SUL_BORDO
        elif snakePosY[0] < UN_PO_PIU_PRIMA_DEL_BORDO_A_DESTRA:
            snakePosY[0] += VAI_INDIETRO_QUANDO_SEI_SUL_BORDO

        # questo è un piccolo ceck se mangia ste palline o no
        if foodPosX == snakePosX[0] and foodPosY == snakePosY[0]:
            snakegrow = True
            randomfood = True
            movementdelay += movementdecrease

        # questo serve a far spawnare cibo in posizioni random
        if randomfood:
            randomfood = False
            retryFlag = True
            while retryFlag:
                foodPosX = random.randint(0, 7)
                foodPosY = random.randint(0, 7)
                retryFlag = False
                for x, y in zip(snakePosX, snakePosY):
                    if x == foodPosX and y == foodPosY:
                        retryFlag = True
                        break

        # update matrix:
        rgb1 = random.randrange(0, 256)
        rgb2 = random.randrange(0, 256)
        rgb3 = random.randrange(0, 256)
        sense.clear()
        sense.set_pixel(foodPosX, foodPosY, RED)
        if snakegrow:
            for x, y in zip(snakePosX, snakePosY):
                sense.set_pixel(x, y, RED)
        else:
            for x, y in zip(snakePosX, snakePosY):
                sense.set_pixel(x, y, rgb1, rgb2, rgb3)

        # quanto il serpente mangia qualcosa diventa piu grande giusto  ecco questa è la funzione di questa parte del codice      
        if snakegrow:
            snakegrow = False
            snakePosX.append(0)
            snakePosY.append(0)
            
        # questo serve a capire se ti mangi da solo perche scrivo sti commenti tanto me lo ricordo va be
        #forse passo al inglese bho non so nemmeno se funziona
        #update sta roba non so perche ma funziona e non ho intenzione di toccarla se funziona funziona
        for i in range(1, len(snakePosX)):
            if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
                gameover = True

        # proff non mi amazzi dovevo mettere questo break come faccievo mettevo un or nell while dell inizio del loop
        # serve per capire se sono morto o meno
        if gameover:
            break
        

        # snake speed (game loop delay):
        time.sleep(movementdelay)
