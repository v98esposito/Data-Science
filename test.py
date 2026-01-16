Test New branches
# x = 30.01 #float
# y = 10 #int
# z = 'stringa' #string
# v = True/False #boolean
# a = [1,2,3,4] #list
# b = (1,2,3) #tuple
# c = range (1,5) #range
# d = {1,2,3} #set
# e = {"nome" : "Mario" , "cognome" : "Rossi", "età" : 25} #dict
# + - / * % ** // operatori matematici
import pandas as pd
import matplotlib.pyplot as plt

df_voti = pd.read_csv('voti.csv')

media_voti = df_voti['Voto'].mean() #esercizio 1
print(media_voti)

media_studenti= df_voti.groupby('Studente')['Voto'].mean() #esercizio 2
print(media_studenti)

marco = df_voti[df_voti['Studente'] == 'Marco'] #esercizio 3
print(marco)

df_voti.plot(king='bar', color='skyblue', x='Studente', y='Voto') #Grafica
plt.show()
