from pyscript import display, document
class Classmate: 
    def __init__(self, name, section, subject): #this is our template, this is to make assinging easier
        self.name = name
        self.section = section
        self.subject = subject

Ara=Classmate("Ara", "Emerald", "Math") #presuppose the 5 required classmates
Yanis=Classmate("Yanis", "Ruby", "Science")
Migi=Classmate("Migi", "Sapphire", "Filipino")
Ioanna =Classmate("Ioanna", "Topaz", "English")
Rycob =Classmate("Rycob", "Jade", "ICT")

classmates = [Ara, Yanis, Migi, Ioanna, Rycob] #this is to store the created classmates so that when we display it shows all the added classmates at once


def Add(e):

    name = document.getElementById("Classmate").value #gets the values that were selected in the html
    section = document.getElementById("Sectiom").value
    subject = document.getElementById("Subject").value

    classmate = Classmate(name, section, subject) #created a new classmate from the values that were selected
    classmates.append(classmate) #the append function add that to the classsmates list above

def Intro(e):

    if not classmates:
        document.getElementById("SHOW").innerHTML = "No classmates addd, please add one first" #try to warn you if you did not any classmates yet to the list

    else:
        show_text = ""
        for c in classmates:      
            show_text += f"Hi, I am {c.name}, I am in {c.section}, and I LOVE my favorite subject, {c.subject} <br>" #for every classmate, it wil add it into show text with all its decriptors, so when it displays it will add all at once and display at once
        document.getElementById("SHOW").innerHTML = show_text

