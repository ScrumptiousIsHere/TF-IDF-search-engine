# This is a sample Python script.
import numpy as np
import re
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    termeni=['company', 'oil', 'is', 'tech', 'stake', 'water', 'for', 'government', 'rice', 'exchange', 'market', 'supplies', 'Soviet', 'company', 'trade', 'goods', 'export', 'economic', 'tonnes', 'money', 'small']
    fisiere=['0.txt','1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt', '11.txt', '12.txt', '13.txt', '14.txt', '15.txt', '16.txt', '17.txt', '18.txt', '19.txt', '20.txt', '21.txt', '22.txt', '23.txt', '24.txt', '25.txt', '26.txt', '27.txt', '28.txt', '29.txt', '30.txt', '31.txt', '32.txt']

    a=(21,33)
    matrice = np.zeros(a)
    for y in range(len(termeni)):
        for x in range(len(fisiere)):
            f = open(fisiere[x], "r")
            text = f.read()
            rezult=[m.start() for m in re.finditer(termeni[y],text)]
            matrice[y,x]=len(rezult)

    print(matrice)



    inp=input("Introduceti cuvintele cautate separate de catre un spatiu:")
    inpsp=inp.split(" ")
    print(inpsp)
    toleranta=float(input("Introduceti toleranta:"))
    filtru_toleranta=[]

    cerere=np.zeros(len(termeni))
    for x in range(len(inpsp)):
        for y in range(len(termeni)):
            if inpsp[x]==termeni[y]:
                cerere[y]=1



    dimensiuni=(len(fisiere))

    met=input("Ce metoda doriti sa folositi? :")

    if met=='cos_vect':


        cos_vect=np.zeros(dimensiuni)
        for y in range(len(fisiere)):
            norme = np.linalg.norm(cerere) * np.linalg.norm(matrice[:, y])
            #print("ASTEA SUNT CALCULELE")
            #print(matrice[:, y])
            #print(cerere)
            #print("ASTEA SUNT CALCULELE")
            dot=np.dot(cerere, matrice[:,y])
            #print(dot)
            #print("ASTA")


            cos_vect[y]=abs(dot/norme)
            #print(dot/norme)
        cos_vect_sort=np.argsort(cos_vect)
        cos_vect_sort_invers=cos_vect_sort[::-1]
        sortat=np.sort(cos_vect[cos_vect_sort])
        sortat_invers=sortat[::-1]

        valfinale=np.hstack((cos_vect_sort_invers,sortat_invers))
        print(cos_vect_sort_invers)
        print(sortat_invers)


        for i in range(len(cos_vect_sort_invers)):
            if sortat_invers[i]<toleranta:
                filtru_toleranta.append(False)
            else:
                filtru_toleranta.append(True)

        cos_vect_sort_invers_filtrat = cos_vect_sort_invers[filtru_toleranta]
        sortat_invers_filtrat = sortat_invers[filtru_toleranta]

        filter = input('Doriti sa vizualizati documentele care se incadreaza in toleranta introdusa ?')
        if filter == 'da':
            if(cos_vect_sort_invers_filtrat.size==0):
                print('Nu exista documente cu toleranta mai mare decat '+str(toleranta)+'!!!')
            else:
                print(cos_vect_sort_invers_filtrat)
                print(sortat_invers_filtrat)

        ds = input('Doriti informatii suplimentare ?')
        if ds=='da':
            for i in range(len(cos_vect_sort_invers)):
                print('Documentul '+str(cos_vect_sort_invers[i])+' are frecventa '+str(sortat_invers[i]))




    elif met=='norma2':
        norma2 = np.zeros(dimensiuni)
        for y in range(len(fisiere)):
            dot = np.dot(cerere, matrice[:, y])
            norma2[y]=np.linalg.norm(dot)
        norma2_sort = np.argsort(norma2)
        norma2_sort_invers = norma2_sort[::-1]
        sortat = np.sort(norma2[norma2_sort])
        sortat_invers = sortat[::-1]

        valfinale = np.hstack((norma2_sort_invers, sortat_invers))
        print(norma2_sort_invers)
        print(sortat_invers)

        for i in range(len(norma2_sort_invers)):
            if sortat_invers[i]<toleranta:
                filtru_toleranta.append(False)
            else:
                filtru_toleranta.append(True)

        norma2_sort_invers_filtrat = norma2_sort_invers[filtru_toleranta]
        sortat_invers_filtrat = sortat_invers[filtru_toleranta]

        filter = input('Doriti sa vizualizati documentele care se incadreaza in toleranta introdusa ?')
        if filter == 'da':
            if (norma2_sort_invers_filtrat.size == 0):
                print('Nu exista documente cu toleranta mai mare decat ' + str(toleranta) + '!!!')
            else:
                print(norma2_sort_invers_filtrat)
                print(sortat_invers_filtrat)


    elif met == 'norma1':
        norma1 = np.zeros(dimensiuni)
        for y in range(len(fisiere)):
            dot = np.dot(cerere, matrice[:, y])
            print(dot)
            print('pauza')
            norma1[y] = np.linalg.norm(dot)
        norma1_sort = np.argsort(norma1)
        norma1_sort_invers = norma1_sort[::-1]
        sortat = np.sort(norma1[norma1_sort])
        sortat_invers = sortat[::-1]

        valfinale = np.hstack((norma1_sort_invers, sortat_invers))
        print(norma1_sort_invers)
        print(sortat_invers)

        for i in range(len(norma1_sort_invers)):
            if sortat_invers[i] < toleranta:
                filtru_toleranta.append(False)
            else:
                filtru_toleranta.append(True)

        norma1_sort_invers_filtrat = norma1_sort_invers[filtru_toleranta]
        sortat_invers_filtrat = sortat_invers[filtru_toleranta]

        filter = input('Doriti sa vizualizati documentele care se incadreaza in toleranta introdusa ?')
        if filter == 'da':
            if (norma1_sort_invers_filtrat.size == 0):
                print('Nu exista documente cu toleranta mai mare decat ' + str(toleranta) + '!!!')
            else:
                print(norma1_sort_invers_filtrat)
                print(sortat_invers_filtrat)