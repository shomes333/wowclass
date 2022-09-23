from random import randint
#   Main Class
class personaje:
    
    def __init__(self, nombre, raza, job, str, dex, int, cha):
        # Atributos de clase
        self.nombre = nombre
        self.raza = raza
        self.clase = job
        self.fuerza = str
        self.destreza = dex
        self.inteligencia = int
        self.carisma = cha
        self.defenza = 14

        #Metodo atacar
    def atacar(self):
        atk = randint(3, 33)
        return atk


#   Nombre de personaje
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","\n")
print("Bienvenido al wow  ̷g̷o̷r̷d̷i̷t̷o̷" "\n","\n","~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","\n","\n")
Name = str(input('\n¿Como quieres que te llamen?\n'))


#   Facción de personaje
print('\n 1-Alianza \n', '2-Horda\n')
lvl = int(input('\n Elige tu Facción: '))
if lvl == 1:
    job = 'Alianza'
elif lvl == 2:
    job = 'Horda'

#   Raza de personaje

if lvl == 1:
    print('\n 1-Humano \n', '2-Enano\n', '3-Elfo de la noche\n', '4-Gnomos\n', '5-Draenei\n', '6-Huargen\n')
    rselect = int(input('\n Elegir Raza: '))
    if rselect == 1:
        race = 'Humano'
    elif rselect == 2:
        race = 'Enano'
    elif rselect == 3:
        race = 'Elfo de la noche'
    elif rselect == 4:
        race = 'Gnomos'
    elif rselect == 5:
        race = 'Draenei'
    elif rselect == 6:
        race = 'Huargen'
elif lvl == 2:
    print ('\n 7-Orcos\n', '8-No-muertos\n', '9-Tauren\n', '10-Trol\n', '11-Elfos de sangre\n', '12-Goblin\n')
    rselect = int(input('\n Elegir Raza: '))
    if rselect == 7:
        race = 'Orco'
    elif rselect == 8:
        race = 'No-muertos'
    elif rselect == 9:
        race = 'Tauren'
    elif rselect == 10:
        race = 'Trol'
    elif rselect == 11:
        race = 'Elfos de sangre'
    elif rselect == 12:
        race = 'Goblin'



#   Estadisticas de personaje

print('\n Tus Estadisticas son las siguientes:\n')
str = randint(3, 33)
dex = randint(3, 33)
int = randint(3, 33)
cha = randint(3, 33)



print(" Fuerza: ",str, "\n","Destreza: ",dex, "\n","Inteligencia: ",int, "\n","Sabiduria: ",cha, "\n","\n")




#   SUBCLASE con datos obtenidos
hero1= personaje(Name,race,job,str,dex,int,cha)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","\n")
print("¡¡¡WELCOME TO WORLD OF WARCRAFT!!!\n","\n","~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","\n","\n")

print(" Te recibe alguien de tu raza, y te da tu primera quest.","\n")
print(" ¡Muy buenas tardes, mi estimado e inigualable",hero1.raza,"! \n")
print(" El capitán ",hero1.raza," hace una reverencia que hizo que su largo abrigo aleteara tras él—. Qué sorpresa encontrarte aquí.")

print(f"' {hero1.nombre} Ayudame por favor! se me ha perdido un mapa por la zona y me solucionarías la vida si lo encontraras'\n")

print(' 1- Por supuesto, mi señor. \n', '2- Encontrar un mapa? Te crees que soy lvl 1?\n', '3- Nah, mejor me voy a la taberna\n', '4- No hacer absolutamente nada\n')
choice1 = (input('\n ¿Cual es tu respuesta?: '))




