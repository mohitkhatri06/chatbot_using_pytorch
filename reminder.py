import datefinder
import winsound
import datetime

def alarm(text):
    dTime = datefinder.find_dates(text)
    for mat in dTime:
        #print(mat)
        stringA = str(mat)
        timeA = stringA[11:]
        hourA = timeA[:-6]
        hourA = int(hourA)
        minA = timeA[3:-3]
        minA = int(minA)
        print("Chatbot: Reminder successfully set for " + str(hourA)+":"+str(minA))

        while True:
            if hourA == datetime.datetime.now().hour:
                if minA == datetime.datetime.now().minute:
                    print("Take the medicine...")
                    winsound.PlaySound('E:\\MCA VIT(sem_1)\\Assignments\\Object Oriented soft. eng\\pytorch-chatbot\\beep-once1.wav',winsound.SND_LOOP)
                elif minA<datetime.datetime.now().minute:
                    print("Reminder is off now")
                    break


#alarm("set alarm at 6:52 pm")
