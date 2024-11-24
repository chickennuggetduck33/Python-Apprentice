from tkinter import simpledialog, messagebox

rooms = {
    1:'',
    2:'',
    3:'',
    4:'',
    5:''
}
extras = ("pool-$30", "gym-$80", "playground-$10", "running water-$90")
def scam():
    scamq = simpledialog.askinteger(None, prompt="how many nights will you stay?")
    scamq = scamq * 413
    messagebox.showinfo(None, message="your charge will be $"+str(scamq))
def checkingin():
    roomnumber = simpledialog.askinteger(None, prompt="what room number?")
    if rooms[roomnumber] == '':
        messagebox.showinfo(None, message="room "+ str(roomnumber)+" is open")
        name = simpledialog.askstring(None, prompt="who would you like to check in?")
        rooms[roomnumber] = name
    else:
        messagebox.showinfo(None, message="room "+str(roomnumber) +" is already reserved")
def checkingout():
    checkoutroom = simpledialog.askinteger(None, prompt="what room number would you like to check out?")
    rooms[checkoutroom] = ''
running = True
def check_in_or_out():
    checkin = simpledialog.askstring(None, prompt="would you like to check in or out a quest? or type info to see all the options")
    print(checkin)
    if checkin == "check in":
       checkingin()
       scam()
    elif checkin == "check out":
       checkingout()
    elif checkin == "exit":
        print("HERE")
        running = False
        return False
    elif checkin == "guide":
        print(rooms)
    elif checkin == "extras":
        print(extras)
    elif checkin == "info":
        messagebox.showinfo(None, message="type guide for the list of guests.  type extras for the list of extras the guest can buy.  type exit to leave the program.")
    else:
        messagebox.showinfo(None, message="try saying check in or check out")

while running:
    if check_in_or_out() == False:
        running = False