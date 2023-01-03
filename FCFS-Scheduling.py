import sys
import os
from prettytable import PrettyTable


def main():
    os.system('cls')
    menu = ['FCFS','SJF','Round Robin','Exit']
    print('#'*30)
    print('MAIN MENU')

    for x,menus in enumerate(menu):
        print('[',x+1,'] .', menus)

    choosemenu = input('Select Menu [0...3] !')
    
    if choosemenu == '1':
        fcfs()
    elif choosemenu == '2':
        sjf()
    elif choosemenu == '3':
        rr()
    elif choosemenu == '4':
        exit()    
    else:
        print('Your input is wrong!')
        main()

def fcfs():
    #input the number of processes
    process_count = int(input("Enter the number of processes : "))
    #initialize list for burst time
    burst_time = []
    #input burst time
    for i in range(process_count):
        burst = int(input(f"Enter the process burst time {i+1}: "))
        burst_time.append(burst)
    #initialize list for waiting time
    waiting_time = []
    #variable for total waiting time
    total_wait = 0
    #calculate waiting time for each process
    for i in range(process_count):
        if i == 0:
            waiting_time.append(0)
        else:
            wait = sum(burst_time[:i]) - sum(waiting_time[:1])
            waiting_time.append(wait)
            total_wait += wait
    #calculate average waiting time
    avg_wt = total_wait/process_count
    #initialize table
    table = PrettyTable(['Process','Burst Time','Waiting Time'])
    #fill in the table with process data 
    for i in range(process_count):
        table.add_row([i+1, burst_time[i], waiting_time[i]])

    print(table)
    print("Average Waiting Time : ", avg_wt)


def sjf():
    print('sjf')
def rr():
    print('rr')
def exit():
    sys.exit()

main()