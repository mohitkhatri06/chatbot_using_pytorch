import random
import json

import torch
import reminder
import todo

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding='utf=8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Chatbot"

print("Let's chat! (type 'quit' to exit)")
while True:
    check = 0  # for checking that any if or if else condition is executed or not
    # sentence = "how to boost immunity?"
    sentence = input("You: ")
    if sentence.lower() == "quit":
        break

    # for reminder
    elif sentence.lower() == "reminder":
        print("Chatbot: Enter the time :")
        getTime = input("You: ")
        reminder.alarm(getTime)
        check = 1

    # for appointment
    elif sentence.lower() == "todo":
        print("Chatbot: Enter the details:")
        todo.todo()
        print("Chatbot: Task is saved succesfully.")
        check = 1

    elif sentence.lower() == "show list":
        check = 1
        f = open("todolist.txt", "r")
        if f.mode == "r":
            contents = f.read()
            print(contents)


    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        if check == 0:
            print(f"{bot_name}: I do not understand...")