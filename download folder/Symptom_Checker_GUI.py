import sys
import csv
from tkinter import *

master = Tk()

def oneSymptom():
    Cause1 = symptomEntry1.get()
    Cause1 = Cause1.lower()
    bList = []
    with open('illnessdatabase.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
            Illness = column[0]
            Symptom1 = column[1]
            Symptom2 = column[2]
            Symptom3 = column[3]
            Symptom4 = column[4]
            Symptom5 = column[5]
            TreatmentLink = column[6]
            if Cause1 == Symptom1 or Cause1 == Symptom2 or Cause1 == Symptom3 or Cause1 == Symptom4 or Cause1 == Symptom5:
                aList = [Illness.upper() + ': ' + Symptom1 + ', ' + Symptom2 + ', ' + Symptom3 + ', ' + Symptom4 + ', ' + Symptom5 + ', ' + TreatmentLink]
                output = Label(master, text = aList)
                output.grid(sticky = W, columnspan = 3)
                #bList = [bList, aList]
                #str1 = ''.join(str(v) for v in bList)
                #print(str1)
                #listbox = Listbox(master, height = 5)
                #listbox.grid(row = 2, ipadx = 650, columnspan = 4, sticky = S)
                #listbox.delete(1)
                #listbox.insert(END , str1)

def twoSymptoms():
    Cause1 = symptomEntry1.get()
    Cause2 = symptomEntry2.get()
    Cause2 = Cause2.lower()
    Cause1 = Cause1.lower()
    with open('illnessdatabase.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
            Illness = column[0]
            Symptom1 = column[1]
            Symptom2 = column[2]
            Symptom3 = column[3]
            Symptom4 = column[4]
            Symptom5 = column[5]
            TreatmentLink = column[6]

            if (Cause1 == Symptom1 or Cause1 == Symptom2 or Cause1 == Symptom3 or Cause1 == Symptom4 or Cause1 == Symptom5) and (Cause2 == Symptom1 or Cause2 == Symptom2 or Cause2 == Symptom3 or
            Cause2 == Symptom4 or Cause2 == Symptom5):
                aList = [Illness.upper() + ': ' + Symptom1 + ', ' + Symptom2 + ', ' + Symptom3 + ', ' + Symptom4 + ', ' + Symptom5 + ', ' + TreatmentLink]
                output = Label(master, text = aList)
                output.grid(sticky = W, columnspan = 3)
                #listbox = Listbox(master, height = 5)
                #listbox.grid(row = 2, ipadx = 650, columnspan = 4, sticky = S)
                #listbox.insert(END, aList)

def threeSymptoms():
    Cause1 = symptomEntry1.get()
    Cause2 = symptomEntry2.get()
    Cause3 = symptomEntry3.get()
    Cause3 = Cause3.lower()
    Cause2 = Cause2.lower()
    Cause1 = Cause1.lower()
    with open('illnessdatabase.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
            Illness = column[0]
            Symptom1 = column[1]
            Symptom2 = column[2]
            Symptom3 = column[3]
            Symptom4 = column[4]
            Symptom5 = column[5]
            TreatmentLink = column[6]

            if (Cause1 == Symptom1 or Cause1 == Symptom2 or Cause1 == Symptom3 or Cause1 == Symptom4 or Cause1 == Symptom5) and (Cause2 == Symptom1 or Cause2 == Symptom2 or Cause2 == Symptom3 or
            Cause2 == Symptom4 or Cause2 == Symptom5) and (Cause3 == Symptom1 or Cause3 == Symptom2 or Cause3 == Symptom3 or Cause3 == Symptom4 or Cause3 == Symptom5):
                aList = [Illness.upper() + ': ' + Symptom1 + ', ' + Symptom2 + ', ' + Symptom3 + ', ' + Symptom4 + ', ' + Symptom5 + ', ' + TreatmentLink]
                output = Label(master, text = aList)
                output.grid(sticky = W, columnspan = 3)
                #listbox = Listbox(master, height = 5)
                #listbox.grid(row = 2, ipadx = 650, columnspan = 4, sticky = S)
                #listbox.insert(END, aList)

def knownIllness():
    InputIllness = illnessEntry.get()
    InputIllness = InputIllness.lower()
    with open('illnessdatabase.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
            Illness = column[0]
            TreatmentLink = column[6]

            if (InputIllness == Illness):
                aList = [Illness.upper()  + ': ' + TreatmentLink]
                output = Label(master, text = aList)
                output.grid(sticky = W, columnspan = 3)
                #listbox = Listbox(master, height = 5) #yscrollcommand = scrollbar.set)
                #listbox.grid(row = 2, ipadx = 650, columnspan = 4, sticky = S)
                #listbox.insert(END, aList)
                #scrollbar.config(command = listbox.yview)



#scrollbar = Scrollbar(master)
#scrollbar.grid(sticky = E, row = 1, rowspan = 100, column = 11, ipady = 55)
#listbox = Listbox(master, yscrollcommand = scrollbar.set)
#listbox.insert(END, output)
#listbox.grid(row = 1, columnspan = 2, sticky = S)
#scrollbar.config(command = listbox.yview)

oneSymptomButton = Button(master, text="One Symptom", command = oneSymptom, width = 50, height = 5)
twoSymptomButton = Button(master, text="Two Symptoms", command = twoSymptoms, width = 50, height = 5)
threeSymptomButton = Button(master, text="Three Symptoms", command = threeSymptoms, width = 50, height = 5)
illnessKnownButton = Button(master, text="Illness Already Known", command = knownIllness, width = 50, height = 5)
oneSymptomButton.grid(row = 0, column = 0, sticky=N)
twoSymptomButton.grid(row = 0, column = 1, sticky=N)
threeSymptomButton.grid(row = 0, column = 2, sticky=N)
illnessKnownButton.grid(row = 0, column = 3, sticky = N)

symptomEntry1 = Entry(master, width = 50)
symptomEntry1.grid(row = 1, column = 0)
symptomEntry1.delete(0, END)
symptomEntry1.insert(0, "Symptom One")

symptomEntry2 = Entry(master, width = 50)
symptomEntry2.grid(row = 1, column = 1)
symptomEntry2.delete(0, END)
symptomEntry2.insert(0, "Symptom Two")

symptomEntry3 = Entry(master, width = 50)
symptomEntry3.grid(row = 1, column = 2)
symptomEntry3.delete(0, END)
symptomEntry3.insert(0, "Symptom Three")

illnessEntry = Entry(master, width = 50)
illnessEntry.grid(row = 1, column = 3)
illnessEntry.delete(0, END)
illnessEntry.insert(0, "Known Illness")
