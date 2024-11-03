from tkinter import simpledialog, messagebox

rooms = {
    1:'',
    2:'',
    3:'',
    4:'',
    5:''
}
running = True
def check_in_or_out():
    checkin = simpledialog.askstring(None, prompt="would you like to check in or out a quest?")
    print(checkin)
    if checkin == "check in":
       roomnumber = simpledialog.askinteger(None, prompt="what room number?")
       if rooms[roomnumber] == '':
           messagebox.showinfo(None, message="room "+ str(roomnumber)+" is open")
           name = simpledialog.askstring(None, prompt="who would you like to check in?")
           rooms[roomnumber] = name
       else:
           messagebox.showinfo(None, message="room "+str(roomnumber) +" is already reserved")
    elif checkin == "check out":
        pass
    elif checkin == "exit":
        print("HERE")
        running = False
        return False
    else:
        messagebox.showinfo(None, message="try saying check in or check out")

while running:
    if check_in_or_out() == False:
        running = False