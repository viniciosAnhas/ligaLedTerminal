import RPi.GPIO as gpio

led = 21

def setup():

	gpio.setmode(gpio.BCM)
	gpio.setup(led, gpio.OUT)
	gpio.output(led, False)

def loop():

	estadoLed = False

	try:

		while True:

			escolha = raw_input("Ligar ou desligar o led ? \n")

			while (escolha != "ligar") and (escolha != "desligar"):

				print "Opcao invalida"

				escolha = raw_input("Ligar ou desligar o led ? \n")

			if (escolha == "ligar") and (estadoLed == False):

				gpio.output(led, True)

				print "Led Ligado :)"

				estadoLed = True

			elif (escolha == "ligar") and (estadoLed == True):

				print "O led ja esta ligado"

			elif (escolha == "desligar") and (estadoLed == True):

				gpio.output(led, False)

				print "Led Desligado :("

				estadoLed = False

			elif (escolha == "desligar") and (estadoLed == False):

				print "O led esta ja esta desligado"

	finally:

		gpio.cleanup()

setup()
loop()
