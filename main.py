from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot('HelperBot')
convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Helper Bot , i am created by Sujata',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which language you talk?',
    'I mostly talk in english'
]

# now training the bot with the help of trainer
trainer = ListTrainer(bot)
trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

main = Tk()
main.geometry("500x650")
main.title("Helper Bot")

# create image
img = PhotoImage(file="logo.png")
photoL = Label(main, image=img)
photoL.pack(pady=0)

# function
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Helper bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)

# creating frame and scrollbar
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Helper bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


main.mainloop()