#   Primera eleccion
if choice1 == "1": 
    print(" Vas a explorar y te encuentras a un ",hero1.raza," peleando ferozmente con alguien de tu facción contraria\n")

    print(f" '{hero1.nombre} Ayudame con el!'\n Tu aliado te pide ayuda!!\n")
    print(f" 'Pibe de la {hero1.clase} esto es un 1v1 si te das la vuelta te dejo vivir!' El Orco te habla, sus dientes estan sangrientos\n")

    print(' 1-Ayudar a tu aliado \n', '2-Me voy a la taberna, no vi nada.\n', '3-Ignorar, y seguir buscando el mapa\n')
    choice12 = (input('\nQue haces?: '))

    if choice12 == "1":
        atk = 0
        while atk < 16:
            atk = hero1.atacar()
            if atk  <= 16:
                print(" Mi ataque fallo") 
            else:
                print(" Junto a tu aliado derrotan al Orco y encuentras el mapa en su bolsillo.")
    if choice12 == "2":
        print(f" '{hero1.nombre} no me abandones!,{hero1.raza} traidor!'\n Abandonaste a tu aliado a su suerte...")
    

    #Alianza
    if choice12 == "3" and hero1.clase == "Alianza":
        print(" Decidiste seguir buscando el mapa\n 1-Peleas con un oso\n 2-Te arrepientes y vuelves a pelear al lado de tu aliado")
        choice123 = (input('\n Que haces?: '))
        if choice123 =="1":
            print(" Empiezas atacando tu al feroz oso.")
            if hero1.fuerza <= 16:
                print(" Intentas acertar el primer golpe... \n Erras el golpe y te mata de un zarpazo")
            else:
                print(" Te acercas sigilosamente y... \n Acertas un golpe critico al oso y antes de tocar el piso ya está muerto")
        if choice123 =="2":
            print(" Ves a tu aliado a punto de perder el encuentro y le metes un stun al Orco, tienes 2 segundos antes de que recupere el conocimiento...")
            if hero1.destreza <= 16:
                print(" Tu destreza no es suficiente y tu ataque falla miserablemente... \n Te tardaste mucho y el Orco los mato a los dos")
            else:
                print(" Con mucha destreza logras un ataque perfecto... \n El orco muere desangrado y lo ultimo que ves antes de que desaparezca es un $#%)&$, te ries con tu aliado y te comparte su mapa.")





    #Horda
    if choice12 == "3" and hero1.clase == "Horda":
        print(" Decidiste seguir buscando el mapa", hero1.raza,"\n 1- Te arrepientes y vuelves a pelear al lado de tu aliado \n 2- Peleas contra un Lobo \n ")
        choice123 = (input('\n Que haces?: '))
        if choice123 =="1":
            print(" Preparas tu ataque y cuando esta listo atacas al Orco")
            if hero1.inteligencia <= 16:
                print(" Tu inteligencia no es suficiente, tu ataque es ineficaz... \n Te tardaste mucho y el Humano los mata a los dos")
            else:
                print(" Con tu gran Inteligencia logras pegar un critico a tu enemigo... \n Vos y el ",hero1.raza, " comparten el mapa y terminan la misión")
        if choice123 =="2":
            print(" El lobo te muerde, te asustas y te vas corriendo.. te mueres desangrado en el camino.")
    



#   Segunda eleccion
elif choice1 == "2":
    print(" Tu aventura termina antes de que pueda comenzar, te asesina el capitan a sangre fría.. \n -Pues si... efectivamente eras lvl 1, eres una escoria para nuestra raza")


#   Tercera eleccion
elif choice1 == "3":
    print(" El dueño de la taberna te mira de arriba abajo estudiante minuciosamente...\n Que quieres? \n\n 1-Quiero que este sea mi hogar \n 2-'Quiero ver tus pertenencias'\n 3- Tratas de convencerlo de que te fie cerveza \n " )
    choice32 = (input('\n Que haces?: '))
    if choice32 == "1":
        print(" -Bien... solo por ser de esta raza tienes permitido spawnear aquí...\n Pasas la noche en la Taberna, mañana será otro día.")
    if choice32 == "2":
        print(" Mis pertenencias? Vete.. No tienes como pagar ni un vaso de agua \n Te enfadas y sacas la espada.")
        atk = 0
        if atk < 16:
            atk = hero1.atacar()
            if atk  <= 16:
                print(" No sabes ni como pero tu cabeza está rodando por la barra... Pierdes la consciencia lentamente...") 
            else:
                print(" El tabernero estaba con unas cervezas de más y le ganas el encuentro a 1 de vida..")
    if choice32 == "3":
        if hero1.carisma <= 16:
            print(" Tu carisma no es suficiente, las palabras no salen como las piensas y te echan con una patada en el culo")
        else:
            print(" De alguna manera consigues convencer al tabernero y logras tomar gratis una cerveza")
    


#   Cuarta eleccion
elif choice1 == "4":
    print(" Escuchas gritos y sonidos de batalla.. Te acercas a ver que pasó \n Econtras el cuerpo de un aliado\n \n 1-Hacer animacion /laugh \n 2-Me llevo la bolsa de oro")
    choice42 = (input('\n Que haces?: '))
    if choice42 == "1":
        print(" Quien lo ha matado te mata a ti también de un básico. Termina tu aventura...")
    if choice42 == "2":
        print(" Revisas sus pertenencias, tenía 1000 de oro y una montura legendaría... tu aventura pinta bien.")
