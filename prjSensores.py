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
import json

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global auxTemp, auxPres, auxLumi
    
class Variaveis():
    
    def __init__(self, temp=0, lumi = 0, pres = 0):
        self.id = None
        self.hora = None
        self.temp = temp
        self.lumi = lumi
        self.pres = pres
    # ----------------------------------------------------------------- GET -----------------------------------------------------------------
    # ------------------------- LEITURA DA TEMPERATURA -------------------------
    # Quando dá erro informa o valor da última leitura
    def getTemp(self):
        self.auxTemp = self.temp

        pino = dht11.DHT11(pin = 2)

        temp = pino.read()

        if temp.is_valid():
            self.temp = temp.temperature
            if self.temp >= 14:
                self.auxTemp = self.temp
                return self.temp
            else:
                return self.auxTemp
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
                self.pres = 1
                self.auxPres = self.pres
                return self.pres
            else:
                self.pres = 0
                self.auxPres = self.pres
                return self.pres
        else:
            return self.auxPres              
    
    # ------------------------- LEITURA DA LUMINOSIDADE -------------------------
    #0 a 100%
    #100% -> 0 95% -> 150000 90% -> 300000 85% -> 450000 80% -> 600000 75% -> 750000 70% -> 900000 65% -> 1050000 60% -> 1200000 55% -> 1350000 50% -> 1500000
    #45% -> 1650000 40% -> 1800000 35% -> 1950000 30% -> 2100000 25% -> 2250000 20% -> 2400000 15% -> 2550000 10% -> 2700000 5% -> 2850000 0% -> 3000000

    def getLumi(self):
        auxLumi = self.lumi
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
            auxLumi = value
            if value >= 0 and value < 150000:
                self.lumi = 100
                return self.lumi 
            if value >= 150000 and value < 300000:
                rself.lumi = 90
                return self.lumi
            if value >= 300000 and value < 450000:
                self.lumi = 85
                return self.lumi
            if value >= 450000 and value < 600000:
                self.lumi = 80
                return self.lumi
            if value >= 600000 and value < 750000:
                self.lumi = 75
                return self.lumi
            if value >= 750000 and value < 1050000:
                self.lumi = 70
                return self.lumi
            if value >= 1050000 and value < 1200000:
                self.lumi = 65
                return self.lumi
            if value >= 1200000 and value < 1350000:
                self.lumi = 60
                return self.lumi
            if value >= 1350000 and value < 1500000:
                self.lumi = 55
                return self.lumi
            if value >= 1500000 and value < 1650000:
                self.lumi = 50
                return self.lumi
            if value >= 1650000 and value < 1800000:
                self.lumi = 45
                return self.lumi
            if value >= 1800000 and value < 1950000:
                self.lumi = 40
                return self.lumi
            if value >= 1950000 and value < 2100000:
                self.lumi = 35
                return self.lumi
            if value >= 2100000 and value < 2250000:
                self.lumi = 30
                return self.lumi
            if value >= 2250000 and value < 2400000:
                self.lumi = 25
                return self.lumi
            if value >= 2400000 and value < 2550000:
                self.lumi = 20
                return self.lumi
            if value >= 2550000 and value < 2700000:
                self.lumi = 15
                return self.lumi
            if value >= 2700000 and value < 2850000:
                self.lumi = 10
                return self.lumi
            if value >= 2850000 and value < 3000000:
                self.lumi = 5
                return self.lumi
            if value >= 3000000:
                self.lumi = 0
                return self.lumi
            
            return switcher.get(value, "nothing")
        except KeyboardInterrupt:
            return auxLumi
    # ----------------------------------------------------------------- SET -----------------------------------------------------------------
    def setTemp(self, temp):
        self.temp = temp

    def setLumi(self, lumi):
        self.lumi = lumi

    def setPres(self):
        return self.pres

    def getAll (self):
        self.temp = self.getTemp()
        self.lumi = self.getLumi()
        self.pres = self.getPres()
        all = {
            "temp" : self.temp,
            "lumi" : self.lumi,
            "pres" : self.pres
        }
        res = json.dumps(all)
        return  res
    
   # ----------------------------------------------------------------- PRINT ----------------------------------------------------------------- 
    def printAll(self):
        self.getAll()
        if self.pres == 0:
            return f'Temperatura: {self.temp} ºC  ' + f'Luminosidade: {self.lumi} %  ' + 'A sala está vazia'
        else:
            return f'Temperatura: {self.temp} ºC  ' + f'Luminosidade: {self.lumi} %  ' + 'Há alguém na sala'
    
if __name__ == '__main__':
    while True:
        val = Variaveis()
        print(val.printAll())
    
