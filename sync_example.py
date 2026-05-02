import time

def fazer_arroz():
    print("Fazendo arroz...")
    time.sleep(3) 
    print("Arroz pronto!")

def fazer_carne():
    print("Fazendo carne...")
    time.sleep(5)
    print("Carne pronta!")

def fazer_feijao():
    print("Fazendo feijão...")
    time.sleep(7)
    print("Feijão pronto!")

def cozinhar():
    fazer_arroz()
    fazer_carne()
    fazer_feijao()
    print("Refeição pronta!")

cozinhar()