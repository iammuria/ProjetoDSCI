# Código para leitura dos Sensores: temperatura (DHT11), presença (HC-SR04), luminosidade (LDR) | Raspberry PI 3
# Autora: Múria Viana
# Disciplina de Desenvolvimento de Sistemas Computacionais I | Sandeco
# ----------- Conexões -----------
# Sensor DHT11 -> Pino 2
# Sensor HC-SR04 -> TRIG Pino 7 | ECHO Pino 8
import RPi.GPIO as GPIO
import dht11
import sys
import time
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global auxTemp, auxPres, auxLumi
auxTemp = 0
auxPres = 0
auxLumi = 0
    
class leituraSensores():
    
    def __init__(self):
        pass
    
    # ------------------------- LEITURA DA TEMPERATURA -------------------------
    # Quando dá erro informa o valor da última leitura
    def getTemp(self):
        self.auxTemp = auxTemp

        pino = dht11.DHT11(pin = 2)

        temp = pino.read()
        
        if temp.is_valid():
            self.auxTemp = temp.temperature
            return temp.temperature
        else:
            return self.auxTemp
    
    # ------------------------- LEITURA DA PRESENÇA -------------------------
    # Se a distância for menor que 50cm -> há alguém (1) | se não -> vazio (0)
    # Quando dá erro informa o valor da última leitura
    def getPres(self):           
        TRIG = 7                               
        ECHO = 8
        
        GPIO.setup(TRIG,GPIO.OUT)             
        GPIO.setup(ECHO,GPIO.IN)                  

        GPIO.output(TRIG, False)               
        time.sleep(2)                         
        GPIO.output(TRIG, True)                
        time.sleep(0.00001)                   
        GPIO.output(TRIG, False)          
    
        while GPIO.input(ECHO)==0:          
            pulse_start = time.time()          
    
        while GPIO.input(ECHO)==1:             
            pulse_end = time.time()    

        pulse_duration = pulse_end - pulse_start 
        
        distance = pulse_duration * 17150        
        distance = round(distance, 2)        

        if distance > 2 and distance < 400:
            if distance < 50:
                auxPres = 1
                return 1
            else:
                auxPres = 0
                return 0
        else:
            return auxPres              
    
    # ------------------------- LEITURA DA LUMINOSIDADE -------------------------
    #0 a 100%
    #100% -> 0 95% -> 150000 90% -> 300000 85% -> 450000 80% -> 600000 75% -> 750000 70% -> 900000 65% -> 1050000 60% -> 1200000 55% -> 1350000 50% -> 1500000
    #45% -> 1650000 40% -> 1800000 35% -> 1950000 30% -> 2100000 25% -> 2250000 20% -> 2400000 15% -> 2550000 10% -> 2700000 5% -> 2850000 0% -> 3000000

    def getLumi(self):
        self.auxLumi = auxLumi
        delayt = .1 
        value = 0
        ldr = 22

        def rc_time (ldr):
            count = 0
    
            GPIO.setup(ldr, GPIO.OUT)
            GPIO.output(ldr, False)
            time.sleep(delayt)

            GPIO.setup(ldr, GPIO.IN)
 
            while (GPIO.input(ldr) == 0):
                count += 1
            return count
 
        try:
            value = rc_time(ldr)
            self.auxLumi = value
            if value >= 0 and value < 150000:
                return 100 
            if value >= 150000 and value < 300000:
                return 90 
            if value >= 300000 and value < 450000:
                return 85
            if value >= 450000 and value < 600000:
                return 80
            if value >= 600000 and value < 750000:
                return 75
            if value >= 750000 and value < 1050000:
                return 70
            if value >= 1050000 and value < 1200000:
                return 65
            if value >= 1200000 and value < 1350000:
                return 60
            if value >= 1350000 and value < 1500000:
                return 55
            if value >= 1500000 and value < 1650000:
                return 50
            if value >= 1650000 and value < 1800000:
                return 45
            if value >= 1800000 and value < 1950000:
                return 40
            if value >= 1950000 and value < 2100000:
                return 35
            if value >= 2100000 and value < 2250000:
                return 30
            if value >= 2250000 and value < 2400000:
                return 25
            if value >= 2400000 and value < 2550000:
                return 20
            if value >= 2550000 and value < 2700000:
                return 15
            if value >= 2700000 and value < 2850000:
                return 10
            if value >= 2850000 and value < 3000000:
                return 5
            if value >= 3000000:
                return 0
            
            return switcher.get(value, "nothing")
        except KeyboardInterrupt:
            return self.auxLumi

if __name__ == '__main__':
    while True:
        val = leituraSensores()
        print("Presença")
        print(val.getPres())
        print("Temperatura")
        print(val.getTemp())
        print("Luminosidade")
        print(val.getLumi())
        print("------------------")
    