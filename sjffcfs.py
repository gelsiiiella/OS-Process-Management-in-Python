import sys
from tabulate import tabulate
from art import *


def main():
    tprint("Main Menu",font="block",chr_ignore=True)
    tprint('''
              First Come First Serve 
              Shortest Job First
            ''', font="cybermedium")
    print("\t\t\t\t\t\t\t\t\tSelect from the following Algorithms:\n\n\n")
    print("\t\t\t\t\t\t\t\t[1] FCFS\t\t [2]SJF\t\t\t [3]Exit\n\n\n")


if __name__ == "__main__":
    main()

menu=int(input('Input your process management: '))

def first_come_first_serve():
    process=int(input('Input number of processes: '))
    burstTime=[]
    wt= [0] * process
    tat= [0] * process

    for i in range(process):
        burst=int(input("Enter burst time for {}:".format(i+1)))
        burstTime.append(burst)

        if i > 0:
            wt[i] = burstTime[i-1]+wt[i-1]
        tat[i] = wt[i]+ burstTime[i]

        avg_wt=sum(wt)/process
        avg_tat=sum(tat)/process

    headers= ['Processes','Burst Time','Turn-Around Time','Waiting Time']
    data = [[i+1,burstTime[i],tat[i],wt[i]]for i in range(process)]

    print(tabulate(data,headers=headers,tablefmt='grid'))

    print("Average Turnaround Time:",round(avg_tat))
    print("Average Waiting Time:",round(avg_wt))


def shortest_job_first():
    process=int(input('Input number of processes:  '))
    burstTime=[]

    for i in range(process):
        burst=int(input("Enter burst time for process {}:".format(i+1)))
        burstTime.append(burst)

    burstTime.sort()
    wt= [0] * process
    tat= [0] * process
    ct= [0] * process

    ct[0] = burstTime[0]  
    tat[0] = burstTime[0] 
    wt[0] = 0   

    for i in range(process):
        if i > 0:
            ct [i] = ct[i-1]+ burstTime[i] 
            tat[i] = ct[i] 
            wt[i]= ct[i]-burstTime[i]

        avg_wt=sum(wt)/process
        avg_tat=sum(tat)/process
        avg_ct = sum(ct)/process

    headers= ['Processes','Completion Time','Turn-Around Time','Waiting Time']
    data = [[i+1,ct[i],tat[i],wt[i]] for i in range(process)]

    print(tabulate(data,headers=headers,tablefmt='grid'))

    print("Average Turnaround Time:",round(avg_tat,2))
    print("Average Waiting Time:",round(avg_wt,2))
    print("Average Completion Time:",round(avg_ct,2))


try:
    if menu == 1:
        first_come_first_serve()
    elif menu ==2:
        shortest_job_first()
    elif menu == 3:
        valid = input('Are you sure to exit? ')
        if valid.upper() == 'Y':
            print('Exiting the program')
            sys.exit(0)
        else:
            main()
    else:
        print('Invalid Input')

except:
    print('Invalid Input')






