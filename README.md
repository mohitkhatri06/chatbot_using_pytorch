### Contextual Chatbot in PyTorch. Simple chatbot implementation with PyTorch.

This bot is trained on json file intents. Customization of intents can be done. Just modify intents.json with possible patterns and responses and re-run the training.

### Steps to build:
1. Stemming, Tokenization (nltk_utils.py)
2. create training data
3. model and training using PyTorch (model.py and train.py)
4. Saving the trained model
5. Pill reminder (reminder.py)
6. making todo list (todo.py)

### Required libraries:
    import numpy
    import random
    import torch
    import datefinder
    import winsound
    import datetime
    import nltk

_Note:_ if torch is not download by IDE the use the following commands:

For _Python 3.5_
-->pip3 install https://download.pytorch.org/whl/cpu/torch-1.0.1-cp35-cp35m-win_amd64.whl

For _Python 3.6_
-->pip3 install https://download.pytorch.org/whl/cpu/torch-1.0.1-cp36-cp36m-win_amd64.whl

For _Python 3.7_
-->pip3 install https://download.pytorch.org/whl/cpu/torch-1.0.1-cp37-cp37m-win_amd64.whl

### Steps to use this code:
run train.py this will create a data.pth file. And then run chat.py



#### Follwing are functionality of this chatbot
1. Covid-19 realted quries
    for the quries this chatbot is use intents in .json file

  * Demo:-
  
         --> user: what is symtoms of coronvirus
         -->Chatbot:Most common symptoms of corona: fever, dry cough, tiredness...

2. Set pil reminder:
    for making a reminder follow the given instructions when entering the details
  * Demo:-
  
        -->user: reminder (all cases are also accepted like 'Reminder' and 'REMINDER')
        -->chatbot: enter the time
        -->user: set for 12:30 PM
        -->chatbot: reminder successfully set for 12:30
      a continues beep sound and a message "Take the medicine" is displayed on the screen when the reminder is activated.


 3. Make TODO details as text file:
    for making a TODO. The entered data is saved into "todolist.txt" file

   * Demo:-
   
    -->user: TODO
    -->Chatbot: Enter the details:
       Name the task: Have to do assignments
       Time: 1:30
    -->Chatbot: Task is saved succesfully.
    
4. Show list:
     for simply view the todo type "show list" then all the sheduled tasks will appear
     
_Note_: for stopping the chatbot simply type 'quit'
