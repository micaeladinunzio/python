loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    noun = input("Ingresa un sustantivo: ")
    p_noun = input("Ingresa un sustantivo en plural: ")
    noun2 = input("Ingresa un sustantivo: ")
    place = input("Ingresa un lugar: ")
    adjective = input("Ingresa un adjetivo : ")
    noun3 = input("Ingresa un sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Hoy trae tu",noun,"y", p_noun)
    print ("No te olvides de", noun2,",")
    print ("Pero no traigas",p_noun,"a",place)
    print ("Porque el clima esta",adjective,".")
    print ()
    print ("Yo me olvide mi",noun3,",")
    print ("Espero que no nos falte nada")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1