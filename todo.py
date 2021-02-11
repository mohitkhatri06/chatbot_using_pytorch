import datefinder
import datetime

def todo():
    outfile = open('todolist.txt','a')
    name = input("Name the task: ")
    timingAp = input("Time: ")
    #Timing(timingAp)
    outfile.write('-----------------------------------------------------\n')
    outfile.write('Task:\t\t\t'+name+'\n')
    outfile.write('Date and time:  '+str(Timing(timingAp))+'\n')
def Timing(timingAp):
    dTime = datefinder.find_dates(timingAp)
    for mat in dTime:
        stringA = str(mat)
        return stringA





