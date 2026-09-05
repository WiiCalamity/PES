#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2 - A situação de logística da Empresa Alpha Entregas está necessitando de melhorias no
controle das saídas e chegadas dos caminhões:
a) Considere que a empresa possui 8 caminhões numerados de 001 a 008;
b) Cada caminhão tem seu respectivo condutor, a relação dos condutores e seus
códigos está abaixo;
c) As entregas são monitoradas através do controle no chegada de cada caminhão;
d) Precisamos receber os dados do código do caminhão e do código do condutor,
somente assim consideraremos que a mercadoria daquela rota foi entregue;
e) O algoritmo deve prever o cadastro dos caminhões e dos condutores;
f) O algoritmo deve prever um cadastro com uma lista de todos os caminhões que
saem diariamente;
g) A cada saída diária dos caminhões, deve-se registrar a data e hora de saída de
cada veículo, bem como o condutor responsável;
h) Quando do chegada de cada caminhão, deve-se registrar a data e hora de
chegada;
i) O sistema deve ter opções para verificar se um determinado caminhão chegadau da
rota ou não, mostrando a data, hora e nome do condutor, consultando por código do
veículo;
j) O sistema deve ter opções para listar o cadastro de caminhões;
k) O sistema deve ter opções para listar os condutores;
l) O sistema deve ter opções para listar, por data, a lista dos veículos que
retornaram;
m) Precisamos saber, em determinado momento, se todas as entregas do dia foram
realizadas.
Relação de Condutores:           Relação dos Veículos
001 – Roberto Souza              001 – Monobloco
002 – João Graciano              002 – Scania 112 HW
003 – Karine Silva               003 – Volkswagen Express 4150
004 – Pedro Luiz                 004 – Volkswagen Express 6160
005 – Maria Catarina             005 – Volkswagen VW 17230 Worker
006 – Júlio Cardoso              006 – Volkswagen Express 9170
007 – Altivo Antônio             007 – Iveco Daily 40s14
008 – Jorge Gonçalves            008 – Iveco Tectro 310E28
009 – Marcos Vinícius
010 – Heleno Nunes
011 – Mara Cristina
012 – Otávio Rocha
"""
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

condutor={"001":"Roberto Souza",   "002":"João Graciano",
          "003":"Karine Silva",    "004":"Pedro Luiz",
          "005":"Maria Catarina",  "006":"Júlio Cardoso",
          "007":"Altivo Antônio",  "008":"Jorge Gonçalves",
          "009":"Marcos Vinícius", "010":"Heleno Nunes",
          "011":"Mara Cristina",   "012":"Otávio Rocha"}

veiculo={"001":["-1", "00/00/0000", "00:00", "Monobloco"],
         "002":["-1", "00/00/0000", "00:00", "Scania 112 HW"],
         "003":["-1", "00/00/0000", "00:00", "Volkswagen Express 4150"],
         "004":["-1", "00/00/0000", "00:00", "Volkswagen Express 6160"],
         "005":["-1", "00/00/0000", "00:00", "Volkswagen VW 17230 Worker"],
         "006":["-1", "00/00/0000", "00:00", "Volkswagen Express 9170"],
         "007":["-1", "00/00/0000", "00:00", "Iveco Daily 40s14"],
         "008":["-1", "00/00/0000", "00:00", "Iveco Tectro 310E28"]}
        # veiculo[key][0]  -> ID do condutor
        # veiculo[key][1]  -> Data de saida
        # veiculo[key][2]  -> Hora de saída
        # veiculo[key][-1] -> Nome do veículo

def isKeyInvalid(key, dictionary):
        if not key in dictionary:
                print("Erro! Chave inválida.")
                return True

def verStatus():
        key=input("Código do veículo: ").zfill(3)
        if isKeyInvalid(key, veiculo): return
        
        print(f"\n> [{key}] {veiculo[key][-1]} <")
        status="DISPONÍVEL" if veiculo[key][0]=="-1" else "EM ROTA"
        print(f"Status: {status}")
        if status=="DISPONÍVEL": return
        
        conductorKey=veiculo[key][0]
        conductorValue=condutor[conductorKey]
        print(f"Condutor: [{conductorKey}] {conductorValue}")
        print(f"Data da saída: {veiculo[key][1]}")
        print(f"Hora da saída: {veiculo[key][2]}")

def verEntregasPendentes():
        date=input("Data a consultar (dd/mm/aaaa): ")
        vehiclesOnRoad=0
        for vehicleValue in veiculo.values():
                if vehicleValue[1]==date:
                        vehiclesOnRoad+=1
        if vehiclesOnRoad==0:
                print("Todos os veículos retornaram nessa data.")
                return
        print(f"Ainda existe(m) {vehiclesOnRoad} veículo(s) em rota.")
                
                        

def registrarSaida():
        key=input("Código do veículo: ").zfill(3)
        if isKeyInvalid(key,veiculo): return
        if veiculo[key][0]!="-1":
                print("Erro! Esse veículo já está em rota!")
                return
        conductorKey=input("Código do condutor: ").zfill(3)
        if isKeyInvalid(conductorKey,condutor): return
        
        departDate=input("Data da saída (dd/mm/aaaa): ")
        departTime=input("Hora da saída (hh:mm): ")
        
        veiculo[key][0]=conductorKey
        veiculo[key][1]=departDate
        veiculo[key][2]=departTime
        print("Saída registrada.")

def registrarChegada():
        key=input("Código do veículo: ").zfill(3)
        if isKeyInvalid(key,veiculo): return
        if veiculo[key][0]=="-1":
                print("Esse veículo não está em rota!")
                return        
        veiculo[key][0]="-1"
        veiculo[key][1]="00/00/0000"
        veiculo[key][2]="00:00"
        print("Chegada registrada.")
        
def listarVeiculos():
        print("\nLISTA DE VEÍCULOS\n")
        for vehicleKey,vehicleValue in veiculo.items():
                print(f"[{vehicleKey}] {vehicleValue[-1]}")
        print()

def listarCondutores():
        print("\nLISTA DE CONDUTORES\n")
        for conductorKey,conductorValue in condutor.items():
                print(f"[{conductorKey}] {conductorValue}")
        print()

while True:
        clear()
        print("-----------------------------------.")
        print("|                                  |")
        print("|        Alpha Entregas 🚚         |")
        print("|                                  |")
        print("|----------------------------------|")
        print("|                                  |")
        print("| [1] Ver status de um veículo     |")
        print("| [2] Ver entregas pendentes       |")
        print("| [3] Registrar saída de veículo   |")
        print("| [4] Registrar chegada de veículo |")
        print("| [5] Listar veículos              |")
        print("| [6] Listar condutores            |")
        print("|                                  |")
        print("| [0] Sair                         |")
        print("|                                  |")
        print("'----------------------------------'")

        match input("Opção: "):
                case "1":
                        verStatus()
                case "2":
                        verEntregasPendentes()
                case "3":
                        registrarSaida()
                case "4":
                        registrarChegada()
                case "5":
                        listarVeiculos()
                case "6":
                        listarCondutores()
                case "0":
                        break
                case _:
                        print("Opção inválida!! @w@")
        input("\nEnter para voltar...")          
