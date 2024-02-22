#Dylan Liesenfelt
#bigGame.py

#DEFINES THE MAIN FUCTION OF THIS PROGRAM
def main():
    #DISPLAYS AN INTRODUCTION AND INSTRUCTIONS
    print('Hello and welcome to my MadLib game!')
    print('Please type in words for the following blanks.\n')

    #VARRIABLES SET BY USER, CALLED LATER TO FILL IN MADLIB
    pnoun1 = input('A plural noun: ')
    fname = input("A person's first name: ")
    noun1 = input('A noun: ')
    lname = input("A person's last name: ")
    pnoun2 = input('Another plural noun: ')
    place1 = input('A place: ')
    pnoun3 = input('Another plural noun: ')
    place2 = input('Another place: ')
    pnoun4 = input('One more plural noun: ')
    noun2 = input('Another noun: ')
    adj1 = input('An adjective: ')
    adj2 = input('Another adjective: ')
    verb = input('A verb: ')
    adj3 = input('Lastly, another adjective: ')
    #ADDS SPACE FOR READABILITY WITHOIUT DROPING THE INPUT OF THE PREVIOUS LINE
    print()

    #DISPLAYS THE MADLIB WITH WORDS INPUT BY USER 
    print('THE BIG GAME!!!\n')
    print('Hello there, sports', pnoun1,'!''\n'
    'This is', fname,', talking to you from the press', noun1,'\n'
    'in', lname, 'Stadium, where 57,000 cheering', pnoun2,'\n'
    'have gathered to watch (the)', place1, pnoun3,'\n'
    'take on (the)', place2, pnoun4,'.\n'
    'Even though the', noun2, "is shining, it's a/an", adj1,'\n'
    'cold day with the temperature in the', adj2, '20s.\n'
    "We’ll be back for the opening", verb,'-off after a few words''\n'
    'from our', adj3,'sponsor. \n')

    #STOPS SCRIPT FROM CLOSING AFTER EXECUTING, ALLOWS USER TO READ MADLIB.
    input('Hit the ENTER key to close program.')

main()




