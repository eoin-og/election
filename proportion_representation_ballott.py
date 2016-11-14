from tkinter import *
import parser
from propRep import *

root = Tk()
root.title('Ballot')

n = 1
buttons = []
displays = []
ballots = []

dt = candidate("Donald Trump")
hc = candidate("Hilary Clinton")
gj = candidate("Gary Johnson")
js = candidate("Jill Stein")
em = candidate("Evan McMullin")

candidates = (dt,hc,gj,js,em)

def clear_all():
    """clears all the content in the Entry widget"""
    for display in displays:
        display.delete(0, END)
    for button in buttons:
        button.config(state=ACTIVE)
    global n
    n = 1

def get_variables(inp):
    """Gets the user input for operands and puts it inside the entry widget"""
    global n
    displays[inp].insert(0,n)
    buttons[inp].config(state=DISABLED)
    n += 1


def create_ballot():
    ballot = []
    global n
    for o in range(1,n):
        for i in range(len(candidates)):
            if displays[i].get() == str(o):
                ballot.append(candidates[i].name)
    
    clear_all()
    ballots.append(ballot)
    
def do_election(votes):
    assignVotes(candidates, votes, 1)

    quota = 2
    elected = 0
    numCands = len(candidates)

    while elected < quota:
        printResults(candidates)
        check = whatNow(candidates, 2, 10)
        print (check)
        if  check == 2:
            eliminate(candidates)
            numCands += -1
        else:
            elect(candidates, 2, 10)
            elected += 1
            numCands += -1
        if numCands == 2:
            break
            
        
    printResults(candidates)

for p in range(len(candidates)):

    root.rowconfigure(p,pad=10)
    root.columnconfigure(p,pad=20)

    candidate_name = candidates[p].name

    new_button = Button(root, text = candidate_name, command = lambda p=p: get_variables(p), font=("Calibri", 12),width=20)
    new_button.grid(row = p, column = 0)
    buttons.append(new_button)
    
    new_display = Entry(root, font = ("Calibri", 13))
    new_display.grid(row = p, column= 1 , sticky = W+E)
    displays.append(new_display)


clear_button = Button(root, text = "Clear All", command = lambda : clear_all(), font=("Calibri", 12),width=20)
clear_button.grid(row = len(candidates), columnspan = 1)


enter_button = Button(root, text = "Enter", command = lambda : create_ballot(), font=("Calibri", 12),width=20)
enter_button.grid(row = len(candidates)+1, columnspan = 1)

done_button = Button(root, text = "Done all Ballots", command = lambda : do_election(ballots), font=("Calibri", 12),width=20)
done_button.grid(row = len(candidates)+2, columnspan = 1)
root.mainloop()
